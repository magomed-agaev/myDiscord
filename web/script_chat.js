// let sendBtn = document.getElementById("send-button");

function send() {  
    var message = document.getElementById("message_input").value;
    eel.set_message(message);
}

eel.expose(set_Message)
function set_Message() {
    var message = document.getElementById("email").value;
    return message

}

