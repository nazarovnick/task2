// http://127.0.0.1:8000/api/countries


// requestURL = 'http://127.0.0.1:8000/api/countries'
document.getElementById('form').addEventListener("submit", checkForm)

function sendRequest(method, url, body = null) {
	const headers = {
		'Content-Type' : 'application/json'
	}


	if (method == 'POST' || method == 'PUT') {
		config = {
			method: method,
			body: body,
			headers: headers
		}} else {
			config = {
				method : method,
				headers : headers
			}
		}


	return fetch(url, config)
		.then(response => {

			if (response.ok) {
				return response.text()
			} else {
				error = `
			Такого API адреса нет. Попробуй следующие маршруты:<br><br>
			<p>http://127.0.0.1:8000/api/countries<br>
			http://127.0.0.1:8000/api/developers<br>
			http://127.0.0.1:8000/api/cars<br>
			http://127.0.0.1:8000/api/comments<br>
			<br>
			http://127.0.0.1:8000/api/countries/1<br>
			http://127.0.0.1:8000/api/developers/1<br>
			http://127.0.0.1:8000/api/cars/1<br>
			http://127.0.0.1:8000/api/comments/1<br>
			<br>
			</p>
			`;
				return error
			}


			})
	}


function checkForm(event) {
	event.preventDefault();
	requestURL = document.getElementById('exampleInputEmail1').value;

	sendRequest(method = 'GET', url = requestURL)
		
		.then(data => {

			outputInner = document.getElementById('outputInner');
			outputInner.innerHTML = data;
			outputWrapper = document.getElementById('outputWrapper');
			outputWrapper.style.cssText = `
			background: rgba(255, 255, 255, .8);
			border-radius: 10px;
			padding: 20px;
			-webkit-box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			-moz-box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			`;

			outputHeader = document.getElementById('outputHeader');
			outputHeader.innerHTML = 'Ответ API';
			outputHeader.style.cssText = `
			display: block;
			font-size: 1.5em;
			font-weight: bold;
			height: 1.5em;
			margin-bottom: 10px;
			`;


			})
		.catch(error => {

			outputInner = document.getElementById('outputInner');
			outputInner.innerHTML = `
			Такого API адреса нет.

			Попробуй следующие марqdaddsшруты:

			`;

			outputWrapper = document.getElementById('outputWrapper');
			outputWrapper.style.cssText = `
			background: rgba(255, 255, 255, .8);
			border-radius: 10px;
			padding: 20px;
			-webkit-box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			-moz-box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			box-shadow: 6px 8px 19px 0px rgba(34, 60, 80, 0.43);
			`;

			outputHeader = document.getElementById('outputHeader');
			outputHeader.innerHTML = "Ошибка";
			outputHeader.style.cssText = `
			display: block;
			font-size: 1.5em;
			font-weight: bold;
			height: 1.5em;
			margin-bottom: 10px;
			`;


			});

}