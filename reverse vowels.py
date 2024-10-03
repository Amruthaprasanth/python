def rev_vow(s):
    vowels="aeiouAEIOU"
    l=list(s)
    i=0,j=len(s)-1
    while i<j:
        if l[i] in vowels and l[j] in vowels:
            l[i],l[j]=l[j],l[i]
            i=i+1
            j=j-1
        elif l[i] not in vowels:
            i=i+1
        elif l[j]not in vowels:
            j=j=1
            
            
