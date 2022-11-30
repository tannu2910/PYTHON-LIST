# a=[2,3,4,[5,6,7,8]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1
#     i=i+1
# print(sum)


# a=[4,3,[12,8],[4,12]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1
#     else:
#         sum=sum+a[i]
        
#     i=i+1
# print(sum)


# a=[1,2,3,4,[6,7],8,9,2,[3,13,[10],4,5]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     sum=sum+a[i][j][k]
#                     k=k+1
#             else:
#                 sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)


# a=[2,34,5,[5,6,7,],[2,4,6],2]
# i=0
# m=1
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             m=m*(a[i][j])
#             j=j+1
#     else:
#         m=m*(a[i])
#         i=i+1
# print(m)



