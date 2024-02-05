import pandas

nato_code_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dic = {row.letter:row.code for (index, row) in nato_code_data.iterrows()}

name = input('Enter a Word: ').upper()

result = [nato_dic[letter] for letter in name]

print(result)