import getpass

password = "admin123"
adminAccess = False

def rename_folder():
    folder_name = input("Enter the name of the folder you want to rename: ")
    new_name = input("Enter the new name for the folder: ")

    for i, folder in enumerate(folders):
        if folder == folder_name:
            folders[i] = new_name
            print(f"The folder '{folder_name}' has been renamed to '{new_name}'.")
            return

    print(f"The folder '{folder_name}' was not found.")


def print_commands():
    if adminAccess:
        print("""
             Commands:
             /CreateFolder
             /RemoveFolder
             /ViewFolders
             /Help
             /RenameFolder
             /MultiCreate (5)
             /RemoveAll """)
    else:
        print("""
        Commands:
        /CreateFolder
        /RemoveFolder
        /ViewFolders
        /Help
        /RenameFolder""")

folders = []

while True:
    
    print("\nYou Can Use /Help For Commands.")
    command = input("-")    

    if command.lower() == "/help":
        print_commands()

    elif command.lower() == "/createfolder":
        folderNaming = input("What Do You Want To Name The Folder?\n-")
        folders.append(folderNaming)
        print("Successfully created a Folder named " + folderNaming + ".")

    elif command.lower() == "/removefolder":
        FolderToRemove = input("What Folder Do You Want To Remove?\n-")
        if FolderToRemove in folders:
            folders.remove(FolderToRemove)
            print("Successfully removed the folder named " + FolderToRemove + ".")
        else:
            print("Folder not found.")

    elif command.lower() == "/viewfolders":
        print(folders)

    elif command.lower() == "/admin":
        passwordInput = input("Password:\n-")
        if passwordInput.lower() == password:
            adminAccess = True
            print("Admin Access Granted!")
        else:
            print("Wrong Password!")
    
    elif command.lower() == "/renamefolder":
        rename_folder()
        
    elif command.lower() == "/multicreate":
        if adminAccess:
            for _ in range(5):
                folderNaming = input("Enter the name of the folder you want to create: ")
                folders.append(folderNaming)
                print(f"Successfully created a folder named '{folderNaming}'.")
        else:
            print("You don't have access to use this command!")
    
    elif command.lower() == "/removeall":
        if adminAccess:
            folders.clear()
            print("All folders removed successfully.")
        else:
            print("You don't have access to use this command!")
            
    else:
        print("Incorrect Command!")
