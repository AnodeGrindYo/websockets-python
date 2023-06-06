import asyncio
import sys
from io import StringIO
import unittest
import websockets
from client import talk_to_server

class TestClient(unittest.TestCase):
    async def fake_server(self, websocket, path):
        """
        Cette fonction est utilisée pour simuler un serveur WebSocket.
        Elle reçoit un message du client et renvoie le même message.
        """
        message = await websocket.recv()
        await websocket.send(message)

    def test_talk_to_server(self):
        """
        Ce test vérifie que le client envoie et reçoit correctement les messages du serveur.
        """
        start_server = websockets.serve(self.fake_server, "localhost", 8767)
        asyncio.get_event_loop().run_until_complete(start_server)
        
        # Redirige la sortie standard vers une variable
        captured_output = StringIO()
        sys.stdout = captured_output

        # Exécute le client
        asyncio.get_event_loop().run_until_complete(talk_to_server('localhost', 8767))

        # Récupère la sortie capturée
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Vérifie que le message de log du client est présent dans la sortie
        self.assertIn("Sending message to server: Hello, Server!", output)

        # Vérifie que le message du serveur est présent dans la sortie
        self.assertIn("Received message from server: Hello, Server!", output)

if __name__ == "__main__":
    unittest.main()
