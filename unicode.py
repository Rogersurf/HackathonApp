import os

def find_problematic_file(directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='cp1252') as f:
                        f.read()
                except UnicodeDecodeError as e:
                    print(f"Problematic file: {file_path}")
                    print(e)

find_problematic_file('G:\My Drive\Colab Notebooks\Portfolio_EDA\Hackaton2')
