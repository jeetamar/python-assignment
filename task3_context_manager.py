"""Task 3: Context Manager.

Simulates a database connection using contextlib.contextmanager to guarantee resource cleanup.
"""

from contextlib import contextmanager
from typing import Generator


class SimulatedDatabase:
    """Simulated database connection object."""

    def execute(self, query: str) -> None:
        """Simulate executing a database query."""
        print(f"Executing query: {query}")


@contextmanager
def database_connection() -> Generator[SimulatedDatabase, None, None]:
    """Context manager for managing a simulated database connection.

    Ensures the connection is always closed via try...finally block.
    """
    print("Connecting to database...")
    db = SimulatedDatabase()
    try:
        yield db
    finally:
        print("Closing database connection...")


def run_demo() -> None:
    """Run demonstration test cases for Task 3."""
    print("=" * 50)
    print("TASK 3: CONTEXT MANAGER DEMO")
    print("=" * 50)

    print("\n--- DEMO 1: SUCCESS CASE ---")
    with database_connection() as db:
        db.execute("SELECT * FROM users")
    print("Result: Connection opened, action performed, connection cleanly closed.")

    print("\n--- DEMO 2: ERROR CASE (EXCEPTION HANDLING) ---")
    try:
        with database_connection() as db:
            db.execute("SELECT * FROM users")
            print("Simulating an unexpected database failure...")
            raise RuntimeError("Simulated database error")
    except RuntimeError as error:
        print(f"Caught exception outside context: {error}")

    print("Result: Connection was guaranteed to close despite the exception.")
    print("=" * 50)


if __name__ == "__main__":
    run_demo()

