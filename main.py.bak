import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
import os


st.set_page_config(
    page_title="LangChain Q&A",
    page_icon=":robot_face:",
    layout="centered",
     menu_items={
        'Get help': 'https://strbbrn.github.io/',
        'Report a bug': "https://www.github.com/strbbrn",
        'About': "Local LLM - RAG!"
    }
)


st.markdown(
    """
    <style>
    .chat-message {
        padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem;
    }
    .user-message {
        background-color: #2b78e4; color: white; text-align: right;
    }
    .bot-message {
        background-color: #f0f0f5; color: #333; text-align: left;
    }
    /* Add more CSS as needed */
    </style>
    """,
    unsafe_allow_html=True,
)

if "history" not in st.session_state:
    st.session_state.history = []


model = Ollama(
        model="phi3",  
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler]),
    )

persist_directory = "./docs/db" 
embeddings = OllamaEmbeddings(model="nomic-embed-text")
if not os.path.exists(persist_directory):
    with st.spinner('🚀 Starting your bot.  This might take a while'):
        
        pdf_loader = DirectoryLoader("./docs/", glob="./*.pdf", loader_cls=PyPDFLoader)
        text_loader = DirectoryLoader("./docs/", glob="./*.txt", loader_cls=TextLoader)
        csv_loader_kwargs={'autodetect_encoding': True} #help you in encoding issues
        csv_loader = DirectoryLoader("./docs/", glob="./*.csv", loader_cls=CSVLoader,loader_kwargs=csv_loader_kwargs)
        
        pdf_documents = pdf_loader.load()
        text_documents = text_loader.load()
        csv_documents = csv_loader.load()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
        
        pdf_context = "\n\n".join(str(p.page_content) for p in pdf_documents)
        text_context = "\n".join(str(p.page_content) for p in text_documents)
        csv_context = "\n".join(str(p.page_content) for p in csv_documents)

        pdfs = splitter.split_text(pdf_context)
        texts = splitter.split_text(text_context)
        csvs = splitter.split_text(csv_context)
        data = pdfs + texts + csvs

        print("Data Processing Complete")

        vectordb = Chroma.from_texts(data, embeddings, persist_directory=persist_directory)
        vectordb.persist()

        print("Vector DB Creating Complete\n")

elif os.path.exists(persist_directory):
    vectordb = Chroma(persist_directory=persist_directory, 
                  embedding_function=embeddings)
    
    print("Vector DB Loaded\n")



template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Use three sentences maximum and keep the answer as concise as possible. 
    {context}
    Question: {question}
    Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )
query_chain = RetrievalQA.from_chain_type(
    llm=model,
    retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
)



for msg in st.session_state.history:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "Assistant" else None):
        st.markdown(msg["content"], unsafe_allow_html=True)


prompt = st.chat_input("Your question:")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = query_chain.invoke({"query": prompt})
        source_documents = response.get("source_documents", [])  

    st.session_state.history.append({"role": "Assistant", "content": response["result"]})
    with st.chat_message("Assistant"):
        st.markdown(response["result"])

        
