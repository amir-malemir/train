mehman = input()
mizban = input()
string_convert = input()


mix_input = mehman + mizban
mix_input = "".join(sorted(mix_input))
diff_string = "".join(sorted(string_convert))
print(mix_input)
print(diff_string)
if mix_input == diff_string:
    print('YES')
else:
    print('No')