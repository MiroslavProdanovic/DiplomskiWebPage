import Adafruit_DHT
import MySQLdb
import sys
import datetime
import time
import smtplib

sender = "diplomski.test123@gmail.com"
receiver = "prodanovicmiroslav64@gmail.com"
password = raw_input("Enter your email account password: ")
lowest_temperature = float(raw_input("Enter the value of lowest temperature. If the temperature is less than that value, the email will be sent to you. Enter value: "))
print("Value of lowest_temperature: ", lowest_temperature)
print("Type of lowest_temperature: ", type(lowest_temperature))
print(password)

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
	
	if temperature < lowest_temperature:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, password)
		message = "Temperature is {:.1f}!".format(temperature) 
		server.sendmail(sender, receiver, message)
		print ("Email sent!")

	sql = "INSERT INTO SensorReadings (DateTime, Temperature, Humidity) VALUES (%s, %s, %s)"
	values = (readingTime, temperature, humidity)

	cursor.execute(sql, values)
	db.commit()
	cursor.execute("SELECT * FROM SensorReadings ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchall()
	print "Inserted values... ID = {:}".format(result[0][0]), " | Date = {:}".format(result[0][1]), " | Temperature = {:.1f}".format(result[0][2]), " | Humidity = {:.1f}".format(result[0][3])
	time.sleep(5)

