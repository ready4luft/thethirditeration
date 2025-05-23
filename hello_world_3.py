names = []
attempts = 0
while True:
    name = input("Enter your name: ")
    
    if not name.strip():
        print("Name string can not be empty!")
        continue        
    
    if name == "stop":
        print("Request is Terminated")
        break
    
    if name == "list":
        print("All names:", ", ".join(names))
        continue

    if name == "find":
        search = input("Name to find: ")
        if search in names:
            print(f"Found {search}!")
        else:
            print(f"{search} not found.")
        continue

    if name == "del":
        target = input("Name to delete: ")
        if target in names:
            names.remove(target)
            print(f"{target} removed!")
            with open("names.txt", "w") as f:
                f.write("\n".join(names))
        else:
            print(f"{target} not found!")
        continue

    if name == "sort":
        names.sort()
        print("List sorted alphabetically!")
        continue

    if name.lower() in [n.lower() for n in names]: #repeats
        print(f"{name} is already marked in our list!")
    
    else: #name entered continiues
        names.append(name)
        print(f"Greetings, {name}!")    
        attempts += 1
        print(f"Attempt №{attempts}")    

with open("names.txt", "w") as f:
    f.write("\n".join(names))
    print("Names file was created or updated.")