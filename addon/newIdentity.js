var token = chrome.storage.local.get(['token'], function(result) {
    console.log('Value currently is ' + result);
  
var resultToken = result.token

document.addEventListener("DOMContentLoaded", initializeListener);

function initializeListener() {
    console.log("fetchData initialize")
    var button = document.getElementById("newID");
    button.addEventListener("click", newIdentity);
}

function newIdentity() {
    fetch(`http://127.0.0.1:5000/${resultToken}/new`)
        .then(response => response.json())
        .then(data => console.log(data));
}