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
      number.style.color='green';
      n=true;
    }
    else{
      number.style.color="red";
      n=false;
    }
  // uppercase
    if(pass.value.match(/[A-Z]/)){
      upper.style.color='green';
      u=true;
    }
    else{
      upper.style.color="red";
      u=false;
    }
  // lowercase
    if(pass.value.match(/[a-z]/)){
      lower.style.color='green';
      lw=true;
    }
    else{
      lower.style.color="red";
      lw=false;
    }
  // length>=6
    if(pass.value.length<6){
      len.style.color="red";
      l=false
    }
    else{
      len.style.color='green';
      l=true
    }
  // special_char
    if(pass.value.match(/[!\@\#\$\^\_\*]/)){
      special_char.style.color='green';
      s=true
    }
    else{
      special_char.style.color="red";
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
    let sp=pass.value.match(/[' ']/)
    let match=document.getElementById('match-pass');
    if(sp){
      match.innerHTML="Space Not Allowed";
      strength.style.color="red";
      match.style.display="block";
      space=false
    }
    if(sp==null){
      match.style.display="none";
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
  // fa-regular fa-eye
  var state=false;
  function toggler(){
      let eyeswitch1=document.getElementById('eyeswitch1');
      let eyeswitch2=document.getElementById('eyeswitch2');
      let pass=document.getElementById('pass1')
      if(state){
        pass.setAttribute('type', 'password')
        eyeswitch1.style.display="block";
        eyeswitch2.style.display="none";

        state=false
      }
      else {
        pass.setAttribute('type', 'text')
        eyeswitch1.style.display="none";
        eyeswitch2.style.display="block";
        state=true
      }
  }

  var state2=false;
  function showhide(){
      let eyeswitch3=document.getElementById('eyeswitch3');
      let eyeswitch4=document.getElementById('eyeswitch4');
      let pass=document.getElementById('pass2')
      if(state2){
        pass.setAttribute('type', 'password')
        eyeswitch3.style.display="block";
        eyeswitch4.style.display="none";

        state2=false
      }
      else {
        pass.setAttribute('type', 'text')
        eyeswitch3.style.display="none";
        eyeswitch4.style.display="block";
        state2=true
      }
  }
