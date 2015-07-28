def reverse(word):
    wordlist = [word[0]]
    for i in range(1, len(word)):
        wordlist.append(word[i])
    wordlist.reverse()
    reverseword = ''.join(wordlist)
    print reverseword
    return

def palindrome(word):
    wordlist = [word[0]]
    for i in range(1, len(word)):
        wordlist.append(word[i])
    wordlist.reverse()
    reverseword = ''.join(wordlist)
    if (word == reverseword):
        palin = True
    else:
        palin = False
    print(palin)

def piglatin(word):
    wordlist = [word[1]]
    for i in range(2, len(word)):
        wordlist.append(word[i])
    endofword = ''.join(wordlist)
    print(endofword + word[0] + "ay")

word = raw_input("Enter your string here ")
piglatin(word)
