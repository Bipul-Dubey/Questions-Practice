let timeSecond = 300;
const timeH = document.querySelector('.timer');

displayTime(timeSecond);

const countDown = setInterval(() => {
    timeSecond--;
    displayTime(timeSecond);
    if (timeSecond == 0 || timeSecond < 1) {
        endCount();
        clearInterval(countDown);
    }
}, 1000);

function displayTime(second) {
    const min = Math.floor(second / 60);
    const sec = Math.floor(second % 60);
    timeH.innerHTML = "Timer:-" + `${min < 10 ? "0" : ""}${min}:${sec < 10 ? "0" : ""}${sec}`;
}

function endCount() {
    timeH.innerHTML = "Time out";
    document.getElementById("subbtn").click()
}

function timeset(){
    let inpt=document.getElementById("time")
    let timmer=document.getElementById("timmer")
    inpt.value=timmer.innerHTML
}