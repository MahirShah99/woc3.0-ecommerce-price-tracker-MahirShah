import smtplib, ssl

def send_email(receive_email, productName, product_price, url):
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = ""   #sender's emailID 
	receiver_email = receive_email
	password = ""       #sender's emailID password
	message = f""" 
	Subject:- Price Tracker

	Product Name:- {productName}
	Product Price:- {product_price}
	URL:- {url}"""

	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)