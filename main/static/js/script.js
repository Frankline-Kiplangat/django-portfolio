$(document).ready(function(){
    $("form#message-form").submit(function(){
      var name = $("input#input1").val();
      if ($("input#input1").val() && $("input#input2").val()){
        alert(name + ",thank you for reaching out. I will get back to you soon.");
      }
      else {
        alert("Please enter your name and email address!");
      }
      
    });
  
  });