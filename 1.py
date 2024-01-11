# add list with words and random word choice
import random
word_list = ("свиня", "собака", "кіт", "кінь", "кентавр", "заєць", "страус")
rand_word = random.choice(word_list)
word_mute = "*" * len(rand_word)


# Users try number
user_num = int(input("Введіть бажану кількість спроб:"))

# Users try number count
def attempt_count (user_count):
    user_count -= 1
    if user_count == 0:
        print("Кількість спроб вичерпана")
    return user_count

# Users word or leter input
while user_num > 0:
    user_gues = str(input("Введіть букву або ціле слово:"))
    if user_gues == rand_word:
        print('Вітаю із перемогою')
        break
    elif user_gues in rand_word:
        word_mute ="".join([c if c == user_gues or disp_c != "*" else "*" for c, disp_c in zip(rand_word, word_mute)])
        print (word_mute)
    else:
        print ("Спробуйте ще :(")
    user_num = attempt_count(user_num)









