import socket

puerto = 8080
ip = "10.0.2.15"
def chat(cliente):
    condicion = True
    while condicion:
        mensaje_cliente = input("")
        mensaje_cliente = str.encode(mensaje_cliente)
        cliente.send(mensaje_cliente)
        mensaje_servidor = cliente.recv(2048).decode("utf-8")
        print(mensaje_servidor)
        
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((ip, puerto))
    chat(cliente)
except KeyboardInterrupt:
    cliente.close()
    print("La conversación se acabó.")
