const imgDiv = document.querySelector('.profile-pic-div');
const img = document.querySelector('#photo');
const file = document.querySelector('#file');
const uploadBtn = document.querySelector('#uploadBtn');
let govIdNode = document.getElementById("gov_id");
let govIdTypeNode = document.getElementById("id_gov_id_type");

console.log(govIdTypeNode.children[0].value, govIdNode.innerHTML);
govIdTypeNode.children[0].value = govIdNode.innerHTML;
govIdTypeNode.children[0].innerHTML = govIdNode.innerHTML;

// govIdTypeNode.children.forEach(element => {
//     if(element.value == govIdNode.innerHTML){
//         element.setAttribute("selected", true);
//     }
// });





imgDiv.addEventListener('mouseenter', function(){
    uploadBtn.style.display = "block";
});


imgDiv.addEventListener('mouseleave', function(){
    uploadBtn.style.display = "none";
});


file.addEventListener('change', function(){
    const choosedFile = this.files[0];

    if (choosedFile) {

        const reader = new FileReader();

        reader.addEventListener('load', function(){
            img.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);
        let uploadedFileNode = document.getElementById("uploaded_file");
        uploadedFileNode.setAttribute("value", "choosedFile");
    }
});