# s = "2" + 203 * "1"
s = "1" + "1" +"1" + "1" + "1"+ "1"+ "1"+ "1" +"2" + 195 * "1"
while "111" in s or "222" in s:
  if "111" in s:
    s = s.replace("111", "22", 1)
  elif "222" in s:
    s = s.replace("222", "11", 1)
  print(s)