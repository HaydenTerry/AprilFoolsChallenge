import random
import os

modded_file = "README.md"

if os.path.exists(modded_file):
    with open(modded_file, "r") as f:
        lines = f.readlines()

    action = random.choice(['add', 'delete'])

    if action == 'add':
        random_line = f"# Added by GitHub Actions: {random.randint(1, 1000)}\n"
        lines.insert(random.randint(0, len(lines)), random_line)

    elif action == 'delete' and len(lines) > 0:
        # Deleting a random line
        lines.pop(random.randint(0, len(lines) - 1))

    with open(modded_file, "w") as file:
        file.writelines(lines)