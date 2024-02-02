import sys
import os
import requests
from colors import default, find, n_find, redirect

args = sys.argv
n = 0

# Exemplo: https://www.google.com
site = args[1]
v = False

while n < len(args):
  if(args[n] == "-v"):
    v = True
  
  n += + 1

with open("directory-small.txt", "r") as wordlist:
  words = wordlist

  for w in words:
    url = f"{site}/{w}"

    try:
      res = requests.get(url)

      if(v):
        print(f"Testando: {url}")
        print(f"{redirect()}Status code: {res.status_code}{default()}\n")
      
      print("fora do continue")

    except requests.exceptions.MissingSchema:
      print(f"Erro: URL inválida - Certifique-se de incluir um esquema válido (http/https) em {site}")

      break

    except Exception as e:
      print(f"Erro ao tentar acessar {url}: {e}")

      break
    


