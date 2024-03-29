"""
Student code for Word Wrangler game
https://py2.codeskulptor.org/#user48_UjjkYWVSPd_2.py
"""

import urllib3
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import poc_wrangler_provided_ignore as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    copied_list = list1[:]
    removed_duplicates = []

    while copied_list:
        element = copied_list.pop(0)
        if element not in removed_duplicates:
            removed_duplicates.append(element)

    return removed_duplicates


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    return [element for element in list1 if element in list2]


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    if not list1 or not list2:
        return list1 or list2

    result = []
    dummy_i, dummy_j = 0, 0
    while len(result) < len(list1) + len(list2):
        if list1[dummy_i] < list2[dummy_j]:
            result.append(list1[dummy_i])
            dummy_i += 1
        else:
            result.append(list2[dummy_j])
            dummy_j += 1
        if dummy_i == len(list1) or dummy_j == len(list2):
            result.extend(list1[dummy_i:] or list2[dummy_j:])
            break

    return result


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1

    middle = len(list1) / 2
    left = merge_sort(list1[:middle])
    right = merge_sort(list1[middle:])

    return merge(left, right)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if not word:
        return ['']

    first = word[0]
    rest = word[1:]

    rest_strings = gen_all_strings(rest)
    rest_strings_copy = list(rest_strings)

    for item in rest_strings_copy:
        for index in range(len(item)):
            rest_strings.append(item[:index] + first + item[index:])
        rest_strings.append(item + first)
    return rest_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # for urllib2:
    # return [word.strip() for word in urllib2.urlopen(codeskulptor.file2url(filename)).readlines()]
    return urllib3.PoolManager().request('GET', codeskulptor.file2url(filename)).data.split()


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)


# Uncomment when you are ready to try the game
run()
