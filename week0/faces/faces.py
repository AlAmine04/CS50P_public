def main():
    text = convert(input("Type your text here: "))
    print(text)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁" )
    return text

main()
