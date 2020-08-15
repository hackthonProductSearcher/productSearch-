const signUpValidate = () => {
    let x, y;

    x = document.querySelector("#email").value;
    y = document.querySelector("#password").value;

    if (x == "" || y == "") {
        alert("error");
    } else {
        window.location.href="./user-type.html";
    }
}

const signUp = document.querySelector("#signUp-button");

signUp.addEventListener("click", function() {
    signUpValidate();
})