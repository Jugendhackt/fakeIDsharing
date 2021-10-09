fetch('http://127.0.0.1:5000/info', {mode: 'no-cors'})
    .then(response => response.json())
    .then(data => console.log(data));