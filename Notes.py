def user_command():
    print("\nThe commands are:\n",
    "\'Add\' to add a new note;\n",
    "\'Show\' to show a saved note;\n",
    "\'Delete\' to delete a saved note;\n",
    "\'Exit\' to exit this program.")
    cmd = input("\nNow input your command: ")
    if cmd == "Add": add()
    elif cmd == "Show": show()
    elif cmd == "Delete": delete()
    elif cmd == "Exit": exit()
    else:
        print("Error, try again!")
        return user_command()

def add():
    n_note = new_notes()
    notes.append(n_note)
    print("Succesfully added!")
    return user_command()

def show():
    note_number = int(input("Input the number of the note you want to read starting by \'1\': "))
    if note_number > 0:
        x = notes[note_number-1]
        print("Name:", x.name)
        print(x.note)
    else: print("Error, try again!")
    return user_command()

def delete():
    del_note = int(input("Input the number of the note you want to delete starting by \'1\': "))
    if del_note > 0:
        del notes[del_note-1]
        print("Succesfully deleted.")
    else: print("Error, try again!")
    return user_command()

class new_notes():
    def __init__(self):
        self.name = input("Input the name of the note: ")
        self.note = input("Input your note below:\n")

notes = []
user_command()