"""
Student code for Word Wrangler game
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
    if not len(list1) or not len(list2):
        return list1 or list2

    result = []
    i, j = 0, 0
    while len(result) < len(list1) + len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
        if i == len(list1) or j == len(list2):
            result.extend(list1[i:] or list2[j:])
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
    all_strings_list = ['']

    if len(word) == 0:
        return all_strings_list
    else:
        rest_strings = word[1:]
        for each_string in gen_all_strings(rest_strings):
            all_strings_list.append(each_string + word[0])

    return all_strings_list

# 3 For each string in rest_strings, generate new strings by inserting the initial character,
# first, in all possible positions within the string.
# 4 Return a list containing the strings in rest_strings as well as the new strings generated in step 3.


# print ['', 'b', 'a', 'ab', 'ba', 'a', 'ab', 'ba', 'aa', 'aa', 'aab', 'aab', 'aba', 'aba', 'baa', 'baa']
print gen_all_strings('aab')


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
# run()
