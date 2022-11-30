def primo(n):
    for x in range(2,n):
        check = int(n/x)
        if check * x == n: return False
       
    return True #Il numero è primo

m = input("dimmi un numero")
bertolucci = int(m)
x = primo(bertolucci)  #return True

print(x)
