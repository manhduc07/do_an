def thapHaNoi(n, toaMot, toaHai, toaBa):

    if n == 1:
        print("Chuyen tu", toaMot, "sang", toaBa)
    else:
        thapHaNoi(n-1,toaMot,toaBa ,toaHai)
        print("Chuyen tu", toaMot, "sang", toaBa)
        thapHaNoi(n-1,toaHai,toaMot, toaBa)
        
thapHaNoi(4,'A','B','C')