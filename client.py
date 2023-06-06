import asyncio
import websockets

async def talk_to_server(host='localhost', port=8766):
    """
    Cette fonction se connecte au serveur WebSocket, envoie un message, et reçoit une réponse.
    """
    async with websockets.connect(f"ws://{host}:{port}") as websocket:
        message = "Hello, Server!"
        print(f"Sending message to server: {message}")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received message from server: {response}")

if __name__ == "__main__":
    """
    Ce bloc de code démarre le client WebSocket et le fait se connecter au serveur pour envoyer un message.
    """
    asyncio.get_event_loop().run_until_complete(talk_to_server())
