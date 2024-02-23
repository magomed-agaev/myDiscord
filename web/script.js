// appel des boutons depuis fichier html
let signupBtn = document.getElementById("signupBtn").click();
let signuinBtn = document.getElementById("signinBtn");
let firstnameField = document.getElementById("firstnameField");
let lastnameField = document.getElementById("lastnameField");
let title = document.getElementById("title");

// fonction onclick de sign in pour cacher les inputs firstname et lastname
signinBtn.onclick = function () {
    firstnameField.style.maxHeight = "0%";
    lastnameField.style.maxHeight = "0%";
    title.innerHTML = "Sign In";
    signupBtn.classList.add("disable");
    signuinBtn.classList.remove("disable");

}

// fonction pour afficher les inputs firstname et lastname
signupBtn.onclick = function () {
    firstnameField.style.maxHeight = "100%";
    lastnameField.style.maxHeight = "100%";
    title.innerHTML = "Sign Up";
    signupBtn.classList.remove("disable");
    signuinBtn.classList.add("disable");
}

document.getElementById("signupBtn").addEventListener("click", async () => {
    const FIRSTNAME = document.getElementById("firstnameField").value;
    const LASTNAME = document.getElementById("lastnameField").value;
    const EMAIL = document.getElementById("emailField").value;
    const PASSWORD = document.getElementById("passwordField").value;

    const result = await eel.signup(FIRSTNAME, LASTNAME, EMAIL, PASSWORD)();
    console.log(result);
});
