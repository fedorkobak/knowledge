import torch
from torch import nn

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