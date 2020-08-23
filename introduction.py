from lots_of_useful.things import *


def starry_introduction():
    star = '*'
    sky = ' '
    line_length = 100
    numbers_list = [number for number in range(line_length / 2)]
    for i in range(0,60):
        if i == 30:
            print('%sW E L C O M E' % (' ' * 20))
        line = ''
        while len(line) < line_length:
            shuffle(numbers_list)
            line += (sky * numbers_list[0])
            line += (star)
        take_a_breath(length_of_breath = 0.2)
        print(line)

title = [
    'the snake and the mouse',
    '~' * 25,
    'a gentle introduction to Python through',
    'poetry &',
    '     s',
    '     c',
    '     r',
    '     o',
    '     l',
    '     l',
    '     i',
    '     n',
    '     g',
    '     words'
]

introduction = [
    'The aim of this workshop is to teach a basic introduction to the Python programming language through the hands-on experience of writing some low-fi, light-weight and fun Python code.',
    'We (the mouse) will work with Python (the snake) to make some playful text-based poem-like work - taking inspiration from the form of concrete poetry.',
    '',
    'Along the way we will touch on the following ideas:',
    '',
    '    * concrete poetry /artists practicing with text-based work',
    '    * coding with empathy, care & kindness',
    '    * writing code like writing stories',
    '    * writing code in our own idiolect (https://www.google.com/search?q=idiolect)',
    '    * coding as your tool'
]

schedule = [
    'A brief introduction to python, looking at what it does / does not understand',
    'A look at some examples of artists working with text',
    'Making some text-based python scripts ourselves',
]

things_you_will_need = [
    'An internet connection',
    'A laptop or desktop computer is preferable to a phone or desktop',
    'NO previous technical skills are required'
]

# Begin..

starry_introduction()

new_page()

# title
for num, line in enumerate(title):
    if num == 0:
        print('\n')
    print('%s%s') % (' ' * (num * 5), line)
take_a_breath()

# introduction
for line in introduction:
    take_a_breath(with_space = False)
    print(line)
take_a_breath()

# schedule
if schedule:
    print('What will we be doing today:')
    for scheduled_item in schedule:
        take_a_breath(with_space = False)
        print('%s* %s' % ((' ' * 5), scheduled_item))
    take_a_breath()

# things_you_will_need
# if things_you_will_need:
#     print('What will you need:')
#     for thing_you_will_need in things_you_will_need:
#         take_a_breath(with_space = False)
#         print('%s* %s' % ((' ' * 5), thing_you_will_need))
#     take_a_breath()
