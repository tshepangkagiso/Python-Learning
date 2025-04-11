# Create a UDP-based chat application that allows multiple clients to communicate.
import socket

def start_server():
    try:
        host = '127.0.0.1'
        port = 65432

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((host, port))
            server.listen()
            print(f"server running on {host}:{port}")

            while True:  # Keep accepting new clients
                conn, addr = server.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"Received: {data.decode('utf-8')}")
                        conn.sendall(data)

    except Exception as ex:
        print(f"start_server error: {ex}")

if __name__ == "__main__":
    try:
        start_server()
    except Exception as ex:
        print(f"program error: {ex}")
