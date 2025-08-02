import string
all_alphabet = string.ascii_lowercase
m = input()
n = list(input().lower())
n.sort()
input_user = set(n)
output_char = "".join(sorted(input_user)).lower()
print(output_char)
if output_char in all_alphabet:
    print('YES')
else:
    print('NO')