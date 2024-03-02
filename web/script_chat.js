
function send() {
    var message = document.getElementById("message_input").value;
    eel.conversation(message);
}

function Close() {
    eel.Close()
}
// setTimeout(function() {
//     location.reload();
// }, 5000);

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

(function refreshChat() {
    eel.Affichage()((result) => {
        var chat = document.getElementById('chat_messages');
        var tab = result;

        chat.innerHTML = '';

        tab.forEach(function (message) {
            chat.insertAdjacentHTML("beforeend", '<p>' + message + '</p>');
        });
        // window.scrollBy(0, window.innerHeight);      
        // Réappeler la fonction refreshChat après un certain délai
        setTimeout(refreshChat, 1000); // Actualise toutes les 1000 millisecondes (toutes les secondes)
    });
})();


}

   
       

    
