age = int(input("Enter Your age: "))

if age >= 100:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
elif age >= 18:
    print("You are too old for this, Pray for yourself")
else:
    print("You are too young for this")