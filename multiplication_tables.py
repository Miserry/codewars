def multiplication_tables(num):
    lst = []
    for mult in range(1, num+1):
        small_lst = []
        for add in range(1, 11):
            x = mult*add
            small_lst.append(x)
        lst.append(small_lst)
        print(small_lst)
    return