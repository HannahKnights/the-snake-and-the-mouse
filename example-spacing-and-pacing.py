"""
    A poem which looks like a staircase, but each step is laid with a pause

    - the pause gets bigger each time with the 'take_a_breath' function,
    the `length_of_breath` getting longer

    python example-spacing-and-pacing.py
"""
from lots_of_useful.things import *

new_page()
print('a')
take_a_breath(length_of_breath = 0.25)
print('    simple')
take_a_breath(length_of_breath = 0.5)
print('        piece')
take_a_breath(length_of_breath = 0.75)
print('            of')
take_a_breath(length_of_breath = 1)
print('                text')
take_a_breath(length_of_breath = 1.25)
print('                    which')
take_a_breath(length_of_breath = 1.5)
print('                        looks')
take_a_breath(length_of_breath = 1.75)
print('                            like')
take_a_breath(length_of_breath = 2)
print('                                a')
take_a_breath(length_of_breath = 2.5)
print('                                    staircase')
take_a_breath(length_of_breath = 1)
