# put your code here.
# open file
# create empty dictionary

    # loop over each line
        # strip white spaces and split words by spaces
        # loop over word list
            # assign each word as a key using .get and update count


def word_count(filename):

    word_counts = {}

    with open(filename) as text:
        for line in text:
            line = line.strip().split(' ')

            for word in line:
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(dictionary):
    for word, count in dictionary.iteritems():
        print word, count


print_word_counts(word_count('twain.txt'))