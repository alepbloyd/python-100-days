import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

input_word = input("Input Word: ")

input_list = [nato_dict[letter.upper()] for letter in input_word]

print(input_list)