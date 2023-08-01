from arcade import *
MOVEMENT_SPEED = 4
def on_key_press(self, symbol, modifiers ):
    if symbol == key.UP:
        self.fish.change_y = MOVEMENT_SPEED
    elif symbol == key.DOWN:
        self.fish.change_y = -MOVEMENT_SPEED
    elif symbol == key.LEFT:
        self.fish.change_x = -MOVEMENT_SPEED
    elif symbol == key.RIGHT:
        self.fish.change_x = MOVEMENT_SPEED

def on_key_release(self, symbol, modifiers):
    if symbol == key.UP or symbol == key.DOWN:
        self.fish.change_y = 0
    elif symbol == key.LEFT or symbol == key.RIGHT:
        self.fish.change_x = 0