import sys
import os
import requests
from colors import default, green, red, yellow, cian

args = sys.argv
c_300 = []
c_200 = []
wlist = "directory-medium.txt"

# Exemplo: https://www.google.com
site = args[1]
v = False

# Armazena(ou apenas executa) cada argumento em sua respectiva variável
if("-h" or "--help" in args):
  print(f"{cian()}usage: find_directory.py https://www.google.com [-v]\n\n")
  print(f"options:\n -h, --help  show this help message and exit\n -v  show all server attempts\n{default()}")

  sys.exit(1)

if("-v" in args):
  v = True

if("-sw" in args):
  wlist = "directory-small.txt"

if("-mw" in args):
  wlist = "directory-medium.txt"

if("-lw" in args):
  wlist = "directory-large.txt"

with open(wlist, "r") as wordlist:
  words = wordlist

  for w in words:
    url = f"{site}/{w}"

    try:
      res = requests.get(url)

      if(v):
        print("=-"*25)
        print(f"Testando: {url}\n")
        print(f"{yellow()}Status code: {res.status_code}{default()}\n")
        print("=-"*25)
      
      if(res.status_code < 300):
        c_200.append(url)
      
      elif(res.status_code < 400):
        c_300.append(url)

    except requests.exceptions.MissingSchema:
      print(f"Erro: URL inválida - Certifique-se de incluir um esquema válido (http/https) em {site}")

      break

    except Exception as e:
      print(f"Erro ao tentar acessar {url}: {e}")

      break
    
print("URLs encontradas mas foram redirecionados: ")
for redirect in c_300:
  print(yellow() + redirect + default())

print("=-"*25)
print("URLs encontradas com sucesso: ")
for sucess in c_200:
  print(green() + sucess + default())


