"""Main entry point for Python Developer Technical Assessment application.

Provides an interactive CLI menu to execute and view demonstrations of all 5 tasks.
"""

import sys
import task1_two_sum
import task2_validator
import task3_context_manager
import task4_large_log
import task5_calculator


def display_menu() -> None:
    """Display the main application menu options."""
    print("\n========================================")
    print("       PYTHON CODE TEST")
    print("========================================")
    print("1. Two Sum Problem")
    print("2. Validator Strategy Pattern")
    print("3. Context Manager")
    print("4. Large Log File Processing")
    print("5. Simple Calculator")
    print("0. Exit")
    print("========================================")


def handle_task_5() -> None:
    """Handle choice for Task 5: Calculator."""
    task5_calculator.run_demo()
    try:
        choice = input("\nWould you like to run the interactive calculator? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            task5_calculator.run_interactive_calculator()
    except (KeyboardInterrupt, EOFError):
        pass


def main() -> None:
    """Main loop for menu-driven CLI application."""
    while True:
        try:
            display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                task1_two_sum.run_demo()
            elif choice == "2":
                task2_validator.run_demo()
            elif choice == "3":
                task3_context_manager.run_demo()
            elif choice == "4":
                task4_large_log.run_demo()
            elif choice == "5":
                handle_task_5()
            elif choice == "0":
                print("\nExiting application. Thank you!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please enter a number between 0 and 5.")

            input("\nPress Enter to return to the main menu...")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting application.")
            sys.exit(0)


if __name__ == "__main__":
    main()

