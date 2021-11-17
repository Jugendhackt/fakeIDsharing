let loginState;

chrome.storage.local.get(["login_state"], function (result) {
    loginState = result.login_state;
    console.log(loginState)

    if (loginState === true) {
        fillIn();
    }
});

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
        console.log(value.email);
    });
    chrome.storage.local.get(["phone"], function (value) {
        document.getElementById("phone").value = value.phone;
    });
}
