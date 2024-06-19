import socket
from tkinter import filedialog
caminho = filedialog.askopenfilename()

print("Cliente")
 
HOST='localhost'
PORT=57000
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
print("conectando com servidor...")
s.connect((HOST,PORT))
 
print("abrindo arquivo...")
arq=open(caminho,'rb')
 
print("enviado  arquivo")
for i in arq:
    s.send(i)
 
print("saindo...")
arq.close()
s.close()
input('Arquivo enviado\nAperte ENTER para sair...')