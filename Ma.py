# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from importlib.resources import contents
from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here
        with open ("story.txt", 'r') as f:
          contents = f.read()
          print (contents)
          return (contents)
read_file_content(filename="story.txt")

def count_words(str):
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    counts= dict()
    text = str.split()
    
    for x in text:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] =1

    return counts
print (count_words("story.txt"))

    