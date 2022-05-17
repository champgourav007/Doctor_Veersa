let usertypeNode = document.getElementById("usertype");
let specialistNode = document.getElementById("specialist");
usertypeNode.addEventListener("click", check)

function check(){
    if(usertypeNode.value == "doctor"){
        specialistNode.style.visibility = "visible";
    }
    else{
        specialistNode.style.visibility = "hidden";
    }
}