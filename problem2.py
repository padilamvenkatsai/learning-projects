#pig Latin

def pig_latin():
    vowels = ["a","e","i","o","u"]
    word = input("enter the word: ")
    if word[0] in vowels:
        print(word + "way")
    else:
        print(word[1:-1]+ word[-1] + "ay")
                
print(pig_latin())

