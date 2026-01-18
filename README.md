# GooglePalm Chatbot with Python

The goal of this project is to create a GooglePalm powered chatbot using Python and integrate it with various data sources to answer questions effectively.

## Project Highlights

- Rude Manners is a online shop that sells clothes for sport
- Their inventory, sales and discounts data is stored in a MySQL database
- We will build an LLM based question and answer system that will use following,
  - Google Palm LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - Chromadb as a vector store
  - Few shot learning
- In the UI, store manager will ask questions in a natural language and it will produce the answers

## Introduction

This project demonstrates how to build a conversational chatbot using GooglePalm language model. It integrates with data sources to provide accurate and helpful responses to user queries.

## Features

- Conversational interface with GooglePalm
- Integration with SQL databases for dynamic queries
- Customizable prompts and responses
- Semantic search using sentence embeddings

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sultanbeishenkulov/Retail-LLM-Integration.git
    cd LLM_project
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Install additional dependencies:
    ```sh
    pip install chromadb langchain huggingface-hub
    ```

## Usage

1. Run the main script to start the chatbot:
    ```sh
    python main.py
    ```

2. Interact with the chatbot through the command line interface or integrate it into your application.


## System Architecture
User Interface: Streamlit app for natural language input.

Semantic Layer: LangChain orchestrator that uses ChromaDB to find the most relevant "Few-Shot" SQL examples.

LLM Logic: GooglePaLM processes the prompt + context to generate a syntax-correct MySQL query.

Data Layer: MySQL database executes the query and returns real-time inventory/sales data.


## Configuration

- I stored all my API key in JSON file (keys.json) as well as local MySQL credentials.
- Modify the `few_shots` list in `few_shots.py` to customize the prompts and responses for the chatbot.

## Examples

Here are some example interactions with the chatbot:

**Query:** How many white color Levi's t shirts we have available?
**Response:** 201

**Query:** If we have to sell all the Levis T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?
**Response:** 23643

