<?php
header('Content-Type: application/json');

define('DB_HOST', 'eu-cdbr-west-03.cleardb.net');
define('DB_USERNAME', 'ba289d584b4966');
define('DB_PASSWORD', '07ab700b');
define('DB_NAME', 'heroku_be22a11ae14ff50');

$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

if(!$mysqli){
  die("Connection failed: " . $mysqli->error);
}

$query = sprintf("SELECT * FROM SensorReadings ORDER BY DateTime DESC LIMIT 20");

$result = $mysqli->query($query);

$data = array();
foreach ($result as $row) {
  $data[] = $row;
}

$result->close();

$mysqli->close();

$reversed_data = array_reverse($data);

print json_encode($reversed_data);