import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


nato_alphabet_dict = {row.letter:row.code for(index,row) in alphabet_data_frame.iterrows()}

name = input("Enter a word:\n").upper()
code_list = [nato_alphabet_dict[letter] for letter in name]
print(code_list)
