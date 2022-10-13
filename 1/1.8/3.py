n = 111 * "1"
while "11111" in n:
  n = n.replace("111", "2", 1)
  n = n.replace("222", "3", 1)
  n = n.replace("333", "1", 1)
  print(n)