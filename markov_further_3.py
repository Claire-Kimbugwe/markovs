"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open first file
    with open(file_path1, 'r') as content1:
        content1 = content1.read()

    #further studies 4 to open a second file and combine with first
    with open(file_path2, 'r') as content2:
        content2 = content2.read()


    return content1+content2

# open_and_read_file('green-eggs.txt')


def make_chains(text_string,ngram=2):
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
    random_start_key = choice(list((chains.keys())))

    #further studies 3: chooses a random key starting with capital letter
    while random_start_key[0][0] != random_start_key[0][0].upper():
        random_start_key = choice(list((chains.keys())))

    #adds first two words in keys to words list
    for word in random_start_key:
        words.append(word)
    print(random_start_key)
    
    #loops through dictionary chains starting at random key
    while random_start_key in chains:
        selected_word = choice(chains[random_start_key])
        words.append(selected_word)
        random_start_key = tuple(words[-2:])
        #further studies 3: if we reach a sentence end punctuation, stop generating and break out
        if selected_word[-1] in ['.','?','!']:
            break

    return " ".join(words)


input_path1 = sys.argv[1] #further studies one to change filename into sys.argv format
input_path2 = sys.argv[2] #further studies four, to take in two files

# Open both the file and turn it into one long string
input_text = open_and_read_file(input_path1, input_path2)

# Get a Markov chain
chains = make_chains(input_text,2)

# Produce random text
random_text = make_text(chains)

print(random_text)
