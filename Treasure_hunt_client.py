import socket
import threading
import tkinter as tk

# Define the game area dimensions
MAP_WIDTH = 10
MAP_HEIGHT = 10

# Function to receive and display server messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("Map:"):
                update_map(message[4:])
            else:
                text_area.insert(tk.END, message)
                text_area.see(tk.END)
                if message.startswith("Congratulations! You found the treasure!"):
                    break
        except ConnectionResetError:
            print("Server closed the connection.")
            break

# Function to update the map display
def update_map(map_data):
    text_area.delete('1.0', tk.END)  # Clear previous map display
    text_area.insert(tk.END, map_data)

# Function to send move when the Return key is pressed
def send_move(event):
    move = entry.get().lower()
    client_socket.send(move.encode())
    if move == 'quit':
        client_socket.close()
        root.destroy()

# Initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "192.168.00.000"  # Replace SERVER_IP_ADDRESS with the IP address of the server machine
server_port = 9993  # Keep the port number consistent with the server
client_socket.connect((server_ip, server_port))

# Create GUI window
root = tk.Tk()
root.title("Treasure Hunt Game")

# Create text area to display messages and map
text_area = tk.Text(root, height=20, width=50)
text_area.pack()

# Create entry for move input
entry = tk.Entry(root, width=30)
entry.pack()
entry.bind('<Return>', send_move)  # Bind send_move function to Return key event

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.daemon = True
receive_thread.start()

# Run the GUI event loop
root.mainloop()
