//Addison Huang
//SoftDev2 pd8
//K #11: Ask Circles [Change || Die] …While On The Go
//2019-03-18

var pic = document.getElementById("vimage");
var clicked = false;
pic.addEventListener('click', function(e){
    var x = e.offsetX;
    var y = e.offsetY;
    if(!circleClicked()){
      var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      c.setAttribute("cx",x);
      c.setAttribute("cy",y);
      c.setAttribute("r",50);
      c.setAttribute("fill","purple");
      c.setAttribute("stroke","black");
      pic.appendChild(c);
      addClick();
      vel.push([1,1])
    }
    else{
      clicked = false;
    }
});
function addClick(){
  child = pic.lastChild;
  child.addEventListener('click',function(e){
    if(this.getAttribute('fill') == "purple"){
      this.setAttribute('fill','lime');
    }
    else{
      this.setAttribute('fill','purple');
      this.setAttribute('cx', Math.random() * 500);
      this.setAttribute('cy', Math.random() * 500);
    }
    clicked = true;
  });
};
function circleClicked(){
  if(pic.children.length == 0){
    return false;
  }
  return clicked;
};
var clear = document.getElementById("clear");
var clearDots = function(e){
  while (pic.hasChildNodes()) {
      pic.removeChild(pic.firstChild);
  }
  vel = []
  moveButClicked = false;
  window.cancelAnimationFrame(requestID);
}
clear.addEventListener("click", clearDots)

var requestID;
var move = document.getElementById("move");
var moveButClicked = false;
var vel = [];
var moveDotsSetup = function(e) {
    window.cancelAnimationFrame(requestID);
    if(!moveButClicked){
        vel = []
        var children = Array.from(pic.children);
        for(var i = 0; i < children.length; i++){
            vel.push([1,1])
        }
        moveButClicked = true;
    }
    var moveDots = function(){
        window.cancelAnimationFrame(requestID);
        var children = Array.from(pic.children);
        var coords = []
        for(var i = 0; i < children.length; i++){
            var x = children[i].getAttribute("cx")
            var y = children[i].getAttribute("cy")
            coords.push([x,y])
        }
        while (pic.hasChildNodes()) {
            pic.removeChild(pic.firstChild);
        }
        for(var i = 0; i < coords.length; i++){
            var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            if(coords[i][0] <= 50 || coords[i][0] >= 450){
                vel[i][0] *= -1
            }
            if(coords[i][1] <= 50 || coords[i][1] >= 450){
                vel[i][1] *= -1
            }
            coords[i][0] = parseInt(coords[i][0]) + vel[i][0]
            coords[i][1] = parseInt(coords[i][1]) + vel[i][1]
            c.setAttribute("cx",coords[i][0]);
            c.setAttribute("cy",coords[i][1]);
            c.setAttribute("r",50);
            c.setAttribute("fill","blue");
            c.setAttribute("stroke","black");
            pic.appendChild(c);
        }
        requestID = window.requestAnimationFrame(moveDots);
    }
    moveDots();
};
move.addEventListener('click',moveDotsSetup);

var rand = document.getElementById("but")
var randDots = function(e) {
    for(var i = 0;i < vel.length; i++){
      vel[i][0] *= -1
      vel[i][1] *= -1
    }
};
rand.addEventListener('click',randDots);
