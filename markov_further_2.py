"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path, 'r') as content:
        content = content.read()


    return content

# open_and_read_file('green-eggs.txt')


def make_chains(text_string,ngram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_list = text_string.split()
    #start=0
    n=len(text_list)
    for index in range(n-ngram):
        stop = index + ngram
        tup_key = tuple(text_list[index:stop])

        value = text_list[stop]

        if tup_key in chains:
            chains[tup_key].append(value)
        else:
            chains[tup_key]= []
            chains[tup_key].append(value)
        
    # your code goes here

    return chains 

#print(make_chains(open_and_read_file('green-eggs.txt')))

def make_text(chains):
    """Return text from chains."""

    words = []

    #your code goes here


    for key,values in chains.items():
        selected_word = choice(values)
        words.append(selected_word)
    print(key)



    return " ".join(words)


input_path = "green-eggs.txt"
# input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,4)

# Produce random text
random_text = make_text(chains)

print(random_text)
