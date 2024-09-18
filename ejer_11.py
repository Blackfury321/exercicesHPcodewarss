codedtext = str(input()).strip().lower()
jump = int(input())
decodedtext = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"


for i in codedtext:
    if i.lower() in alphabet:
        position = alphabet.find(i.lower())
        newpos = (position - jump) % len(alphabet)
        newchar = alphabet[newpos]
        decodedtext += newchar
    else:
        decodedtext += " "

print(decodedtext.upper())
    
