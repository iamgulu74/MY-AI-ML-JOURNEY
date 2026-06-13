try:
    x=int(input("Enter a number: "))
    ans=10/x
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print(f"The answer is {int(ans)}")
finally:
    print("This will always be executed.")