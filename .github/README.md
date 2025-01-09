# LangChain Q&A App

This Local LLM application, It leverages LangChain for powerful question-answering capabilities and Ollama as the Local language model.

![demo](https://github.com/strbbrn/local-llm-with-rag/blob/main/ragwithphi3outputs.png?raw=true)
## Features

*   **Intuitive Chat Interface:** Ask questions in plain English and receive concise answers.
*   **Enhanced Visuals:** Enjoy a polished chat interface with themed colors and chat bubbles.
*   **Progress Indication:** Get visual feedback while the model is processing your query.
*   **Error Handling:** Receive clear error messages for a smooth user experience.

## Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone 
    cd local-llm-with-rag
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Make sure you have `ollama` installed and running. Refer to its documentation for setup instructions.[OLLAMA](https://ollama.com/download))

3.  **Set up Model Type:**
    *   Add your Ollama model name: `phi3`
      ```bash
      ollama pull phi3
      ollama pull nomic-embed-text
      ```
      
    
4.  **Prepare Your Documents:**
    *   Place your PDF, TXT, or CSV files in the `docs` directory.
    *   The first time you run the app, it will create a vector database from your documents. This might take some time.

5.  **Run the App:**
    ```bash
    streamlit run main.py
    ```

## Usage

1.  Open the app in your browser.
2.  Type your question in the input box and press Enter.
3.  The app will process your query and display the answer along with relevant context from your documents.

## Customization

*   **Model:** Modify the `model_type` and `model` variables in `main.py` to use different language models (e.g., OpenAI).
*   **Embeddings:** Experiment with different embedding models by changing the `OllamaEmbeddings` model name.
*   **Theme:** Customize the CSS in the `st.markdown` section of `main.py` to change the appearance of the app.


## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the Apache License.
