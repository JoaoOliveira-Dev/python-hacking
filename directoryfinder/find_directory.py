import sys
import os
import requests
from colors import default, green, red, yellow, cian

args = sys.argv
c_300 = []
c_200 = []
wlist = "directory-default.txt"

# Exemplo: https://www.google.com
site = args[1]
v = False

# Armazena(ou apenas executa) cada argumento em sua respectiva variável
if("-h" in args):
  print(f"{cian()}usage: find_directory.py https://www.google.com [-v] [-sw]\n\n"
        f"options:\n -h, --help  show this help message and exit\n"
        f" -v          show all server attempts\n"
        f" -sw         set the SMALL wordlist{default()}")

  sys.exit(1)

if("-v" in args):
  v = True

if("-sw" in args):
  wlist = "directory-small.txt"

if("-tw" in args):
  wlist = "teste.txt"

with open(wlist, "r") as wordlist:
  words = wordlist

  print("=-"*25)
  for w in words:
    url = f"{site}/{w.strip()}"

    try:
      res = requests.get(url)

      if(v):
        print(f"Testando: {url}")
            
      if 300 <= res.status_code < 400:
        c_300.append(url)
      elif res.status_code < 300:
        c_200.append(url)

    except requests.exceptions.MissingSchema:
      print(f"Erro: URL inválida - Certifique-se de incluir um esquema válido (http/https) em {site}")

      break

    except Exception as e:
      print(f"Erro ao tentar acessar {url}: {e}")

      break
    

if (len(c_300) > 1):
  print("=-"*25)
  print("URLs encontradas mas foram redirecionados: ")
  for redirect in c_300:
    print(yellow() + redirect + default())

else:
  print("=-"*25)
  print("Nenhum redirecionamento encontrado")

print("=-"*25)
print("URLs encontradas com sucesso: ")
for sucess in c_200:
  print(green() + sucess + default())