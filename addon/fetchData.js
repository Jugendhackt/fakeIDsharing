    var token = chrome.storage.local.get(['token'], function(result) {
        console.log('Value currently is ' + result);
      
    var resultToken = result.token
    if (resultToken == null) {
        resultToken = "default"
    }

    console.log(result)
    fetch(`http://127.0.0.1:5000/${resultToken}/info`)
        .then(response => response.json())
        .then(data => fillIn(data));
})
function fillIn(jsonData) {
    document.getElementById("fakename").value = jsonData["name"];
    document.getElementById("birthday").value = jsonData["Geburtsdatum"];
    document.getElementById("gender").value = jsonData["Geschlecht"];
    document.getElementById("address").value = jsonData["Addresse"];
    document.getElementById("email").value = jsonData["Email"];
    document.getElementById("phone").value = jsonData["Telefon"];
    document.getElementById("lol").value = jsonData["Email_Webaddresse"];
}