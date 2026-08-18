students = []

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")  
    choice = input("Choice: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        
        info = {"id": sid, "name": name, "dob": (sid, dob)}
        students.append(info)
        print("Added!")

    elif choice == "2":
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, DOB: {s['dob'][1]}")

    elif choice == "3":
        sid = input("ID to delete: ")
        for i, s in enumerate(students):
            if s['id'] == sid:
                del students[i]  
                print("Deleted!")
                break

    elif choice == "4":
        break  