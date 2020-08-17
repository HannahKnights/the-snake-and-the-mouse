from lots_of_useful.things import *

"""
This python script will "read" a haiku by Gracie Starkie. I found it
printed on a bottle of green tea (https://www.are.na/block/8357062)
and later discovered the haiku was one of the winners of a celebrated Haiku
competition in Japan (https://www.theguardian.com/uk-news/2017/sep/01/british-schoolgirl-named-first-non-japanese-winner-of-haiku-contest)


Features of the display of this poem:
    - Each word of the poem will be "read" separately and spaced at random intervals
    # - Each line of the poem will be indented more to create a diagonal form
    # - There will be a pause of 2.5 seconds after each line
    # - If the line ends in a full stop (.) we will pause for 5 seconds
    # - After we have printed the poem we will print the name of the author and the title of the poem

You can see it like so:

python my-my_muddled_thoughts.py
"""

my_muddled_thoughts = [
    'freshly mown grass',
    'clinging to my shoes',
    'my muddled thoughts'
]

# READ THE POEM...
new_page()
# a space at the beginning
print('\n')


for each_line in my_muddled_thoughts:
    this_line = []
    a_space = ' '
    for each_word in each_line.split(a_space):
        random_number = pick_a_random_number(to_that = 40)
        this_line.append((' ' * random_number) + each_word)
    print(''.join(this_line))
    take_a_breath()
