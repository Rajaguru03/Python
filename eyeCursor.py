import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        Writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            Writer.writerow(info_list)

if __name__ == '__main__':
    condition = True  
    student_num= 1

    while(condition):
        student_info= input("Enter student #{} details:".format(student_num)) 
        student_info_list=student_info.split(' ')
        print("Entered splited up information is: \nName: {} \nAge: {} \nContact_number: {} \nE-mail_id:{} ".format(student_info_list[0] ,student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check =input("Is the entered information is corret?(yes/no): ")

        if choice_check =="yes":
            write_into_csv(student_info_list)

            condition_check=input("Enter (yes/no)if you want to continue:" )
            if condition_check == "yes":
                condition = True
                student_num = student_num +1
            elif condition_check =="no":
                condition = False
        elif choice_check =="no":
            print("\nPlease re-enter the values!")    
    
    
