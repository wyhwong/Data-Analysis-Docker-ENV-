import matplotlib.pyplot as plt

from .logger import get_logger
from dataclasses import dataclass

LOGGER = get_logger("utils | visualization")

@dataclass
class Padding:
    tpad: float = 2.5
    lpad: float = 0.1
    bpad: float = 0.12

@dataclass
class Labels:
    title: str = ""
    xlabel: str = ""
    ylabel: str = ""
    zlabel: str = ""

def initialize_plot(nrows=1, ncols=1, figsize=(10, 6), labels=Labels(), padding=Padding(), fontsize=12):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    fig.tight_layout(pad=padding.tpad)
    fig.subplots_adjust(left=padding.lpad, bottom=padding.bpad)
    fig.suptitle(labels.title, fontsize=fontsize)
    fig.text(x=0.04, y=0.5, s=labels.ylabel, fontsize=fontsize, rotation="vertical", verticalalignment='center')
    fig.text(x=0.5, y=0.04, s=labels.xlabel, fontsize=fontsize, horizontalalignment='center')
    return fig, axes


def initialize_plot_3D(nrows=1, ncols=1, figsize=(10, 6), labels=Labels(), padding=Padding(), fontsize=12):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, subplot_kw={'projection': '3d'})
    fig.tight_layout(pad=padding.tpad)
    fig.subplots_adjust(left=padding.lpad, bottom=padding.bpad)
    fig.suptitle(labels.title, fontsize=fontsize)
    if ncols==1 and nrows==1:
        axes.set(xlabel=labels.xlabel, ylabel=labels.ylabel, zlabel=labels.zlabel)
    else:
        axes[0].set(xlabel=labels.xlabel, ylabel=labels.ylabel, zlabel=labels.zlabel)
    return fig, axes
