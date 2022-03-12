import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
content=""
def extractnews(url):
    print("extracting news ....")
    cnt=''
    cnt+=('<b> Top Headings </b>\n'+'<br>'+"-"*50+'<br>')
    response=requests.get(url)
    content= response.content
    soup=BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt+= ((str(i+1)+'::'+tag.text+"\n"+'<br>') if tag.text!='More' else '')
    return cnt
cnt=extractnews('https://news.ycombinator.com/')
content+=cnt
content+=("<br>--------</br>")
content+= ('<br><br>End of Message')
print("composing Email ....")
Server="smtp.gmail.com"
Port="587"
From="kumar.priyanshu2k02@gmail.com"
To=input('enter the receiver\'s mail address: \n')
Pass="Lonewolfpk@2305"
msg=MIMEMultipart()
msg['Subject']=f"Top Hackernews Headlines {now.day}-{now.month}-{now.year}"
msg['To']=To
msg['From']=From
msg.attach(MIMEText(content,'html'))
print("initialising server")
server=smtplib.SMTP(Server, Port)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(From,Pass)
server.sendmail(From,To,msg.as_string())
server.quit()
print("email sent")

