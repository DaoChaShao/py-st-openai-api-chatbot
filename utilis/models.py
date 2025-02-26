#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/26 10:57
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from openai import OpenAI
from dotenv import dotenv_values


def opener(config: dict, prompt: str) -> str:
    client = OpenAI(api_key=config["API_KEY"], base_url="https://api.openai.com/v1")
    # print(len(config["API_KEY"]))  # 164-digit key

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=messages,
        stream=False,
        temperature=0.7,
        top_p=0.9,
    )
    return completion.choices[0].message.content


class Opener(object):

    def __init__(self, api_key: str, temperature: float = 0.7, top_p: float = 0.9) -> None:
        self._api_key = api_key
        self._temperature = temperature
        self._top_p = top_p
        # self._config = dotenv_values(".env")

    def client(self, content: str, prompt: str, model: str) -> str:
        # client = OpenAI(api_key=self._config["API_KEY"], base_url="https://api.openai.com/v1")
        client = OpenAI(api_key=self._api_key, base_url="https://api.openai.com/v1")
        # print(len(config["API_KEY"]))  # 164-digit key

        messages = [
            {"role": "system", "content": content},
            {"role": "user", "content": prompt},
        ]

        completion = client.chat.completions.create(
            model=model,
            store=False,
            messages=messages,
            stream=False,
            temperature=self._temperature,
            top_p=self._top_p,
        )
        return completion.choices[0].message.content
