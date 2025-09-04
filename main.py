## Biblioteca operator system
import os
import google.generativeai as genai
from dotenv import load_dotenv

## Carregando a função
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

## Definindo a persona do modelo
prompt_sistema = "Liste apenas os nomes dos produtos, e ofereça uma breve descrição de cada um."

llm = genai.GenerativeModel(
    model_name= MODELO_ESCOLHIDO,
    system_instruction= prompt_sistema
)

prompt_usuario = "Liste três produtos de moda sustentável para ir ao shopping."

resposta = llm.generate_content(prompt_usuario)

print(f"Resposta Gemini: {resposta.text}")