#!/usr/bin/env python
from websocket import create_connection

# pip install websocket-client


def short_lived_connection():

    ws = create_connection("ws://localhost:8000/")
    print("Sending 'Hello Server'...")
    ws.send("Hello, Server")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received '%s'" % result)
    ws.close()


if __name__ == "__main__":
    short_lived_connection()
