def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # calculate the tip by multiplying dollars to the peek ercentage
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# convert dollars to float
def dollars_to_float(d):
    dollars = float(d.strip("$"))
    return dollars


# convert percentge to float
def percent_to_float(p):
    percent = float(p.strip("%")) / 100
    return percent


main()
