glossary = {
    'string': 'A string is a sequence of characters.',
    'comment': 'You can use comments to provide explanations or add notes to your code for better understanding.',
    'list': 'A collection of items in a particular order.',
    'loop': ' A control flow statement that allows you to repeatedly execute a block of code',
    'dictionary': "A collection of key-value pairs.",
    'key': 'It refers to the value that is used to uniquely identify an element in a dictionary.',
    'value': 'It refers to the data that is associated with a key in a dictionary or stored in a variable..',
    'conditional test': 'It refers to an expression or statement that evaluates to either .',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'It is used in if statement or while loop.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")