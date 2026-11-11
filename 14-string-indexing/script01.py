credit_number = "1234-5678-1225-4628"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-2])
print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1]
print(credit_number)