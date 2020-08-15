const sellerCard = document.querySelector("#seller");
const buyerCard = document.querySelector("#buyer");

sellerCard.addEventListener("click", function(){
    window.location.href="./seller-profile.html";
})

buyerCard.addEventListener("click", function(){
    window.location.href="./buyer-page.html";
})