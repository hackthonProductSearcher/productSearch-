const loginBtn = document.getElementById("login-button");
const signUplink = document.querySelector(".sign-up-link");

loginBtn.addEventListener("click", function(){
    window.location.href="./seller-profile.html";
})
signUplink.addEventListener("click", function(){
    window.location.href="./sign-up.html";
})