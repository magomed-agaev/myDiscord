// eel.expose(get_Message)
// function get_Message() {
//     var message = document.getElementById("message_input").value;

//     return message;
// }
    
// function send() {
//     var message = document.getElementById("message_input").value;
//     var m = eel.get_iduser()
//     console.log(m)
//     eel.conversation(m,message);
// }
function send() {
    var message = document.getElementById("message_input").value;
    console.log(message);
    eel.conversation(message);
}

function Close() {
    eel.Close()
}

window.onload = function () {
    // eel.Affichage()((result) =>{
        
    //     var chat = document.getElementById('chat_messages');
    //     var tab = result;
    
    //     tab.forEach(function (message) {
    //         chat.insertAdjacentHTML("beforeend", '<p>' + message + '</p>');
            
    //         })
    //     });
             
    (function refreshChat() {
        eel.Affichage()(function(result){ //fonction callback function(result)
            var chat = document.getElementById('chat_messages');
            var tab = result;
        
            chat.innerHTML = ''; //réinitialise tout le contenue de la <div> chat_message
            // var div = document.createElement("div");
            tab.forEach(function (message) {
                var div = '<div class = bulle_chat>'+

                        '<span class="auteur">' + message[0] + '</span>' + 
                            
                        '<p class="message">' + message[1] + '</p>' +
                        
                        '<span class="time">' + message[3] + '</span>' + 
                        '</div >';          
                
            chat.insertAdjacentHTML("beforeend", div);
            });
        }); setTimeout(refreshChat, 1000);  
    // eel.Affichage()(function(result){ //fonction callback function(result)
    //     var chat = document.getElementById('chat_messages');
    //     var tab = result;

    //     chat.innerHTML = ''; //réinitialise tout le contenue de la <div> chat_message

    //     tab.forEach(function (message) {
    //         chat.insertAdjacentHTML("beforeend",
                
    //             '<p class = message>' + message[1] + '</p>' +
    //             '<span class = auteur>' + message[0] + '</span>' + "" +
    //             '<span class = time>' + message[3] + '</span>' );           
        
    //     });
    // }); setTimeout(refreshChat, 1000);  
     
})();// IIEF -->mmediately Invoked Function Expression, encapsule tout le code et l'execute direct.
}



       

    
