from lots_of_useful.things import *

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
    'Along the way we will pause & touch on the following ideas:',
    '',
    '    * empathetic coding',
    '    * coding with care & kindness',
    '    * writing code like writing stories',
    '    * writing code in our own idiolect',
    '    * coding as your tool',
    '    * python exception handling as a model for empathy',
    '    * concrete poetry / fluxus',
    '    * de-mystifying programming'
]

schedule = [
    # 'An introduction (10 mins)',
    # 'A presentation on exceptions in Python (20 mins)',
    # 'An activity (20 mins)',
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
if things_you_will_need:
    print('What will you need:')
    for thing_you_will_need in things_you_will_need:
        take_a_breath(with_space = False)
        print('%s* %s' % ((' ' * 5), thing_you_will_need))
    take_a_breath()
