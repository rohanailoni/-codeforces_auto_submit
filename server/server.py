import socket
import json 
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

serv_sock.bind(('127.0.0.1', 6543))

serv_sock.listen(10)

while True:
    # Accept new connections in an infinite loop.
    client_sock, client_addr = serv_sock.accept()
    print('New connection from', client_addr)
    while True:
        # Keep reading while the client is writing.
        data = client_sock.recv(2048)
        if not data:
            break
        data=data.decode('utf8').split("\r\n")[1:]
        output={}
        print("data",data)
        for field in data:
            try:
                d=field.split(":",maxsplit=1)
                output[d[0]]=d[1]
            except ValueError:
                continue
            except KeyError:
                continue
            except IndexError:
                continue
            except:
                continue
        form="""HTTP/1.1 200 OK
                Content-Type: text/html

                <html><body>Hello World</body></html>"""
        client_sock.sendall((form+json.dumps(output,indent=2)).encode('utf-8'))
        client_sock.close()
        break

