import eventlet

eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

pixels = [['#FFFFFF' for _ in range(64)] for _ in range(64)]

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("draw_pixel")
def handle_draw(data):
    x, y, color = data["x"], data["y"], data["color"]
    pixels[y][x] = color
    emit("update_pixel", data, broadcast=True)

@socketio.on("get_canvas")
def handle_get_canvas():
    emit("load_canvas", pixels)

@socketio.on("clear_canvas")
def handle_clear_canvas():
    global pixels
    pixels = [['#FFFFFF' for _ in range(64)] for _ in range(64)]
    emit("load_canvas", pixels, broadcast=True)

background_color = '#FFFFFF'

@socketio.on("change_bgcolor")
def handle_change_bgcolor(data):
    global background_color, pixels
    background_color = data["color"]
    pixels = [[background_color for _ in range(64)] for _ in range(64)]
    emit("load_canvas", pixels, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
