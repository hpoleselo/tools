import socket
import sys
 

def firstTutorial():
    HOST = '' 
    PORT = 5555 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((HOST, PORT))
        
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
        
    print('Socket bind complete')
    s.listen(10)

    conn, addr = s.accept()

    print('Connected with ' + addr[0] + ':' + str(addr[1]))


def secondTutorial():
    HOST = '127.0.0.1'     # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print('Para sair use CTRL+X\n')
    msg = raw_input()
    while msg <> '\x18':
        tcp.send (msg)
        msg = raw_input()
    tcp.close()

secondTutorial()