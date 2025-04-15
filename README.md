Here's the updated **README** with your requested changes:

---

# 🗺️ Treasure Hunt Game

This project is a treasure hunt game built using a client-server architecture. The game runs on two separate systems: one for the server and one for the client. The client and server communicate, allowing players to make treasure hunt moves interactively.

## 🧠 Overview

- **Client File:** `Treasure_hunt_client.py`
- **Server File:** `Treasure_hunt_server.py`

The server randomly chooses a treasure location on a 10x10 grid, while each client controls a player via a graphical user interface (GUI). Players issue move commands (using keyboard keys), and the client displays updates, including the current map. When a player reaches the treasure location, a congratulatory message is sent.

## How It Works

1. **Server Responsibilities:**
   - Generates random treasure coordinates (within a 10x10 grid).
   - Listens for incoming client connections on port `9993`.
   - Sends the current game map (with player positions and the treasure) to the clients.
   - Receives move commands from clients, updates their positions, and checks if the treasure has been found.
   - Notifies the appropriate client with a "Congratulations! You found the treasure!" message when the treasure is found.

2. **Client Responsibilities:**
   - Connects to the server using its designated IP address and port.
   - Presents a GUI (built with Tkinter) where moves and game updates are displayed.
   - Sends move commands (e.g., `w`, `e`, `n`, `s`) to the server based on player input.
   - Updates the on-screen map based on data received from the server.
   - Ends the game session if the treasure is found or if the player enters `quit`.

## ⚙️ Setup and Execution

### Prerequisites

- Python 3.x
- Standard Python libraries: `socket`, `threading`, `tkinter` (for the client)

---

### Steps to Run the Game on Two Different Systems

#### 1. Server Side (System 1)

1. **Run the Server Code:**
   - Open a terminal on the system that will act as the **server**.
   - Run the server file with this command:

     ```bash
     python Treasure_hunt_server.py
     ```

2. **Server Output:**
   - The server will print the message `Server is listening... Treasure is located at position (X, Y)`, where `(X, Y)` is a random coordinate for the treasure.

3. **Network Configuration:**
   - **Important:** Make sure that the server machine is accessible from the client machine over the network.
   - Ensure that the **server’s IP address** (shown in the code as `server_ip = "192.168.00.000"`) is given(check your system ip address and replace it) and reachable by the client machine. You should verify the server's IP address and replace it in the client code.
   - If you're using a **local network**, both systems should be on the same network.
   - If you're using **remote systems**, ensure that your firewall or security rules allow traffic on port `9993`.

#### 2. Client Side (System 2)

1. **Run the Client Code:**
   - Open a terminal on the **client** system.
   - Run the client file with this command:

     ```bash
     python Treasure_hunt_client.py
     ```

2. **Configure the Client to Connect to the Server:**
   - In the client code, ensure the server's IP address is correct:

     ```python
     server_ip = "192.168.00.000"  # Replace with the actual server IP address
     ```

   - The client will try to connect to the server's IP on port `9993`.

3. **Client GUI:**
   - The client will open a GUI window where the player will be prompted to enter their name.
   - Once entered, the game instructions and the map will be displayed.

---

### Troubleshooting

- **Client Connection Issues:** Verify that the server's IP address and port are correctly configured in the client file.
- **Network Restrictions:** Confirm that your firewall or network settings allow connections on port `9993`.
- **GUI Not Displaying:** Ensure that Python's Tkinter library is installed and functioning on your client system.

---

### Expected Behavior on the Client:

- **Graphical User Interface (GUI) Appearance:**
  - A window opens with a text area for displaying messages and the game map.
  - Initially, the client will prompt for the player's name (displayed in the text area).

- **After Entering Your Name:**
  - You will see a welcome message along with game instructions:
    ```
    Instructions:
    - Type 'w' to move west
    - Type 'e' to move east
    - Type 'n' to move north
    - Type 's' to move south
    ```

- **During Gameplay:**
  - Each move you enter and send (by pressing the Return key) updates the map displayed on the GUI.
  - When you reach the treasure's location, the game will display:
    ```
    Congratulations! You found the treasure!
    ```

- **To Exit the Game:**
  - Type `quit` into the move input area and press Return.

---

This should now reflect the correct setup and execution process, without mentioning SSL/SSH. Let me know if you need any further adjustments! 😊
