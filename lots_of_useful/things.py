import os
import time
from random import shuffle


def new_page():
    os.system('clear')

def blink(words, length_of_blink = 1):
    print(words)
    take_a_breath(length_of_breath = length_of_blink)
    new_page()

def starry_introduction():
    star = '*'
    sky = ' '
    line_length = 100
    numbers_list = [number for number in range(line_length / 2)]
    line_length = 100
    for i in range(0,100):
        if i == 50:
            print('%sW E L C O M E' % (' ' * 20))
        line = ''
        while len(line) < line_length:
            shuffle(numbers_list)
            line += (sky * numbers_list[0])
            line += (star)
        take_a_breath(length_of_breath = 0.3)
        print(line)

def take_a_breath(number_of_breaths = 1, with_space = True, length_of_breath = 4):
    """
        the `take_a_breath` function creates a small pause. When you use the
        `take_a_breath` fucntion then the Python code will stop running for
        however long we specify the `length_of_breath` in number of seconds.
    """
    for number in range(0, number_of_breaths):
        time.sleep(length_of_breath)
        if with_space:
            print('\n')

def pick_a_random_number(from_this = 0, to_that = 100):
    """
        Pick a random number from between a low and high option
    """
    list_of_numbers = [number for number in range(from_this, to_that + 1)]
    # shuffle them
    shuffle(list_of_numbers)
    # return the first one
    return list_of_numbers[0]
