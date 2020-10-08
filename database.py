import Adafruit_DHT
import MySQLdb
import datetime
import time
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('mailsending'))
from_email = Email("app186703148@heroku.com")
subject = "Hello World!"
to_email = Email("prodanovicmiroslav64@gmail.com")
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

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

	sql = "INSERT INTO SensorReadings (DateTime, Temperature, Humidity) VALUES (%s, %s, %s)"
	values = (readingTime, temperature, humidity)

	cursor.execute(sql, values)
	db.commit()
	cursor.execute("SELECT * FROM SensorReadings ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchall()
	print "Inserted values... ID = {:}".format(result[0][0]), " | Date = {:}".format(result[0][1]), " | Temperature = {:.1f}".format(result[0][2]), " | Humidity = {:.1f}".format(result[0][3])
	time.sleep(5)

