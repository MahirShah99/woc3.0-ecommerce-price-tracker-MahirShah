from selenium import webdriver
from datetime import datetime
import time
from scrapDataBase import insert_into_table, delete_row, get_data, update_row
from datetime import timedelta
from send_email import send_email

def webScrapAmazon(link, desired_price, email):
	deal_price_exist = False
	data = {}
	global status
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	try:
		driver.get(link)
		productName = driver.find_element_by_id("productTitle")
		productName = productName.text
		price = driver.find_element_by_id("priceblock_ourprice")
		price = price.text.split()[1]
		price = float("".join(price.split(",")))
		price = round(price)
		print("Price:- ", price)

		try:
			deal_price = driver.find_element_by_id("priceblock_dealprice")
			deal_price = deal_price.text.split()[1].split(".")[0]
			deal_price = int("".join(deal_price.split(",")))
			print("Deal Price:- ", deal_price)
		except:
			pass
	except:
		print("No selector")
		return 
	finally:
		driver.quit()

	try:
		if(deal_price):
			deal_price_exist = True
	except:
		pass
	
	if(deal_price_exist):		
		if(deal_price <= desired_price):
			data["price"] = deal_price
			status = True
	else:
		if(price <= desired_price):
			data["price"] = price
			status = True

	data["link"] = link
	data["status"] = status
	data["scrapTime"] = datetime.now()
	data["email"] = email
	data["desired_price"] = desired_price
	data["productName"] = productName
	return data


print("="*50)
print("Enter 1 to search for last link entered")
print("Enter 2 to search for new product")
ch = int(input("Enter your choice:- "))

if ch==1:
	"""
	get the url for whose status is false and search for it again
	"""
	data = get_data("amazon")
	print(data)

	if(len(data.items()) > 0):
		
		link = data['link']
		
		desired_price = int(data['desired_price'])
		
		email = data['email']

		scrapTime = data['scrapTime']
		print(scrapTime)
		(dt, mSecs) = scrapTime.strip().split(".") 
		dt = datetime(*time.strptime(dt, "%Y-%m-%d %H:%M:%S")[0:6])
		mSeconds = timedelta(microseconds = int(mSecs))
		scrapTime = dt + mSeconds
		print(scrapTime)

		status = bool(data['status'])
		print(status)

	elif(len(data.items()) == 0):
		link = ""
		status = True
		print("No Data")


elif ch==2:
	""" 
	get data from user if no data from table having status false
	"""
	link = input("Enter Product Link:- ")
	desired_price = int(input("Enter Desired Price(Integer Value):- "))
	email = input("Enter Email:- ")
	status = False

	"""  insert data into table """
	insert_into_table(link, desired_price, email, datetime.now(), status, "amazon")

else:
	print("Wrong Choice")

flag_choice = 0
while(not status):

	if(flag_choice==0):
		if(ch==1):
			hr = ((datetime.now() - scrapTime).seconds)//3600
			if(hr < 12):
				# time.sleep(4*60*60)
				print("Sleep for 2 seconds")
				time.sleep(2)
			else:
				pass
		else:
			pass
		flag_choice=1

	data = webScrapAmazon(link, desired_price, email)
	"""
	Update scrapTime into table Remaining
	"""
	update_row(datetime.now(), "amazon")

	if(data['status'] == True):
		delete_row("amazon")
		send_email(email, data["productName"], data["price"], data["link"])
		print(data['desired_price'])
		break

	# time.sleep(12*60*60)
	time.sleep(2)
print("Desired")
