"""Task 2: Validator Strategy Pattern.

Implements the Strategy Design Pattern allowing runtime switching of validation logic
without modifying caller code.
"""

from abc import ABC, abstractmethod
import re


class ValidationStrategy(ABC):
    """Abstract base strategy for input validation."""

    @abstractmethod
    def validate(self, value: str) -> bool:
        """Validate the input value.

        Args:
            value: The string value to validate.

        Returns:
            True if valid, False otherwise.
        """
        pass


class EmailValidator(ValidationStrategy):
    """Concrete strategy for email validation."""

    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    def validate(self, value: str) -> bool:
        """Validate email string format."""
        if not isinstance(value, str):
            return False
        return bool(self.EMAIL_REGEX.match(value.strip()))


class PasswordValidator(ValidationStrategy):
    """Concrete strategy for password strength validation.

    Rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    """

    def validate(self, value: str) -> bool:
        """Validate password against complexity requirements."""
        if not isinstance(value, str):
            return False
        if len(value) < 8:
            return False
        has_upper = any(char.isupper() for char in value)
        has_lower = any(char.islower() for char in value)
        has_digit = any(char.isdigit() for char in value)

        return has_upper and has_lower and has_digit


class Validator:
    """Context class that maintains a reference to a validation strategy."""

    def __init__(self, strategy: ValidationStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy) -> None:
        """Switch validation strategy at runtime."""
        self._strategy = strategy

    def validate(self, value: str) -> bool:
        """Execute validation using current strategy."""
        return self._strategy.validate(value)


def run_demo() -> None:
    """Run demonstration test cases for Task 2."""
    print("=" * 50)
    print("TASK 2: VALIDATOR STRATEGY PATTERN DEMO")
    print("=" * 50)

    # Initialize context with EmailValidator strategy
    validator = Validator(EmailValidator())
    print("[Strategy: EmailValidator]")

    email_samples = [
        ("test@example.com", True),
        ("john.doe@gmail.com", True),
        ("invalid-email", False),
        ("user@", False),
        ("@domain.com", False),
    ]

    for email, expected in email_samples:
        is_valid = validator.validate(email)
        status = "PASS" if is_valid == expected else "FAIL"
        print(f"Email: '{email}' -> Valid: {is_valid} (Expected: {expected}) [{status}]")

    # Switch strategy at runtime to PasswordValidator
    print("\n[Switching Strategy -> PasswordValidator]")
    validator.set_strategy(PasswordValidator())

    password_samples = [
        ("StrongPassword123", True),
        ("password", False),      # missing upper, digit, length < 8
        ("12345678", False),      # missing upper, lower
        ("PASSWORD123", False),   # missing lower
        ("Short1", False),        # length < 8
    ]

    for password, expected in password_samples:
        is_valid = validator.validate(password)
        status = "PASS" if is_valid == expected else "FAIL"
        print(f"Password: '{password}' -> Valid: {is_valid} (Expected: {expected}) [{status}]")

    print("=" * 50)


if __name__ == "__main__":
    run_demo()

