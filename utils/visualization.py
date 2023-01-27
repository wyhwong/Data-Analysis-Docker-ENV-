import matplotlib.pyplot as plt

from .common import getLogger

LOGGER = getLogger("Visualization")


def initializePlot(nrows=1, ncols=1, height=6, width=10, title="", xlabel="", ylabel="", tpad=2.5, lpad=0.1, bpad=0.12, fontsize=12):
    LOGGER.debug(f"Initializing plot, {nrows=}, {ncols=}, {height=}, {width=}, {title=}, {xlabel=}, {ylabel=}, {tpad=}, {lpad=}, {bpad=}, {fontsize=}.")
    fig, axes = plt.subplots(nrows, ncols, figsize=(width, height))
    fig.tight_layout(pad=tpad)
    fig.subplots_adjust(left=lpad, bottom=bpad)
    fig.suptitle(title, fontsize=fontsize)
    fig.text(x=0.04, y=0.5, s=ylabel, fontsize=fontsize, rotation="vertical", verticalalignment='center')
    fig.text(x=0.5, y=0.04, s=xlabel, fontsize=fontsize, horizontalalignment='center')
    LOGGER.info("Initialized plot.")
    return fig, axes


def initialize3DPlot(nrows=1, ncols=1, height=7, width=7, title="", xlabel="X", ylabel="Y", zlabel="Z", tpad=2.5, lpad=0.1, bpad=0.12, fontsize=12):
    LOGGER.debug(f"Initializing 3D plot, {nrows=}, {ncols=}, {height=}, {width=}, {title=}, {xlabel=}, {ylabel=}, {zlabel=}, {tpad=}, {lpad=}, {bpad=}, {fontsize=}.")
    fig, axes = plt.subplots(nrows, ncols, figsize=(width, height), subplot_kw={'projection': '3d'})
    fig.tight_layout(pad=tpad)
    fig.subplots_adjust(left=lpad, bottom=bpad)
    fig.suptitle(title, fontsize=fontsize)
    if ncols==1 and nrows==1:
        axes.set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)
    else:
        axes[0].set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)
    LOGGER.info("Initialized 3D plot.")
    return fig, axes
