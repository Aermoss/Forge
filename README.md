# Forge Engine
A simple 2D game engine written in Python with pygame.

## Getting Started
1) Install Python
2) Open cmd/terminal and type:

```
pip install aerforge
```

## Examples
# Creating a window
``` python
from aerforge import *

forge = Forge()

@forge.event
def update():
    pass

forge.run()
```

# Creating a rect
``` python
from aerforge import *

forge = Forge()

class Rect(Entity):
    def __init__(self):
        super().__init__(
            window = forge,
            shape = shape.Rect,
            width = 20,
            height = 20,
            x = 0,y = 0,
            color = color.Color(0, 255, 255)
        )

        self.center()

rect = Rect()

@forge.event
def update():
    pass

forge.run()
```
