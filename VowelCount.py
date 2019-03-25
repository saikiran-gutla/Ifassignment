str = input("Enter a string : ")
up = str.upper()
a_cnt = e_cnt = i_cnt = o_cnt = u_cnt = 0
temp = " "
for i in up:
    if i in 'A':
        a_cnt += 1
        if i not in temp:
            temp += i
    elif i in 'E':
        e_cnt += 1
        if i not in temp:
            temp += i
    elif i in 'I':
        i_cnt += 1
        if i not in temp:
            temp += i
    elif i in 'O':
        o_cnt += 1
        if i not in temp:
            temp += i
    elif i in 'U':
        u_cnt += 1
        if i not in temp:
            temp += i
print(f'Vowels in given string are: {temp}')
if a_cnt >= 1:
        print(f' a count is {a_cnt}')
if e_cnt >= 1:
        print(f' e count is {e_cnt}')
if i_cnt >= 1:
        print(f' i count is {i_cnt}')
if o_cnt >= 1:
        print(f' u count is {o_cnt}')
if u_cnt >= 1:
        print(f' u count is {u_cnt}')
