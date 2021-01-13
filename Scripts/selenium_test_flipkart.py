from selenium import webdriver
from datetime import datetime
import time
from scrapDataBase import insert_into_table, delete_row, get_data, update_row
from datetime import timedelta
from send_email import send_email

def webScrapFlipkart(link, desired_price, email):
	global status
	data = {}
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	try:
		driver.get(link)
		main_div = driver.find_element_by_class_name("dyC4hf")
		in_div = main_div.find_element_by_class_name("CEmiEU")
		in_div = in_div.find_element_by_class_name("_25b18c")

		productName = driver.find_element_by_class_name("B_NuCI")
		productName = productName.text

		price = in_div.text.split("₹")[1]
		price = float("".join(price.split(",")))
		price = round(price)
	except:
		print("No data")
	finally:
		driver.quit()

	if(price <= desired_price):
		status = True

	data["price"] = price
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
	data = get_data("flipkart")

	if(len(data.items()) > 0):
		link = data['link']
		desired_price = data['desired_price']
		email = data['email']

		scrapTime = data['scrapTime']
		print(scrapTime)
		(dt, mSecs) = scrapTime.strip().split(".") 
		dt = datetime(*time.strptime(dt, "%Y-%m-%d %H:%M:%S")[0:6])
		mSeconds = timedelta(microseconds = int(mSecs))
		scrapTime = dt + mSeconds

		status = bool(data['status'])

	elif(len(data.items()) == 0):
		link = ""
		status = True
		print("No Data")

elif ch==2:
	link = input("Enter Product Link:- ")
	desired_price = int(input("Enter Desired Price(Integer Value):- "))
	email = input("Enter Email:- ")
	status = False
	
	insert_into_table(link, desired_price, email, datetime.now(), status, "flipkart")
else:
	print("Wrong Choice")

flag_choice = 0
while(not status):
	if(flag_choice==0):
		if(ch==1):
			hr = ((datetime.now() - scrapTime).seconds)//3600
			if(hr < 12):
				# time.sleep(4*60*60)
				print("sleep for 2 seconds")
				time.sleep(2)
			else:
				pass
		else:
			pass
		flag_choice = 1

	data = 	webScrapFlipkart(link, desired_price, email)

	"""
	Update scrapTime into table Remaining
	"""
	update_row(datetime.now(), "flipkart")

	if(data['status'] == True):
		delete_row("flipkart")
		send_email(email, data["productName"], data["price"], data["link"])
		break
	# time.sleep(12*60*60)
	time.sleep(2)
print("Product Price is in your Desired Price")