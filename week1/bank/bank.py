greeting = input("Greeting: ").strip()

#  check if the greeting starta wiht "Hello"
if greeting.startswith("Hello"):
    print("$0")
#  check if the greeting starts with simply an "H"
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")
