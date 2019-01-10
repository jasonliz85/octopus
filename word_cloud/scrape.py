import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from pprint import pprint 

TAGS_TO_CHECK = ['p', 'div']

def get_words_from_website(url, tags_to_check=None):

    if not tags_to_check:
        tags_to_check = TAGS_TO_CHECK

    ## Fetch the response from the url
    response_results = requests.get(url)

    ## Build soup class from html
    soup = BeautifulSoup(response_results.content, "lxml")

    ## Build word counter
    total_words  = Counter()
    escape_chars = punctuation + '–’'
    
    for tag in tags_to_check: 
        ## scrape tags
        text = (''.join(s.findAll(text=True)) for s in soup.findAll(tag)) 

        ## build word list and filter
        words = []
        for line in text:
            for word in line.split():
                word = word.translate(str.maketrans('', '', escape_chars)).lower()

                if word:
                    words.append(word)

        total_words = Counter(words)

    return total_words

def normalise_results(counter, max_size=30, min_size=10):
    ## This function is needed for the js font sizes i.e. the font 
    ##  size will be proportional to the most occuring and least 
    ##  occuring frequencies
    if not counter:
        return []
    min_val = counter[-1][1]
    max_val = counter[0][1]
    scale_factor = (max_size - min_size) / (max_val - min_val)
    return [[word, ((value - min_val) * scale_factor + min_size)] for word, value in counter]

    
if __name__ == '__main__':
    get_words_from_website("https://en.wikipedia.org/wiki/Octopus", TAGS_TO_CHECK)

