const loginButton = document.querySelector("#login-button");
const signUplink = document.querySelector(".sign-up-link");

loginButton.addEventListener("click", function(){
    window.location.href="./seller-profile.html";
})
signUplink.addEventListener("click", function(){
    window.location.href="./sign-up.html";
})