class patient:
    def __init__(self, id=None, name=None, age=None, bloodgroup=None, next=None, prev=None):
        self.id = id
        self.name=name
        self.age=age
        self.bloodgroup=bloodgroup
        self.next=next
        self.prev=prev


class WRM:
    def __init__(self):
        self.head = patient(None, None, None, None, None, None)
        self.tail = self.head
        
        ## ok so making node circular
        self.head.next = self.head
        self.head.prev = self.head
        
    def RegisterPatient(self, id, name, age, bloodgroup):
        new_patient=patient(id, name, age, bloodgroup, None, None)
        temp = self.head.prev
        self.head.prev = new_patient
        new_patient.next = self.head
        temp.next = new_patient
        new_patient.prev = temp
        print()
        print(f"Registration Successful.\n{name} is registered.")
    def ServePatient(self):
        dhead = self.head
        if self.head.next != self.head:
            print(f'{self.head.next.name} is served.')
            self.head.next = self.head.next.next
            self.head.next.next.prev = self.head
        else:
            print("No patient to serve.")
        
    def CancelAll(self):
        self.head.next = self.head
        self.head.prev = self.head
        print("Cancelling all appoinment.")
    def CanDoctorGoHome(self):
        if self.head.next != self.head:
            return False
        else:
            return True
    def ShowAllPatient(self):
        current = self.tail
        flag = 1
        if current.next == self.head:
            print("No patients are in the waiting room.")
        else:
            while current.next != self.head:
                print(f"{flag}. name: {current.next.name}")
                current = current.next
                flag+=1
    
    
    
########################################################
### Test class ####

function =  WRM()

while True:
    print()
    print()
    print("welcome to patient waiting room management system")
    print("======== please choose an option ========")
    print("1. Register Patient\n2. Serve Patient\n3. Cancel All\n4. Can Doctor Go Home?\n5. Show details of all patient\n6. exit\n########################")
    user = int(input("please choose a task using number: "))
    if user == 1:
        print("======Registering patient======\n")
        id = int(input("please enter id: "))
        name = input("please enter patient name: ")
        age = int(input("please enter patient age: "))
        bloodgroup=input("please enter patient blood group: ")
        function.RegisterPatient(id, name, age, bloodgroup)
    elif user == 2:
        function.ServePatient()
    elif user == 3:
        function.CancelAll()
    elif user == 4:
        if function.CanDoctorGoHome() == False:
            print("No, Doctor can not go home.\nPatients are still in waiting room")
        else:
            print("Yes, doctor can go home now.")
    elif user == 5:
        function.ShowAllPatient()
    elif user == 6:
        print("====== closing the program ======")
        break
    else:
        print("please enter a valid input")
    