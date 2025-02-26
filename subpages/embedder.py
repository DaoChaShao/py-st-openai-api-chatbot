#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/26 14:37
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   embedder.py
# @Desc     :

from pandas import DataFrame
from streamlit import (empty, sidebar, button, balloons, spinner,
                       data_editor, plotly_chart)

from utilis.chart_plot import PCALearnerDimensionsReducer, scatter_2d
from utilis.models import Embedder
from utilis.tools import parameters_embedder, Timer, api_key_checker

empty_message: empty = empty()

model_name, api_key, thing_x, thing_y, thing_z = parameters_embedder()

if api_key and api_key_checker(api_key):
    empty_message.success("The API key has been set.")

    if thing_x and thing_y and thing_z:
        prompt: list = [thing_x, thing_y, thing_z]
        with sidebar:
            embed = button("Embedder", type="primary", help="Embed the text.")

        if embed:
            with spinner("Embedding the text...", show_time=True):
                with Timer(2, "Embedding Model Call") as timer:
                    response = Embedder(api_key).client(prompt, model_name)

                    df_embed: DataFrame = DataFrame(response, index=prompt)
                    data_editor(df_embed, disabled=True, use_container_width=True)

                    # Reduce the dimensions of the features using UMAP
                    reducer: DataFrame = PCALearnerDimensionsReducer().fit(df_embed)
                    data_editor(reducer, hide_index=True, disabled=True, use_container_width=True)

                    # Display the chart of scatter
                    chart = scatter_2d(reducer, point_size=10, font_size=18)
                    plotly_chart(chart)

                    balloons()

                empty_message.success(timer)
    else:
        empty_message.error("Please enter the text to embed.")
else:
    empty_message.error("Please enter the API key for the model.")
