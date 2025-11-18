# ENADE_CategorizacaoQuestoes_ExtracaoConteudo
Projeto para categorização das questões do ENADE de acordo com os descritores e habilidades previstas nas [Diretrizes Curriculares Nacionais (DNCs)](https://www.gov.br/mec/pt-br/cne/normas-classificadas-por-assunto/diretrizes-curriculares-cursos-de-graduacao).
Este repositório faz parte de um projeto com subsistemas distribuído.

Repositório Geral:
https://github.com/AlexandreNP9/ENADE_CategorizacaoQuestoes_GERAL

# Objetivos deste repositório
Utilizar a API do Google Flash 2.5 com OCR  
Extrair conteúdo das questões já tratadas do ENADE  
Nas questões que contém figuras, a OCR descreve a figura.

A extração do conteúdo do gabarito e do padrão de resposta é mais fácil fazer no Gemini direto, e só colocar aqui.

# Especifidades técnicas
## Programas e bibliotecas
Linux Mint 22.1  
Python 3  
Gemini 2.5 flash

# Antes de executar o código
Espera-se que já tenha o python3 instalado

## Criar variável de ambiente (caso necessário)
```
python3 -m venv venv  
source venv/bin/activate  
```

## Para instalar o Google GenAI
```
pip3 install google-genai
```

## Chave API
Obter API key no Google AI Studio  
https://aistudio.google.com/app/api-keys  

Adicionar ao código na variável de ambiente com:  
```
export GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

## Tenacity para tratamento de falhas
```
pip3 install tenacity
```

## Executar o script
```
python3 extrair-conteudo.py
```