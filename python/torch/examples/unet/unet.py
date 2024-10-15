'''
Tools that is used for fitting evaluating and saving UNet models.
'''

import torch
from torch import nn
from torch.utils.data import DataLoader

from tqdm import tqdm
import huggingface_hub
from pathlib import Path
from typing import Callable
from tempfile import TemporaryDirectory

class DoubleConv(nn.Module):
    '''
    Implementation of double conv layer.

    Parameters
    ----------
    in_channels: int
        Expected number of elements in the third dimension of the model's input.
    out_channels: int
        Number of elements in the third dimension of the model's output.
    mid_channels: int
        Number of channels used for communication between the first and second
        convolutions.
    '''
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        mid_channels: int|None=None
    ) -> None:
        super().__init__()

        if not mid_channels:
            mid_channels = out_channels

        self.double_conv = nn.Sequential(
            nn.Conv2d(
                in_channels=in_channels,
                out_channels=mid_channels,
                kernel_size=3,
                padding=1
            ),
            nn.BatchNorm2d(num_features=mid_channels),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
            nn.Conv2d(
                in_channels=mid_channels,
                out_channels=out_channels,
                kernel_size=3,
                padding=1
            ),
            nn.BatchNorm2d(num_features=out_channels),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.double_conv(x)


class Down(nn.Module):
    '''
    Downscaling block. Applies MaxPooling2D and double convolution. As a result,
    the output feature maps will have a dimensionality of n/2 - 2, where n is
    the size of the input feature map.

    Parameters
    ----------
    in_channels: int
        Channels number of the input data.
    out_channesl: int
        Channels number of the output data.
    '''

    def __init__(self, in_channels: int, out_channels: int) -> None:
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels=in_channels, out_channels=out_channels)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.maxpool_conv(x)


class Up(nn.Module):
    '''
    Upscaling block. Takes "down" and "left" inputs, concatenates them, and
    applies double convolutional transformations. If the "down" dimension does
    not have enough elements to be concatenated with the "left" input, it will
    be padded to have the corresponding shape.

    Parameters
    ----------
    in_channels: int
        Number of input channels.
    out_channels: int
        Number of output channels.
    '''

    def __init__(self, in_channels: int, out_channels: int) -> None:
        super().__init__()

        self.up = nn.Upsample(
            scale_factor=2,
            mode="bilinear",
            align_corners=True
        )
        self.conv = DoubleConv(
            in_channels=in_channels,
            out_channels=out_channels
        )

    def forward(self, x: torch.Tensor, x_left: torch.Tensor) -> torch.Tensor:
        x = self.up(x)

        diffY = x_left.shape[2] - x.shape[2]
        diffX = x_left.shape[3] - x.shape[3]

        # Pad upsampled "x" to diffX//2 from left - other from right.
        # Similarly with Y.
        pad = [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2]
        x = torch.nn.functional.pad(input=x, pad=pad)

        x = torch.cat([x_left, x], dim=1)

        return self.conv(x)
    

@torch.inference_mode
def evaluate(
    model: nn.Module,
    loader: DataLoader,
    loss_fun: Callable,
    tqdm_desc: str = None
) -> tuple[float, float]:

    """
    Evaluate the model on the given data loader.

    Parameters
    ----------
    model: nn.Module  
        The model to be evaluated.  
    loader: DataLoader  
        The DataLoader used for model evaluation.  
    loss_fun: Callable  
        The loss function used for evaluation.  
    tqdm_desc: str  
        The description displayed in the tqdm progress bar for batches.

    Returns
    -------
    out: tuple[float, float]
        - Pixel accuracy of the evaludated model.
        - Average loss over the batches of the estimated model.
    """

    model.eval()

    total_pixels = 0
    correct_pixels = 0
    loss_cumulative = 0

    for X, y in tqdm(loader, desc=tqdm_desc):

        predict = model(X)

        loss_cumulative += loss_fun(input=predict, target=y).item()

        correct_pixels += (predict.argmax(dim=1) == y).sum()
        total_pixels += y.numel()

    return (correct_pixels/total_pixels).item(), loss_cumulative/len(loader)


def run_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_fun: Callable,
    optimizer: torch.optim.Optimizer
):
    model.train()
    for X, y in tqdm(loader, desc="Fitting"):
        optimizer.zero_grad()
        predict = model(X)
        loss_value = loss_fun(input=predict, target=y)
        loss_value.backward()
        optimizer.step()


hf_api = huggingface_hub.HfApi()
def save_model(model: torch.nn.Module, name: str):
    with TemporaryDirectory() as tmpdir:
        torch.save(model.state_dict(), Path(tmpdir)/name)
        hf_api.upload_folder(
            repo_id="fedorkobak/knowledge",
            folder_path=tmpdir
        )


def  load_model(model: torch.nn.Module, name: str):
    cached_model = huggingface_hub.hf_hub_download(
        repo_id="fedorkobak/knowledge",
        filename=name
    )
    model.load_state_dict(
        torch.load(cached_model, map_location=torch.device('cpu')),
    )
    return model
