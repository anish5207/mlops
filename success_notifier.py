import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "skabhi005@gmail.com"
host_pass = "8002730184"
guest_address = "skabhi001@gmail.com"
subject = "Regarding Success of your model "
content = '''Hello, 
		   Developer,Your last commit trained model has given the best accuracy .
				Congratulations on your success.
			THANK YOU ...'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')



