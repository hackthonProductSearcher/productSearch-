const loginValidate = () => {
    let x, y;

    x = document.querySelector("#email").value;
    y = document.querySelector("#password").value;

    if (x == "" || y == "") {
        alert("error");
    } else {
        window.location.href="./seller-profile.html";
    }
}

const loginButton = document.querySelector("#login-button");
const signUpButton = document.querySelector(".sign-up-link");

loginButton.addEventListener("click", function() {
    loginValidate();
})
signUpButton.addEventListener("click", function() {
    window.location.href="./sign-up.html";
})