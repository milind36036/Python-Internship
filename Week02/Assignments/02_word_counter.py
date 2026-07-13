# Word Counter from Text File

try:
    with open("sample.txt", "r") as file:
        data = file.read()

    # Count lines
    lines = data.splitlines()

    # Count words
    words = data.split()

    # Count characters
    characters = len(data)

    print("===== FILE CONTENT =====")
    print(data)

    print("\n===== WORD COUNTER =====")
    print("Lines      :", len(lines))
    print("Words      :", len(words))
    print("Characters :", characters)

except FileNotFoundError:
    print("sample.txt file not found.")