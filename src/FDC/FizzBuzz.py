def FizzBuzz(entry):
    result = ""
    if entry % 3 == 0:
        result = "Fizz"
    if entry % 5 == 0:
        result = result+"Buzz"
    if result != "":
        return result
    else:
        return entry

output = ""
for i in range(1,101):
    output = output+str(FizzBuzz(i))

print(output)
