# j = ""
def F(n):
  j = str(n + 2*n + 1)
  if n > 1:
    j = str(3*n - 8)
    F(n - 1)
    F(n - 4)
  
# for i in range(100000):
#   j = ""
#   F(i)
#   print(j)

# def f(n):
#   if n < 1:
#     return n + 2*n + 1
#   else:
#     return n + 2*n + 1 + 3*n - 8 + f(n-1) + f(n - 4)
# print(sum(str(f(28))))


print(sum("11111"))