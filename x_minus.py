import json
import pyglet
from pyglet import shapes


config = json.load(open("configs.json", 'r'))

X = config['x']
Y = config['y']

window = pyglet.window.Window(X, Y)
batch = pyglet.graphics.Batch()


y = shapes.Line(x=X // 2, y=0, x2=X // 2, y2=Y, batch=batch)
x = shapes.Line(x=0, y=Y // 2, x2=X, y2=Y // 2, batch=batch)


line = shapes.Line(x=0, y=Y, x2=X, y2=0, batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()