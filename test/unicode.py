import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError as e:
                print(f"Problem with file: {os.path.join(root, file)}")
                print(e)
