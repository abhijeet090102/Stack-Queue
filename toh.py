def toh(n,beg,end,aux):
    if n>1:
        toh(n-1,beg,aux,end)
        print(f' The value beg {beg} goes to --> {end}')
        beg,end = end,beg
        toh(n-1,aux,end,beg)
    else:
       beg,end = end,beg
am = toh(3,'b','e','a')
