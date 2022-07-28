# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the setly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import json
import os
import random
import string
import time
import requests
from typing import Dict, List


def give_me_five() -> int:
    """Returns the integer five."""
    return 5


def password_please() -> str:
    """Returns a string, 8 or more characters long, contains at
    least one upper case letter and one lowercase letter.
    TIP: don't put in a real password!"""
    return "123456Ab"


def list_please() -> list:
    """Returns a list, you can put anything in the list."""
    return []


def int_list_please() -> list:
    """Returns a list of integers, any integers are fine."""
    return [1, 2]


def string_list_please() -> list:
    """Returns a list of strings, any string are fine."""
    return ["a", "b"]


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    return {}


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    if some_number == 5:
        return True
    else:
        return False


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    return some_number - 5


def greet(name="Towering Timmy") -> str:
    """Return a greeting.
    return a string of "Well hello, " and the name argument.
    E.g. if given as "Towering Timmy" it should
         return "Well hello, Towering Timmy"
    """
    return f"Well hello, {name}"


def one_counter(input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of 1s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 2
    """
    count = 0
    for thing in input_list:
        if thing == 1:
            count += 1
    return count


def n_counter(search_for_this, input_list=[1, 4, 1, 5, 1, 1]) -> int:
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0
    for thing in input_list:
        if thing == search_for_this:
            count += 1
    return count


def fizz_buzz() -> List:
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."

    from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special,
    and a string if it is. E.g.
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14,
         'FizzBuzz', 16, 17, ...]
    """
    fizz_buzz_list = []
    # your code here
    for number in range(1, 101):
        appendthis = ""
        special = False
        if (number % 3) == 0:
            appendthis += "Fizz"
            special = True
        if (number % 5) == 0:
            appendthis += "Buzz"
            special = True
        if special == False:
            appendthis = int(number)
        fizz_buzz_list.append(appendthis)

    return fizz_buzz_list


def set_it_on_fire(input_string="very naughty boy") -> str:
    """Interleave the input_string with the 🔥 emoji.

    Given any string, interleave it with 🔥. Also make it be upper case.
    e.g. "very naughty boy" should return the string
    "🔥V🔥E🔥R🔥Y🔥 🔥N🔥A🔥U🔥G🔥H🔥T🔥Y🔥 🔥B🔥O🔥Y🔥"
    TIP: strings are pretty much lists of chars.
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a 🔥 on both ends of the string.
    """
    list_input_string = list(input_string)
    final_string = "🔥"
    for letter in list_input_string:
        final_string += letter.upper() + "🔥"
    return final_string


def pet_filter(letter="a") -> List:
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
        "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken", 
        "guinea pig", "donkey", "duck", "water buffalo", "python", "scorpion",
        "western honey bee", "dromedary camel", "horse", "silkmoth", 
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca", 
        "guineafowl", "ferret", "muscovy duck", "barbary dove", "cichlid",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi", 
        "canary", "society finch", "fancy mouse", "siamese fighting fish", 
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
    ]
    # fmt: on
    filtered = []

    for pet in pets:
        appendboolean = False

        for character in pet:
            if character == letter:
                appendboolean = True

        if appendboolean == True:
            filtered.append(pet)

    return filtered


def best_letter_for_pets() -> str:
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    TIP: use the function you just wrote to help you here!
    TIP: you've seen this before in the pokedex.
    """
    import string

    the_alphabet = string.ascii_lowercase
    most_popular_letter = ""
    longest_len_pet_filter = -1

    for letter in the_alphabet:

        len_pet_filter = len(pet_filter(letter))

        if longest_len_pet_filter < len_pet_filter:
            longest_len_pet_filter = len_pet_filter
            most_popular_letter = letter

    return most_popular_letter


def make_filler_text_dictionary() -> Dict:
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library
    """
    # With requests imported

    # url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="

    wd = {}

    for length in range(3, 8):
        list_words = []
        for number_words in range(0, 4):
            url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
            r = requests.get(url)
            list_words.append(r.text)
        wd[length] = list_words

    return wd


def random_filler_text(number_of_words=200) -> str:
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library,
        e.g. random.randint(low, high)
    """

    # With random imported

    my_dict = make_filler_text_dictionary()
    words = []

    for word_length in range(0, number_of_words):
        random_length = random.randint(3, 7)
        random_word = random.randint(0, 3)
        words.append(my_dict[random_length][random_word])

    return " ".join(words)


def fast_filler(number_of_words=200) -> str:
    """Makes filler text, but really fast.

    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_cache.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the
    dictionary into and out of the file. Be careful when you read it back in,
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """

    fname = "dict_cache.json"
    paragraph = ""
    words = []

    try:
        with open(fname, "r", encoding="utf-8") as dict_filler_text_file:
            loadthis = dict_filler_text_file.read()
            my_dict = json.loads(loadthis)
            print("Loaded")
    except Exception as e:
        with open(fname, "w", encoding="utf-8") as dict_filler_text_file:
            my_dict = make_filler_text_dictionary()
            savethis = json.dumps(my_dict)
            dict_filler_text_file.write(savethis)
            print("Saved")

        with open(fname, "r", encoding="utf-8") as dict_filler_text_file:
            loadthis = dict_filler_text_file.read()
            my_dict = json.loads(loadthis)
            print("Loaded")

    for word_length in range(0, number_of_words):
        random_length = str(random.randint(3, 7))
        random_word = random.randint(0, 3)
        words.append(my_dict[random_length][random_word])
        return_this = " ".join(words)
    return_this = return_this.capitalize() + "."
    return return_this


if __name__ == "__main__":
    print("give_me_five", give_me_five(), type(give_me_five()))
    print(
        "strong_password_please",
        password_please(),
        type(password_please()) == str,
    )
    print("int_list_please", int_list_please(), type(int_list_please()) == list)
    print(
        "string_list_please", string_list_please(), type(string_list_please()) == list
    )
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", one_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", set_it_on_fire())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(4):
        print(i, fast_filler(number_of_words=20), "\n")
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
