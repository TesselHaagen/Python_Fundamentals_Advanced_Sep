import random

capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = capitals.lower()
numbers = '0123456789' 
specials = '.,?/!()&'

part1 = random.choices(capitals, k=1)
part2 = random.choices(lowers, k=1)
part3 = random.choices(numbers, k=1)
part4 = random.choices(specials, k=1)
part5 = random.choices(capitals+lowers+numbers+specials, k=2)

password_list = part1 + part2 + part3 + part4 + part5
random.shuffle(password_list)
password = ''.join(password_list)

print(password)