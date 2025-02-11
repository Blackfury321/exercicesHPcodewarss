import re 
def convert_text_to_expression(text): 
    mapping = { 
        "zero": "0", 
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9", 
        "ten": "10", 
        "eleven": "11", 
        "twelve": "12", 
        "thirteen": "13", 
        "fourteen": "14", 
        "fifteen": "15", 
        "sixteen": "16", 
        "seventeen": "17", 
        "eighteen": "18", 
        "nineteen": "19", 
        "twenty": "20", 
        "thirty": "30", 
        "forty": "40", 
        "fifty": "50", 
        "sixty": "60", 
        "seventy": "70", 
        "eighty": "80", 
        "ninety": "90", 
        "hundred": "100", 
        "plus": "+", 
        "minus": "-", 
        "dividedBy": "/", 
        "multipliedBy": "*" 
    } 
    words = text.split('-') 
    words=re.split('-| ',text) 
    expression="" 
    lastnumber=0 
    for word in words: 
        if word in ['plus','minus','multipliedBy','dividedBy']: 
            expression += str(lastnumber) 
            expression += mapping.get(word, word) 
            lastnumber=0 
        else: 
            lastnumber=lastnumber+int(mapping.get(word, word)) 
    expression += str(lastnumber) 
    solution=str(int(eval(expression))) 
    expression += "=" 
    expression += solution 
    return expression 
text = input("") 
expression = convert_text_to_expression(text) 
print(expression)