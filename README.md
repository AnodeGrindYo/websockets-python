# WebSocket avec Python

Ce repository contient un exemple simple d'utilisation de WebSockets en Python avec un serveur et un client.

## Qu'est-ce qu'un WebSocket ?

WebSocket est une technologie qui permet l'établissement d'une communication bidirectionnelle interactive entre un client (généralement un navigateur web) et un serveur. Contrairement au protocole HTTP, où la communication est initiée par le client et le serveur répond, WebSocket permet au serveur d'envoyer des données au client sans être sollicité, et vice versa.

WebSocket est particulièrement utile pour les applications qui nécessitent des mises à jour en temps réel, comme les jeux en ligne, le chat, les notifications en temps réel, etc.

## Structure du Repository

1. `server.py` : Fichier contenant le code pour un serveur WebSocket simple.
2. `client.py` : Fichier contenant le code pour un client WebSocket qui se connecte au serveur.
3. `test_client.py` : Fichier contenant des tests pour le client WebSocket.
4. `requirements.txt` : Fichier listant toutes les dépendances Python nécessaires pour exécuter le projet.

## Comment exécuter le projet ?

Assurez-vous d'avoir installé toutes les dépendances listées dans `requirements.txt`.

Pour démarrer le serveur WebSocket, exécutez la commande suivante :

```bash
python server.py
```

Pour démarrer le client WebSocket, exécutez la commande suivante dans une autre console :

```bash
python client.py
```

Pour exécuter les tests du client, utilisez la commande suivante :
```bash
python test_client.py
```

## Ressources supplémentaires

Pour plus d'informations sur WebSocket et son utilisation en Python, vous pouvez consulter les ressources suivantes :

[Documentation officielle de Python sur les asyncio - WebSocket](https://docs.python.org/3/library/asyncio-protocol.html#websockets)

[WebSocket API - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
