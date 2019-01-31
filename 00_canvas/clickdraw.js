
//Addison Huang
//SoftDev 2 pd8
//K00 -- I See a Red Door
//2019-01-31


var c = document.getElementById("slate");
var ctx = c.getContext("2d");
c.addEventListener("click", fill);
ctx.fillStyle="red";

function fill(e) {
    x=e.clientX-8
    y=e.clientY-121.78125
    if (state == 0) {
	ctx.fillRect(x,y,10,10);
    }
    else {
	ctx.beginPath();
	ctx.ellipse(x, y, 5, 5, Math.PI / 4, 0, 2 * Math.PI);
	ctx.fill();
    }
};

var state = 0;
var toggle = document.getElementById("toggle");
var clear = document.getElementById("clear");
toggle.addEventListener("click", tog);
clear.addEventListener("click", clean);

function clean() {
    ctx.clearRect(0,0,600,600);
};
    
function tog() {
    if (state == 0) {
	state = 1;
    }
    else {
	state=0;
    }
    console.log(state);
};
