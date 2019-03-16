import socket
ip = "10.0.2.15"
puerto = 8080
respuestas = 2
def lee_mensaje(cliente):
    condicion = True
    while condicion:
        mensaje_cliente = cliente.recv(2048).decode("utf-8")
        print(mensaje_cliente)
        mensaje_servidor = input("")
        mensaje_servidor = str.encode(mensaje_servidor)
        cliente.send(mensaje_servidor)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((ip, puerto))
    serversocket.listen(respuestas)
    print("Esperando conexion en el puerto:",puerto,"y en la ip:",ip)
    (cliente, address) = serversocket.accept()
    lee_mensaje(cliente)

except KeyboardInterrupt:
    cliente.close()
    serversocket.close()
    print("La conversación se acabó...")
