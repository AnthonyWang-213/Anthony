#Anthony Wang AT1 Education System
#User Name is your first name
#Password is "213"

#Bug List:

#Login System:
for i in range (3):
    print()
    print("*********** Wellcome to Gowan Brae Public School Education System ***********")
    print()
    print("========= Login System =========")
    User_Name = input('Please Enter your user name: ')
    Password=input('Please Enter your password: ')
    print("================================")
    #Create a List for student
    studentList=[]
    #Create a list for student's grade
    studentGrade=[]

    #Function: Add information
    def addInfo(F_name,L_name,score,Class,grade):
        #Create a dict to temporaly stored information
        tempInfo={}
        tempInfo['First_name']=F_name
        tempInfo['Last_name']=L_name
        tempInfo['score']=score
        tempInfo['Class']=Class
        tempInfo['grade']=grade

        #Adding the dict information into student list
        studentList.append(tempInfo)
        #Adding the grade value into studentGrade
        studentGrade.append(grade)

        print('Following information had been add:')
        print("-------------------------------------")
        print("Student Name:",tempInfo['First_name'],tempInfo['Last_name'])
        print("Class:",tempInfo['Class'])
        print("Score:",tempInfo['score'])
        print("-------------------------------------")
        print()
        input("********** Press 'Return' to back to Main Menu **********")

    #Function: Delete Information
    def delInfo(number):
        #Check is there any information in StudentList
        if int(number)<len(studentList) and int(number)>=0 :
            del studentList[int(number)]
            del studentGrade[int(number)]
            print()
            print("---------------------------------")
            print('Student ID:',number,'had been delated.')
            print("---------------------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")
        else:
            print()
            print("---------------------")
            print("Invalid Student ID")
            print("---------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")

    #Function: Change Information
    def changeInfon(change_ID,F_name,L_name,score,Class,grade):
        if int(change_ID)<len(studentList) and int(change_ID)>=0 :
            #temporary dict to store information
            tempInfo={}
            tempInfo['First_name']=F_name
            tempInfo['Last_name']=L_name
            tempInfo['score']=score
            tempInfo['Class']=Class
            tempInfo['grade']=grade

            #Change the information in this dict as the latest information in student list
            #change_ID表示学生列表所要更改的那组数
            studentList[int(change_ID)]=tempInfo
            #Change the grade value in the grade list
            studentGrade[int(change_ID)]=grade

            print()
            print('Edit successfully, latest information is below:')
            print("--------------------------------------------------")
            print("Student Name:",tempInfo['First_name'],tempInfo['Last_name'])
            print("Class:",tempInfo['Class'])
            print("score:",tempInfo['score'])
            print("-----------------------------------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")
        else:
            print("---------------------")
            print("Invalid Student ID:")
            print("---------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")

    #Create a loop
    #Determine if the password is correct
    while User_Name != '' and Password == '213':

                
#Main Menu
        print('\n')
        print("====================================================================")
        #Print out your name according the user name that you entered
        print("Hello %s!"%(User_Name))
        print("Welcome to Gowan Brae Public School Education System")
        print("====================================================================")
        print('\n')
        print("================ Welcome to Main Menu ================")
        print('1:Enter score for all student')
        print('2:Print out all student information')
        print('3:Edit Score')
        print('4:Student Band')
        print('5:Band Percentage')
        print('6:Quit Program')
        print("======================================================")
        print('\n')

#User select  menu
        Menu_Select =input('Please enter a number(1-6) to select a menu: ')

        #Use for avoiding bug
        if Menu_Select==(""):
            print()
            print("-------------------------------")
            print("You haven't enter any number")
            print("Please enter number from 1-6")
            print("-------------------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")

        #Menu 1 start: 
        elif int(Menu_Select)==1:
            print('\n')
            print("============= Class Score =============")
            print("Please select student's Class:")
            print("-------")
            print("# AL")
            print("# AM")
            print("# BL")
            print("# BM")
            print("-------")
            Class=input("Please enter the Class code (AL,AM,BL,BM):")

            #Check if the class is correct
            if Class==("AL") or Class==("AM") or Class==("BL") or Class==("BM"):
                F_name=input("Please enter Student's First Name: ")
                L_name=input("Please enter Student's Last Name: ")
                score=input("Please enter Student's score(0-100): ")
                #Check if the score is a number and is in range 0-100
                if score.isdigit():
                    print('=======================================')
                    print()
                    #Below code will operate when incorrect information were added.
                    if F_name==("") and L_name==(""):
                        print("----------------------------------")
                        print("You haven't enter student name")
                        print("----------------------------------")
                        print()
                        input("********** Press 'Return' to back to Main Menu **********")
                    elif score==(""):
                        print("----------------------------------")
                        print("You haven't enter sutdent score")
                        print("----------------------------------")
                        print()
                        input("********** Press 'Return' to back to Main Menu **********")
                    elif int(score)>100 or int(score)<0:
                        print("-------------------------------------------------------")
                        print("Invalid score")
                        print("Please enter a number from 0-100 as a student’s score.")
                        print("-------------------------------------------------------")
                        print()
                        input("********** Press 'Return' to back to Main Menu **********")
                    #Decided the band for the student
                    else:
                        if int(score)>=90 and int(score)<=100:
                            grade=("A")
                        elif int(score)>=80 and int(score)<90:
                            grade=("B")
                        elif int(score)>=70 and int(score)<80:
                            grade=("C")
                        elif int(score)>=60 and int(score)<70:
                            grade=("D")
                        elif int(score)>=50 and int(score)<60:
                            grade=("P")
                        elif int(score)>=0 and int(score)<50:
                            grade=("E")
                        #Use function "addInfo"
                        addInfo(F_name,L_name,score,Class,grade)
                else:
                    print()
                    print("--------------------------------------")
                    print("Please enter number(0-100) as a score")
                    print("--------------------------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")   
            else:
                print()
                print("--------------------")
                print("Invalid Class Code")
                print("Please re-enter")
                print("--------------------")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                #Menu 1 End

        #Menu 2 Start:
        elif int(Menu_Select)==2:
            print('\n')
            print("============= Student Detail Information =============")
            print()
            #Check are there any information in the list
            if 0==len(studentList):
                print("-------------------------------")
                print("No student data in the system.")
                print("-------------------------------")
                print()
                print("======================================================")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                continue
            i=0
            #print out all information in the list
            for info in studentList:
                print("First Name:%s    Last Name:%s   Score:%s   Class:%s"\
                      %(info['First_name'],info['Last_name'],info['score'],info['Class']))
                i+=1
            print()
            print("======================================================")
            print('\n')
            input("********** Press 'Return' to back to Main Menu **********")
            #Menu 2 End

        #Menu 3 Start:
        elif int(Menu_Select)==3:
            print()
            print("============= Edit Score =============")
            print("1.Edit existing score:")
            print("2.Delete existing score")
            print("======================================")
            print()
            #Input number to select edit score or delete score.
            Edit_Select=input("Please enter a number from 1-2 to select a function:")
            print()

            if Edit_Select==(""):
                print("============= Edit Score =============")
                print()
                print("-------------------------------------------------------")
                print("You haven't enter any number")
                print("Please enter a number from 1-2 to select the function")
                print("-------------------------------------------------------")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                continue
            
            #Edit Score Part (The code and logic for this part is similar as menu 1):
            if int(Edit_Select)==1:
                print("============== Edit existing score ==============")
                print()
                if 0==len(studentList):
                    print("-------------------------------------------------------")
                    print("There is no student information in the current system")
                    print("-------------------------------------------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")
                    continue
                i=0
                for info in studentList:
                    print("Student ID:%d    Last Name:%s    First Name:%s   Score:%s   Class:%s"%(i,info['Last_name'],info['First_name'],info['score'],info['Class']))
                    i+=1
                print()
                print("=================================================")
                print()
                change_ID=input("Enter the student ID that you want to change:")

                if change_ID==(""):
                    print()
                    print("----------------------------------")
                    print("You haven't enter any student ID")
                    print("----------------------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")
                    continue

                if int(change_ID)<len(studentList) and int(change_ID)>=0 :
                    print("Please select student's Class:")
                    print("-------")
                    print("# AL")
                    print("# AM")
                    print("# BL")
                    print("# BM")
                    print("-------")
                    #Input and collect the class
                    Class=input("Please enter the Class code (AL,AM,BL,BM):")

                    if Class==("AL") or Class==("AM") or Class==("BL") or Class==("BM"):
                        #Input and colleact data (student name and student score)
                        F_name=input("Please Enter Student's First Name: ")
                        L_name=input("Please Enter Student's Last Name: ")
                        score=input("Please Enter Student's Score(0-100)： ")
                        #The code below will operate when incorect information were entered.
                        if F_name==("") and L_name==(""):
                            print()
                            print("---------------------------------")
                            print("You haven't enter student name")
                            print("---------------------------------")
                            print()
                            input("********** Press 'Return' to back to Main Menu **********")
                        elif score==(""):
                            print()
                            print("---------------------------------")
                            print("You haven't enter sutdent score")
                            print("---------------------------------")
                            print()
                            input("********** Press 'Return' to back to Main Menu **********")
                        elif int(score)>100 or int(score)<0:
                            print()
                            print("------------------------------------------------------")
                            print("Invalid score")
                            print("Please enter a number from 0-100 as a student score.")
                            print("------------------------------------------------------")
                            print()
                            input("********** Press 'Return' to back to Main Menu **********")
                        else:# Define student band(grade) according to their score
                            if int(score)>=90 and int(score)<=100:
                                grade=("A")
                            elif int(score)>=80 and int(score)<90:
                                grade=("B")
                            elif int(score)>=70 and int(score)<80:
                                grade=("C")
                            elif int(score)>=60 and int(score)<70:
                                grade=("D")
                            elif int(score)>=50 and int(score)<60:
                                grade=("P")
                            elif int(score)>=0 and int(score)<50:
                                grade=("E")
                                
                            #Use function (ChangeInfon)
                            changeInfon(change_ID,F_name,L_name,score,Class,grade)
                            print()

                    else:
                        print()
                        print("--------------------")
                        print("Invalid Class Code")
                        print("Please re-enter")
                        print("--------------------")
                        print()
                        input("********** Press 'Return' to back to Main Menu **********")

                else:
                    print()
                    print("--------------------")
                    print("Invalid Student ID")
                    print("--------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")
                #Edit Part End
                    
            #Delete Part Start      
            elif int(Edit_Select)==2:
                print("============== Delete existing score ==============")
                print()
                #Check is there any information
                if 0==len(studentList):
                    print("-------------------------------------------------------")
                    print("There is no student information in the current system")
                    print("-------------------------------------------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")
                    continue
                #Print out information
                i=0
                for info in studentList:
                    print("Student ID:%d    Last Name:%s    First Name:%s   Score:%s   Class:%s"%(i,info['Last_name'],info['First_name'],info['score'],info['Class']))
                    i+=1
                    print()
                    print("===============================================")
                    print()
                number=input("Enter the student ID that you want to delete:")

                if number==(""):
                    print()
                    print("-----------------------------------")
                    print("You haven't enter any student ID")
                    print("-----------------------------------")
                    print()
                    input("********** Press 'Return' to back to Main Menu **********")
                    continue
                else:
                #Use function (delInfo)
                    delInfo(number)
                #Delete Part End

            else:
                print("-----------------------------------")
                print("You have enter an invalid number.")
                print("Please enter a number from 1-2.")
                print("-----------------------------------")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                #Edit Score Menu End

        #Menu 4 Start:
        elif int(Menu_Select)==4:
            print("============= Student Band =============")
            print()
            #Check Information
            if 0==len(studentList):
                print("--------------------------------")
                print("No student data in the system.")
                print("--------------------------------")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                continue
            i=0
            #Print Information
            for info in studentList:
                print("Name:%s %s   Score:%s   Achieved Band:%s"\
                      %(info['First_name'],info['Last_name'],info['score'],info['grade']))
                i+=1
            print()
            print()
            print("========================================")
            print('\n')
            input("********** Press 'Return' to back to Main Menu **********")
            #Menu 4 End

        #Menu 5 Start:
        elif int(Menu_Select)==5:
            print("============= Band Percentage =============")
            print()
            #StudentGrade is a list that created in the function "addInfo"
            #Calculate the frequency of different band occur within the list
            #Import
            from collections import Counter
            Grade_num1 = {}
            for i in set(studentGrade):
                Grade_num1[i] = studentGrade.count(i)
            #Grade_num1 dict is used to count the number of different band in the Gradelist

            #Grade_num1 dict information will updated to Grade_num2 dict.
            #This is to ensure that all 6 band have at least 0 value in the dict.
            Grade_num2 = {'A':0,'B':0,'C':0,'D':0,'P':0,'E':0}
            Grade_num2.update(Grade_num1)
            
            #Define the number of different band(grade) occur in the list
            A_num=Grade_num2['A']
            B_num=Grade_num2['B']
            C_num=Grade_num2['C']
            D_num=Grade_num2['D']
            P_num=Grade_num2['P']
            E_num=Grade_num2['E']
            Total_num=A_num + B_num + C_num + D_num + P_num + E_num

            #Check is there any information in the list
            if len(studentGrade)==0:
                print("------------------------------------------------------")
                print("No student information in the system.")
                print("Please back to Menu 1 to enter student infotmation.")
                print("------------------------------------------------------")
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                continue
            
            elif len(studentGrade)>0:
                #Print out the percentage of different band
                print("---------------------------------------")
                print("%d percent of students achieved Band A"%(A_num/Total_num*100))
                print("%d percent of students achieved Band B"%(B_num/Total_num*100))
                print("%d percent of students achieved Band C"%(C_num/Total_num*100))
                print("%d percent of students achieved Band D"%(D_num/Total_num*100))
                print("%d percent of students achieved Band P"%(P_num/Total_num*100))
                print("%d percent of students achieved Band E"%(E_num/Total_num*100))
                #formula of calculate percentage
                print("---------------------------------------")
                print()
                print("===========================================")
                print('\n')
                input("********** Press 'Return' to back to Main Menu **********")
                #Menu 5 End

        #Menu 6 Start:
        elif int(Menu_Select)==6:
            print()
            print("--------------------------------")
            print("Enter '1' to reconfirm the quit")
            print("Enter '2' to back to main menu")
            print("--------------------------------")
            print()
            #This code is used to select different function
            Exit_6=input("Enter the number ‘1’ or ‘2’ to confirm your choice: ")
            if int(Exit_6)==1:
                print()
                print("************ Program Exit ************")
                import sys
                sys.exit("Bye, %s!"%(User_Name))
                # When Select 1: End Program
            elif int(Exit_6)==2:
                #When select 2: Back to main menu
                print()
                input("********** Press 'Return' to back to Main Menu **********")
            else:
                print()
                print("-------------------------------------")
                print("You haven't enter '1' or '2'")
                print("System automaticaly back to main menu")
                print("-------------------------------------")
                #When Select others number, back to main menu.
                print()
                input("********** Press 'Return' to back to Main Menu **********")
                #Menu 6 End

        #This code is related to the Main Menu
        #This code will operate when user do not enter a correct number
        else:
            print("-------------------------------------------------------")
            print("You have enter an invalid number.")
            print("Please enter a number from 1-6 to select the function")
            print("-------------------------------------------------------")
            print()
            input("********** Press 'Return' to back to Main Menu **********")
 
    #This code is related to the Login System when password is inccorect
    else:
        if User_Name=="":
            print()
            print("------------------------------------------------------------")
            print("You haven't enter your username, you have %d chance left" %(2-i))
            print("------------------------------------------------------------")
            print()
        else:
            print()
            print("----------------------------------------------")
            print('Invalid password, you have %d chance left' %(2-i))
            print("----------------------------------------------")
            print()

#This code is use to end program when the password is inccorect over three time
else:
    print("************** Invalid password over 3 time, System logout **************")
    #Whole Program End

    

