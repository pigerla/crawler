__author__ = 'spy'
#encoding:utf-8
import smtplib
from email.mime.text import MIMEText
mail_host="smtp.126.com"  #设置服务器
mail_user="name of email"    #用户名
mail_pass="password of email"   #口令
mail_postfix="126.com"  #发件箱的后缀

def send_mail(sub,content):
    to_list=['1xxx@xxx.com', '2xxx@xxx.com', '3xxx@xxx.com', '4xxx@xxx.com']

    me= "Alert Message! " + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail("hello","hello world！"):
        print "发送成功"
    else:
        print "发送失败"