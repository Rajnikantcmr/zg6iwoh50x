#take input from user
user_string=input("enter the string:")

#breakdown the string into list of words
words=user_string.split()

#sort the list
words.sort()

#display the sorted words
for letter in words:
    print(letter)


