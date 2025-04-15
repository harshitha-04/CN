import socket
import random
import threading

# Define the game area dimensions
MAP_WIDTH = 10
MAP_HEIGHT = 10

# Generate random coordinates for the treasure
treasure_x = random.randint(0, MAP_WIDTH - 1)
treasure_y = random.randint(0, MAP_HEIGHT - 1)

# Dictionary to store player positions
players = {}

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.00.0.0', 9993))
server_socket.listen()

print(f"Server is listening... Treasure is located at position ({treasure_x}, {treasure_y})")

# Function to generate the map with players and treasure
def generate_map(player_x, player_y):
    map_data = [['.' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    for _, (x, y) in players.items():
        map_data[y][x] = 'P'
    map_data[player_y][player_x] = 'P'
    map_data[treasure_y][treasure_x] = 'T'

    map_display = '\n'.join(' '.join(row) for row in map_data)
    return map_display

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    # Ask for player's name
    client_socket.send("Enter your name: ".encode())
    player_name = client_socket.recv(1024).decode().strip()

    # Generate random initial position for the player
    player_x = random.randint(0, MAP_WIDTH - 1)
    player_y = random.randint(0, MAP_HEIGHT - 1)
    players[player_name] = (player_x, player_y)
    client_socket.send(f"Welcome, {player_name}, to the treasure hunt game!\n".encode())

    # Instructions for the player
    instructions = "Instructions:\n- Type 'w' to move west\n- Type 'e' to move east\n- Type 'n' to move north\n- Type 's' to move south\n"
    client_socket.send(instructions.encode())

    while True:
        try:
            # Send the map with player positions
            client_socket.send(f"Map:\n{generate_map(players[player_name][0], players[player_name][1])}\n".encode())

            # Receive player's move
            move = client_socket.recv(1024).decode().strip().lower()
            if move == 'quit':
                break

            # Update player's position based on the move
            if move == 'n':
                players[player_name] = (players[player_name][0], max(0, players[player_name][1] - 1))
            elif move == 's':
                players[player_name] = (players[player_name][0], min(MAP_HEIGHT - 1, players[player_name][1] + 1))
            elif move == 'w':
                players[player_name] = (max(0, players[player_name][0] - 1), players[player_name][1])
            elif move == 'e':
                players[player_name] = (min(MAP_WIDTH - 1, players[player_name][0] + 1), players[player_name][1])

            # Check if player found the treasure
            if players[player_name] == (treasure_x, treasure_y):
                client_socket.send("Congratulations! You found the treasure!\n".encode())
                break

        except ConnectionResetError:
            break

    del players[player_name]
    client_socket.close()
    print(f"Player {player_name} disconnected.")

# Accept incoming client connections
while True:
    client_socket, client_address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
