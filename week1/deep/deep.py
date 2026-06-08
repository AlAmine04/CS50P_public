answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
# delete all spces (even single one), interpret the input in lowercase
answer = answer.strip().lower().replace(" ", "-")

# check if the answer if 42 (or in letter)
match answer:
    case "42" | "forty-two":
        print("Yes")
    case _:
        print("No")
