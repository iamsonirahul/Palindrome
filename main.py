# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# a program that checks a string to see if it is a palindrome.

# Yes. We know that Python has the built in function string.reverse() that you could use.

#Zero points for that today, we want you to think hard and utilize your skills in:

#recursion
#string slicing
#looping
#Your program should:

#Prompt the user to input a word.
#Analyze the word to see if it is a palindrome.
#Output a relevant 'yes/no message.

def is_palindrome(word):
    # Base case: if the string has length 0 or 1, it is a palindrome
    if len(word) <= 1:
        return True

    # Recursive case: check if the first and last alphabetic characters are the same
    # If they are, remove them from the string and recursively call the function on the remaining string
    first_char = word[0].lower()
    last_char = word[-1].lower()
    if not first_char.isalpha():
        return is_palindrome(word[1:])
    elif not last_char.isalpha():
        return is_palindrome(word[:-1])
    elif first_char == last_char:
        return is_palindrome(word[1:-1])
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prompt the user to input a word
    word = input("Enter a word: ")

    # Check if the word is a palindrome and output a relevant message
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
