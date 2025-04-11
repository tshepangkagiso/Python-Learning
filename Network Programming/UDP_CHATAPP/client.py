import socket

def start_client(msg="Hello Server!"):
    try:
        host = '127.0.0.1'
        port = 65432

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((host, port))
            full_msg = f"message to server: {msg}"
            client.sendall(full_msg.encode('utf-8'))

            # Receive echo back from server
            response = client.recv(1024)
            print(f"Server responded: {response.decode('utf-8')}")

    except Exception as ex:
        print(f"start_client error: {ex}")

if __name__ == "__main__":
    try:
        while True:
            msg = input("Enter message (or 'quit' to exit): ")
            if msg.lower() == "quit":
                break
            elif msg != "":
                start_client(msg)
            else:
                start_client()
    except Exception as ex:
        print(f"program error: {ex}")
