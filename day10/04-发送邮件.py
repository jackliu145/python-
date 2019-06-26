from email.mime.text import MIMEText
from smtplib import SMTP_SSL

msg = MIMEText('hello world!', 'plain', 'utf-8')

from_addr = '188075841@qq.com'
password = input('授权码:')
to_addr = '798415944@qq.com'
# to_addr = 'jack.liu145@gmail.com'

smtp_server = 'smtp.qq.com'
# smtp_server = 'smtp.gmail.com'

import smtplib
# server = smtplib.SMTP_SSL(smtp_server, 587)
server = SMTP_SSL(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg)
server.quit()