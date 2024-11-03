import socket

def start_qotd_server():
    HOST = 'localhost'  # Listen on localhost
    PORT = 1717         # Use a non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"QOTD server running on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Send a quote to the client
                quote = "Keep pushing forward! - QOTD\n"
                conn.sendall(quote.encode('utf-8'))
                print("Quote sent, closing connection.")

if __name__ == "__main__":
    start_qotd_server()
