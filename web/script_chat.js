
function send() {
    var message = document.getElementById("message_input").value;
    eel.conversation(message);
}

function Close() {
    eel.Close()
}

window.onload = function () {
// eel.expose(get_Message)
// function get_Message() {
//     var message = document.getElementById("email").value;
//     return message;
// }
    
// eel.Affichage()((result) =>{
    
//     var chat = document.getElementById('chat_messages');
//     var tab = result;

//     tab.forEach(function (message) {
//         chat.insertAdjacentHTML("beforeend", '<p>' + message + '</p>');
        
//         })
    //     });


// (function refreshChat() {
//     eel.Affichage()((result) => {
//         var chat = document.getElementById('chat_messages');
//         var tab = result;

//         chat.innerHTML = '';

//         tab.forEach(function (message) {
//             chat.insertAdjacentHTML("beforeend", '<p>' + message + '</p>');
//         });
//         setTimeout(refreshChat, 1000); // Actualise toutes les 1000 millisecondes (toutes les secondes)
//     });
// })();
                       

(function refreshChat(){
    eel.Affichage()(function(result) { //fonction callback function(result)
        var chat = document.getElementById('chat_messages');
        var tab = result;


        chat.innerHTML = ''; //réinitialise tout le contenue de la <div> chat_message

        tab.forEach(function (message) {
            chat.insertAdjacentHTML("beforeend", '<p>' + message + '</p>');
        });
                       
    });
      
})();// IIEF -->mmediately Invoked Function Expression, encapsule tout le code et l'execute direct.

}


       

    
