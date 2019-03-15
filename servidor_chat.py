import socket
ip = '127.0.0.1'
puerto = 8081
respuestas = 2
def lee_mensaje(clientsocket):
    condicion = True
    while condicion:
        mensaje_cliente = clientsocket.recv(2048).decode("utf-8")
        if mensaje_cliente == "adios":
            condicion = False
        mensaje_servidor = input("")
        send_bytes = str.encode(mensaje_servidor)
        clientsocket.send(send_bytes)
    clientsocket.close()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((ip, puerto))
    serversocket.listen(respuestas)
    print('Esperando conexion en {ip},{puerto}'.format(ip = ip, puerto = puerto))
    (cliente, address) = serversocket.accept()
    lee_mensaje(clientsocket)

except KeyboardInterrupt:
    cliente.close()
    servidor.close()
    print('Cerrando el chat...')
