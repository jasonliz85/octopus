import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from pprint import pprint 

# We get the url

TAGS_TO_CHECK = ['p', 'div']

def get_words_from_website(url, tags_to_check):
    ## Fetch the response from the url
    try:
        response_results = requests.get(url)
    except Exception as e:
        raise "Could not fetch url content - %s - %s"%(url, e)

    ## Build soup class from html
    soup = BeautifulSoup(response_results.content, "lxml")

    ## Build word counter
    total_words  = Counter()
    escape_chars = punctuation
    
    for tag in tags_to_check: 
        ## scrape tags
        text = (''.join(s.findAll(text=True)) for s in soup.findAll(tag)) 

        ## build word list and filter
        words = []
        for line in text:
            for word in line.split():
                word = word.rstrip(escape_chars).rstrip(escape_chars).lower()
                if word:
                    words.append(word)

        total_words = Counter(words)

    return total_words
    
if __name__ == '__main__':
    get_words_from_website("https://en.wikipedia.org/wiki/Octopus", TAGS_TO_CHECK)

