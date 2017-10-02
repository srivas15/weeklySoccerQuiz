var selectedOption = 0;

function option1() {
    selectedOption = 1;
    document.getElementById('answer').value = selectedOption;
    document.getElementById('question').submit();
}

function option2() {
    selectedOption = 2;
    document.getElementById('answer').value = selectedOption;
    document.getElementById('question').submit();
}

function option3() {
    selectedOption = 3;
    document.getElementById('answer').value = selectedOption;
    document.getElementById('question').submit();
}

function option4() {
    selectedOption = 4;
    document.getElementById('answer').value = selectedOption;
    document.getElementById('question').submit();
}

function timerDone() {
	selectedOption = 0;
	document.getElementById('answer').value = selectedOption;
    document.getElementById('question').submit();
}

/*timer bar*/
var timerLength = 50; /*5 seconds*/
function move() {
  var elem = document.getElementById("myBar");   
  var width = 100;
  var id = setInterval(frame, timerLength);
  function frame() {
    if (width <= 0) {
      clearInterval(id);
      timerDone();
    } else {
      width--; 
      elem.style.width = width + '%'; 
    }
  }
}

$(move);