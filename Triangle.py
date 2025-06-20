def Triangle(Array):

  count = 0
  triangular = []

  for p in range(n - 2):
    for q in range(p + 1 , n - 1):
      for r in range(q + 1, n):
        if (Array[p] + Array[q] > Array[r] and
            Array[q] + Array[r] > Array[p] and
            Array[r] + Array[p] > Array[q]):                # O(1)
          count +=1                                         # O(n)
          triangular.append((Array[p] , Array[q] , Array[r]))
  print(f"count = {count}")
  return triangular

n = int(input("Enter the Elements of The List: "))
Array = []
for i in range(n):                                          # O(n)
  x = int(input(f"Enter number {i + 1}: "))
  Array.append(x)

result = Triangle(Array)
if result:
  for triangular in result:                                 # O(n)
    print(triangular,",")
else:
  print("not triangular")
