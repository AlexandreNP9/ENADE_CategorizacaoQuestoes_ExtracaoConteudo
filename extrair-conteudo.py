import os
from google import genai
from google.genai import types

# ---------------- CONFIGURAÇÃO ----------------
# O nome da pasta onde suas imagens .png estão salvas
INPUT_DIR = "questoes_enade"
# O nome da pasta onde os arquivos .txt de saída serão salvos
OUTPUT_DIR = "textos_extraidos"
# Modelo recomendado (rápido e excelente para multimodalidade)
MODEL_NAME = "gemini-2.5-flash"

# Prompt otimizado para a tarefa
PROMPT_ANALISE = """
Você é um sistema de análise de questões do ENADE.
Sua tarefa é extrair o conteúdo completo de uma imagem de questão, seguindo as regras:
1. **Extração de Texto:** Transcreva todo o texto da imagem (enunciado, opções, notas) de forma fiel.
2. **Descrição de Figuras:** Se a questão contiver figuras, gráficos, fluxogramas, diagramas ou códigos, insira a descrição da figura *imediatamente* antes ou após a menção dela no texto, usando a seguinte sintaxe: **[FIGURA: Descrição Completa e Interpretativa]**. A descrição deve ser o mais completa e técnica possível.
3. **Formato da Saída:** Não adicione introduções ou encerramentos. Apenas forneça o texto formatado da questão, incluindo as descrições das figuras onde for necessário.
"""

def processar_pasta():
    """Percorre a pasta de entrada, processa cada imagem PNG com a API Gemini
    e salva o resultado na pasta de saída."""
    
    if not os.getenv("GEMINI_API_KEY"):
        print("ERRO: A variável de ambiente 'GEMINI_API_KEY' não está definida.")
        print("Por favor, configure sua chave antes de rodar o script.")
        return

    try:
        client = genai.Client()
        print("Cliente Gemini inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar o cliente Gemini: {e}")
        return

    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Verificando imagens em: {INPUT_DIR}")
    print(f"Saída será salva em: {OUTPUT_DIR}")

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(INPUT_DIR, filename)
            output_filename = filename.replace(".png", ".txt")
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            print(f"\n-> Processando: {filename}")
            
            try:
                # --- CORREÇÃO AQUI ---
                # 1. Lê a imagem como bytes
                with open(image_path, "rb") as f:
                    image_bytes = f.read()
                
                # 2. Cria a parte com os bytes lidos
                image = types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                )
                # ---------------------
                
                # Prepara o conteúdo da requisição
                contents = [
                    PROMPT_ANALISE, 
                    image
                ]
                
                # Faz a chamada à API
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=contents,
                )
                
                # Salva o resultado no arquivo .txt
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                
                print(f"   SUCESSO: Conteúdo salvo em {output_path}")
                
            except Exception as e:
                print(f"   FALHA ao processar {filename}: {e}")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(f"ERRO DE PROCESSAMENTO:\n{e}")

if __name__ == "__main__":
    processar_pasta()