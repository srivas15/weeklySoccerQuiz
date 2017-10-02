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

/*responsive font size of question based on length*/
function changeSize() {
  var $question = $(".question");
    
  var $numChar = $question.text().split("").length;
    
  if ($numChar > 60) {
      if($(document).height() <= 760)
        document.getElementById("questionText").style.fontSize = "8vw";
      else
        document.getElementById("questionText").style.fontSize = "5vw";
  }
}

$(move);

$(changeSize);
