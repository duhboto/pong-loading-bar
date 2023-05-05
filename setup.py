﻿from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pong-loading-bar",
    version="1.0.0",
    author="Spencer Duh",
    author_email="spencerduh@gmail.com",
    description="A loading bar simulator using the game Pong",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/pong-loading-bar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
