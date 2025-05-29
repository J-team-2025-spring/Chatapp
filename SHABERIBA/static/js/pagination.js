document.addEventListener("DOMContentLoaded", () => {
const channels = document.getElementsByClassName("channel-title-box");
console.log(channels.length);
const backbtn = document.getElementById("backbtn");
const nextbtn = document.getElementById("nextbtn");
const ul = document.getElementById("pagenation");
const itemsPerPage = 4
let currentPage = 1 ;
let TOTAL;

const render = () => {
    for (let i = 0; i < channels.length; i++) {
        if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
        channels[i].style.display = "";
        }
        else{
        channels[i].style.display = "none";
        }
    }
};

const page_total = () =>{
    if(channels.length % itemsPerPage == 0){
        TOTAL = channels.length / itemsPerPage;
    }
    else{
        TOTAL = Math.floor(channels.length / itemsPerPage) + 1; 
    }
};

const block = () =>{
    page_total()
    for (let i = 0; i < TOTAL ;i++){
        var li = document.createElement('li');
        ul.appendChild(li);
        li.dataset.page = i + 1;
        var text = document.createTextNode(i + 1);
        li.appendChild(text);
        li.addEventListener("click",(e) => {
            currentPage = Number(e.target.dataset.page);
            render();
        })}  
};

const pagenation = () =>{
    
    backbtn.addEventListener("click",() =>{
        if(currentPage > 1){
            currentPage--;
            render();
    }})

    nextbtn.addEventListener("click",() =>{
        if(currentPage < TOTAL){
            currentPage++;
            render();
    }})
};

render();
block();
pagenation();
});