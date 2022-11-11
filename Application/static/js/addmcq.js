// this is for mcq question from
document.getElementById('input_mcq_topic').value = "";
// this is for mcq option option form
document.getElementById('inputopt_mcq_ques').value = "";
// this is for showing topic and if topic is none then add option
function showMe(val) {
    if (val == 'None') {
        document.getElementById('x').style.display = "block";
    }
    else {
        document.getElementById('x').style.display = "none";
        document.getElementById('input_mcq_topic').value = val;
    }
}
// this is for if mcq question not present in list
function showMeQuestion(val) {
    if (val == 'NewQue') {
        document.getElementById('addnewmcq').style.display = "block";
        document.getElementById('inputopt_mcq_ques').value = "";
    }
    else {
        document.getElementById('addnewmcq').style.display = "none";
        document.getElementById('inputopt_mcq_ques').value = val;
    }
}

$(".readonly").keydown(function(e){
    e.preventDefault();
});