# Anagram checker
# Author: Michael Jordan
# Email:michael53161@gmail.com

def character_count(string):
    characters = {}    # declaring empy dictionary
    for ch in string:
        if ch in characters:
            characters[ch] = character[ch]+1
        else:
            characters[ch] = 1
    return characters

def main():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    count1 = character_count(word1)
    count2 = character_count(word2)
    if count1 ==count2:
        print("Those strings are anagrams")
    else:
        print("Those strings are not anagrams")

if __name__=="__main__":
    main()

    

        
