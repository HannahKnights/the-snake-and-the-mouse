from lots_of_useful.things import *

"""
This python script will run through a few links to practitioners within
art / poetry who manipulate and use text in some way

You can see it like so:

python poetry-text-art-inspiration.py
"""

words_to_highlight = [
    'visually',
    'verbally',
    'reduced',
    'consumed',
    'reformed',
    'circulated',
    'pauses',
    'flashes',
    'phrasing'
]

inspirations = [
    # concrete poetry quote
    '"Concrete poets endeavoured to create a universal language that could be read both visually and verbally a form of compressed communication for a new world in which language had begun to be rapidly reduced consumed reformed and circulated." (From Bryony Gillard\'s essay: http://www.documnt.net/bryony-gillard-an-exploration-of-verbivocovisual-borders-and-margins)',
    # womens contribution to concrete poetry
    'A collection of concrete poetry contributions by women: https://www.are.na/sarah-hamerman/women-in-concrete-poetry',
    # use of technology, like typewritters in patern creation
    'Anni Albers (https://www.are.na/block/3926891)',
    # more direct visual representation, "visual" poetry
    'Mary Ellen Solt, Forsythia (https://www.are.na/block/3199184)',
    # a classic conrete poet
    'Ian Hamilton Finlay, The Blue and the Brown Poems (https://www.are.na/block/8414719)',
    # Artists using text as a material...
    'Adam Pendleton, The Silence Perpetuates (https://www.are.na/block/8414629)',
    # homour and playing with the meaning of words..
    'Kay Rosen, Steps (https://www.are.na/block/8414768)',
    # as murals, with flourishes
    'Lawrence Weiner (https://www.are.na/block/8414711)',
    # jenny holzer, artist working with text - pauses, flashes, phrasing...
    'Jenny Holzer (https://www.are.na/block/8411464)\npauses flashes phrasing',
]

def display_inspirational_link(inspiration):
    """
    - Give the link a bit of space above (4 lines)
    - Give the link a bit of space below (2 lines)
    - If there is a comma in the text, break the line
    - If the text includes a word to highlight (from words_to_highlight), capitalise the word and display it on a separate line, indented 4 spaces
    """
    print('\n\n\n\n') # 4 new lines
    # find any keywords
    for word_to_highlight in words_to_highlight:
        if word_to_highlight in inspiration:
            inspiration = inspiration.replace(word_to_highlight, ('\n\n' + word_to_highlight.upper() + '\n\n'))
    print(',\n'.join(inspiration.split(',')))
    print('\n\n') # 2 new lines

for inspiration in inspirations:
    last_link = True if inspiration == inspirations[-1] else False
    display_inspirational_link(inspiration)
    if not last_link:
        raw_input('and more...')
        new_page()
