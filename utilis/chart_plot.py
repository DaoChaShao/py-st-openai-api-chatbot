#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/26 15:26
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   chart_plot.py
# @Desc     :   

from pandas import DataFrame
from plotly import express
from sklearn.decomposition import PCA


class PCALearnerDimensionsReducer(object):
    """ Reduce the dimensions of the features using PCA """

    def __init__(self, dimensions: int = 3):
        self._dims = dimensions

    def fit(self, features: DataFrame, seed=None) -> DataFrame:
        """ Fit and transform the features using PCA """
        # Extract words (keys) and their vectors (values)
        categories = features.index.tolist()
        vectors = features.values

        # Reduce from ND to 3D using PCA
        pca = PCA(n_components=self._dims, random_state=seed)
        vectors = pca.fit_transform(vectors)

        df = DataFrame(vectors, columns=categories)

        # print(df)
        return df


def scatter_2d(features: DataFrame, point_size: int, font_size: int):
    """ Display the 2 dimensions chart of scatter """
    # Define the columns to be used for plotting
    categories: list = features.columns.tolist()

    fig = express.scatter_3d(
        data_frame=features,
        x=features.iloc[0].values,
        y=features.iloc[1].values,
        z=features.iloc[2].values,
        color=categories,
        text=categories,
        title=f"Feature Differences among {categories[0]}, {categories[1]} and {categories[2]}",
        height=600,
    )

    # Specific adjustments
    fig.update_traces(marker=dict(size=point_size), textfont=dict(size=font_size))

    # Adjust layout settings for better positioning
    fig.update_layout(
        legend=dict(
            orientation="h",  # Set the legend to be horizontal
            yanchor="bottom",  # Position legend at the bottom
            xanchor="center",  # Center the legend
            y=-0.15,  # Adjust vertical positioning of legend (move further down)
            x=0.5  # Center the legend horizontally
        )
    )

    return fig
