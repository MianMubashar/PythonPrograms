num=[2,1,6,4,7,9,0,8]

# we ha this in_Build methode to sort a list but we will write our own algo to sort
# f=sorted(num)
# print(f)
def sort(num):
    l=len(num)-1
    for i in range(l,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                pos=num[j]
                num[j]=num[j+1]
                num[j+1]=pos
sort(num)    
print(num)
