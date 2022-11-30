# a=[12,67,98,34]
# b=[]
# for i in a:
#     sum=0
#     for digit in str(i):
#         sum=sum+int(digit)
#         b.append(sum)
#     print("sum"+str(b))

# a=[1,1,2,2,3,3,4,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in(b):
#         b.append(a[i])
#     i=i+1
# print(b)

a=[15,81,11,23]
i=0
b=[]
while i<len(a):
    y=(a[i])//10
    z=(a[i])%10
    c=y+z
    b.append(c)
    i=i+1
print(b)