# Python Technical Assessment Project

## Overview

This project is a clean, practical, and standard-library-only Python Developer Technical Assessment. It contains 5 independent tasks designed to demonstrate core computer science concepts, object-oriented design patterns, Python-specific features (context managers), streaming file I/O for high performance and low memory consumption, and clean error handling.

All implementations strictly follow PEP 8 conventions, include type annotations, use clean abstractions, and require no external third-party dependencies.

---

## Requirements

- **Python Version**: Python 3.14+ (or Python 3.9+)
- **Dependencies**: Python Standard Library only (no `pip` packages required)

---

## Setup

To activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

---

## Run Main Application

Launch the interactive command-line menu to run all task demonstrations from a single prompt:

```bash
python main.py
```

---

## Run Individual Tasks

Each task module is completely independent and can be run directly:

```bash
python task1_two_sum.py
python task2_validator.py
python task3_context_manager.py
python task4_large_log.py
python task5_calculator.py
```

---

## Technical Explanations

### Task 1 — Two Sum Problem (`task1_two_sum.py`)

- **Approach**: Utilizes a Python dictionary (hash map) to store visited numbers and their indices in a single pass.
- **Why O(n) Time Complexity?**
  Looking up keys in a Python dictionary has an average time complexity of $O(1)$. By iterating over the list of $n$ numbers once and checking if `target - current_number` exists in the hash map, the total running time is $O(n)$ linear time. This avoids the $O(n^2)$ time penalty of nested loop comparisons.
- **Space Complexity**: $O(n)$ auxiliary space to store at most $n$ elements in the dictionary.
- **Duplicates Handling**: Duplicate values (such as `numbers = [3, 3]`, `target = 6`) are handled correctly because the lookup occurs *before* inserting the current index into the hash map.

---

### Task 2 — Validator Strategy Pattern (`task2_validator.py`)

- **Design Pattern**: **Strategy Pattern** (Behavioral Design Pattern).
- **Core Concept**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. The caller interacts with a unified `Validator` context object without needing to change invocation code when strategies switch.
- **Implementations**:
  - `ValidationStrategy` (Abstract Base Class using `abc.ABC`): Defines the contract `validate(value: str) -> bool`.
  - `EmailValidator`: Validates email string format using a regular expression (`re`).
  - `PasswordValidator`: Validates password complexity (at least 8 characters, containing uppercase, lowercase, and digit characters).
- **Runtime Strategy Switching**:
  ```python
  validator = Validator(EmailValidator())
  validator.validate("test@example.com")

  # Switch strategy at runtime seamlessly
  validator.set_strategy(PasswordValidator())
  validator.validate("StrongPassword123")
  ```

---

### Task 3 — Context Manager (`task3_context_manager.py`)

- **Feature**: Resource management using `contextlib.contextmanager`.
- **Core Concept**: Guarantees acquisition and teardown of external resources (like database connections or file handles) using Python's `with` statement.
- **Guaranteed Cleanup via `try...finally`**:
  ```python
  @contextmanager
  def database_connection():
      print("Connecting to database...")
      db = SimulatedDatabase()
      try:
          yield db
      finally:
          print("Closing database connection...")
  ```
  The code inside the `finally` block is **guaranteed to execute**, even if an uncaught exception occurs within the `with` block. This prevents resource leaks and guarantees database connection closure.

---

### Task 4 — Large Log Processing (`task4_large_log.py`)

- **Problem**: Processing a 10GB log file on a system with only 8GB RAM.
- **Why Streaming is Necessary**:
  Loading a 10GB file using `file.read()` or `file.readlines()` attempts to allocate memory for the entire file at once, causing an `OutOfMemoryError` (OOM crash) on an 8GB system.
- **Solution — Line-by-Line Streaming**:
  Using Python's file iterator (`for line in file:`) reads chunked buffers into memory line-by-line.
- **Complexity**:
  - **Time Complexity**: $O(n)$, where $n$ is the total amount of data / lines processed in the file.
  - **Space Complexity**: $O(1)$ auxiliary memory, as only the current line resides in RAM at any given moment.
- **Counting Multiple Errors**:
  Instead of `if "ERROR" in line` (which counts at most 1 per line), `line.count("ERROR")` is used to accurately count multiple `"ERROR"` occurrences appearing on the exact same log line.

---

### Task 5 — Simple Calculator (`task5_calculator.py`)

- **Core Function**: `calculate(first_number, operator, second_number)`
- **Supported Operators**: `+`, `-`, `*`, `/`
- **Exception Handling**:
  - `ZeroDivisionError`: Catches division by zero and returns a clear error message.
  - `ValueError`: Raised when an unsupported operator is supplied or numeric conversion fails.
  - `TypeError`: Raised when inputs are not valid numeric types.

---

## Project Structure

```text
python-code-test/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
├── task1_two_sum.py
├── task2_validator.py
├── task3_context_manager.py
├── task4_large_log.py
└── task5_calculator.py
```

---

## Example Output

### Running Main Menu (`python main.py`)

```text
========================================
       PYTHON CODE TEST
========================================
1. Two Sum Problem
2. Validator Strategy Pattern
3. Context Manager
4. Large Log File Processing
5. Simple Calculator
0. Exit
========================================
Enter your choice: 1

========================================
TASK 1: TWO SUM PROBLEM DEMO
========================================
Description : Standard case
Input       : numbers = [2, 7, 11, 15], target = 9
Output      : [0, 1]
Verification: 2 + 7 = 9
----------------------------------------
Description : Duplicate numbers case
Input       : numbers = [3, 3], target = 6
Output      : [0, 1]
Verification: 3 + 3 = 6
----------------------------------------
```

### Running Task 2 (`python task2_validator.py`)

```text
==================================================
TASK 2: VALIDATOR STRATEGY PATTERN DEMO
==================================================
[Strategy: EmailValidator]
Email: 'test@example.com' -> Valid: True (Expected: True) [PASS]
Email: 'john.doe@gmail.com' -> Valid: True (Expected: True) [PASS]
Email: 'invalid-email' -> Valid: False (Expected: False) [PASS]

[Switching Strategy -> PasswordValidator]
Password: 'StrongPassword123' -> Valid: True (Expected: True) [PASS]
Password: 'password' -> Valid: False (Expected: False) [PASS]
==================================================
```

### Running Task 3 (`python task3_context_manager.py`)

```text
==================================================
TASK 3: CONTEXT MANAGER DEMO
==================================================

--- DEMO 1: SUCCESS CASE ---
Connecting to database...
Executing query: SELECT * FROM users
Closing database connection...
Result: Connection opened, action performed, connection cleanly closed.

--- DEMO 2: ERROR CASE (EXCEPTION HANDLING) ---
Connecting to database...
Executing query: SELECT * FROM users
Simulating an unexpected database failure...
Closing database connection...
Caught exception outside context: Simulated database error
Result: Connection was guaranteed to close despite the exception.
==================================================
```

