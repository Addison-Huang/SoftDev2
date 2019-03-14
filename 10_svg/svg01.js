var pic =document.getElementById("vimage");
var counter = 0;
var clicked = false;

pic.addEventListener("click", function(e){
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    var x = e.offsetX;
    var y = e.offsetY;
    if(!circleClicked()) {
	c.setAttribute("cx",x);
	c.setAttribute("cy",y);
	c.setAttribute("r","20");
	c.setAttribute("fill", "Fuchsia");
	c.setAttribute("stroke", "black");
	pic.appendChild(c);
	c.addEventListener('click',function(e){
	    if(this.getAttribute('fill') == "Fuchsia"){
		this.setAttribute('fill','Lime')
	    }
	    else{
		this.setAttribute('fill','Fuchsia')
		this.setAttribute('cx', Math.random() * 501)
		this.setAttribute('cy', Math.random() * 501)
	    }
	    clicked = true;
	});
    }
    else {
	clicked = false;
    }
})

function circleClicked(){
    if(pic.children.length == 0){
	return false;
    }
    return clicked
}



var clear = document.getElementById("but_clear");
clear.addEventListener("click", function(e) {
    while (pic.lastChild){
	pic.removeChild(pic.lastChild);
    }
    counter =0
});

