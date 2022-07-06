def digital_root(n):
    while n > 9:
        n = str(n)
        root = []

        for num in n:
            if len(n) > 1:
                root.append(num)

        while len(root) > 1:
            total = 0
            for val in root:
                total += int(val)
            total = [int(a) for a in str(total)]
            root = total

        return root[-1]
    return n


#I literally spent hours on that (i am still learning, yeah...) and then i saw the solution in one line, was like FML...

def digital_root(n):
    return n % 9 or (n and 9)
