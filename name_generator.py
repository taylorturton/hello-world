import random

first_names = ["Alfie", "Connor", "Deji", "Ed", "George", "Harry", "Jack", "Leo", "Matthew", "Stephen", "Tyler", "William", "Zeki"]
last_names = ["Adekoye", "Bray", "Eccles", "Garraway", "Halls", "Klein", "Little", "McMann", "Peterson", "Rushton", "Simpson", "Turner"]

random_first_name = random.choice (first_names)
random_last_name = random.choice (last_names)
random_name = random_first_name + " " + random_last_name

print("Name: ", random_name)