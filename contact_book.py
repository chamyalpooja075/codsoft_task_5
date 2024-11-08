contacts={}
def add_contact():
    name=input("Enter your Name:\t")
    phone=input("Enter your Phone:\t")
    if name in contacts:
        print("This Contact already Exists")
    if len(phone) ==10:
        contacts[name]=phone
        print("Contact added Successfully")
    else:
        print("Enter valid number")
            
def delete_contact():
    name=input("Enter Name:\t")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("This Contact doesn't Exist.")
        
def update_contact():
    name=input("Enter Name\t: ")
    for contact in contacts:
        if contact== name:
            phone=input("Enter new Phone Number-")
            if len(phone)==10:
                contact[name]=phone
                print("Contact updated Successfully")
                break
            else:
                print("Enter invalid contact")
        else:
            print("Enter doesn't exist contact")
            
            
def search_contact():
    name=input("Name :\t")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("Contact found")
            print(contact),contact[contact]
            break
        else:
            print("Contact not found")
            
def display_contact():
    if contacts=={}:
        print("there are no contacts")
    else:
        print("Contact List:\n")
        for name,phone in contacts.items():
            print("Name: ",name,"\t","Ph.No.: ",phone,"\n")

repeat=True         
while repeat:
    print("\n\nContact Book Menu:")
    print("--------------------------------")
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Update Contact")
    print("4.Search Contact")
    print("5.Display Contact")
    print("6.Exit")
    
    choice=int(input("Enter Your Choice(1-6):"))
    if choice==1:
        add_contact()
    elif choice==2:
        delete_contact()
    elif choice==3:
        update_contact()
    elif choice==4:
        search_contact()
    elif choice==5:
        display_contact()
    elif choice==6:
        print("Existing Contact Book. Goodbye!")
        break
    else:
        print("Please enter valid choice between 1 to 6!")
    if not input("wanna any other operation perform? (yes/no): ").lower() == "yes":
        repeat = False

print("Thanks for interacting with me!")
