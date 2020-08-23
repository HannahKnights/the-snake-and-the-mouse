"""
    A poem which will "flash" word by word or line by line

    '\n' is a new line :)

    python example-flashing-poem.py
"""
from lots_of_useful.things import *

new_page()
blink('\n  A  \n', length_of_blink = 1)
blink('\n  POEM  \n', length_of_blink = 1)
blink('\n  TO  \n', length_of_blink = 1)
blink('\n  FLASH  \n', length_of_blink = 0.2)
blink('\n  \n', length_of_blink = 0.2)
blink('\n  FLASH  \n', length_of_blink = 0.2)
blink('\n  \n', length_of_blink = 0.2)
blink('\n  FLASH  \n', length_of_blink = 0.2)
blink('\n  \n', length_of_blink = 0.2)
blink('\n  ON  \n', length_of_blink = 1)
blink('\n  BY  \n', length_of_blink = 1)
