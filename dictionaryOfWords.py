"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Cat"] = "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."
word_definitions["Dog"] = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."
word_definitions["Bear"] = "a large, heavy, mammal that walks on the soles of its feet, with thick fur and a very short tail. Bears are related to the dog family but most species are omnivorous."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["Awesome"])
print(word_definitions["Cat"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (word,definition) in word_definitions.items():
    print(f'The definition of {word} is: {definition}')
