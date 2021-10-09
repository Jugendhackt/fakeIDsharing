fetch('http://127.0.0.1:5000/fhwhjjh/info')
    .then(response => response.json())
    .then(data => fillIn(data));

function fillIn(jsonData) {
    document.getElementById("fakename").value = jsonData["name"];
    document.getElementById("birthday").value = jsonData["Geburtsdatum"];
    document.getElementById("gender").value = jsonData["Geschlecht"];
    document.getElementById("address").value = jsonData["Addresse"];
    document.getElementById("email").value = jsonData["Email"];
    document.getElementById("phone").value = jsonData["Telefon"];
}