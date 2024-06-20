import pickle
def count_rec():
    admission_number=input("Enter your Admission number:")
    Name=input("Enter your name:")
    Percentage=input("Enter your percentage:")
    record={admission_number:"Admission_number",Name:"Name",Percentage:"Percentage"}
    
    with open("STUDENT.DAT","wb") as file:
        pickle.dump(record,file)
      
    count = 0
    students_above_75 = []
    
    with open("STUDENT.DAT","rb") as file:
        while True:
                b= pickle.load(file)
                if b["Percentage"]> 75:
                    print(b)
count_rec()
    
  