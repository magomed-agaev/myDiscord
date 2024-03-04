

function login() {
    var email = document.getElementById("email_adress").value;
    var password_hash = document.getElementById("password").value;
    eel.Signin(email, password_hash)

}
function signup() {

    var nom = document.getElementById("signupLastname").value;
    var prenom = document.getElementById("signupFirstname").value;
    var email = document.getElementById("email_adress").value;
    var password_hash = document.getElementById("password").value;
    eel.Signup(nom, prenom, email, password_hash)

}

eel.expose(redirect_chat);
function redirect_chat() {
    window.location.href = "index_chat.html";
}


