import string
def stringoperation():
    a = open("words.txt","r")
    punct = string.punctuation
    for my in a:
        my = my.strip()
        my = my.replace(" ","")
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        print(my)

stringoperation()






