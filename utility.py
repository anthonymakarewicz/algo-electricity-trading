import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import numpy as np

from constants import PLOT_CONFIGS

def plot_histograms(df, bins=30, figsize=(12, 8), title=None, plot_configs=None):
    """
    Plots histograms for a DataFrame's columns. Adapts to single or multiple columns
    and supports a grid layout for multiple variables.

    Args:
        df (pd.DataFrame or pd.Series): DataFrame or Series containing the data.
        bins (int): Number of bins for the histograms.
        figsize (tuple): Size of the figure.
        title (str): Overall title for the plot (optional).
        plot_configs (dict): Optional plot configuration dictionary for each column.
                             Uses global PLOT_CONFIGS if not provided.
    """
    if plot_configs is None:
        plot_configs = PLOT_CONFIGS

    if isinstance(df, pd.Series) or df.shape[1] == 1:
        column = df.columns[0] if isinstance(df, pd.DataFrame) else df.name
        skewness = stats.skew(df.dropna())
        kurtosis = stats.kurtosis(df.dropna(), fisher=False)

        plt.figure(figsize=figsize)
        plt.hist(df.dropna(), bins=bins, color=plot_configs[column]["color"], alpha=0.7, edgecolor="black")
        plt.title(plot_configs[column]["title"], fontsize=12, fontweight="bold")
        plt.xlabel(plot_configs[column]["label"])
        plt.ylabel("Frequency")
        plt.legend([f"Skewness: {skewness:.2f}\nKurtosis: {kurtosis:.2f}"], loc="upper right", fontsize=10)
        plt.grid(True)
        if title is not None:
            plt.title(title, fontsize=16, fontweight="bold")
        plt.tight_layout()
        plt.show()
    else:
        num_cols = df.shape[1]
        rows = int(np.ceil(np.sqrt(num_cols)))
        cols_in_row = int(np.ceil(num_cols / rows))

        fig, axes = plt.subplots(rows, cols_in_row, figsize=figsize)
        if title is not None:
            fig.suptitle(title, fontsize=16, fontweight="bold")
        axes = axes.flatten()

        for idx, col in enumerate(df.columns):
            skewness = stats.skew(df[col].dropna())
            kurtosis = stats.kurtosis(df[col].dropna(), fisher=False)

            axes[idx].hist(df[col].dropna(), bins=bins, color=plot_configs[col]["color"], alpha=0.7, edgecolor="black")
            axes[idx].set_title(plot_configs[col]["title"], fontsize=12, fontweight="bold")
            axes[idx].set_xlabel(plot_configs[col]["label"])
            axes[idx].set_ylabel("Frequency")
            axes[idx].grid(True)
            axes[idx].legend([f"Skewness: {skewness:.2f}\nKurtosis: {kurtosis:.2f}"], loc="upper right", fontsize=10)

        for idx in range(num_cols, len(axes)):
            axes[idx].axis("off")

        plt.tight_layout()
        plt.show()