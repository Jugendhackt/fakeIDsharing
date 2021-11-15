function login(event) {
    event.preventDefault();
    fetch("http://127.0.0.1:5000/login", {
        method: "POST", // or 'PUT'
        headers: {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        },
        body: new URLSearchParams({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
            console.log(data);
            //window.location.replace("../start.html");
            chrome.storage.local.set({ token: data.token });
            chrome.storage.local.get(["token"], function (result) {
                console.log("Value currently is " + result.token);
            });
            if (data["token"] == "") {
                console.log("Login Failed");
            } else {
                window.location.replace("../start.html");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}

document.getElementById("loginForm").addEventListener("submit", login);
