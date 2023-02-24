import websocket
import time
import websocket_functions
import _thread

def on_message1(ws, message):
    websocket_functions.on_messagews1(ws, message)
def on_message2(ws, message):
    websocket_functions.on_messagews2(ws, message)

def on_error(ws, error):
    print("Error: ", error)


def on_close(ws):
    print("Connection closed")


def on_open1(ws):
    print("Connected to WebSocket")
    ws.send(
        '42["init",{"boardId":7}]'
    )

def on_open2(ws):
    print("Connected to WebSocket")
    ws.send(
        '42["init",{"boardId":8}]'
    )


def send_message1(ws):
    while True:
        time.sleep(25)
        ws.send("2")
        print("Sent7: 2")

def send_message2(ws):
    while True:
        time.sleep(25)
        ws.send("2")
        print("SentMVP: 2")


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws1 = websocket.WebSocketApp(
        "wss://pixelplace.io/socket.io/?EIO=3&transport=websocket",
        on_message=on_message1,
        on_error=on_error,
        on_close=on_close,
    )
    ws1.on_open = on_open1
    _thread.start_new_thread(ws1.run_forever, ())
    _thread.start_new_thread(send_message1, (ws1,))

    ws2 = websocket.WebSocketApp(
        "wss://pixelplace.io/socket.io/?EIO=3&transport=websocket",
        on_message=on_message2,
        on_error=on_error,
        on_close=on_close,
    )
    ws2.on_open = on_open2
    _thread.start_new_thread(ws2.run_forever, ())
    _thread.start_new_thread(send_message2, (ws2,))
    ws2.run_forever()