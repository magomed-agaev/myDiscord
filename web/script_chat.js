// eel.expose(get_Message)
// function get_Message() {
//     var message = document.getElementById("message_input").value;

//     return message;
// }
    
function send() {
    var message = document.getElementById("message_input").value;
    console.log(message);
    eel.conversation(message,1);
}

function send_audio() {
    eel.set_audio()
}

function get_audio() {
    eel.get_audio()
}

function Close() {
    eel.Close()
}

window.onload = function () {
    (function refreshChat() {
        eel.Affichage()(function(result) {
            var chat = document.getElementById('chat_messages');
            var tab = result;

            chat.innerHTML = ''; // Réinitialise tout le contenu de la <div> chat_message

            tab.forEach(function (message) {
                // message[2] --> type_msg type = 1 ->txt type = 2 ->audio
                if (message[2] === 1) {
                    var div = '<div class="bulle_chat">' +
                        '<span class="auteur">' + message[0] + '</span>' +
                        '<p class="message">' + message[1] + '</p>' +
                        '<span class="time">' + message[3] + '</span>' +
                        '</div>';
                    chat.insertAdjacentHTML("beforeend", div);
                } else {
                    var div = '<div class="bulle_chat">' +
                    '<span class="auteur">' + message[0] + '</span>' +
                    '<p class="message" onclick="get_audio()">' + Message_audio + '</p>' +
                    '<span class="time">' + message[3] + '</span>' +
                    '</div>';
                    chat.insertAdjacentHTML("beforeend", div);
                    }
            });
            setTimeout(refreshChat, 1000);
        });
    })();// IIEF -->immediately Invoked Function Expression, encapsule tout le code et l'execute direct.
};




       

    
