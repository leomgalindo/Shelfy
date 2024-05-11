# Shelfy

### Seu ajudante de coleções chegou!
Chega de preencher planilhas para manter sua coleção atualizada e em dia. Agora você pode fazer tudo isso com apenas uma imagem!

## Abstract
Created 15.05.2024  
For Alura + Google - AI Immersion hosted by Alura, a brazilian school of technology  
This project aims to be part of the final presentation after a week of free classes
about AI related techniques ("prompt engineering") and the Google Gemini & Google AI Studio

### Português - Como rodar
Bem-vindo ao Clube do Livro! Este é um aplicativo que permite aos usuários enviar uma foto de uma estante de livros para que seja feita uma lista dos títulos dos livros, autores, sinopses e etiquetas de gênero.
Como usar
    
    0. Clone esse repositório com "git clone"
    1. Execute o script no terminal usando "streamlit run shelfy.py"
    2. Você será recebido com um título e uma breve descrição do aplicativo.
    3. Forneça uma chave API do Google AI Studio.
    4. Carregue uma imagem de uma estante de livros clicando no botão "Escolha uma foto de livros ou estante".
    5. Aguarde o processamento da imagem.
    6- Após o processamento, uma tabela será exibida com as informações extraídas da estante, incluindo título, autor, categoria e sinopse.

## Requisitos

Certifique-se de ter todas as bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte comando:

```pip install streamlit pillow google-generativeai pandas```

## Configuração da API

Antes de executar o aplicativo, é necessário configurar a chave da API do Google Generative AI.   

## Limitações e Considerações

    O aplicativo pode não ser capaz de extrair todas as informações corretamente dependendo da qualidade da imagem e do posicionamento dos objetos na estante.
    Certifique-se de que a imagem enviada seja nítida e tenha uma iluminação adequada para melhores resultados.
    A precisão da extração de informações pode variar e exigir ajustes dependendo das características das imagens enviadas.

## Próximos Passos

    1. OCR para reconhecimento de objetos
        No presente momento, o Gemini apesar de conseguir reconhecer objetos ainda tem dificuldade quando a quantidade de objetos na imagem aumenta, fazendo com que o resultado não seja exato em todos os casos.
        Usando OCR, podemos passar para o Gemini apenas os títulos e retonar dados como resumo e ISBN de forma mais constante e precisa.
    2. Análise de dados
        Guardando os dados fornecidos pelo Gemini em SQLite, podemos fazer pequenas análises de dados para o usuário, como: Distribuição ordernada por gênero de livros, média de páginas, "idade" da biblioteca, entre outras.
    3. Few-Shot Prompts
        No presente momento, é gerado apenas um prompt para cada imagem. Usando a estratégia de Few-Shots, podemos fazer com que o Gemini retorne resultados mais próximos dos esperados, fornecendo exemplos do que queremos que o resultado final seja.
         

## Contato

Para quaisquer dúvidas, problemas ou sugestões, entre em contato conosco por aqui :)