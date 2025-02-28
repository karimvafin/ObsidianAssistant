import os


def read_obsidian_notes(vault_path):
    notes = {}
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    notes[file] = file[:-3] + ': ' + f.read()
    return notes
