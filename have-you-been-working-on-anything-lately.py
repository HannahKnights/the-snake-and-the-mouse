from lots_of_useful.things import pick_a_random_number
from random import shuffle

"""
This python script will create a poem for you out of the 100 most
common english words. It will save the poem for you as a file.

You can use it like so:

python have-you-been-working-on-anything-lately.py

"""

the_100_most_common_words = [
    'a',
    'about',
    'all',
    'also',
    'and',
    'as',
    'at',
    'be',
    'because',
    'but',
    'by',
    'can',
    'come',
    'could',
    'day',
    'do',
    'even',
    'find',
    'first',
    'for',
    'from',
    'get',
    'give',
    'go',
    'have',
    'he',
    'her',
    'here',
    'him',
    'his',
    'how',
    'I',
    'if',
    'in',
    'into',
    'it',
    'its',
    'just',
    'know',
    'like',
    'look',
    'make',
    'man',
    'many',
    'me',
    'more',
    'my',
    'new',
    'no',
    'not',
    'now',
    'of',
    'on',
    'one',
    'only',
    'or',
    'other',
    'our',
    'out',
    'people',
    'say',
    'see',
    'she',
    'so',
    'some',
    'take',
    'tell',
    'than',
    'that',
    'the',
    'their',
    'them',
    'then',
    'there',
    'these',
    'they',
    'thing',
    'think',
    'this',
    'those',
    'time',
    'to',
    'two',
    'up',
    'use',
    'very',
    'want',
    'way',
    'we',
    'well',
    'what',
    'when',
    'which',
    'who',
    'will',
    'with',
    'would',
    'year',
    'you',
    'your'
]

a_poem = []
number_of_lines = pick_a_random_number(from_this = 1, to_that = 6)
last_line_number = number_of_lines - 1

for line_number in range(number_of_lines):
    this_line = []
    is_the_last_line = True if last_line_number == line_number else False
    number_of_words = pick_a_random_number(from_this = 1, to_that = 5)
    for word_number in range(number_of_words):
        shuffle(the_100_most_common_words)
        this_line.append(the_100_most_common_words[0])
    this_line = ' '.join(this_line)
    a_poem.append(this_line + ('' if is_the_last_line else ','))

poem_title = a_poem[0].replace(',', '') # the first line of the poem
poem_filename = '%s.txt' % poem_title.replace(' ', '-') # the first line of the poem
finished_poem = '\n'.join(a_poem)

finished_poem_file = open(poem_filename, 'w')
finished_poem_file.write(finished_poem)
finished_poem_file.close()

print('\n')
print('Hey, I wrote a poem for you')
print('It\'s called \'%s\'' % poem_title)
print('\n')
print(finished_poem)
print('\n')
print('%s' % poem_filename)
print('\n')
