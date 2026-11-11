
try:
    number = int(input("Number: "))
    print(1/number)

except ZeroDivisionError:
    print("Can not divide by 0")
except ValueError:
    print("Only use numbers")
except Exception:
    print("Something went wrong")

finally:
    print("Clean up")