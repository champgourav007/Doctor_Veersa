let usertypeNode = document.getElementById("usertype");
let specialistNode = document.getElementById("specialist");
usertypeNode.addEventListener("click", check)

function check(){
    if(usertypeNode.value == "doctor"){
        changeVisibility();
    }
    else{
        changeVisibility();
    }
}


function changeVisibility(){
    if(specialistNode.style.visibility == "visible"){
        specialistNode.style.visibility = "hidden"
    }
    else{
        specialistNode.style.visibility = "visible"
    }
}