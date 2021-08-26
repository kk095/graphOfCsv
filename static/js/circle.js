// Multiple Animated Circle - Get Canvas element by Id
var canvas4 = document.getElementById( "canvas" );
var color="#f00"



// Set Canvas dimensions
canvas4.width   = 500;
canvas4.height  = 500;

// Get drawing context
var c4 = canvas4.getContext( '2d' );
c4.strokeStyle = color;

// The Circle class
function chng(x){
    c4.strokeStyle = x;
}
function Circle( x, y, dx, dy, radius ) {

  this.x  = x;
  this.y  = y;
  this.dx = dx;
  this.dy = dy;

  this.radius = radius;

  this.draw = function() {

    c4.beginPath();

    c4.arc( this.x, this.y,  this.radius, 0, Math.PI * 2, false  );

      
    c4.stroke();
  }

  this.update = function() {

    if( this.x + this.radius > 500 || this.x - this.radius < 0 ) {

      this.dx = -this.dx;
    }

    if( this.y + this.radius > 500 || this.y - this.radius < 0 ) {

      this.dy = -this.dy;
    }

    this.x += this.dx;
    this.y += this.dy;

    this.draw();
  }
}

var circles = [];

// Radius
var radius = 50;

for( var i = 0; i < 5; i++ )  {
  
  // Starting Position
  var x = Math.random() * ( 500 - radius * 2 ) + radius;
  var y = Math.random() * ( 500 - radius * 2) + radius;

  // Speed in x and y direction
    var dx = ( Math.random() - 0.5 ) * 2;
    var dy = ( Math.random() - 0.5 ) * 2;

  circles.push( new Circle( x, y, dx, dy, radius ) );
}

function animate4() {
  
  requestAnimationFrame( animate4 );

  c4.clearRect( 0, 0, 500, 500 );

  for( var r = 0; r < 5; r++ ) {

    circles[ r ].update();
  }
}

animate4();