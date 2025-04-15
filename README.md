---

# 🗺️ Treasure Hunt Game

This project is a treasure hunt game built using a client-server architecture. The game runs on two separate systems: one for the server and one for the client. The client and server communicate securely over SSL/SSH, allowing players to make treasure hunt moves interactively.

## 🧠Overview

- **Client File:** `Treasure_hunt_client.py`
- **Server File:** `Treasure_hunt_server.py`

The server randomly chooses a treasure location on a 10x10 grid, while each client controls a player via a graphical user interface (GUI). Players issue move commands (using keyboard keys) and the client displays updates, including the current map. When a player reaches the treasure location, a congratulatory message is sent.

## How It Works

1. **Server Responsibilities:**
   - Generates random treasure coordinates (within a 10x10 grid).
   - Listens for incoming client connections on port 9993.
   - Sends the current game map (with player positions and the treasure) to the clients.
   - Receives move commands from clients, updates their positions, and checks if the treasure has been found.
   - Notifies the appropriate client with a "Congratulations! You found the treasure!" message when the treasure is found.

2. **Client Responsibilities:**
   - Connects to the server using its designated IP address and port.
   - Presents a GUI (built with Tkinter) where moves and game updates are displayed.
   - Sends move commands (e.g., `w`, `e`, `n`, `s`) to the server based on player input.
   - Updates the on-screen map based on data received from the server.
   - Ends the game session if the treasure is found or if the player enters `quit`.

##⚙️ Setup and Execution

### Prerequisites

- Python 3.x
- Standard Python libraries: `socket`, `threading`, `tkinter` (for the client)
- Ensure SSL/SSH is properly configured on your network if using encryption

### Running the Server 💻 (On System 1)

Open a terminal or command prompt on the system designated as the server, then run:

```bash
python Treasure_hunt_server.py
```

**Expected Output on the Server Terminal:**

```
Server is listening... Treasure is located at position (X, Y)
```
✅ Server is now ready to accept client connections.

*Note:* `(X, Y)` will be randomly generated numbers within the range `0-9`.

### Running the Client 💻 (On System 2)

On the client system, open a terminal and run:

```bash
python Treasure_hunt_client.py
```

**Expected Behavior on the Client:**

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

## Secure Connection Details

Although the project description mentions secure SSL or SSH-based communication between systems, ensure that:

- The proper SSL/SSH certificates and keys are set up on both the server and client machines.
- The network permits SSL/SSH connections on the designated port.

## Troubleshooting

- **Client Connection Issues:** Verify that the server's IP address and port are correctly configured in the client file.
- **Network Restrictions:** Confirm that your firewall or network settings allow SSL/SSH connections on port 9993.
- **GUI Not Displaying:** Ensure that Python's Tkinter library is installed and functioning on your client system.

---
