# COS 101 assignment
def force(mass, acceleration):
    return mass * acceleration


def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


def potential_energy(mass, height, g=9.81):
    return mass * g * height


def voltage(current, resistance):
    return current * resistance


def displacement(initial_velocity, time, acceleration):
    return initial_velocity * time + 0.5 * acceleration * time ** 2


if __name__ == "__main__":
    print(force(10, 3))
    print(kinetic_energy(2, 5))
    print(potential_energy(2, 10))
    print(voltage(2, 5))
    print(displacement(2, 3, 1))
