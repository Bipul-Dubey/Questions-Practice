// this is for showing topic and if topic is none then add option
  document.getElementById('input_subj_topic').value="";
  function showMe(val){
    if(val=='None'){
      document.getElementById('x').style.display="block";
    }
    else{
      document.getElementById('x').style.display="none";
      document.getElementById('input_subj_topic').value=val;
    }
  }
  $(".readonly").keydown(function(e){
    e.preventDefault();
  });
