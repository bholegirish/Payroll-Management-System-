# Menu for Payroll Management System
import mysql.connector
from datetime import date
import datetime

mycon=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="payroll_management_system")

if mycon.is_connected() == False :
    print("Not connected")

cursor=mycon.cursor()



def Employees_Details():
    print("\n\n\n")
    print(" "*25, "In Employees_Details function ")

    while True :
        print("="*20,"PAYROLL MANAGEMENT SYSTEM","="*20)
        print("|"," "*25,"1. Add_new_employee","                  |")
        print("|"," "*25,"2. Modify_employee_details","           |")
        print("|"," "*25,"3. Delete_employee_details","           |")
        print("|"," "*25,"0. Quit","                              |")
        print("="*77)
        ch=input("                    Enter your Choice (1/2/3/0) : ")

        if ch== "1":
            print("Write Add_new_employee function above and call it here  ")
            Add_new_employee()
        elif ch=="2" :
            print("Write Modify_employee_details function above and call it here  ")
            Modify_employee_details()
        elif ch=="3" :
            print("Write Delete_employee_details function above and call it here  ")
            Delete_employee_details()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! ","                                   ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) ")

def Add_new_employee():
    print("\n\n\n")
    print(" "*25, "In Add_new_employee function ")
    print("\n\n\n")

 
    em_name = input("Add Name of Employee ")
    
    cursor.execute("select * from department")
    data=cursor.fetchall()
    for row in data:
        print(row)
    deptid = int(input("Add Department ID "))

    dyears=0   
    birthdate = input("Enter Birth Date in YYYY/MM/DD Format ")
    format = '%Y/%m/%d'
    bdate = datetime.datetime.strptime(birthdate, format)  
    difference  = bdate- datetime.datetime.now()
    dyears = (difference.days + difference.seconds/86400)/365.2425
    dyears=dyears*(-1)
    if dyears < 18 :
        print("Employee's age is less than 18 so not allowed to hire ")
        return 
        
    jobtitle = input("Add Job Title ")

    basicsalary = int(input("Add basicsalary "))
    
    qr="insert into employees (em_name,deptid,birthdate,jobtitle,basicsalary) values ('%s', '%s' , '%s' , '%s' , %s)"%(em_name,deptid,birthdate,jobtitle,basicsalary)

    print("Employee Details Added Successfully")
    print()
    print()
    cursor.execute(qr)
    mycon.commit()
          

def Modify_employee_details():
    print("\n\n\n")
    print(" "*25, "In Modify_employee_details function ")
    print("\n\n\n")


    cursor.execute("select * from employees")
    dt=cursor.fetchall()
        
       
    for row in dt:
        print(row)
        
    em_no=int(input("Emloyee ID "))
    qr="select * from employees where em_no=%s"%(em_no)
        
    cursor.execute(qr)
    dt=cursor.fetchall()
        

    for row in dt:
        em_name=row[1]
        deptid=row[2]
        birthdate=row[3]
        jobtitle=row[4]
        basicsalary=row[5]
           
        
    print(" "*25,"1. Employee Name ")
    print(" "*25,"2. Department ID ")
    print(" "*25,"3. Birth Date ")
    print(" "*25,"4. Job Title ")
    print(" "*25,"5. Basic Salary ")
    ch=int(input("Pls enter which field you wish to modify "))


                    
    while True : 
                    if ch==1:
                          em_name=input("Enter Employee Name ")
                          break
                    elif ch==2:
                          deptid=input("Enter Department ID ")
                          break
                    elif ch==3:
                          birthdate=input("Enter Birth Date ")
                          break
                    elif ch==4:
                          jobtitle=input("Enter Job Title ")
                          break
                    elif ch==5:
                          basicsalary=input("Enter Basic Salary ")
                          break
                    else :
                          print(" "*25,"Please enter right choice (1/2/3/4/5/0) ")
                      
    qr="update employees set em_name='%s', deptid=%s, birthdate='%s',jobtitle='%s',basicsalary=%s where em_no=%s"%(em_name,deptid,birthdate,jobtitle,basicsalary,em_no)

    print("Employee Details Updated Successfully")    
    cursor.execute(qr)
    mycon.commit()
    print()
    print()
    print("="*77)

def Delete_employee_details() :
    print("\n\n\n")
    print(" "*25, "In Delete_employee_details function ")

    cursor.execute("select * from employees")
    dt=cursor.fetchall()
        
       
    for row in dt:
        print(row)  
        
    em_no=int(input("Emloyee ID "))
                          
    qr="update employees set empstatus='Resigned' where em_no=%s"%(em_no)
    print("Employee Details Deleted Successfully")
    cursor.execute(qr)
    mycon.commit()
    print("Record for Employee",qr,"has been deleted Successfully")
    print()
    print()
    print("="*77)





def Salary_Details():
    print("\n\n\n")
    print(" "*25, "In Salary_Details function ")

    while True :
        print("="*20,"PAYROLL MANAGEMENT SYSTEM","="*20)
        print("|"," "*25,"1. Add_Allowances/Deduction","                              |")
        print("|"," "*25,"2. Modify_Allowances/Deduction","                           |")
        print("|"," "*25,"3. Delete_Allowances/Deduction","                           |")
        print("|"," "*25,"0. Quit","                                                  |")
        print("="*77)
        ch=input("                    Enter your Choice (1/2/3/0) : ")

        if ch== "1":
            print("Write Add_Allowances/Deduction function above and call it here  ")
            Add_Allowances_Deductions()
        elif ch=="2" :
            print("Write Modify_Allowances/Deduction function above and call it here  ")
            Modify_Allowances_Deductions()
        elif ch=="3" :
            print("Write Delete_Allowances/Deduction function above and call it here  ")
            Delete_Allowances_Deductions()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! ","                                   ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) ")

def Add_Allowances_Deductions():
    print("\n\n\n")
    print(" "*25, "In Add_Allowances_Deductions function ")
    print("\n\n\n")

    cursor.execute("select * from salarydetails")
    data=cursor.fetchall()
    for row in data:
        print(row)
        
    allowancesdeductions = input("Add Allowances/Deductions ")
    percentage = int(input("Add Percentage For Allowances/Deductions "))
    Type = input("Add A for Allowances/D for Deductions (A/D)")
    
    qr="insert into salarydetails (allowancesdeductions,percentage,Type) values ('%s' , %s , '%s' )"%(allowancesdeductions,percentage,Type)

    print("Allowances/Deductions Added Successfully ")
    print()
    print()
    cursor.execute(qr)
    mycon.commit()

    
    
def Modify_Allowances_Deductions():
    print("\n\n\n")
    print(" "*25, "In Modify_Allowances/Deduction function ")
    print("\n\n\n")

    cursor.execute("select * from salarydetails")
    dt=cursor.fetchall() 
    for row in dt:
        print(row)
        
    salarydetailsid=int(input("Salary Details ID "))
    qr="select * from salarydetails where salarydetailsid=%s"%(salarydetailsid)
        
    cursor.execute(qr)
    dt=cursor.fetchall()
        

    for row in dt:
        allowancesdeductions=row[1]
        percentage=row[2]
        Type=row[3]
           
        
    print(" "*25,"1. Allowances/Deductions ")
    print(" "*25,"2. Percentage ")
    print(" "*25,"3. Type ")
    ch=int(input("Pls enter which field you wish to modify "))


                    
    while True : 
                    if ch==1:
                          allowancesdeductions=input("Enter Allowances/Deductions ")
                          break
                    elif ch==2:
                          percentage=input("Enter Percentage ")
                          break
                    elif ch==3:
                          Type=input("Enter Type ")
                          break
                    else :
                          print(" "*25,"Please enter right choice (1/2/3/0) ")
                      
    qr="update salarydetails set allowancesdeductions='%s', percentage=%s, Type='%s' where salarydetailsid=%s"%(allowancesdeductions,percentage,Type,salarydetailsid)

    print("Allowances/Deductions Updated Successfully")    
    cursor.execute(qr)
    mycon.commit()
    print()
    print()         
    print("="*77)

    
def Delete_Allowances_Deductions():
    print("\n\n\n")
    print(" "*25, "In Delete_Allowances/Deduction function ")
    print("\n\n\n")

    cursor.execute("select * from salarydetails")
    dt=cursor.fetchall()   
    for row in dt:
        print(row)  
        
    salarydetailsid=int(input("Salary Details ID "))                          
    qr="delete from salarydetails where salarydetailsid=%s"%(salarydetailsid)    
    print("Allowances/Deductions Deleted Successfully ")
    cursor.execute(qr)
    mycon.commit()
    print("Record for ",salarydetailsid," salarydetails is deleted Successfully")
    print()
    print()
    print("="*77)




        
def Department() :
    print("\n\n\n")
    print(" "*25, "In Department function ")

    while True :
        print("="*20,"PAYROLL MANAGEMENT SYSTEM","="*20)
        print("|"," "*25,"1. Add_Department","                   |")
        print("|"," "*25,"2. Modify_Department","                |")
        print("|"," "*25,"2. Delete_Department","                |")
        print("|"," "*25,"0. Quit","                             |")
        print("="*77)
        ch=input("                    Enter your Choice (1/2/3/0) : ")

        if ch== "1":
            print("Write Add_Department  function above and call it here  ")
            Add_Department()
        elif ch=="2" :
            print("Write Modify_Department function above and call it here  ")
            Modify_Department()
        elif ch=="3" :
            print("Write Delete_Department function above and call it here  ")
            Delete_Department()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! ","                                   ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/0) ")

def Add_Department():
    print("\n\n\n")
    print(" "*25, "In Add_Department function ")
    print("\n\n\n")

    cursor.execute("select * from department")
    data=cursor.fetchall()
    for row in data:
        print(row)
    deptid = int(input("Add Department ID "))
    deptname = input("Add Departpart Name ")
    
    qr="insert into department (deptid,deptname) values (%s, '%s')"%(deptid,deptname)
    print("Department Added Successfully")
    print()
    print()
    cursor.execute(qr)
    mycon.commit()
    
def Modify_Department():
    print("\n\n\n")
    print(" "*25, "In Modify_Department function ")
    print("\n\n\n")

    cursor.execute("select * from department")
    dt=cursor.fetchall()
        
       
    for row in dt:
        print(row)
        
    deptid=int(input("Department ID "))
    
    deptname=input("Enter Department Name ")
                    
                 
    qr="update department set deptname='%s' where deptid=%s"%(deptname,deptid)
    print("Department Updated Successfully")
    print()
    print()
    cursor.execute(qr)
    mycon.commit()                
    print("="*77)

def Delete_Department():
    print("\n\n\n")
    print(" "*25, "In Delete_Department function ")
    print("\n\n\n")

    cursor.execute("select * from department")
    dt=cursor.fetchall()
        
       
    for row in dt:
        print(row)  
        
    deptid=int(input("Department ID "))                          
    qr="delete from department where deptid=%s"%(deptid)    
    cursor.execute(qr)
    mycon.commit()
    print("Record for ",deptid," department is deleted Successfully")
    print()
    print()
    print("="*77)



        
def Calculate_Montly_Salary() :
       
    dt=str(date.today())
    print("Today's Date is ",dt)
    dt=str(dt)
    day=int(dt[8]+dt[9])
    
    monthn=['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
    if day==10:
        mn=int(dt[5]+dt[6])
        mn=mn-2
        monthname=monthn[mn]
        yy=int(dt[0]+dt[1]+dt[2]+dt[3])
        str1=str("Enter total working days for the month %s : "%(monthname))
        twdays=int(input(str1 ))
        
        eid=0
        empid=[]
        cursor.execute("select * from employees")
        data=cursor.fetchall()
        for row in data:
            str1=str("Enter working days for %s : "%(row[0]))
            eid=int(row[0])
            wkd=int(input(str1))
            print("Working Days : ",wkd)
            cbasic=(row[5]/twdays)*wkd
           
            cbasic=(row[5]/twdays)*wkd
            cbasic = float("{:.2f}".format(cbasic))
            print("type cbasic ",cbasic)
            
            cursor.execute("select * from salarydetails")
            data=cursor.fetchall()
            for r in data:
                Percent=int(r[2])
                Type=r[3]
                if Type=='A':
                    All=((cbasic*Percent)/100)
                    tAll=cbasic+All
                elif Type=='D' :  
                    Dec= ((cbasic*Percent)/100)
                    tDec=cbasic+Dec
            
            Allowance=tAll
            Deduction=tDec
            NetSalary = (cbasic + Allowance) - Deduction
            NetSalary = "{:.2f}".format(NetSalary)
          
            print("Month Name : ",monthname)
            print("Year : ",yy)
            print("Employee Id : ",eid)
            print("Total Working Days : ",twdays)
            print("Working Days: ",wkd)
            print("Total Monthly Salary : ",cbasic)
            print("Net Salary: ",NetSalary)
            print()
            print()
            
            qr="insert into monthlysalary (monthname,year,empid,totalworkingdays,workingdays,netsalary) values ('%s' , %s , %s , %s , %s, %s)"%(monthname,yy,eid,twdays,wkd,NetSalary)
            print("Net Salary Has Been Calculated Successfully ")
            cursor.execute(qr)
            mycon.commit()


        

   

def MainMenu():
    print("\n"*30 )
    Calculate_Montly_Salary()
    while True :
        
        print("="*20,"PAYROLL MANAGEMENT SYSTEM","="*20)
        print("|"," "*25,"1. Employees_Details","                           |")
        print("|"," "*25,"2. Allowances & Deductions","                     |")
        print("|"," "*25,"3. Department","                                  |")
        print("|"," "*25,"4. Calculate_Montly_Salary","                     |")
        print("|"," "*25,"0. Exit","                                        |")
        print("="*77)
        
        ch=input("                    Enter your Choice (1/2/3/4/0) : ")
        

        if ch== "1":
            print("Write Employees_Details function above and call it here  ")
            Employees_Details()
        elif ch=="2" :
            print("Write Salary_Details function above and call it here  ")
            Salary_Details()
        elif ch=="3" :
            print("Write Department function above and call it here  ")
            Department()
        elif ch=="4":
            print("Write Calculate_Montly_Salary function above and call it here  ")
            Calculate_Montly_Salary()
        elif ch=="0" :
                print(" "*30," THANK YOU!!! ","                                   ")
                break
        else :
            print(" "*25,"Please enter right choice (1/2/3/4/5/0) ")

MainMenu()
