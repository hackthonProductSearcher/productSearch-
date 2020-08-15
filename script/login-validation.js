const loginValidate = () => {
    let x;

    x = document.querySelector(".input-field").value;

    if (x == "") {
        alert("error");
    }
}

const loginButton = document.querySelector("#login-button");

loginButton.addEventListener("click", function() {
    loginValidate();
})