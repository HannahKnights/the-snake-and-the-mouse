"""
Here are some examples of using
to go with python introductions/4-types-and-attributes.py

To run this:
    python introductions/4-types-and-attributes-examples.py
"""

# example 1...

this_is_a_list = [
    'this',
    'that',
    'other'
]

this_is_a_list.append('more things')
this_is_a_list.append('what a long list!')

print('Here is a long list of things:')
for thing_in_the_list in this_is_a_list:
    print(thing_in_the_list)

# example 2
# when you print the item in the list you could add a bullet-point

print('\n')
print('Here is a long list of things:')
for thing_in_the_list in this_is_a_list:
    print(' * ' + thing_in_the_list)

# example 3...

print('\n')

lucky_number = 7
number_of_seconds_a_fish_can_remember = '3' # apparently?

print('A fish has a ' + number_of_seconds_a_fish_can_remember + ' second memory')

# example 4...

('\n')
print('If...')
print(lucky_number)
print('is lucky, does that make...')
print(lucky_number + lucky_number)
print('extra lucky?')

# example 5...

('\n')
print('If you wrap me, caringly, in a `str()`, I become a ' + str(lucky_number) + 'ssssstring')
print('.. now that is lucky')
