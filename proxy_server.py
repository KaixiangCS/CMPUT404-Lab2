import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024
def get_remote_ip(host):
    #print()
    try:
        remote_ip = socket.gethostbyname(host)
    except:socket.gaierror:
        print("Hostname could not resolved. Exiting")
        sys.exit()
    #print
    return remote_ip

def main():
    host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(1)
        while True:
            conn,addr = proxy_start.accept
            print("Connected by", addr)
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:
                print("Connected to Google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip,port))
                send_full_data = conn.recv(BUFFER_SIZE)
                #print
