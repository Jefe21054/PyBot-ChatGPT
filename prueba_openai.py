import os
import openai
from dotenv import load_dotenv

load_dotenv('.env')
openai.api_key = os.environ.get('PRUEBA_SECRET_KEY')

while True:
    try:
        prompt = input('\nIntroduce una pregunta: (o "Salir")')
        cod = prompt.upper()
        if cod == 'SALIR':
            break
        chatbot = openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=2048)
        print(chatbot.choices[0].text) # type: ignore
    except KeyboardInterrupt:
        os.system('clear')
        print('Programa terminado por el usuario')
        break