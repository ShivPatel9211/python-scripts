# Question 1
row=5
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# row = int(input("Enter th value of row : "))
# #col = int(input("Enter the value of columns"))
# for i in range(row):
#     for j in range(i):
#         print (i,end=" ")
#     print("")
# Question 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
# for i in range(1,row+1):
#     for  j in range(1,i+1):
#         print(j, end=" ")
#     print("")
# Question 3
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# a=0
# for i in range(row ,0,-1):
#     a += 1
#     for j in range(1,i+1):
#        print(a, end=' ')
#     print('')
# Question 4
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
# a=5
# for i in range(row ,0,-1):
#     for j in range(1,i+1):
#        print(a, end=' ')
#     print('')
# Question 5 
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# for i in range(row,0,-1):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print("")
# Question 6  using while loop
# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9
# i=1
# while i<=row:
#     j=1
#     while j<=i:
#         print((i*2-1), end=" ")
#         j+=1
#     print('')
#     i+=1
# Question 7
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(row,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print('')
# Question 8 
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,row+1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print('')
# Question 9
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# for i in range(row , 0 ,-1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print('')

# Question  10
# 1
# 3 2
# 6 5 4
# 10 9 8 7
# Question  11
#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 

# for i in range(1,row+1):
#     num=1
#     for j in range(row, 0 ,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(num ,end=" ")
#             num+=1
#     print('')
# Question 12
# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5
# for i in range(1, row+1):
#     for j in range(1,row+1):
#         num=1
#         if i<=j:
#             print(j,end=" ")
#         else:
#             print(i,end=" ")
#     print('')

# Question 13
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# for i in range(1,row+1):
#     for j in range(i):
#         print("*", end=" ")
#     print('')
        
# Question 14
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# for i in range(1,row+1):
#     for j in range(row,0,-1):
#         if j>i:
#             print(' ',end=' ')
#         else:
#             print('*', end=' ')
#     print('')

# for i in range(row,0,-1):
#     for j in range(i):
#         print('*', end=" ")
#     print('')

# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

# for j in range(row):
#     n=j
#     while n>0:
#         print(end=" ")
#         n-=1
#     b=row-j
#     while b>0:
#         print("*", end=" ")
#         b-=1
#     print("")

# for j in range(row):
#     n=j
#     while n>0:
#         print(end="  ")
#         n-=1
#     b=row-j
#     while b>0:
#         print("*", end=" ")
#         b-=1
#     print("")
