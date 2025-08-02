import string
all_alphabet = string.ascii_lowercase
m = int(input())
n = list(input().lower())
if m >= 26:
    n.sort()
    input_user = set(n)
    output_char = "".join(sorted(input_user)).lower()
    if output_char in all_alphabet:
        print('YES')
    else:
        print('NO')
else:
    print('NO')