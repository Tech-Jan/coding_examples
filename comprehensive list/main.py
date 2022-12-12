import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# row.letter = row["letter"] and row["code"] would be the same as row.code
my_nato_dict = {row.letter: row["code"] for index, row in data.iterrows()}
# print(my_nato_dict)
print([my_nato_dict[letter.upper()] for letter in input("whats ur names") if letter != " "])

#
##
###
#### more examples
###
##
#
numbers = [1, 2, 3, 4, 5]

numbers2 = [n * n for n in numbers]
numbers2 = [n ** 2 for n in numbers]
numbers3 = [n ** 2 for n in numbers]
name = "mybiglongnname"
name_list = [1 for letta in name]
name_list = [letta for letta in name]
my_list = [n * 2 for n in range(1, 5)]
crazy_list = [n * 3 for n in range(1, 5) if n != 3]
names = ["Alex", "Meth", "Caroline", "Dave", "Alex", "Fredd", ]
names = ["Alex", "Meth", "Caroline", "Dave", "Alex", "Freddssa", ]
newlsit = [myname.upper() for myname in names if len(myname) > 5]

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (temp_c * 9 / 5) + 32 for (key, temp_c) in weather_c.items()}

print(weather_f)
