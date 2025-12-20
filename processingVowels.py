vowels = ['a','e','i','o','u']
numVowels = 0
otherChars = 0

str = input("Enter a word/sentence: ")

for i in str:
    if i in vowels:
        numVowels+=1
    else:
        otherChars+=1

print("Number of vowels: ", numVowels)
print("Other characters: ", otherChars)