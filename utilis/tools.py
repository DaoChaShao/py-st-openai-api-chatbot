#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/26 10:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :

from streamlit import (sidebar, header, selectbox, caption, text_input,
                       segmented_control, slider, empty)
from time import perf_counter
from yaml import safe_load


def api_key_checker(api_key: str, category: str = "OpenAI") -> bool:
    """ Check the API key format
            - The length of an OpenAI API key is 164-digit key

    :param api_key: enter the API key of the deepseek
    :param category: the category of the API key
    :return: True if the API key is valid
    """
    if api_key.startswith("sk-"):
        if category == "OpenAI" and len(api_key) == 164:
            return True
        elif category == "DeepSeek" and len(api_key) == 35:
            return True
    return False


def yaml_loader(file_path: str = "utilis/config.yaml") -> dict:
    """ Load the YAML file
            - pip install pyyaml

    :param file_path: the file path
    :return: the dictionary of the YAML file
    """
    with open(file_path, "r", encoding="utf-8") as y:
        config = safe_load(y)
    return config


def parameters() -> tuple[str, str, str, float, float]:
    """ Set the hyperparameters for the Ollama model.

    :return: the model name, temperature, and top P
    """
    content: str = ""
    temperature: float = 0.0
    temp: float = 0.0
    top_p: float = 0.0

    with sidebar:
        header("Hyperparameters")

        model_types: list = ["OpenAI", "DeepSeek"]
        model_category: str = segmented_control(
            "Model Category", model_types, default=model_types[0], selection_mode="single",
            help="Select the model category."
        )

        match model_category:
            case "OpenAI":
                options: list = ["gpt-4o-mini"]
            case "DeepSeek":
                options: list = ["deepseek-chat"]
        model_name: str = selectbox(
            "Model", options, disabled=True, help="Select a model"
        )
        caption(f"The model you selected is: **{model_name}**")

        api_key: str = text_input(
            "API Key", placeholder="Enter your API key", type="password",
            max_chars=200, help="The API key for the model."
        )

        if api_key_checker(api_key, model_category):
            caption(f"The **{len(api_key)}**-digit API key is **valid**")

            match model_category:
                case "OpenAI":
                    temps: list = ["Low", "Medium", "High"]
                case "DeepSeek":
                    temps: list = ["Math/Code", "General", "Creative"]
            temperature: str = segmented_control(
                "Temperature", temps, default=temps[1], selection_mode="single",
                help="Select the the randomness of the output."
            )
            match temperature:
                case "Low":
                    content = yaml_loader()["openai_system_content"]["low"]["content"]
                    temp = 0.1
                case "Medium":
                    content = yaml_loader()["openai_system_content"]["medium"]["content"]
                    print(content)
                    temp = 0.7
                case "High":
                    content = yaml_loader()["openai_system_content"]["high"]["content"]
                    temp = 1.5
                case "Math/Code":
                    content = yaml_loader()["deepseek_system_content"]["low"]["content"]
                    temp = 0.0
                case "General":
                    content = yaml_loader()["deepseek_system_content"]["medium"]["content"]
                    temp = 1.3
                case "Creative":
                    content = yaml_loader()["deepseek_system_content"]["high"]["content"]
                    temp = 1.5
            caption(f"The temperature you selected is: **{temperature}**")

            top_p: int = slider("Top Probability Sampling", 0.0, 1.0, 0.9, help="The probability of the output.")
            caption(f"The top P you selected is: **{top_p}**")
        else:
            caption(f"The **{api_key}**-digit API key is **invalid**")

        return model_name, api_key, content, temp, top_p


class Timer(object):
    """ A simple timer class to measure the elapsed time.

    :param precision: the number of decimal places to round the elapsed time
    :param description: the description of the timer
    """

    def __init__(self, precision: int = 5, description: str = None):
        self._precision = precision
        self._description = description

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, *args):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
