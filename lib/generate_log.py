from datetime import datetime


def generate_log(data):
    # Only lists are accepted
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Filename follows the pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # An empty list still creates a valid, empty file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    generate_log(["User logged in", "User updated profile", "Report exported"])