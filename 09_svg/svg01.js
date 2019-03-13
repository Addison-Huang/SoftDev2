var pic =document.getElementById("vimage");
var xprev;
var yprev;
var counter = 0;
pic.addEventListener("click", function(e){
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    var x = e.offsetX;
    var y = e.offsetY;
    c.setAttribute("cx",x);
    c.setAttribute("cy",y);
    c.setAttribute("r","10");
    c.setAttribute("fill", "red");
    c.setAttribute("stroke", "black");
    if (counter > 0) {
	var l = document.createElementNS("http://www.w3.org/2000/svg","line");
	l.setAttribute("x1",xprev);
	l.setAttribute("x2",x);
	l.setAttribute("y1",yprev);
	l.setAttribute("y2",y);
	l.setAttribute("style","stroke:black;stroke-width:2");
	pic.appendChild(l);
	var ci = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	var x = e.offsetX;
	var y = e.offsetY;
	ci.setAttribute("cx",xprev);
	ci.setAttribute("cy",yprev);
	ci.setAttribute("r","10");
	ci.setAttribute("fill", "red");
	ci.setAttribute("stroke", "black");
	pic.appendChild(ci)
	
    }
    pic.appendChild(c);
    counter +=1;
    xprev=x;
    yprev=y;
});

var clear = document.getElementById("but_clear");
clear.addEventListener("click", function(e) {
    pic.innerHTML = "";
    counter = 0;
});
    
