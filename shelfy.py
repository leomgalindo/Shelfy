import streamlit as st
import PIL.Image
import google.generativeai as genai
import json
import pandas as pd

# Set Page configuration
st.set_page_config(page_title="Shelfy", page_icon=":books:")

# Title and description
st.title("Bem-vindo ao Shelfy!")
st.write("Me mande uma foto da sua estante de livros ou jogos de tabuleiro para que eu possa fazer uma lista!")
api_key = st.text_input("Forneça uma chave de API para começarmos:")

# Upload button
uploaded_file = st.file_uploader("Escolha uma foto de livro, jogo ou estante", type=["jpg", "jpeg", "png"])

genai.configure(api_key=api_key)

# Set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_instruction = ("You are a chatbot that will receive a picture of a shelf. "
                      "This shelf can contain either books or boardgames."
                      "You will extract the following information:"
                      "1. Name of book or boardgame"
                      "2. Author"
                      "3. Genre of the book or boardgame, according to the internet"
                      "4.ISBN, when applicable")


model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              generation_config=generation_config,
                              #system_instruction=system_instruction,
                              safety_settings=safety_settings)

if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)

    convo = model.generate_content(
        ["Analise a seguinte imagem se ela é um jogo de tabuleiro ou uma estante de livros. "
         "Caso seja um jogo de tabuleiro, extraia o nome e a editora."
         "Caso seja uma estante de livros, extraia os títulos dos livros, autores. Com essa informação, procure ISBNs, "
         "Resumos e Etiquetas de Gênero baseado no título encontrado."
         "Se alguma das categorias não foi encontrada, apenas preencha com 'Não encontrado'"
         "Sempre comece com 'livros' em caso de livros encontrados ou 'tabuleiro', em caso de jogo de tabuleiro.", img], stream=True)

    with st.spinner("Enviando prompt..."):
        convo.resolve()

    response = convo.text

    st.divider()
    st.header("Resultado")

    data = json.loads(response)
    try:
        # Check if data contains 'livros'
        if "livros" in data:
            df_books = pd.json_normalize(data['livros'])
            df_books.columns = [f"Livro_{col}" for col in df_books.columns]  # Rename columns to avoid conflicts

            df_other = pd.DataFrame.from_dict({k: v for k, v in data.items() if k != 'Livros'}, orient='index').T

            # Concatenate both DataFrames
            df_final = pd.concat([df_other, df_books], axis=1)
            df_final.drop('livros', axis=1, inplace=True)


        elif 'tabuleiro' in data:
            # Normalize tabuleiro data into a DataFrame
            tabuleiro = pd.json_normalize(data['tabuleiro'])

            # Set column names for tabuleiro DataFrame
            tabuleiro.columns = ['tabuleiro_' + col for col in tabuleiro.columns]

            # Create a DataFrame for the remaining data excluding 'tabuleiro'
            other_data = {k: v for k, v in data.items() if k != 'tabuleiro'}
            other_df = pd.DataFrame.from_dict(other_data, orient='index').T

            # Concatenate both DataFrames
            df_final = pd.concat([other_df, tabuleiro], axis=1)

        st.dataframe(df_final)
    except (TypeError, KeyError):
        st.error("Erro ao processar os dados. Verifique se o formato do JSON está correto.")