# Check if a character appears twice in a String in Python

my_str = 'bobbyhadz.com'

if my_str.count('o') == 2:
    # 👇️ this runs
    print('The character appears twice in the string')
else:
    print('The character does NOT appear twice in the string')

print(my_str.count('o'))  # 👉️ 2
print(my_str.count('.'))  # 👉️ 1
print(my_str.count('b'))  # 👉️ 3