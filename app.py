from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE")

texto = input("Cole o texto para resumir: ")

resposta = client.responses.create(
    model="gpt-4.1-mini",
    input="Resuma o seguinte texto:\n" + texto
)

print(resposta.output_text)
