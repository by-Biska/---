s = open("24.txt").readline()

# while "OREOREO" in s:
#     s = s.replace("OREOREO", "OREO OREO")
# print(s.count("OREO"))

# k = 0

# for i in range(len(s) - 3):
#     if s[i : i + 4] == "YAYA":
#         k += 1
# print(k)

print(s.count("BBB"))
while "BBBB" in s:
	s = s.replace("BBBB", "BBB BBB")
print(s.count("BBB"))