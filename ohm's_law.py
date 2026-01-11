"""
Ohm's Law Calculator
Purpose: Calculates Voltage, Amperage, Resistance, or Wattage based on user input.
Features: Input cleaning, error handling, and a persistent loop.
"""

def calculate_ohms_law():
    print("\n--- Advanced Ohm's Law Calculator ---")
    print("Select the value you want to find:")
    print("V) Volts  A) Amps  R) Resistance  W) Watts  Q) Quit")
    
    # .strip() removes accidental spaces; .upper() handles lowercase inputs
    choice = input("Option: ").strip().upper()

    try:
        # Exit the function if the user wants to quit
        if choice == 'Q':
            return False

        if choice == 'V':
            # Formula: V = I * R
            a = float(input("Input Amperage (A): "))
            r = float(input("Input Resistance (Ω): "))
            v = a * r
            w = v * a  # Also calculating Power (P = V * I)
            print(f"Result: {v:.2f} V | {w:.2f} W")

        elif choice == 'A':
            # Formula: I = V / R
            v = float(input("Input Voltage (V): "))
            r = float(input("Input Resistance (Ω): "))
            a = v / r
            w = v * a
            print(f"Result: {a:.3f} A | {w:.2f} W")

        elif choice == 'R':
            # Formula: R = V / I
            v = float(input("Input Voltage (V): "))
            a = float(input("Input Amperage (A): "))
            r = v / a
            print(f"Result: {r:.2f} Ω")

        elif choice == 'W':
            # Formula: P = V * I
            v = float(input("Input Voltage (V): "))
            a = float(input("Input Amperage (A): "))
            w = v * a
            print(f"Result: {w:.2f} W")

        else:
            print("Invalid selection. Please choose V, A, R, or W.")

    # Catches cases where user enters text instead of a number
    except ValueError:
        print("Error: Please enter numbers only (e.g., 12.5).")
    # Catches division by zero (e.g., if Amperage is 0 in Resistance calc)
    except ZeroDivisionError:
        print("Error: Calculation would involve division by zero.")
    
    # Return True to keep the 'while' loop running
    return True

# This block ensures the script only runs if executed directly (not imported)
if __name__ == "__main__":
    running = True
    while running:
        # Update 'running' based on whether the user chose to 'Q'uit
        running = calculate_ohms_law()
#Stay tuned for more....
