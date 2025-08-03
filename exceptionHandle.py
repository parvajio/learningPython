# exception = An event that interrupts the flow of a program
                # (ZeroDivisionError, TypeError, ValueError)
                # 1.try, 2.except, 3. finally

try:
    number = int(input("Enter a num : "))
    print(1/number)
except ZeroDivisionError:
    print("Not zero")
except ValueError:
    print("Only number")
except Exception: #for all exception
    print("Something went wrong")
finally: 
    print("Do some cleanup here")