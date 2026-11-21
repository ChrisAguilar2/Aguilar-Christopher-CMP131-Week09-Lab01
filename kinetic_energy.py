def kineticEnergy(mass, velocity):
    energy = 0.5 * mass * velocity**2
    return energy
def main():
    print("===== KINETIC ENERGY CALCULATOR =====")
    mass = float(input("Enter Mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    if mass < 0 or velocity < 0:
        print("Error: Mass and velocity cannot be negative.")
        return

    kinetic_energy = kineticEnergy(mass, velocity)

    print(f"Mass: {mass} kg")
    print(f"Velocity: {velocity} m/s")
    print(f"Kinetic Energy: {kinetic_energy:.2f} joules")

main()