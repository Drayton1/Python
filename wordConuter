#How many words are in a text. & How often a word appears.
text = """
a a b c A d d d e it
"""
print(f"Characters: {len(text)}")
print(f"Words: {len(text.split())}")
print(text.split())
word_count = {}

for x in text.split():
    if x in word_count:
        word_count[x] += 1
    else: 
        word_count[x] = 1

print(word_count)
