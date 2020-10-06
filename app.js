$(document).ready(function(){
	dataHandler();
	setInterval(dataHandler, 5000);
});

function dataHandler(){
	$.ajax({
		url: "https://pracenje-parametara-susare.herokuapp.com/data.php",
		method: "GET",
		success: function(data) {
			console.log(data);
			var dateTime = [];
			var temperature = [];
			var humidity = [];

			for(var i in data) {
				dateTime.push(data[i].DateTime);
				temperature.push(data[i].Temperature);
				humidity.push(data[i].Humidity);
			}

			var temperatureChart = $("#temperatureGraph");
			var lineChart1 = new Chart(temperatureChart, {
				type: 'line',
				data: {
					labels: dateTime,
					datasets : [
						{
							label: 'Temperatura vazduha',
							fill: false,
							backgroundColor: 'white',
							borderColor: 'red',
							pointBackgroundColor: 'red',
							pointRadius: '5',
							pointHoverBackgroundColor: '#eeeeee',
							pointHoverBorderColor: '#bbbbbb',
							pointHoverRadius: '5',
							data: temperature
						}
					]
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					title: {
						display: true,
						fontSize: 16,
						fontColor: 'black',
						text: 'Merenje temperature vazduha u susari'
					},
					animation: {
						duration: 0
					},
					scales: {
						yAxes: [{
							ticks: {
								suggestedMin: 20,
								suggestedMax: 50
							}
						}]
					}
				}
			});

			var humidityChart = $("#humidityGraph");
			var lineChart2 = new Chart(humidityChart, {
				type: 'line',
				data: {
					labels: dateTime,
					datasets : [
						{
							label: 'Vlaznost vazduha',
							fill: false,
							backgroundColor: 'white',
							borderColor: 'blue',
							pointBackgroundColor: 'blue',
							pointRadius: '5',
							pointHoverBackgroundColor: '#eeeeee',
							pointHoverBorderColor: '#bbbbbb',
							pointHoverRadius: '5',
							data: humidity
						}
					]
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					title: {
						display: true,
						fontSize: 16,
						fontColor: 'black',
						text: 'Merenje vlaznosti vazduha u susari'
					},
					animation: {
						duration: 0
					},
					scales: {
						yAxes: [{
							ticks: {
								suggestedMin: 20,
								suggestedMax: 80
							}
						}]
					}
				}
			});

		},

		error: function(data) {
			console.log(data);
		}
	});
}
