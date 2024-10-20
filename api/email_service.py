import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(papers, recipient_email):
    sender_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Recommended Research Papers"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    html = "<html><body><h2>Recommended Papers</h2>"
    for paper in papers:
        html += f"<h3>{paper['title']}</h3>"
        html += f"<p>{paper['abstract']}</p>"
        html += f"<a href='{paper['link']}'>Read more</a><br><br>"
    html += "</body></html>"
    
    part = MIMEText(html, 'html')
    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.example.com', 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
