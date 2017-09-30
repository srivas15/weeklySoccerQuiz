var selectedOption = 0

function option1() {
    selectedOption = 1
}

function option2() {
    selectedOption = 2
}

function option3() {
    selectedOption = 3
}

function option4() {
    selectedOption = 4
}

function submit() {
	if (selectedOption != 0)
	{
		document.getElementById('answer').value = selectedOption;
		document.getElementById('question').submit();
	}
}