# How I "Trained" ChatGPT to My Own Documents

This repository provides a guide on how to seamlessly integrate your personal data storage with a powerful language model such as OpenAI's GPT. By leveraging LlamaIndex, developers can bypass the need for time-consuming fine-tuning and excessive prompts.

## Features

- **Data Integration**: LlamaIndex provides connectors that allow you to seamlessly integrate your existing data sources and formats, such as APIs, PDFs, documents, and SQL databases.
- **Data Structuring**: Easily structure your data using documents and nodes, enabling efficient storage and retrieval.
- **Advanced Retrieval and Query Interface**: LlamaIndex offers a powerful retrieval and query interface that enhances your interactions with the language model. It retrieves relevant context and augments the output with enriched knowledge.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies listed in the `requirements.txt` file. --> pip3 install -r requirements.txt
3. Set up your OpenAI API key in the `.env` file.
4. Place your pdf files into the `resources` folder.
5. Run the `chatbot.py` file.

## Usage

Once the project is set up and running, you can start interacting with the language model by providing prompts. The chat engine powered by LlamaIndex will generate responses based on the context of your data. The data is retrieved from folder "resources" so just place your pdf into this folder.

## Credits

This project is inspired by the article ["Build a Chatbot with Custom Data Sources Powered by LlamaIndex"](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/) written by Caroline Frasca, Krista Muir, and Yi Ding. Special thanks to the authors for providing valuable insights and a starting point for this project.

## Author

Johannes
https://jhayer.tech
