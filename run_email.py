#now comment

import os

#importing libraries to create connection

import imaplib, email


##FUNCTION##to authenticate and create the email connection
def auth(user,password,imap_url):
#create connection
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con

def new_email(con):
    count=0
    numEmails=len(get_emails(search('FROM','cscourseproject2022@gmail.com',con),con))
    while count==0:
        con.select('INBOX')
        newNumEmails=len(get_emails(search('FROM','cscourseproject2022@gmail.com',con),con))
        if newNumEmails>numEmails:
            toQuery,subject=getByte(newNumEmails,con)
            count+=1
            
    return toQuery,subject

                
#search for a particular email
def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data


#extracts emails from byte array
def get_emails(result_bytes,con):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

def getByte(newNumEmails,con):
    emailByte=search('TO','cscourseproject2022@gmail.com',con)
    lastEmail=[]
    for each in emailByte[0].split():
        lastEmail.append(each)   
    byte=lastEmail[len(lastEmail)-1]
    toQuery,subject=getSubject(byte,con)
    return toQuery,subject

def getSubject(byte,con):
    result, data = con.fetch(byte,'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    subject=raw['subject']
    attachment_dir = 'C:/Users/Chibueze/Documents/Compsci project/Project Code/Backend'
    toQuery=get_attachments(raw,attachment_dir,subject)
    return toQuery,subject


def get_attachments(msg,attachment_dir,subject):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()+subject+'.txt'

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
    return fileName


##MAIN FUNCTION##to pass login information and select the inbox to start accessing data
def main():
#Information for login
    user = 'cscourseproject2022@gmail.com'
    password = '@Course2022'
#Define server
    imap_url = 'imap.gmail.com'
#passes login information and obtains variable for connection
    con = auth(user,password,imap_url)
#Selects inbox to begin accessing data
    con.select('INBOX')
    toQuery,subject=new_email(con)

    return toQuery,subject






















##            return toQuery
##        else:
##            return False
#        count+=1
  #  dectdEmail='YES'
##    dectdEmail='NO'
##    while dectdEmail!='YES': #I think the while true will go in the send email section but we shall see
  #  print(dectdEmail)
  #      if toQuery!=False:

      #      dectdEmail=True



        

