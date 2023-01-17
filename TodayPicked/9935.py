string = input()
boom = input()
stack = ""
pointer = 0
idx = 0
while idx < len(string):
    stack += string[idx]
    if string[idx] == boom[pointer]:
        pointer += 1

        if pointer == len(boom):
            stack = stack[:-len(boom)]
            pointer = 0
    else:
        pointer = 0
        idx += 1

if stack == "":
    print("FRULA")
else:
    print(stack)
