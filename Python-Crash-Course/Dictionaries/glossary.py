# Define the glossary dictionary with programming words and their meanings
glossary = {
    'variable': 'memory location to store values.',
    'function': 'A block of code which only runs when it is called.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is reached.',
    'list': 'A collection which is ordered and changeable. Allows duplicate members.',
    'dictionary': 'A collection which is unordered, changeable, and indexed. No duplicate members.'
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n{meaning}\n")