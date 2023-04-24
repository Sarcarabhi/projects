/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
  
  /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
  }
  
  
let btn = document.querySelector("button");

btn.addEventListener("click", active);

function active() {
  btn.classList.toggle("is_active");
}


function printPageArea(areaID){
  var printContent = document.getElementById(areaID).innerHTML;
  var originalContent = document.body.innerHTML;
  document.body.innerHTML = printContent;
  window.print();
  document.body.innerHTML = originalContent;
}

// show form
window.onload = function() {
  document.getElementById('ifYes').style.display = 'none';
  document.getElementById('ifNo').style.display = 'none';
}
function yesnoCheck() {
  if (document.getElementById('yesCheck').checked) {
      document.getElementById('ifYes').style.display = 'block';
      document.getElementById('ifNo').style.display = 'none';
      document.getElementById('redhat1').style.display = 'none';
      document.getElementById('aix1').style.display = 'none';
  } 
  else if(document.getElementById('noCheck').checked) {
      document.getElementById('ifNo').style.display = 'block';
      document.getElementById('ifYes').style.display = 'none';
      document.getElementById('redhat1').style.display = 'none';
      document.getElementById('aix1').style.display = 'none';
 }
}
function yesnoCheck1() {
 if(document.getElementById('redhat').checked) {
     document.getElementById('redhat1').style.display = 'block';
     document.getElementById('aix1').style.display = 'none';
  }
 if(document.getElementById('aix').checked) {
     document.getElementById('aix1').style.display = 'block';
     document.getElementById('redhat1').style.display = 'none';
  }
}


document.getElementById("todaydate").value = new Date().toLocaleDateString(); 


var loadFile = function(event) {
  var image = document.getElementById('output');
  image.src=URL.createObjectURL(event.target.files[0]);
};

const targetDiv = document.getElementById("mydiv");
const btn1 = document.getElementById("toggle");
btn1.onclick = function () {
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
};