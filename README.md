# ENADE_CategorizacaoQuestoes_ExtracaoConteudo
Extrair o conteúdo das imagens das questões já tratadas, utlizando OCR
O repositório do tratamento das imagens é: https://github.com/AlexandreNP9/ENADE_CategorizacaoQuestoes_TratamentoImagens

# Softwares utilizados
Linux Mint 22.1  
Python 3  
Gemini 2.5 flash

# Instalar softwares
Espera-se que já tenha o python3 instalado

## Variável de Ambiente (caso necessário)
python3 -m venv venv  
source venv/bin/activate  

## Para instalar o Google GenAI
pip3 install google-genai

## Chave API
Obter API key no Google AI Studio  
https://aistudio.google.com/app/api-keys  

Adicionar ao código na variável de ambiente com:  
export GEMINI_API_KEY="SUA_CHAVE_AQUI"
