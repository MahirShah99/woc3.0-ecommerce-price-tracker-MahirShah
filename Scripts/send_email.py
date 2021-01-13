# import smtplib

# def send_email(receive_email, productName, product_price, url):
# 	msg = f"""Product Name:- {productName}, Current Price:- {product_price}, URL:- {url}"""
# 	print(msg)
# 	try:
# 		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# 		server.login("mahir8239@gmail.com", "mahirshahshahmahir")
# 		server.sendmail("mahir8239@gmail.com", receive_email, msg)
# 		print("Mail Sent")
# 	except:
# 		print("Cannot send Mail")
# 	finally:
# 		server.quit()



import smtplib, ssl

def send_email(receive_email, productName, product_price, url):
	port = 587  # For starttls
	smtp_server = "smtp.gmail.com"
	sender_email = "mahir8239@gmail.com"
	receiver_email = receive_email
	password = "mahirshahshahmahir"
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