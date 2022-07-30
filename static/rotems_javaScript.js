

window.addEventListener('load', main);

function ApproveSub() {
    var text = "Cool!";
    document.getElementById("button").innerHTML = text;
}

function main() {
  const title = document.getElementById("title");
  title.addEventListener("mouseover", changeFlower);
  title.addEventListener("mouseout", changeDarkFlower);

   //nav bar
  const activePage = window.location.pathname;
  const navLinks = document.querySelectorAll('nav a').forEach(link => {    
    if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

function changeFlower() {
  title.classList.remove('dark_flower');
  title.classList.add('flower');
}


function changeDarkFlower() {
  title.classList.remove('flower');
  title.classList.add('dark_flower');
}


}




