let dateNode = document.getElementById("date");
let formNode = document.getElementById("form");
let timeDivNode = document.getElementById("time-label");
let slotFormNode = document.getElementById("slot-form");


dateNode.addEventListener("change", changeSlots);

function changeSlots(){
    formNode.submit();
}


// function addTime(){
//     // timeDivNode = slotFormNode.children[slotFormNode.children.length - 2]
//     let timeInput = document.createElement("input");
//     timeInput.setAttribute("type","time");
//     timeInput.setAttribute("id", "time");
//     timeInput.setAttribute("name", "time");
//     timeInput.setAttribute("onchange", "addTime()");
//     // let timeInput = document.getElementById("time");
//     console.log(timeInput)
//     timeDivNode.appendChild(timeInput);
//     console.log(timeDivNode)
//     // timeDivNode.appendChild(timeInput);

// }