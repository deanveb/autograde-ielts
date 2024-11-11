arr = [6, 8, 2]
patt = 0
current_page = 6

# START current +2 END (START +1) -1
while (current_page < 216):
    start = current_page + 2 if patt != 2 else current_page
    end = current_page + arr[patt] - 1
    current_page += arr[patt]
    for i in range(start, end+1, 1):
        print(i, end=',')
    
    patt = patt + 1 if patt + 1 < 3 else 0