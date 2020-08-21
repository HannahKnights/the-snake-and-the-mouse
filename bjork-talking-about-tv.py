from lots_of_useful.things import *

"""
This python script will provide subtitles to a clip of Bjork describing
how a television works.

The ideal set-up for this is to have a browser window and a terminal
window both open in the same screen of your computer, side-by-side

In your browser window open up the following link and pause it immeadiately:
    https://www.youtube.com/watch?v=75WFTHpOw8Y&feature=youtu.be&t=31

In a terminal window run the python script (see below), you will be prompted
when to start playing the YouTube clip:

    >> python bjork-talking-about-tv.py
"""

subtitles = [
    # ('[subtitle]', [time in seconds]),
    ('But now I am curious', 31),
    ('I have switched the tv off', 33),
    ('and now I want to see how it operates', 36),
    ('How it can', 39),
    ('put me into all those weird situations', 42),
    ('So', 47),
    ('It\'s about time', 50),
    ('See', 65),
    ('This is what it looks like', 74),
    ('Look at this', 77),
    ('this looks like a city', 79),
    ('Like a little model of a city', 81),
    ('And all the houses which are here', 83),
    ('And streets', 85),
    ('This is maybe an elevator', 87),
    ('To go up there', 89),
    ('And here are all the wires', 91),
    ('These wires', 94),
    ('They really take care of all the electrons when they come through here', 98),
    ('They take care that they are powerful enough to get all the way through here', 102),
    ('I read that in a Danish book this morning', 107),
    ('And this beautiful television has put me like I said before', 114),
    ('In all sorts of situations', 117),
    ('I remember being very scared of it because',  120),
    ('An Icelandic poet told me that', 123),
    ('Not like in cinemas where', 126),
    ('the thing that throws the picture from it', 129),
    ('Just sends lights on the screen', 135),
    ('But this is different', 137),
    ('This is millions and millions of little screens', 139),
    ('Who send light on some sort of electrical light', 143),
    ('But because there\'s so many of them', 152),
    ('And infact your watching many many frames when you are watching tv', 154),
    ('You\'re head is very busy all the time to', 159),
    ('Calculate and put it all together into one picture', 163),
    ('And then because you\'re so busy doing that', 167),
    ('You don\'t watch very carefully what the program that you\'re watching is really about', 170),
    ('So you become hypnotised', 176),
    ('So all that\'s on tv it just goes directly into your brain', 177),
    ('And you stop judging if it\'s right or not', 182),
    ('So you just swallow and swallow', 184),
    ('This is what an Icelandic poet told me once', 187),
    ('And I became so scared of television that I always got headaches when I watched it', 189),
    ('But then later on when I got my danish book on television', 195),
    ('I stopped being afraid because I read the truth', 199),
    ('And that\'s the scientifical truth', 204),
    ('Which is much better', 206),
    ('You shouldn\'t let poets lie to you', 208),
]

# instructions
new_page()
take_a_breath(length_of_breath = 1)
print('We will count to 3, and then ask you to "Play video", ready?')

# count to 3...
for number in range(1, 4):
    take_a_breath(length_of_breath = 1)
    print('%s ...' % number)
# go!
take_a_breath(length_of_breath = 1)
print('"Play video!"')
take_a_breath(length_of_breath = 1)
new_page()

previous_subtitle_time = 0

for subtitle in subtitles:
    subtitle_text = subtitle[0]
    subtitle_time = subtitle[1]
    length_of_breath = subtitle_time - previous_subtitle_time if previous_subtitle_time > 0 else 0
    take_a_breath(length_of_breath = length_of_breath, with_space = True)
    new_page()
    print(('\n' * 10) + subtitle_text.lower())
    previous_subtitle_time = subtitle_time

take_a_breath()
new_page()
