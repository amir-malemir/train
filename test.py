mehman = input()
mizban = input()
string_convert = input()


mix_input = mehman + mizban
mix_input = "".join(sorted(mix_input))
diff_string = "".join(sorted(string_convert))
if mix_input == diff_string:
    print('YES')
else:
    print('NO')