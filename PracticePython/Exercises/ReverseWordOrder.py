# Write a program (using functions) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def reverse():
    sentence = input("Enter a sentence: ")
    split_sentence = sentence.split()
    new_sentence = split_sentence[::-1]
    print(new_sentence)

reverse()