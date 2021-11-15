var resultToken = "";

chrome.storage.local.get(["token"], function (result) {
    resultToken = result.token;
    console.log("Value currently is " + resultToken);

    fetch(`http://127.0.0.1:5000/${resultToken}/info`)
        .then((response) => response.json())
        .then((data) => {
            var dataParsed = JSON.parse(JSON.stringify(data));
            saveData(dataParsed);
            fillIn();
        });
});

function saveData(jsonData) {
    chrome.storage.local.set({ fakename: jsonData["name"] });
    chrome.storage.local.set({ birthdate: jsonData["Geburtsdatum"] });
    chrome.storage.local.set({ gender: jsonData["Geschlecht"] });
    chrome.storage.local.set({ address: jsonData["Addresse"] });
    chrome.storage.local.set({ email: jsonData["Email"] });
    chrome.storage.local.set({ phone: jsonData["Telefon"] });
    chrome.storage.local.set({ email_link: jsonData["Email_Webaddresse"] });
}

function fillIn() {
    chrome.storage.local.get(["fakename"], function (value) {
        document.getElementById("fakename").value = value.fakename;
    });
    chrome.storage.local.get(["birthdate"], function (value) {
        document.getElementById("birthday").value = value.birthdate;
    });
    chrome.storage.local.get(["gender"], function (value) {
        document.getElementById("gender").value = value.gender;
    });
    chrome.storage.local.get(["address"], function (value) {
        document.getElementById("address").value = value.address;
    });
    chrome.storage.local.get(["email"], function (value) {
        document.getElementById("email").value = value.email;
    });
    chrome.storage.local.get(["phone"], function (value) {
        document.getElementById("phone").value = value.phone;
    });
    chrome.storage.local.get(["email_link"], function (value) {
        document.getElementById("email_link").value = value.email_link;
    });
}
