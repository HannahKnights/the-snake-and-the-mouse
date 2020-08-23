"""
Here are some examples of using `if` and `else` and `for`
to go with python introductions/3-arrangements.py

To run this:
    python introductions/3-arrangements-examples.py
"""

"""
'if' this is true, do something

    OR

'if' this is true, do something, otherwise do this other thing
"""

# example 1...

print('\n')

this_is_true = True

if this_is_true:
    print('It is true! Do something...')

# example 2...

print('\n')

if this_is_true:
    print('Do this thing')
else:
    print('Do this other thing')

# example 3...

print('\n')

you_understand = False

if you_understand:
    print('I totally understand')
else:
    print('This is confusing, I do not understand')


# EXAMPLE 2
"""
'for' every item on this list, do something

"""

# example 4...
we_are_talking_about = ['snakes', 'mice']
print('\n')
print('We are talking about...')
for thing in we_are_talking_about:
    print(thing)

# example 5...
# after the use of `for` you are giving the same
# name to each item in the 'list'
# it doesn't matter what that is though...

print('\n')
print('We are still talking about...')
for this_word_can_be_anything in we_are_talking_about:
    print(this_word_can_be_anything)
