import socket
import json 
import signal

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

serv_sock.bind(('127.0.0.1', 6543))
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# to make sure the server restarts once the force exits
serv_sock.listen(10)


def recv_all(sock):
    r'''Receive everything from `sock`, until timeout occurs, meaning sender
    is exhausted, return result as string.'''

    # dirty hack to simplify this stuff - you should really use zero timeout,
    # deal with async socket and implement finite automata to handle incoming data
    MAX_PACKET = 32768
    prev_timeout = sock.gettimeout()
    try:
        sock.settimeout(0.1) # keeping connection time as 0.1 to 1 is optimal below may throw some errors
        rdata = []

        while True:
            try:
                data=sock.recv(MAX_PACKET)
                print("data:-",data)
                if data.decode("utf8")=="":
                    return ''.join(rdata)
                
                rdata.append(data.decode("utf8"))
                
            except socket.timeout:
                return ''.join(rdata)
    # unreachable mostly ig
    finally:
        sock.settimeout(prev_timeout)
def normalize_line_endings(s):
    r'''Convert string containing various line endings like \n, \r or \r\n,
    to uniform \n.'''

    return ''.join((line + '\n') for line in s.splitlines())

def run():
    while True:
        # Accept new connections in an infinite loop.
        client_sock, client_addr = serv_sock.accept()
        print('New connection from', client_addr)
        while True:
            recv_all_info=recv_all(client_sock)
            request = normalize_line_endings(recv_all_info) 
            request_head, request_body = request.split('\n\n', 1)# setting max_split to 1
            form="""HTTP/1.1 200 OK
                    Content-Type: text/html

                    <html>
                        <body>
                            Got the request
                        </body>
                    </html>
                """
            client_sock.sendall((form).encode('utf-8'))
            client_sock.close()
            print("client socket is close")
            break

if __name__=="__main__":
    run();