var idList = [];
let idNumbers = [];
let array = [];
var resultToken;
var identitys;
var selectedId;
var selectID = document.getElementById("selectID");
var compareDict = {};

//Create and append select list
var selectList = document.createElement("select");
selectList.setAttribute("id", "mySelect");
selectID.appendChild(selectList);

const dropdown = document.getElementById("mySelect");

document.getElementById("mySelect").addEventListener("change", function () {
    //console.log('You selected: ', this.value);
    selectedId = this.value;
    fetch(`http://127.0.0.1:5000/${resultToken}/${selectedId}/profile`)
        .then((response) => response.json())
        .then((data) => {
            var dataParsed = JSON.parse(JSON.stringify(data));
            saveData(dataParsed);
            fillIn();
        });
});

chrome.storage.local.get(["token"], function (result) {
    resultToken = result.token;
    //console.log('Value currently is ' + resultToken);
});

fetch(`http://127.0.0.1:5000/${resultToken}/all`)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        console.log(idList);
        for (const a of data) {
            idList.push(a);
        }
        //idList = idList.concat(data)
        //console.log(idList)

        for (const id of idList) {
            fetch(`http://127.0.0.1:5000/${resultToken}/${id}/profile`)
                .then((response) => response.json())
                .then((data) => {
                    //console.log(data["id"])

                    var option = document.createElement("option");
                    option.setAttribute("value", data["id"]);
                    option.text = data["name"];
                    selectList.appendChild(option);
                });
        }
    });

//var option = document.createElement("option");
//option.setAttribute("value", array[i]);
//option.text = array[i];
//selectList.appendChild(option);
