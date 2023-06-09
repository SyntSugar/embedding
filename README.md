# Embedding

A one-stop HTTP service for sentence semantic embedding, based on the advanced Sentence Transformers model.

- [Embedding](#embedding)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [1\. Set IP writelist](#1-set-ip-writelist)
    - [2\. Start http server](#2-start-http-server)
  - [License](#license)

## Requirements

- Miniconda
- Python 3.8+
- PyTorch 1.6+
- Uvicorn

## Installation

First, you need to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Then, you can use the following commands to create and activate a new conda environment:

```
conda env create -f environment.yml
conda activate embedding
```

## Usage

### 1. Set IP writelist

Add your request server ip address in `/conf/{env}/config.toml`.

### 2. Start http server

```
uvicorn main:app --reload
```

## License

This project is licensed under the terms of the [MIT License](LICENSE).
