# Yiska Levi

import string

def count_words(text):
    line_lengths = (i.lower() for i in text
                    if i.isspace() or i.isalpha())
    clean_text = ''.join([c for c in text if c.isalpha() or c.isspace()])
    words=clean_text.split()
    dic = {i.lower(): len(i) for i in words}
    return dic

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

if __name__ == '__main__':
    print(count_words(text))

