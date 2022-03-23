#either get the number of queiroes from text file either number or the number of lines
#get images and run api then save file location of object to DB by querying

import run_email
import sqlite3

def get_text(toQuery):
    queryTxt=[]
    with open(toQuery,mode='r',encoding='utf-8') as queryDBFile:
        for each in queryDBFile:
            queryTxt.append(each.rstrip('\n'))
    return queryTxt

def decrypt(cipherTxt):
    plainTxt=[]
    for each in range(0,len(cipherTxt)):
        addList=''
        for eachChar in cipherTxt[each]:
            addList=addList+chr(ord(eachChar)-5)
        plainTxt.append(addList)
    return plainTxt

def query(subject,plainTxt):
    toStrip=""",'(')"""
    conn=sqlite3.connect('server.db')
    c=conn.cursor()        
        
    if subject=='validateLogin':
        c.execute("SELECT UName FROM TblCustomer WHERE UName="+"""'"""+plainTxt[0]+"""'""")
        resultU=c.fetchone()
        c.execute("SELECT PWord FROM TblCustomer WHERE PWord="+"""'"""+plainTxt[1]+"""'""")
        resultP=c.fetchone()
        if resultU!=None and resultP!=None:
            return True
        else:
            return False            

    elif subject=='newUser':
        a="""'"""
        b=","
        c.execute("SELECT UName FROM TblCustomer WHERE UName="+a+plainTxt[5]+a)
        resultU=c.fetchone()
        print(resultU)
        if resultU==None:
            c.execute("INSERT INTO TblCustomer (FName,SName,Tel,UName,Pword) VALUES ("+a+plainTxt[0]+a+b+a+plainTxt[1]+a+b+a+plainTxt[4]+a+b+a+plainTxt[5]+a+b+a+plainTxt[6]+a+")")
            c.execute("SELECT userID FROM TblCustomer WHERE UName="+a+plainTxt[0]+a)
            userID=str(c.fetchone()).strip(toStrip)
            c.execute("INSERT INTO TblPostCode (userID,PostCode,Address) VALUES ("+a+userID+a+b+a+plainTxt[2]+a+b+a+plainTxt[3]+a+")")
            result= True
        else:
            result= False
        

    elif subject=='getEnvironment':
        c.execute("SELECT userID FROM TblCustomer WHERE UName="+a+userID+a)
        userID=str(c.fetchone()).strip(toStrip)
        c.execute("SELECT * FROM TblEorder WHERE userID="+a+userID+a)
        rslt=c.fetchall()
        num=print(len(rslt))

    elif subject=='getDesign':
        c.execute("SELECT userID FROM TblCustomer WHERE UName="+a+userID+a)
        userID=str(c.fetchone()).strip(toStrip)
        c.execute("SELECT * FROM TblDorder WHERE userID="+a+userID+a)
        rslt=c.fetchall()
        num=print(len(rslt))
        
    #commiting changes and closing db connection
    conn.commit()
    conn.close()

    


#javascript code saves username to email back to get specific files
#    elif toQuery=='photogrammetry'#If get attachments can handle multiple attachments
#    else: #get 3D  Design
        
    

def main():
    toQuery,subject=run_email.main()
    cipherTxt=get_text(toQuery)
    plainTxt=decrypt(cipherTxt)
    result=query(subject,plainTxt)
    print(result)
main()
