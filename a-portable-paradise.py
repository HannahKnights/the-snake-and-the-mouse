from lots_of_useful.things import *

"""
This python script will "read" a poem called `A portable paradise` by
Roger Robinson (https://nationalpoetryday.co.uk/poem/a-portable-paradise/)

Features of the display of this poem:
    - Each line of the poem will be "read" separately
    - Each line of the poem will be indented more to create a diagonal form
    - There will be a pause of 2.5 seconds after each line
    - If the line ends in a full stop (.) we will pause for 5 seconds
    - After we have printed the poem we will print the name of the author and the title of the poem

You can see it like so:

python a-portable-paradise.py
"""

poem_name = 'A portable paradise'
authors_name = 'Roger Robinson'

# here is the poem, line by line
a_portable_paradise = [
    'And if I speak of Paradise,',
    'then I\'m speaking of my grandmother',
    'who told me to carry it always',
    'on my person, concealed, so',
    'no one else would know but me.',
    'That way they can\'t steal it, she\'d say.',
    'And if life puts you under pressure,',
    'trace it\'s ridges in your pocket,',
    'smell its piney scent on yout handkerchief,',
    'hum its anthem under your breath.',
    'And if your stresses are sustained and daily,',
    'get yourself to an empty room - be it hotel,',
    'hostel or hovel - find a lamp',
    'and empty your paradise onto a desk:',
    'your white sands, green hills and fresh fish.',
    'Shine the lamp on it like the fresh hope',
    'of morning, and keep staring at it till you sleep.'
]

last_line = a_portable_paradise[-1] # it is useful to know which line is the last line, so we can print the credits
number_of_spaces_for_the_indent = 0 # we will lay the poem out diagnoally, this sets a starting position of 0

# READ THE POEM...

# a space at the beginning
print('\n')

for each_line in a_portable_paradise:
    this_line = each_line
    is_the_last_line = True if this_line == last_line else False
    number_of_spaces_for_the_indent = number_of_spaces_for_the_indent + 2 # to be increased by 2 each time
    print((' ' * number_of_spaces_for_the_indent) + this_line)
    if this_line.endswith('.'):
        take_a_breath(length_of_breath = 5, with_space = False)
    else:
        take_a_breath(length_of_breath = 2.5, with_space = False)
    if is_the_last_line:
        print('\n')
        print((' ' * number_of_spaces_for_the_indent) + ('*' * 10))
        print((' ' * number_of_spaces_for_the_indent) + poem_name)
        print((' ' * number_of_spaces_for_the_indent) + 'by ' + authors_name)

# a space at the end
print('\n')
