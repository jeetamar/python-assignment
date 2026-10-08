"""Task 4: Large Log File Processing.

Demonstrates streaming a large log file line-by-line with O(1) memory complexity.
Simulates processing a 10GB file on an 8GB RAM system without loading the file into memory.
"""

import os


def count_error_occurrences(file_path: str) -> int:
    """Count total occurrences of the word 'ERROR' in a log file line-by-line.

    Args:
        file_path: Path to the log file.

    Returns:
        Total count of 'ERROR' occurrences, or -1 if file access fails.
    """
    total_errors = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Count all occurrences per line (a single line may contain multiple ERRORs)
                total_errors += line.count("ERROR")
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' was not found.")
        return -1
    except OSError as e:
        print(f"Error reading file '{file_path}': {e}")
        return -1

    return total_errors


def create_sample_log(file_path: str = "sample.log") -> None:
    """Create a small sample log file for demonstration purposes."""
    sample_content = (
        "2026-10-08 INFO Application started\n"
        "2026-10-08 ERROR Database connection failed\n"
        "2026-10-08 ERROR ERROR Multiple errors\n"
        "2026-10-08 INFO Application stopped\n"
    )
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(sample_content)


def run_demo() -> None:
    """Run demonstration test cases for Task 4."""
    print("=" * 50)
    print("TASK 4: LARGE LOG FILE PROCESSING DEMO")
    print("=" * 50)

    sample_log_path = "sample.log"

    try:
        # Create a tiny sample log file for testing
        create_sample_log(sample_log_path)
        print(f"Created sample log file: '{sample_log_path}'")

        print("Processing log file line-by-line (streaming)...")
        error_count = count_error_occurrences(sample_log_path)

        print(f"Sample Log Analysis Complete.")
        print(f"Total 'ERROR' occurrences found: {error_count} (Expected: 3)")

        # Verify handling of missing files
        print("\nTesting non-existent file handling:")
        count_error_occurrences("non_existent_file.log")

    finally:
        # Cleanup temporary sample log file
        if os.path.exists(sample_log_path):
            os.remove(sample_log_path)
            print(f"\nCleaned up sample log file: '{sample_log_path}'")

    print("=" * 50)


if __name__ == "__main__":
    run_demo()

