
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
        
        var height_page = window.innerHeight
        console.log(height_page)
        window.scrollTo(0,height_page);
               
        setTimeout(refreshChat, 1000); // Actualise toutes les 1000 millisecondes (toutes les secondes)
    });
})();


}

   
       

    
