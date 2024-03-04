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


function appendMessage(sender, content) {
    var chatMessages = document.getElementById("chat-messages");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");

    var senderElement = document.createElement("div");
    senderElement.classList.add("message-sender");
    senderElement.textContent = sender;

    var contentElement = document.createElement("div");
    contentElement.classList.add("message-content");
    contentElement.textContent = content;

    messageElement.appendChild(senderElement);
    messageElement.appendChild(contentElement);

    chatMessages.appendChild(messageElement);

    // // Scroll to the bottom of the chat messages
    // chatMessages.scrollTop = chatMessages.scrollHeight;
}




