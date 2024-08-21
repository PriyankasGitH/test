print("============ Range within a loop : with only end value ============")
for x in range(15):
    print(x)

print("============ Range within a loop : with start and end value ============")
for x in range(1,15):
    print(x)

print("============ Range within a loop : with start, end and step value ============")
for x in range(1,15,6):
    print(x)

print("============ Else within a loop : with end value ============")
for x in range(15):
    print(x)
else:
    print("finally finished")

print("============ Else within a loop with break statement : with end value ============")

fruits = ["Pineapple", "Cherry", "Strawberry"]
for x in fruits:
  if x == "Cherry": break
  print(x)
else:
    print("finally finished")