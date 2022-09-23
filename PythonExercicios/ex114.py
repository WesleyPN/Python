import urllib
from urllib import request, error
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
