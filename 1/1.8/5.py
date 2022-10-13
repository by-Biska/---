n = 123 * "4"
while "4444" in n or "7777" in n:
  if "4444" in n:
    n = n.replace("4444", "77", 1)
  else:
    n = n.replace("7777", "44", 1)
  print(n)