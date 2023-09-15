import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
import sys

DEBUG = bool(os.getenv('DEBUG', True))

# UNSPLASH_KEY = "ZtRy9ZraRDsD4za42EAjAUkNleBxJJjF5Hje0gM4kr4"
UNSPLASH_KEY = load_dotenv(dotenv_path='./.env.local')
UNSPLASH_KEY = os.getenv('UNSPLASH_KEY')
# print(UNSPLASH_KEY)
# sys.exit()
UNSPLASH_URL = "https://api.unsplash.com/photos/random"

if not UNSPLASH_KEY:
  raise EnvironmentError('Enviormental variable UNSPLASH_KEY is not present in the .env.local file')

app = Flask(__name__)

app.config['DEBUG'] = DEBUG


@app.route('/new-images')
def new_images():
  word = request.args.get('query')

  headers = {
    "Accept-version" : "v1",
    "Authorization" : "Client-ID "+ UNSPLASH_KEY
  }

  params = {
    "query":word
  }

  response = requests.get(url=UNSPLASH_URL, headers=headers)
  
  data = response.json()

  return data

if __name__=="__main__":
  app.run(host="0.0.0.0", port=5050)