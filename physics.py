# COS 101 Assignment


#Formula Functions
def Newton():
    m = float(input("Enter Mass: "))
    a = float(input("Enter Acceleration: "))
    Force = m * a
    print(Force, "N")


def kinetic_energy():
    m = float(input("Enter Mass: "))
    v = float(input("Enter Velocity: "))
    kinetic = 0.5 * m * v ** 2
    print(kinetic, "J")


def Gravitational():
    m = float(input("Enter Mass: "))
    h = float(input("Enter Height: "))
    g = 10
    Potential = m * g * h
    print(Potential, "J")


def ohm():
    i = float(input("Enter Current: "))
    r = float(input("Enter Resistance: "))
    V = i * r
    print(V, "ohms")


def displacement():
    u = float(input("Enter Initial Velocity: "))
    t = float(input("Enter Time: "))
    a = float(input("Enter Acceleration: "))
    s = u * t + (1/2) * a * t ** 2
    print(s, "m")


#Code Loop
def Run_code():
    print(
        "\nCOS 101 PHYSICS FORMULAS\n"
        "1. Newton's Second Law\n"
        "2. Kinetic Energy\n"
        "3. Gravitational Potential Energy\n"
        "4. Ohm's Law\n"
        "5. Displacement"
    )

    user_input = input("Pick A Number: ")

    if user_input == "1":
        Newton()

    elif user_input == "2":
        kinetic_energy()

    elif user_input == "3":
        Gravitational()

    elif user_input == "4":
        ohm()

    elif user_input == "5":
        displacement()

    else:
        print("Invalid Option. Choose between 1-5")


run = True

while run == True:
    Run_code()

    while True:
        text = input("Would You Like To Continue? (y/n): ")
        user_choice = text.lower()

        if user_choice == "y":
            break

        elif user_choice == "n":
            print("Thank You For Using This Program")
            run = False
            break

        else:
            print("Invalid Input. Choose y/n")
