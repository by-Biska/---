n = 219 * "219"
while "21" in n or "9999" in n:
  n = n.replace("21", "9", 1)
  n = n.replace("9999", "9", 1)
  print(n)