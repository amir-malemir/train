mehman = input()
mizban = input()
string_convert = input()

for i in range(1 , len(mehman)):
    check_mehman = mehman[i:]
    check_mizban = mizban[i:]
    if check_mehman and check_mizban in string_convert:
        print('YES')
print('NO')