import os

names = []
attempts = 0
SAVE_FILE = "names.txt"

# Загрузка сохраненных имен при старте
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r") as f:
        names = [line.strip() for line in f.readlines()]
    print(f"Loaded {len(names)} names from storage.")

while True:
    name = input("\nEnter name (commands: stop|list|find|del|sort|clear): ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        continue        
    
    # Блок команд
    if name == "stop":
        print("Session terminated.")
        break
        
    elif name == "list":
        print(f"Stored names ({len(names)}):\n" + "\n".join(names) if names else "No names stored.")
        continue
        
    elif name == "find":
        search = input("Search name: ").strip()
        matches = [n for n in names if search.lower() in n.lower()]
        print(f"Found {len(matches)} matches:" if matches else "No matches found.")
        for match in matches:
            print(f"- {match}")
        continue
    
    elif name == "del":
        target = input("Name to delete: ").strip()
        if target in names:
            names.remove(target)
            print(f"'{target}' removed successfully.")
            with open(SAVE_FILE, "w") as f:
                f.write("\n".join(names))
        else:
            print(f"Error: '{target}' not found!")
        continue

    elif name == "sort":
        names.sort(key=str.lower)  # Сортировка без учета регистра
        print("List sorted alphabetically (case insensitive).")
        continue
        
    elif name == "clear":
        names.clear()
        print("All names cleared from memory.")
        continue

    # Блок обработки имен
    if any(n.lower() == name.lower() for n in names):
        print(f"Notice: '{name}' already exists (case insensitive).")
    else: 
        names.append(name)
        attempts += 1
        print(f"Greetings, {name}! (Attempt #{attempts})")
        with open(SAVE_FILE, "w") as f:
            f.write("\n".join(names))

print("\nSession summary:")
print(f"- Total attempts: {attempts}")
print(f"- Names in storage: {len(names)}")
print(f"- Saved to: {os.path.abspath(SAVE_FILE)}")