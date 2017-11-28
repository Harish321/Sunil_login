from django.shortcuts import render, HttpResponse
import subprocess,time,sys
from threading import Thread
from .models import check_login 
def home(request):
    a = check_login.objects.get(id=1)
    print a.value
    if request.method == "POST":
        if request.POST.get("login"):
            cmd = 'curl -i -k --data "fw_username=sunil.j&fw_password=iiits@123&fw_domain=LDAP&action=fw_logon&fw_logon_type=logon" https://10.0.1.1:4100/wgcgi.cgi > tmp.txt'
            subprocess.call(cmd,shell=True)
            strings = ("Location: /./logon.shtml?errcode=505","Location: /./success.shtml","Location: /./logon.shtml?errcode=501")
            f = open("tmp.txt","r")
            for line in f:
                if strings[0] in line:
                    error = "Already logged in"
                    tp = "login"
                elif strings[1] in line:
                    a.value = 1
                    a.save()
                    print a.value
                    error = "success"
                    tp = "logout"
                elif strings[2] in line:
                    error = "Invalid Credentials"
                    tp = "login"
            f.close()
            context={
                'error':error,
                'type':tp
            }
            return render(request,'login/login.html',context)
        if request.POST.get("logout"):
            cmd ='curl -k --data "action=fw_logon&fw_logon_type=logout" https://10.0.1.1:4100/wgcgi.cgi'
            subprocess.call(cmd,shell=True)
            a.value = 0
            a.save()
            print a.value
            t= Thread(target=sunil_login)
            t.start()
            context={
                'type':"login"
            }
            return render(request,'login/login.html',context)
    
    if(a.value == 0):
        context = {
            'type':"login"
        }
        return render(request,'login/login.html',context)
    if(a.value == 1):
        context={
            'type':"logout"
        }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')
        

def sunil_login():
    time.sleep(30)
    a = check_login.objects.get(id=1)
    while 1:
        cmd = 'curl -i -k --data "fw_username=sunil.j&fw_password=iiits@123&fw_domain=LDAP&action=fw_logon&fw_logon_type=logon" https://10.0.1.1:4100/wgcgi.cgi > tmp.txt'
        subprocess.call(cmd,shell=True)
        f=open("tmp.txt","r")
        strings = ("Location: /./logon.shtml?errcode=505","Location: /./success.shtml")
        for line in f:
            if strings[0] in line:
                print "Already login"
            if strings[1] in line:
                print "success"
                a.value = 1
                a.save()
                print a.value
                return
        f.close()
        time.sleep(15)
        