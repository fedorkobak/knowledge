import io
import PIL
from PIL import Image

import numpy as np
from sklearn.neighbors import NearestNeighbors

import matplotlib.pyplot as plt

def get_picture(
    coordinates : list[float],
    nn : NearestNeighbors,
    X : np.array,
    title : str
) -> PIL.PngImagePlugin.PngImageFile:
    '''
    Get picture that show neighbours
    for given coordinates.

    Parameters
    ----------
    coordinates : list[float]
        сoordinates for which you need 
        to find neighbours;
    nn : sklearn.neighbors.NearestNeighbors
        algorithm under consideration;
    X : np.array of shape (n_samples, 2)
        this is two dimentional objects
        that will be represented at the
        scatter plot;
    title : str
        title that will be used for plot.

    Returns
    -------
    out : PIL.PngImagePlugin.PngImageFile
        picture with scatters.
    '''
    
    # getting neighrours
    distances, indices = nn.kneighbors([coordinates])

    # plotting scatter
    fig, ax = plt.subplots()
    ax.scatter(
        coordinates[0],
        coordinates[1],
        color="Green",
        s=100
    )
    ax.scatter(X[:,0], X[:,1])
    ax.scatter(X[indices, 0], X[indices, 1], color="red")
    plt.title(title)
    
    # saving to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    return Image.open(buf)

def get_gif(
    coordinates : list[list[float]], 
    nn : NearestNeighbors, 
    X : np.array,
    pictures_args : dict = {}
)->io.BytesIO:
    '''
    Get buffer containing gif
    file with animation where point 
    for which neighbours, moving
    according to given array.

    Parameters
    ----------
    coordinates : list[list[float]]
        array of coordinate combinations 
        along which the point will move 
        and for which we need to find neighbours;
    nn : sklearn.neighbors.NearestNeighbors
        algorithm under consideration;
    X : np.array of shape (n_samples, 2)
        this is two dimentional objects
        that will be represented at the
        scatter plot;
    pictures_args : dict
        this funciton is wrapper under get_picture
        so you can specify arguemnst to it.
    '''
    # generate frames on which the 
    # coordinate to which neighbours 
    # are searched moves in a circle.
    frames = [
        get_picture(
            coordinates=cord,
            nn=nn,
            X=X,
            **pictures_args
        )
        for cord in coordinates
    ]

    # creating buffer with gif file
    # and displaying it
    gif_buf = io.BytesIO()
    frames[0].save(
        gif_buf, 
        format='GIF', 
        save_all=True, 
        append_images=frames[1:], 
        duration=100, 
        loop=0
    )
    gif_buf.seek(0)
    return gif_buf

def get_circle_gif(
    nn : NearestNeighbors,
    X : np.array,
    radius : float = 5, 
    frames : int = 100,
    center : list = [0,0],
    pictures_args : dict = {}
)->io.BytesIO:
    '''
    Visualises the nearest neighbours to a 
    point that walks in a circle.

    Parameters
    ----------
    nn : sklearn.neighbors.NearestNeighbors
        algorithm under consideration;
    X : np.array of shape (n_samples, 2)
        this is two dimentional objects
        that will be represented at the
        scatter plot;
    radius : float, default=5
        radius of the circle;
    frames : int, deafult=5
        number of frames that will
        be used to build the gif;
    center : list[float] of len 2, default=[0,0]
        center of the circle;
    pictures_args : dict
        this funciton is wrapper under get_picture
        so you can specify arguemnst to it.
    '''
    return get_gif(
        coordinates=[
            [
                center[0] + np.cos(angle)*radius, 
                center[1] + np.sin(angle)*radius
            ]
            for angle in np.linspace(0, 2*np.pi, frames)
        ],
        nn=nn, X=X,
        pictures_args=pictures_args,
    )
