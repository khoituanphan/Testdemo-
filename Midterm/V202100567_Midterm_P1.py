import random

user_enter = input("Enter a sentence: ")
num_char = len(user_enter)
num_word = len(user_enter.split())

ran_fun = random.randint(0, num_word)
word_ran = user_enter.split()[ran_fun]

print("Number of character is {}".format(num_char))
print("Number of word is {}".format(num_word))
print('The word at position {} is "{}"'.format(ran_fun, word_ran))
new_user = user_enter.replace(word_ran, word_ran.upper())
print("""New sentence is:
{}""".format(new_user))


