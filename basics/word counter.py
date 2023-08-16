str_1 = input(" Enter your input here:  ")


def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'" or i == "\n" or i == " \n" or i == " \n " or i == list:
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " " or j == "\n" or j == " \n" or j == " \n " or j == list:
            word_count += 1
    return word_count


print(word_counter(str_1))
