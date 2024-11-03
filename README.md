# QOTD Server (Quote of the Day)

A simple Python implementation of a Quote of the Day (QOTD) server that listens on a specified port and sends a quote to each client that connects. This server is designed to demonstrate basic TCP socket programming and follows the QOTD protocol's behavior: sending a message and closing the connection.

## Features
- Sends a quote to each connected client
- Continuously runs, allowing multiple clients to connect sequentially
- Lightweight and easy to run on `localhost`

## Getting Started

### Prerequisites
- **Python 3.x** installed on your system
- **Telnet** or **Netcat (nc)** for testing (optional but recommended)

### Running the Server
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/qotd-server.git
   cd qotd-server

2. **Run the QOTD Server**:
   ```bash
   python port1717.py
   
3. If everything is set up correctly, you should see:
   ```bash
   QOTD server running on localhost:1717...

### Connecting to the Server
Once the server is running, you can connect to it using either Telnet or Netcat. Each connection will receive the quote and then disconnect automatically.

**Using Telnet**

   1. Open a terminal and type:
      ```bash
      telnet localhost 1717

**Using Netcat**
   1. Alternatively, you can use nc (Netcat) to connect:
      ```bash
      nc localhost 1717
   2. After connecting, you should see the server’s response:
      ```arduino
      Keep pushing forward! - QOTD

### Example Output
1. When a client connects, the server will display output similar to:
      ```vbnet
      QOTD server running on localhost:1717...
      Connected by ('127.0.0.1', 54321)
      Quote sent, closing connection.

### Troubleshooting
If you don’t see the quote:
   1. **Firewall**: Ensure port 1717 is open for local connections.
   2. **Permissions**: Use a non-privileged port like 1717 instead of the standard QOTD port (17), which requires root/admin privileges.

### Modifying the Quote
1. To customize the quote, edit the line in port1717.py:
      ```python
      quote = "Keep pushing forward! - QOTD\n"
Replace with your desired message.

### Project Structure
      ```bash
      qotd-server/
      │
      ├── port1717.py   # The main server script
      └── README.md        # Project documentation

### Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

### License
This project is open source and available under the MIT License.











  

