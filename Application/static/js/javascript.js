const inputs = document.querySelectorAll('.input');

function focusFunc(){
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus');
}

function blurFunc(){
    let parent = this.parentNode.parentNode;
    if(this.value == ""){
        parent.classList.remove('focus');
    }
}

inputs.forEach(input => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur', blurFunc);
});

function validate(){
    let pass=document.getElementById('pass1');
    let upper=document.getElementById('upper');
    let lower=document.getElementById('lower');
    let special_char=document.getElementById('special');
    let number=document.getElementById('number');
    let len=document.getElementById('length');
  
    let u=false
    let lw=false
    let s=false
    let n=false
    let l=false
  // number
    if(pass.value.match(/[0-9]/)){
      number.style.display='none';
      n=true;
    }
    else{
      number.style.display="inline-flex";
      n=false;
    }
  // uppercase
    if(pass.value.match(/[A-Z]/)){
      upper.style.display='none';
      u=true;
    }
    else{
      upper.style.display='inline-flex';
      u=false;
    }
  // lowercase
    if(pass.value.match(/[a-z]/)){
      lower.style.display='none';
      lw=true;
    }
    else{
      lower.style.display='inline-flex';
      lw=false;
    }
  // length>=6
    if(pass.value.length<6){
      len.style.display='inline-flex';
      l=false
    }
    else{
      len.style.display="none";
      l=true
    }
  // special_char
    if(pass.value.match(/[!\@\#\$\^\_\*]/)){
      special_char.style.display='none';
      s=true
    }
    else{
      special_char.style.display="inline-flex";
      s=false
    }
  
  // strength matching
    let weak=/[a-z,A-Z]/;
    let medium=/\d+/;
    let strong=/.[!,@,#,$,^,_,*]/;
    let strength=document.getElementById("strength");
    if(pass.value.length<6 && pass.value.match(weak) ||  pass.value.match(medium) || pass.value.match(strong)){
      strength.style.color="red";
    }
    if(pass.value.length >= 6 && ((pass.value.match(weak) && pass.value.match(medium)) || (pass.value.match(medium) && pass.value.match(strong)) || (pass.value.match(weak) && pass.value.match(strong)))){
      strength.style.color="yellow";
    }
    if (pass.value.length >=9 && pass.value.match(weak) && pass.value.match(medium) && pass.value.match(strong)) {
      strength.style.color="green";
    }
    let space=false;
    let sp=pass.value.match(/[' ','']/)
    let pass_space=document.getElementById('pass-space');
    if(sp){
      pass_space.innerHTML="Space Not Allowed";
      strength.style.color="red";
      pass_space.style.display="block";
      space=false
    }
    if(sp==null){
      pass_space.style.display="none";
      space=true
    }
  
    let button=document.getElementById('subbtn');
    if(u && lw && s && n && l && space){
      button.disabled=false;
    }
    else{
      button.disabled=true;
    }
}

var state=false;
function toggler(){
    let eyeswitch1=document.getElementById('eyeswitch1');
    let eyeswitch2=document.getElementById('eyeswitch2');
    let pass=document.getElementById('pass1')
    if(state){
      console.log('true');
      pass.setAttribute('type', 'password')
      eyeswitch1.style.display="block";
      eyeswitch2.style.display="none";

      state=false
    }
    else {
      console.log('false');
      pass.setAttribute('type', 'text')
      eyeswitch1.style.display="none";
      eyeswitch2.style.display="block";
      state=true
    }
}