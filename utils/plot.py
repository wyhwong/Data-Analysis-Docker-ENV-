import matplotlib.pyplot as plt

def get_base_plot(nrows=1, ncols=1, height=6, width=10, title="", xlabel="", ylabel="", tpad=2.5, lpad=0.1, bpad=0.12, fontsize=12):
    fig, axes = plt.subplots(nrows, ncols, figsize=(width, height))
    fig.tight_layout(pad=tpad)
    fig.subplots_adjust(left=lpad, bottom=bpad)
    fig.suptitle(title, fontsize=fontsize)
    fig.text(x=0.04, y=0.5, s=ylabel, fontsize=fontsize, rotation="vertical", verticalalignment='center')
    fig.text(x=0.5, y=0.04, s=xlabel, fontsize=fontsize, horizontalalignment='center')
    return fig, axes

def get_base_plot_3D(nrows=1, ncols=1, height=7, width=7, title="", xlabel="X", ylabel="Y", zlabel="Z", tpad=2.5, lpad=0.1, bpad=0.12, fontsize=12):
    fig, axes = plt.subplots(nrows, ncols, figsize=(width, height), subplot_kw={'projection': '3d'})
    fig.tight_layout(pad=tpad)
    fig.subplots_adjust(left=lpad, bottom=bpad)
    fig.suptitle(title, fontsize=fontsize)
    if ncols==1 and nrows==1:
        axes.set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)
    else:
        axes[0].set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)
    return fig, axes
