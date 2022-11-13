def prime(x):
  return x>1 and all(x%i != 0 for i in range(2, int(x** 0.5) + 1))

for i in range(4202865, 4202924):
  if prime(i): print(i)