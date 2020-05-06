#Question1 Print Pattern
def Pattern(n):
    i=1
    while i<n*2:               
        if i<n+1:
            for j in range(0,i):
                print("*",end=" ")
            print(" ")
            
        else:
            k=(n*2)-i
            for j in range(0,k):
                print("*", end=' ')
            print(" ")
        i+=1
Pattern(5) 


#Question2 Print reverse of word

word=input("Enter word to be reversed:")
reverseword=" "
for i in word:
    reverseword=i + reverseword
print(reverseword)