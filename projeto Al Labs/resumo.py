import openai
     import os

  
     openai.api_key = os.getenv('OPENAI_API_KEY')

     def gerar_ideia_startup(input_usuario):
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=f"Gerar uma ideia inovadora de startup com base no seguinte input: {input_usuario}",
             max_tokens=2048,
         )
         return response.choices[0].text.strip()

arquivo = 'artigo.txt'
texto = ler_arquivo(arquivo)
print (resumo(texto))
