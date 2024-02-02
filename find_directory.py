import sys
import os
import requests
from colors import default, green, red, yellow, cian

args = sys.argv
c_300 = []
c_200 = []
n = 0

# Exemplo: https://www.google.com
site = args[1]
v = False

# Armazena(ou apenas executa) cada argumento em sua respectiva variável
if("-v" in args):
  v = True

if("-h" in args):
  print(f"{cian()}python3 find_directory.py https://www.google.com [-v]\n\n")
  print(f"options:\n -h  show this help message and exit\n -v  show all server attempts\n{default()}")

  sys.exit(1)
# while n < len(args):
#   if(args[n] == "-v"):
#     v = True
  
#   n += + 1

with open("directory-small.txt", "r") as wordlist:
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
      
      if(res.status_code >= 200):
        c_200.append(url)
      
      elif(res.status_code >= 300):
        c_300.append(url)

    except requests.exceptions.MissingSchema:
      print(f"Erro: URL inválida - Certifique-se de incluir um esquema válido (http/https) em {site}")

      break

    except Exception as e:
      print(f"Erro ao tentar acessar {url}: {e}")

      break
    
print("fora do balango beiço")


