var ele=document.getElementById("img2");
var doc=document.querySelector("#side");
var item=document.getElementById("cross");
ele.addEventListener("mouseover",event=>{
    doc.style.display="block";
    doc.style.transform="ease-in";
})
item.addEventListener("click",event=>{
    doc.style.display="none";
});