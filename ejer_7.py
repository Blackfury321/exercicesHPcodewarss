def remove_letters(string):
    onlynumber = ""
    for char in string:
        if char.isnumeric():
            onlynumber += char
    return onlynumber
original = input()
result=remove_letters(original) 
print (result)
