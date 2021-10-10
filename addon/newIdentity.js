var token = chrome.storage.local.get(['token'], function(result) {
    console.log('Value currently is ' + result);
  
var resultToken = result.token
if (resultToken == null) {
    resultToken = "default"
}

function newIdentity() {
    fetch(`http://127.0.0.1:5000/${resultToken}/new`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            chrome.storage.local.set({id: data.id});
            fillIn(data);
        });
}

document.addEventListener("DOMContentLoaded", initializeListener);

function initializeListener() {
    console.log("fetchData initialize")
    var button = document.getElementById("newID");
    button.addEventListener("click", newIdentity);
}

function fillIn(jsonData) {
    document.getElementById("fakename").value = jsonData["name"];
    document.getElementById("birthday").value = jsonData["Geburtsdatum"];
    document.getElementById("gender").value = jsonData["Geschlecht"];
    document.getElementById("address").value = jsonData["Addresse"];
    document.getElementById("email").value = jsonData["Email"];
    document.getElementById("phone").value = jsonData["Telefon"];
    document.getElementById("lol").value = jsonData["Email_Webaddresse"];
}

})
