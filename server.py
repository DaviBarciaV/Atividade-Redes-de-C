# Importa o módulo socket
from socket import *
import sys # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
#Fill in start
serverPort = 6789 # porta do servidor
serverSocket.bind(('', serverPort)) # liga o socket ao endereço local
serverSocket.listen(1)# escuta a conexão, permitindo 1 na fila
#Fill in end

while True: # mantém o servidor rodando
    #Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # aceita a conexão de cliente
    #Fill in end
    
    try:
        # Recebe a mensagem do cliente (requisição HTTP) (1024 bytes)
        #Fill in start
        message = connectionSocket.recv(1024).decode()
        #Fill in end
        
        filename = message.split()[1] 
        f = open(filename[1:])
        # extrai o nome do arquivo da requisição get

        #Fill in start
        outputdata = f.read() 
        #Fill in end
        
        # Envia a linha de status do cabeçalho HTTP
        #Fill in start
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header.encode()) 
        #Fill in end
        
        # Envia o conteúdo do arquivo ao cliente caractere por caractere
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        #Fecha a conexão com o cliente
        connectionSocket.close()
        
    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        #Fill in start
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        response = "" \
        "<html>" \
        "<body>" \
        "<h1>404 Not Found</h1>" \
        "</body>" \
        "</html>"
        connectionSocket.send(header.encode())
        connectionSocket.send(response.encode())
        #Fill in end
        
        #Fecha o socket do cliente
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit() # Encerra o programa