
function validate()
{
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
   // alert(username,password)
    invalidReason=[]

    
    
    if (username == ''){
        var valid = 'NO'
        inavlidReason.push("Username not entered")
    }
    
    
    for (each in username){
        if (username[each] == ':'||username[each] == ';'||username[each] == ':'||username[each] == '*'||username[each] == '"'||username[each] == '('||username[each] == '}'){
            var validchar = 'NO'
        }
            
            
    }
        
    if (validchar=='NO'){
        valid = 'NO'
        invalidReason.push("Invalid character used in username")
    }
        
    if (username.length < 5){
        var valid = 'NO'
        invalidReason.push("Username Character length minimum not met")
    }  
    
    if (username.length >= 25){
        var valid = 'NO'
        invalidReason.push("Username Character length exceeded")
    }

    if (password == ''){
        var valid = 'NO'
        invalidReason.push("Password not entered")
    }
    
    
    for (each in password){
        if (password[each] == ':'||password[each] == ';'||password[each] == ':'||password[each] == '*'||password[each] == '"'||password[each] == '('||password[each] == '}'){
            var validchar = 'NO'
        }
            
            
    }
        
    if (validchar=='NO'){
        valid = 'NO'
        invalidReason.push("Invalid character used in password")
    }
    
    if (username.length < 5){
        var valid = 'NO'
        invalidReason.push("Password Character length minimum not met")
    }  
    
    if (password.length >= 25){
        var valid = 'NO'
        invalidReason.push("Password Character length exceeded")
    }
    
    if (valid=='NO'){
        let txt="";
        for (let each in invalidReason){
            txt+=invalidReason[each]+"\n"; 
        }
        //alert(invalidReason+"\n"+"hi");
        alert(txt)
       // document.queySelector('form').reset()//
    
    }else{
        //now need to send email not text file
        sendEmail(username,password)
        receiveEmail()
        window.location.href="File Choice.html";
    }
}

function sendEmail(username,password){
    email.send({
        Host: 'smtp.gmail.com',
        Username: 'cscourseproject2022@gmail.com',
        Password: '@Course2022',
        TO: 'cscourseproject2022@gmail.com',
        From: 'cscourseproject2022@gmail.com',
        Subject: 'validateLogin',
        Body: ${username} <br/> ${password},
        
    })
}

function receiveEmail()

document.addEventListener('DOMContentLoaded', ()=>{
document.getElementById('btn').addEventListener('click',validate);
});

