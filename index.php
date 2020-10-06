<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="shortcut icon" href="/favicon-icon.ico">
		<title>Diplomski rad</title>
		<meta name="author" content="Miroslav Prodanovic">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="/main.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	</head>

	<body>
		<div class="container-fluid">
			<div class="row">
				<div class="col-xs-12">
					<h1 class="page-title">Koncept sistema za pracenje parametara okruzenja u komornim susarama</h1>
				</div>
			</div>
			
			<div class="row">
				<div class="col-xs-12 col-md-6 graphWrapper">
					<canvas id="temperatureGraph"></canvas>
				</div>
			
				<div class="col-xs-12 col-md-6 graphWrapper">
					<canvas id="humidityGraph"></canvas>
				</div>	
			</div>
			
			<div class="row">
				<div class="col-xs-12 col-sm-6 map-wrapper">
					<p>Lokacija postrojenja: <span>Miše Dimitrijevića 22, Novi Sad</span></p>
					<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2809.1292991873215!2d19.82958461555014!3d45.24517807909895!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x475b103dd622518d%3A0xbf6151236f95e9c7!2sMi%C5%A1e%20Dimitrijevi%C4%87a%2022%2C%20Novi%20Sad%20403761!5e0!3m2!1sen!2srs!4v1601990952260!5m2!1sen!2srs" width="100%" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
				</div>
			</div>
		</div>

		<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
		<script type="text/javascript" src="app.js"></script>
	</body>
</html>