from pathlib import Path

def list_current_directory():
    path = Path.cwd()
    print(f"Содержимое директории {path.name}\n")
    for item in path.iterdir():
        if item.is_dir():
            print(f"/{item.name}")
        else:
            print(f"{item.name}")

if __name__ == "__main__":
    list_current_directory()

# EOF
