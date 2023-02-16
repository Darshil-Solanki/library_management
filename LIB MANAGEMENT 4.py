
#library management(BETA)
#created by Sankalp and Darshil
#resources+modules suite:-
import urllib
import webbrowser
import time
from prettytable import PrettyTable
members=open('member-data.dat','w+')
members1=open('member-activity.dat','w+')
library=open('library-data.dat','w+')
bookorder=open('book-order.dat','w+')
member1=['darshil','saurav','kashyap','parthiv','brij']
library1=['harry potter','IDLE GUI','hunger games','divergent']
#functions suite:-
def bookmodif(book1,book2):
        if book1 not in library1:
                print('this book does not exist at the first place.')
        else:
                library1.remove(book1)
                library1.append(book2)
                library.writelines(book2)
def passwordcheck(ID, password):
        if ID=='sankalp' and password==1312:
                return True
        elif ID=='darshil' and password==1234:
                return True
        elif ID=='pradeep sir' and password==1729:
                return True
        elif ID=='Kashyap' and password==4209:
                return True
        else:
                return False
def membercheck(user1):
        if user1 in member1:
                members1.write(user1)
        else:
                print('you are not a member yet.')
def bookindividual(g,g1,g2):
    fileopen1=open(g+',dat','w')
    elements1=('bookname:'+str(g)+'\n'+'author name:'+str(g1)+'\n'+'publisher name:'+str(g2)+'\n')
    fileopen1.writelines(elements1)
    fileopen1.close()
def memberindividual(b,bb,bbb):
    fileopen=open(g+'.dat','w')
    elements=('member name:-'+str(b)+'\n'+'date of enrollment'+str(bb)+'\n'+'email ID:-'+str(bbb)+'\n')
    fileopen.writelines(elements)
    fileopen.close()
def memberadd(a,aa,aaa):
    bce=('member name:-'+str(a)+'\n'+'date of enrollment'+str(aa)+'\n'+'email ID:-'+str(aaa)+'\n')              
    members.writelines(bce)
    member1.append(a)
def memberdel(b):                           
    mem1=open('member-data.dat','r')
    bbb=mem1.readlines()
    mem2=open('member-data.dat','w')
    z5=len(bbb)
    for c5 in range(z5):
        f5=bbb[c5]
        mem2.writelines(f5)
def bookissue(c):
        lib1=open('library-data.dat','r')
        read11=lib1.readlines()
        lib3=open('library-data.dat','w')
        z=len(read11)
        for c in range(z):
            f=read11[c]
            lib3.writelines(f)
def bookreturn(d):
        lib1=open('library-data.dat','r')
        read12=lib1.readlines()
        lib2=open('library-data.dat','w')
        z1=len(read12)
        for c1 in range(z1):
            f1=read12[c1]
            lib2.writelines(f1)
def bookadd(f,f1,f2):
        abc=('bookname:'+str(f)+'\n'+'author name:'+str(f1)+'\n'+'publisher name:'+str(f2)+'\n')             
        library.writelines(abc)
        library1.append(f)  
def bookremove(g):
        lib1=open('library-data.dat','r')
        read14=lib1.readlines()
        lib14=open('library-data.dat','w')
        z4=len(read14)
        for c4 in range(z4):
            f4=read14[c4]
            lib14.writelines(f4)
def bookorderremove(h):
        lib1=open('book-order.dat','r')
        read13=lib1.readlines()
        lib12=open('bookorder.dat','w')
        z2=len(read13) 
        for c3 in range(z2):
            f2=read13[c3] 
            lib12.writelines(f2)    
#main program:-          
print('--WELCOME TO LIBRARY MANAGEMENT SYSTEM--')
time.sleep(1)
while True:
    t5=PrettyTable(['MAIN MENU'])
    t5.add_row(['1. Initiate program'])
    t5.add_row(['2. Exit program'])
    t5.add_row(['3. View credits'])
    t5.add_row(['4. update database online'])
    print(t5)
    time.sleep(1)
    masteroption=int(input('choose(1-4):'))
    if masteroption==1:
        time.sleep(1)
        t4=PrettyTable(['SNo.','options'])
        t4.add_row(['1.','Librarian'])
        t4.add_row(['2.','Member'])
        print(t4)
        time.sleep(1)
        hello=int(input('choose any one(1-2):-'))
        if hello==1:
            while True:
                ID=(input('Enter user ID:-'))
                PASSWORD=int(input('enter Password:-'))
                a12=passwordcheck(ID,PASSWORD)
                time.sleep(1)
                if a12==True:
                        print('access granted')
                        break
                else:
                        time.sleep(1)
                        print('user ID or password incorrect.')
                        continue
            t1=PrettyTable(['SNo.','Options'])
            t1.add_row(['1.','Add/Remove/Edit a book'])
            t1.add_row(['2.','Issue a book(as a member)'])
            t1.add_row(['3.','Return a book(as a member)'])
            t1.add_row(['4.','Reserve a book(as a member)'])
            t1.add_row(['5.','Add a new member/Cancel membership'])
            t1.add_row(['6.','view member activity'])
            t1.add_row(['7.','change to member'])
            t1.add_row(['8.','update database online'])
            print(t1)
            time.sleep(1)
            while True:
                choice1=int(input('select your option(1-7):'))
                if choice1==1:
                    time.sleep(1)
                    t2=PrettyTable(['S.No','choice'])
                    t2.add_row(['1.','Add a book to the Database'])
                    t2.add_row(['2.','Remove a book from Database'])
                    t2.add_row(['3.','Edit book info'])
                    print(t2)
                    while True:
                        time.sleep(1)
                        choice12=int(input('Choose an option(1-3):'))
                        while True:
                            if choice12==1:
                                time.sleep(1)
                                bookname=(input('enter the name of book:'))
                                bookauthor=(input('enter the name of author:'))
                                bookpublish=(input('enter the name of publishing house:'))
                                bookadd(bookname,bookauthor,bookpublish)
                                bookindividual(bookname,bookauthor,bookpublish)
                                choice13=str(input('modifications complete(Y/N):'))
                                if choice13=='y' or choice13=='Y':
                                    break
                                else:
                                    continue
                            elif choice12==2:
                                time.sleep(1)
                                bookname=(input('enter the name of book:'))
                                bookremove(bookname)
                                choice14=(input('modifications complete(Y/N):'))
                                if choice14=='y' or choice14=='Y':
                                    break
                                else:
                                    continue
                            elif choice12==3:
                                time.sleep(1)
                                bookname=str(input('enter the name of book:'))
                                bookname1=str(input('enter the modification of the book'))
                                bookmodif(bookname,bookname1)
                                choice15=str(input('modifications complete(Y/N):'))
                                if choice15=='y' or choice15=='Y':
                                    print(library1)
                                    break
                                else:
                                    continue
                                time.sleep(1)
                        choice16=str(input('final modification(Y/N):'))
                        if choice16=='y' or choice16=='Y':
                            break
                        else:
                            continue
                elif choice1==2:
                        time.sleep(1)  
                        while True:
                                bookissue1=str(input('what book would you like to issue?:'))
                                if bookissue1 in library1:
                                    time.sleep(1)
                                    print('you have issued the book',bookissue1)
                                    bookissue(bookissue1)
                                    break
                                elif bookissue1 not in library1:
                                    time.sleep(1)
                                    print('sorry! book not available')
                                    break
                                else:
                                    time.sleep(1)
                                    print('error 505! book not found.')
                                    continue
                elif choice1==3:
                    time.sleep(1)
                    bookret=str(input('what book do you want to return:'))
                    bookreturn(bookret)
                elif choice1==4:
                    time.sleep(1)
                    bookreser=str(input('what book would you like to reserve:'))
                    bookorder(bookreser)
                elif choice1==5:
                            time.sleep(1)
                            t6=PrettyTable(['SNo.','choice'])
                            t6.add_row(['1.','add a member'])
                            t6.add_row(['2.','delete a member'])
                            print(t6)
                            option5=(input('choose command(1-2):'))
                            if option5==1:
                                    while True:
                                            user1=(input('enter member name:'))
                                            DOE=(input('enter date of enrollment:'))  
                                            emailID=(input('enter email-ID:-'))
                                            memberadd(user1,DOE,emailID)
                                            memberindividual(user1,DOE,emailID)
                                            choice152=('would you like to add more members?(Y/N):')
                                            if choice152=='y' or choice152=='Y':
                                                    continue
                                            else:
                                                    break
                            elif choice15==2:
                                user2=(input('enter member name:'))
                                memberdel(user2)
                                print(user2,' has been deleted.')
                                choice153=('would you like to delete more members?(Y/N):')
                                if choice153=='y' or choice153=='Y':
                                        continue
                                else:
                                        break
                                choice5=(input('final modification?(Y/N):'))
                                if choice5=='y' or choice5=='Y':
                                        continue
                                else:
                                        break
                elif choice1==6:
                    a=members1.readlines()
                    print(a)
                    break
                elif choice1==7:
                    break
                elif choice1==8:
                        Weburl=urllib.request.urlopen('http://127.0.0.1:8000/data/')
                        URL=Weburl.geturl()
                        webbrowser.open_new(URL)
        elif hello==2:
            user=(input('hello there, fellow member. please input your name:'))
            if user in member1:
                membercheck(user)
                time.sleep(1)
                print('Hello,',user,'what would you like to do?:')
                t3=PrettyTable(['S.No','choice'])
                t3.add_row(['1.','Issue a book'])
                t3.add_row(['2.','Return a book'])
                t3.add_row(['3.','Reserve a book'])
                t3.add_row(['4.','Cancel membership'])
                print(t3)
                time.sleep(1)
                choice7=int(input('what would you like to do?(1-4):'))
                while True:
                    if choice7==1:
                        time.sleep(1)
                        bookissue1=str(input('what book would you like to issue?:'))
                        if bookissue1 in library1:
                            time.sleep(1)
                            print('you have issued the book',bookissue1)
                            bookissue(bookissue1)
                            break
                        elif bookissue1 not in library1:
                            time.sleep(1)
                            print('sorry! book not available')
                            break
                        else:
                            time.sleep(1)
                            print('error 505! book not found.')
                            continue
                    elif choice7==2:
                        time.sleep(1)
                        bookret=(input('what book do you want to return:'))
                        bookremove(bookret)
                        print('thank you for returning your book on time.')
                        break
                    elif choice7==3:
                        time.sleep(1)
                        bookreser=(input('what book would you like to reserve:'))
                        bookorder(bookreser)
                        break
                    elif choice7==4:
                        time.sleep(1)
                        prompt=(input('are you sure you want to cancel membership?(Y/N):'))
                        if prompt=='Y' or prompt=='y':
                            memberdel(user)
                            time.sleep(1)
                        print('thank you for your time!')
                        break
                        time.sleep(1)
    elif masteroption==2:
        print('Thank you for your time!')
        break
    elif masteroption==3:
        print('program developed in year 2019 by Darshil &Sankalp(KVR)')
        break
    elif masteroption==4:

        Weburl=urllib.request.urlopen('http://127.0.0.1:8000/data/')
        URL=Weburl.geturl()
        webbrowser.open_new(URL)

