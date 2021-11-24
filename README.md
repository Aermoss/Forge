# AerForge
A game engine made with SDL.

## Getting Started
1) Install Python
2) Open cmd/terminal and type:

```
pip install AerForge
```

## Examples
# Creating a window
``` python
from aerforge import *

forge = Forge()

while True:
    forge.updateall()
```

# Creating a cube
``` python
from aerforge import *

forge = Forge()

class Cube(Entity):
    def __init__(self):
        super().__init__(
            window = forge,
            shape = shape.Rect,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = color.Color(0, 255, 255)
        )

        self.center()

cube = Cube()

while True:
    forge.drawall()
    forge.updateall()
```