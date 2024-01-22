#       01234567
word = "pynative"

print("Orginal String is  pynative")
print("Printing only even index chars")

for arrangement in range(8):
    if arrangement%2 == 0:
        print(word[arrangement])