# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

word = input("Enter a word: ")

result_1 = '' .join(char * 2 for char in word)

print(result_1)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

input_2 = input("Enter a range of letters (e.g., a-z): ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
start, end = alphabet.split('-')
user_range = input("Enter a range of letters (e.g., a-z): ")

result_2 = '' .join(chr(i) for i in range(ord(start), ord(end) + 1))

print(result_2)