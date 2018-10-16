
n = 5
while n > 0 :
    print(n)
    n= n-1
    print("blastoff!")
    print(n)
   


x = 0
while x>0:
    print("Lather")
    print("rinse")
    print("dry off!")



while True:
    line = raw_input(">")
    if line == "done" :
        break
    print(line)
print("Done!")


largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
