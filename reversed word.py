def reverse_word(word):
    reversed_word=""
    for i in range(len(word)-1,-1,-1):
        reversed_word+=word[i]
    return reversed_word
word=input("enter a word:")
reversed_word=reverse_word(word)
print("reversed word:",reversed_word)
