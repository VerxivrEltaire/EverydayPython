# Soulmate calculator
name1 = input()
name2 = input()
combined_names = name1.lower() + name2.lower()

s = combined_names.count('s')
o = combined_names.count('o')
u = combined_names.count('u')
l = combined_names.count('l')
first_digit = s + o + u + l

m = combined_names.count('m')
a = combined_names.count('a')
t = combined_names.count('t')
e = combined_names.count('e')
second_digit = m + a + t + e

soul_mate_score = int(first_digit + second_digit)

if soul_mate_score < 10 or soul_mate_score > 90:
    print(f'Your soulmate score is {soul_mate_score}, you go together like gasoline and a match stick')
elif soul_mate_score >= 40 and soul_mate_score <= 50:
    print(f'Your love score is {soul_mate_score}, you are okay together')
else:
    print(f'Your love score is {soul_mate_score}')

