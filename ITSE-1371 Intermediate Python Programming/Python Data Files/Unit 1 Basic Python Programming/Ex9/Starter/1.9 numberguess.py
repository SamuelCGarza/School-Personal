import math

low = int(input("Enter the smaller number: "))
high = int(input("Enter the higher number: "))
max_tries = round(math.log(high - low + 1, 2))

tries = 0
while tries < max_tries:
    tries += 1
    mid = (low + high) // 2
    print("Your number is", mid)
    ch = input("Enter =, <, or >: ")
    if ch == "=":
        print("Hooray, I've got it in {} tries!".format(tries))
        break
    elif ch == ">":
        low = mid + 1
    else:
        high = mid - 1
    if tries == max_tries:
        print("You're cheating!")
