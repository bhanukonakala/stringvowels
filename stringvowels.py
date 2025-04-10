s1=input("enter a string:")
print("Palindrome" if s1==s1[::-1] else "Not Palindrome" )

s2=input("enter a string: ")
vc,cc,wc=0,0,0
vowels="aeiouAEIOU"
for i in s2:
    if i>="A" and i<="Z" or i>="a" and i<="z":
        if i in vowels:
            vc+=1
        else:
            cc+=1
    elif i==" ":
        wc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("White spaces:",wc)