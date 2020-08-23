"""
python (the snake):
    - has expectations about what is possible for cerain "types" (the definition of type-cast!)
    - some things have specific actions associated with them...
    - some things cannot be combined together...

Tips:

    this_is_a_list = [
        'this',
        'that',
        'other'
    ]

    - you can add new things to the list using 'append'
    but, you cannot add new things to a string using 'append'

    this_is_a_number = 1
    this_is_a_string = '100' # i know it looks like a number ! but there are quotes around it

    - you can add a string to a string

    new_thing = this_is_a_string + this_is_a_string

    - you can add a number to a number

    new_number = this_is_a_number + this_is_a_number

    - but, you can't add a string to a number... !

    - you can turn a number into a string !

    see these example by looking at the code and/ or running:
        python introductions/4-types-and-attributes-examples.py

python introductions/4-types-and-attributes.py
"""

things_in_the_sky = [
    'sun',
    'moon',
    'stars',
    'planets',
    'satellite',
    'clouds',
    'rain',
    'wind'
]

'sky'.append('birds')

for thing_number, a_thing_in_the_sky in enumerate(things_in_the_sky):
    print(thing_number + '. ' + a_thing_in_the_sky)
