import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()
random.shuffle(key)


# encrypt
plain_text = input("Enter message to encrypt: ")
cypher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]
print(f"Original msg: {plain_text}")
print(f"Encrypted msg: {cypher_text}")

# decrypt
plain_text = input("Enter message to decrypt: ")
plain_text = ""
for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Original msg: {cypher_text}")
print(f"Decrypted msg: {plain_text}")