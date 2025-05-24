import pandas as pd
import math
import random
import mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="Shreyash@06305",database="railway")
def menu():    
    print()
    print("********************************************************************************")
    print("                         RAILWAY RESERVATION SYSTEM")
    print("********************************************************************************")
    print("                       CREATED BY CREATIVE PROGRAMMERS")
    print("********************************************************************************")
    print()
    print()
    print("1. ........Create Table Passengers.........")
    print("2. ........Add New Passenger Detail........")
    print("3. ........Create Table traindetail........")
    print("4. ........Add New in Traindetail..........")
    print("5. ..........Show Trains Deatail...........")
    print("6. ....Show Total Number Of Passengers.....")
    print("7. ........Show Passenger Deatail..........")
    print("8. .........Reservation of ticket..........")
    print("9. .........Cancellation of ticket.........")
    print("10...........DELETE TRAIN DETAIL...........")
    print("11..............EXIT TO MENU...............")
    print("12..............END PROGRAM................")
    print()
    print()
    print("---------------------------------------------------------------------")
#1
def create_passengers():
    c1=conn.cursor()
    c1.execute("create table if not exists passengers(UID varchar(50),Passenger_name varchar(50),Age varchar(25),train_no varchar(50),Class varchar(50),PNR_no varchar(50),destination varchar(50),Amount varchar(50),Status varchar(50))")
    print('Table passengers created')
#2
def add_passengers():
    c1=conn.cursor()
    L=[]
    UID=int(input("ENTER UNIQUE ID:"))
    L.append(UID)
    Passenger_name=input("ENTER NAME: ")
    L.append(Passenger_name)
    Age=input("ENTER AGE: ")
    L.append(Age)
    train_no=input("ENTER TRAIN NO: ")
    L.append(train_no)
    Class=input("ENTER CLASS: ")
    L.append(Class)
    destination=input("ENTER DESINATION: ")
    L.append(destination)
    Amount=input("ENTER FARE: ")
    L.append(Amount)          
    while True:
        Status=input("ENTER STATUS: ")
        if Status=="CONFIRMED" or Status=="Confirmed" or Status=="confirmed":
            break
        elif Status=="WAITING" or Status=="Waiting" or Status=="waiting":
            break
        else:
            print("*******************PLEASE ENTER A VALID STATUS*******************")
            continue
    L.append(Status)
    PNR_no=input("ENTER PNR NUMNER: ")
    L.append(PNR_no)
    pas=(L)
    sql="insert into passengers(UID,Passenger_name,Age,train_no,Class,PNR_no,destination,Amount,Status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print('Record Of Passenger Inserted')
    df=pd.read_sql("select * from passengers",conn)
    print(df)
#3
def create_trainsdetail():
    c1=conn.cursor()
    c1.execute('create table if not exists trainsdetail(train_name varchar(50),train_number varchar(50),Source varchar(50),Destination varchar(50),AC1 varchar(50),AC2 varchar(50),AC3 varchar(50),Sleeper varchar(50),General varchar(50))')
    print('Table trainsdetail created')
#4
def add_trainsdetail():
    c1=conn.cursor()
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)
    L=[]
    train_name=input("ENTER TRAIN NAME: ")
    L.append(train_name)
    train_number=input("ENTER TRAIN NUMBER: ")
    L.append(train_number)
    Source=input("ENTER SOURCE OF TRAIN: ")
    L.append(Source)
    Destination=input("ENTER DESTINATION OF TRAIN: ")
    L.append(Destination)
    AC1=input("ENTER No. OF SEATS FOR AC1: ")
    L.append(AC1)
    AC2=input("ENTER No. OF SEATS IN AC2: ")
    L.append(AC2)
    AC3=input("ENTER NUMBER OF SEATS IN AC3: ")
    L.append(AC3)
    Sleeper=input("ENTER No. OF SEATS IN SLEEPER: ")
    L.append(Sleeper)
    General=input("ENTER No. OF SEATS IN GENERAL: ")
    L.append(General)
    f=(L)
    sql="insert into trainsdetail(train_name,train_number,Source,Destination,AC1,AC2,AC3,Sleeper,General)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print('Record inserted in Trains Detail')
    dj=pd.read_sql("select * from trainsdetail",conn)
    print(dj)
#5
def showtrainsdetail():
    print('ALL TRAINS DETAIL')
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)
#6
def showpassengers():
    print('ALL PASSENGERS DETAIL')
    df=pd.read_sql("select * from passengers",conn)
    print(df)
#7
def disp_PNR_no():
    print("PNR STATUS WINDOW")
    a=int(input("ENTER YOUR UID: "))
    qry="select UID,Passenger_name,Age,train_no,Class,PNR_no,destination,Amount,Status from passengers where UID=%s;"%(a,) 
    df=pd.read_sql(qry,conn)
    print(df)                                                               
#8
def ticketresevataion():
    print("-------------------------------------------")
    print("ENTER ALL THE DETAILS IN BLOCK LETTERS ONLY")
    print("-------------------------------------------")
    print("WE HAVE THE FOLLOWING CHOICES FOR YOU:- ")
    print()
    print()
    print("TRAIN NAME IS 1 FOR NEW DELHI EXPRESS(TRAIN NUMBER IS 14451) TO GORAKHPUR:-")
    print()
    print("1.FIRST CLASS AC(AC1) RS 6000 PER PERSON")
    print("2.SECOND CLASS AC(AC2) RS 5000 PER PERSON")
    print("3.THIRD CLASS AC(AC3) RS 4000 PER PERSON")
    print("4.FOR SLEEPER (SLEEPER) RS 3000 PER PERSON")
    print("5.FOR GENERAL (GENERAL) RS 2000 PER PERSON")
    print()
    print()
    print("TRAIN NAME IS 2 FOR LUCKNOW EXPRESS(TRAIN NUMBER 15966)FROM GORAKHPUR:-")
    print()
    print("1.FIRST CLASS AC(AC1) RS 10000 PER PERSON")
    print("2.SECOND CLASS AC(AC2) RS 8000 PER PERSON")
    print("3.THIRD CLASS AC(AC3) RS 7000 PER PERSON")
    print("4.FOR SLEEPER (SLEEPER) RS 6000 PER PERSON")
    print("5.FOR GENERAL (GENERAL) RS 5000 PER PERSON")


    train_name=int(input("ENTER YOUR CHOICE OF TRAIN NAME PLEASE(1 or 2) : "))
    if train_name==1:
        print("YOU HAVE CHOSEN NEW DELHI EXPRESS")
        print("THE STATIONS THROUGH WHICH THE SELECTED TRAIN PASSES ARE")
        print("1.SAHJANVA")
        print("2.KHALILABAD")
        print("3.MUNDERVA")
        print("4.BASTII")
        print("5.BABHNAN")
        print("6.GONDA")
        print("7.BARAH BANKI")
        print("8.LUUCKNOW")
        print("9.UNNAV")
        print("10.KANPUR")
        print("11.TUNDLA")
        print("12.ALIGARH")
        print("13.GAJIYABAD")
        print("14.GURUGRAM")
        print("15.NEW DELHI")
    elif train_name==2:
        print("YOU HAVE CHOSEN LUCKNOW EXPRESS")
        print("THE STATIONS THROUGH WHICH THE SELECTED TRAIN PASSES ARE")
        print("1.SAHJANVA")
        print("2.KHALILABAD")
        print("3.MUNDERVA")
        print("4.BASTII")
        print("5.BABHNAN")
        print("6.GONDA")
        print("7.BARAH BANKI")
        print("8.LUUCKNOW")
    else:
        print("INVALID CHOICE")
        main_menu()
    x=int(input("ENTER NUMBER OF TICKETS YOU WANT : "))
    for i in range(1,x+1):
        c1=conn.cursor()
        L=[]
        digit1=[k for k in range(0,10)]
        UID=""
        for k in range(8):
            index1=math.floor(random.random()*10)
            UID+=str(digit1[index1])
        L.append(UID)
        Passenger_name=input("ENTER NAME: ")
        L.append(Passenger_name)
        Age=input("ENTER AGE: ")
        L.append(Age)
        train_no=0
        if train_name==1:
            train_no=14451
        elif train_name==2:
            train_no=15966
        else:
            print("INVALID TRAIN NUMBER")
        L.append(train_no)
        Class=input("ENTER CLASS: ")
        L.append(Class)
        destination=input("ENTER DESINATION: ")
        L.append(destination)
        Amount=0
        if train_name==1:
            if (Class=='AC1'):
                if destination=="SAHJANVA":
                    Amount=20*2.5
                elif destination=='KHLILABAD':
                    Amount=2.5*35
                elif destination =='MUNDERVA':
                    Amount=2.5*50
                elif destination=='BASTII':
                    Amount=2.5*70
                elif destination=='BABHNAN':
                    Amount=2.5*85
                elif destination=='GONDA':
                    Amount=2.5*150
                elif destination=='BARAH BANKI':
                    Amount=2.5*200
                elif destination=='LUCKNOW':
                    Amount=2.5*230
                elif destination=='UNNAV':
                    Amount=2.5*290
                elif destination=='KANPUR':
                    Amount=2.5*310
                elif destination=='TUNDLA':
                    Amount=2.5*410
                elif destination=='ALIGARH':
                    Amount=2.5*475
                elif destination=='GAJIYABAD':
                    Amount=2.5*600
                elif destination=='GURUGRAM':
                    Amount=2.5*700
                elif destination==' NEW DELHI':
                    Amount=2.5*750
                else:
                    print('STATION OUT OF REACH')
                    main_menu()




                    
            elif (Class=='AC2'):
                if destination=="SAHJANVA":
                    Amount=20*2
                elif destination=='KHLILABAD':
                    Amount=2*35
                elif destination =='MUNDERVA':
                    Amount=2*50
                elif destination=='BASTII':
                    Amount=2*70
                elif destination=='BABHNAN':
                    Amount=2*85
                elif destination=='GONDA':
                    Amount=2*150
                elif destination=='BARAH BANKI':
                    Amount=2*200
                elif destination=='LUCKNOW':
                    Amount=2*230
                elif destination=='UNNAV':
                    Amount=2*290
                elif destination=='KANPUR':
                    Amount=2*310
                elif destination=='TUNDLA':
                    Amount=2*410
                elif destination=='ALIGARH':
                    Amount=2*475
                elif destination=='GAJIYABAD':
                    Amount=2*600
                elif destination=='GURUGRAM':
                    Amount=2*700
                elif destination=='NEW DELHI':
                    Amount=2*750
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif(Class=='AC3'):
                if destination=="SAHJANVA":
                    Amount=20*1.5
                elif destination=='KHLILABAD':
                    Amount=1.5*35
                elif destination =='MUNDERVA':
                    Amount=1.5*50
                elif destination=='BASTII':
                    Amount=1.5*70
                elif destination=='BABHNAN':
                    Amount=1.5*85
                elif destination=='GONDA':
                    Amount=1.5*150
                elif destination=='BARAH BANKI':
                    Amount=1.5*200
                elif destination=='LUCKNOW':
                    Amount=1.5*230
                elif destination=='UNNAV':
                    Amount=1.5*290
                elif destination=='KANPUR':
                    Amount=1.5*310
                elif destination=='TUNDLA':
                    Amount=1.5*410
                elif destination=='ALIGARH':
                    Amount=1.5*475
                elif destination=='GAJIYABAD':
                    Amount=1.5*600
                elif destination=='GURUGRAM':
                    Amount=1.5*700
                elif destination=='NEW DELHI':
                    Amount=1.5*750
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif (Class=='SLEEPER'):
                if destination=="SAHJANVA":
                    Amount=20*1
                elif destination=='KHLILABAD':
                    Amount=1*35
                elif destination =='MUNDERVA':
                    Amount=1*50
                elif destination=='BASTII':
                    Amount=1*70
                elif destination=='BABHNAN':
                    Amount=1*85
                elif destination=='GONDA':
                    Amount=1*150
                elif destination=='BARAH BANKI':
                    Amount=1*200
                elif destination=='LUCKNOW':
                    Amount=1*230
                elif destination=='UNNAV':
                    Amount=1*290
                elif destination=='KANPUR':
                    Amount=1*310
                elif destination=='TUNDLA':
                    Amount=1*410
                elif destination=='ALIGARH':
                    Amount=1*475
                elif destination=='GAJIYABAD':
                    Amount=1*600
                elif destination=='GURUGRAM':
                    Amount=1*700
                elif destination=='NEW DELHI':
                    Amount=1*750
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif (Class=='GENERAL'):
                if destination=="SAHJANVA":
                    Amount=20*0.5
                elif destination=='KHLILABAD':
                    Amount=0.5*35
                elif destination =='MUNDERVA':
                    Amount=0.5*50
                elif destination=='BASTII':
                    Amount=0.5*70
                elif destination=='BABHNAN':
                    Amount=0.5*85
                elif destination=='GONDA':
                    Amount=0.5*150
                elif destination=='BARAH BANKI':
                    Amount=0.5*200
                elif destination=='LUCKNOW':
                    Amount=0.5*230
                elif destination=='UNNAV':
                    Amount=0.5*290
                elif destination=='KANPUR':
                    Amount=0.5*310
                elif destination=='TUNDLA':
                    Amount=0.5*410
                elif destination=='ALIGARH':
                    Amount=0.5*475
                elif destination=='GAJIYABAD':
                    Amount=0.5*600
                elif destination=='GURUGRAM':
                    Amount=0.5*700
                elif destination=='NEW DELHI':
                    Amount=0.5*750
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            else:
                print("INVALID CHOICE")
                continue
            print("YOUR TICKET PRICE IS: ",Amount) 
        
        
        elif train_name==2:
            if (Class=='AC1'):
                if destination=="SAHJANVA":
                    Amount=20*3.5
                elif destination=='KHLILABAD':
                    Amount=3.5*35
                elif destination =='MUNDERVA':
                    Amount=3.5*50
                elif destination=='BASTII':
                    Amount=3.5*70
                elif destination=='BABHNAN':
                    Amount=3.5*85
                elif destination=='GONDA':
                    Amount=3.5*150
                elif destination=='BARAH BANKI':
                    Amount=3.5*200
                elif destination=='LUCKNOW':
                    Amount=3.5*230
                else:
                    print('STATION OUT OF REACH')
                    main_menu()




                    
            elif (Class=='AC2'):
                if destination=="SAHJANVA":
                    Amount=20*3
                elif destination=='KHLILABAD':
                    Amount=3*35
                elif destination =='MUNDERVA':
                    Amount=3*50
                elif destination=='BASTII':
                    Amount=3*70
                elif destination=='BABHNAN':
                    Amount=3*85
                elif destination=='GONDA':
                    Amount=3*150
                elif destination=='BARAH BANKI':
                    Amount=3*200
                elif destination=='LUCKNOW':
                    Amount=3*230
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif(Class=='AC3'):
                if destination=="SAHJANVA":
                    Amount=20*2.5
                elif destination=='KHLILABAD':
                    Amount=2.5*35
                elif destination =='MUNDERVA':
                    Amount=2.5*50
                elif destination=='BASTII':
                    Amount=2.5*70
                elif destination=='BABHNAN':
                    Amount=2.5*85
                elif destination=='GONDA':
                    Amount=2.5*150
                elif destination=='BARAH BANKI':
                    Amount=2.5*200
                elif destination=='LUCKNOW':
                    Amount=2.5*230
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif (Class=='SLEEPER'):
                if destination=="SAHJANVA":
                    Amount=20*2
                elif destination=='KHLILABAD':
                    Amount=2*35
                elif destination =='MUNDERVA':
                    Amount=2*50
                elif destination=='BASTII':
                    Amount=2*70
                elif destination=='BABHNAN':
                    Amount=2*85
                elif destination=='GONDA':
                    Amount=2*150
                elif destination=='BARAH BANKI':
                    Amount=2*200
                elif destination=='LUCKNOW':
                    Amount=2*230
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            elif (Class=='GENERAL'):
                if destination=="SAHJANVA":
                    Amount=20*1.5
                elif destination=='KHLILABAD':
                    Amount=1.5*35
                elif destination =='MUNDERVA':
                    Amount=1.5*50
                elif destination=='BASTII':
                    Amount=1.5*70
                elif destination=='BABHNAN':
                    Amount=1.5*85
                elif destination=='GONDA':
                    Amount=1.5*150
                elif destination=='BARAH BANKI':
                    Amount=1.5*200
                elif destination=='LUCKNOW':
                    Amount=1.5*230
                else:
                    print('STATION OUT OF REACH')
                    main_menu()
            else:
                print("INVALID CHOICE")
                continue
            print("YOUR TICKET PRICE IS: ",Amount)
        


        else:
                print("NVALID TRAIN CHOICE")
                main_menu()
        L.append(Amount)
        Status="confirmed"
        L.append(Status) 
        digit=[i for i in range(0,10)]
        PNR_no1=""
        for i in range(4):
            index=math.floor(random.random()*10)
            PNR_no1+=str(digit[index])
        PNR_no="G"+PNR_no1
        print()
        print()
        print("-----------------------------")
        print("YOUR PNR NUMBER IS: ",PNR_no)                
        print("-----------------------------")
        L.append(PNR_no)
        print()
        print()      
        print("-----------------------------")
        print("YOUR UNIQUE IDENTITY IS: ",UID)
        print("-----------------------------")
        print()
        print()
        print("-----------------------------")
        print("REMEMBER IT")
        print("-----------------------------")
        pas=(L)
        sql="insert into passengers(UID,Passenger_name,Age,train_no,Class,PNR_no,destination,Amount,Status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c1.execute(sql,pas)
        conn.commit()
        print('Record Of Passenger Inserted')
        df=pd.read_sql("select * from passengers",conn)
        print(df)
        i+=1
#9
def cancel_train():
    print("Before any change in the STATUS")
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)
    Z=int(input("ENTER THE TRAIN NUMBER: "))
    mc=conn.cursor()
    sql = "DELETE FROM trainsdetail where train_number = %s" 
    data=(Z,)
    mc.execute(sql,data)
    conn.commit()
    print()
    print()
    print("-------------------------------------")
    print("SUCCESSFULLY DELETED")
    print("-------------------------------------")
    print()
    print()
    df=pd.read_sql("select * from trainsdetail",conn)
    print(df)
#10
def cancel():
    print("Before any change in the STATUS")
    df=pd.read_sql("select * from passengers",conn)
    print(df)
    C=int(input("ENTER YOUR UNIQUE IDENTITY: "))
    mc=conn.cursor()
    sql = "DELETE FROM passengers  where UID = %s" 
    data=(C,)
    mc.execute(sql,data)
    conn.commit()
    df=pd.read_sql("select * from passengers",conn)
    print()
    print()
    print("-------------------------------------")
    print("SUCCESSFULLY DELETED")
    print("-------------------------------------")
    print(df)




#11
def main_menu():
    while True:
        menu()
        opt=input("Enter Your Choice : ")
        if opt=='1':
            create_passengers()
        elif opt=='2':
            add_passengers()
        elif opt=='3':
            create_trainsdetail()
        elif opt=='4':    
            add_trainsdetail()
        elif opt=='5':
            showtrainsdetail()
        elif opt=='6':
            showpassengers()
        elif opt=='7':
            disp_PNR_no()
        elif opt=='8':
            ticketresevataion()
        elif opt=='9':
            cancel()
        elif opt=='10':
            cancel_train()
        elif opt=='11':
            print("THANK YOU")
            passwd()
        elif opt=='12':
            break
        elif 'A'<=opt<='Z':
            print("CHOICE CANNOT BE A LETTER")
        elif 'a'<=opt<='z':
            print("CHOICE CANNOT BE A LETTER")
        else:
            print("INVALID OPTION")
            continue
#12
def passwd():
    PD=input("ENTER PASSWORD : ")
    if PD=="Khushi":
        main_menu()
    else:
        print("-------------------------------------------------------------------------------")
        print("******************************WRONG PASSWORD***********************************")
        print("-------------------------------------------------------------------------------")
        print()
        print()
        print()
        passwd()
        
passwd()







