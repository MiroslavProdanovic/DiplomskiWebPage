import Adafruit_DHT
import MySQLdb
import sys
import datetime
import time
import smtplib
import getpass

sender = "pracenje.parametara.susare@gmail.com"
receiver = "prodanovicmiroslav64@gmail.com"
password = getpass.getpass("Enter system email account password: ")

try:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)
except:
	print ("Incorrect password!")
	sys.exit()

email_counter = 0
minimum_temperature = float(raw_input("Enter the value of minimum temperature. If the temperature is less than that value, the email will be sent to you. Enter value: "))
maximum_temperature = float(raw_input("Enter the value of maximum temperature. If the temperature is higher than that value, the email will be sent to you. Enter value: "))

used_sensor = Adafruit_DHT.DHT22
pin = 4

db = MySQLdb.connect("eu-cdbr-west-03.cleardb.net","ba289d584b4966","07ab700b","heroku_be22a11ae14ff50")
cursor = db.cursor()

while True:
	readingTime = datetime.datetime.now()
	humidity, temperature = Adafruit_DHT.read(used_sensor, pin)

	if temperature is None or humidity is None:
		time.sleep(1)
		print "Reading is not possible at this moment!"
		continue
	
	if temperature < minimum_temperature or temperature > maximum_temperature:
		if email_counter < 5:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(sender, password)
			message = "Temperature is: {:.1f}!".format(temperature)
			server.sendmail(sender, receiver, message)
			print ("Email sent!")
			email_counter += 1

	sql = "INSERT INTO SensorReadings (DateTime, Temperature, Humidity) VALUES (%s, %s, %s)"
	values = (readingTime, temperature, humidity)

	cursor.execute(sql, values)
	db.commit()
	cursor.execute("SELECT * FROM SensorReadings ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchall()
	print "Inserted values... ID = {:}".format(result[0][0]), " | Date = {:}".format(result[0][1]), " | Temperature = {:.1f}".format(result[0][2]), " | Humidity = {:.1f}".format(result[0][3])
	time.sleep(5)

