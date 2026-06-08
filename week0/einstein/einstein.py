def main():
    energy = energy_of(int(input("mass(in kg): ")))
    print(energy)


def energy_of(mass):
    energy = mass * ((3 * 10 ** 8) ** 2)
    return energy


main()
