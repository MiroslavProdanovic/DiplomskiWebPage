import Adafruit_DHT
import MySQLdb
import datetime
import time

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
	cursor.execute("SELECT * FROM SensorReadings ORDER BY DateTime DESC LIMIT 1")
	result = cursor.fetchall()
	print "Inserted values... Date & Time = {:}".format(result[0][0]), " | Temperature = {:.1f}".format(result[0][1]), " | Humidity = {:.1f}".format(result[0][2])
	time.sleep(5)
