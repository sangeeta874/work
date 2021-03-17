n= int(input())

i=1
ch='A'
while i<=n :
    j=1 
    while j<=i :
        
        print(ch,end="")
        ch = chr(ord(ch) + 1)
        j=j+1
    print("")    
    i=i+1