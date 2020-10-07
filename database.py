import Adafruit_DHT
import MySQLdb
import datetime
import time

used_sensor = Adafruit_DHT.DHT22
pin = 4
id = 0

db = MySQLdb.connect("eu-cdbr-west-03.cleardb.net","ba289d584b4966","07ab700b","heroku_be22a11ae14ff50")
cursor = db.cursor()

while True:
	readingTime = datetime.datetime.now()
	humidity, temperature = Adafruit_DHT.read(used_sensor, pin)

	if temperature is None or humidity is None:
		time.sleep(1)
		print "Reading is not possible at this moment!"
		continue
	
	cursor.execute("SELECT * FROM SensorReadings ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchall()
	id = result
	id++

	sql = "INSERT INTO SensorReadings (ID, DateTime, Temperature, Humidity) VALUES (%s, %s, %s, %s)"
	values = (id, readingTime, temperature, humidity)

	cursor.execute(sql, values)
	db.commit()
	cursor.execute("SELECT * FROM SensorReadings ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchall()
	print "Inserted values... ID = {:}".format(result[0][0]), "Date = {:}".format(result[0][1]), " | Temperature = {:.1f}".format(result[0][2]), " | Humidity = {:.1f}".format(result[0][3])
	time.sleep(5)

