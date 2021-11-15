console.log("test");
// window.onload = initializeListener
document.addEventListener("DOMContentLoaded", initializeListener);
//chrome.browserAction.onClicked.addListener(initializeListener)
function copy(event) {
    console.log(event);
    /* Get the text field */
    var copyText = event.target.previousElementSibling;
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
}

function initializeListener() {
    console.log(document.getElementsByClassName("copyText"));
    var buttons = document.getElementsByClassName("copyText");

    for (var button of buttons) {
        button.addEventListener("click", copy);
    }
}
