import asyncio
import websockets

async def echo(websocket, path):
    """
    Cette fonction asynchrone est appelée à chaque fois qu'un client se connecte.
    Elle reçoit un message du client, et renvoie le même message.
    """
    async for message in websocket:
        print(f"Received message from client: {message}")
        await websocket.send(message)

if __name__ == "__main__":
    """
    Ce bloc de code démarre le serveur WebSocket.
    Il écoute sur 'localhost' et le port 8765.
    """
    start_server = websockets.serve(echo, "localhost", 8766)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
