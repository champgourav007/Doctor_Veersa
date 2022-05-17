let dateNode = document.getElementById("date");
let formNode = document.getElementById("form");

dateNode.addEventListener("change", changeSlots);

function changeSlots(){
    formNode.submit();
}
