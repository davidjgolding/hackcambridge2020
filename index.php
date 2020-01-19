<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="stylesheet.css" />
  <meta charset="UTF-8" />
  <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
</head>

<?php
$message = shell_exec('python3 retrieve.py');
?>

<script>

  let count = 1;
  function light_switch() {
    if (count == 0) {
      document.getElementById("l_img1").style.display='inline';
      document.getElementById("l_img2").style.display='none';
      document.getElementById("l_img3").style.display='none';
      document.getElementById("l_img4").style.display='none';
    } else if (count == 1) {
      document.getElementById("l_img1").style.display='none';
      document.getElementById("l_img2").style.display='inline';
      document.getElementById("l_img3").style.display='none';
      document.getElementById("l_img4").style.display='none';
    } else if (count == 2) {
      document.getElementById("l_img1").style.display='none';
      document.getElementById("l_img2").style.display='none';
      document.getElementById("l_img3").style.display='inline';
      document.getElementById("l_img4").style.display='none';
    } else if (count == 3) {
      document.getElementById("l_img1").style.display='none';
      document.getElementById("l_img2").style.display='none';
      document.getElementById("l_img3").style.display='none';
      document.getElementById("l_img4").style.display='inline';
    }
    count = (count+1) % 3;
  }
  function test() {
    $.ajax({
            url: "submit.php",
            type: "POST",
            beforeSend: function() {
                $("#submitStatus").text("Just processing your message...");
                $("#submitStatus").removeClass("submitFailure");
                $("#submitStatus").removeClass("submitSuccess");
                $("#submitStatus").addClass("submitProcessing");
                $("#submit").attr("disabled", true);
            },
            success: function(state) {
                $("#submitStatus").text(
                    "Your message was successfully submitted."
                );
                $("#submitStatus").removeClass("submitProcessing");
                $("#submitStatus").removeClass("submitFailure");
                $("#submitStatus").addClass("submitSuccess");
                $("#formWithoutTitle").css("display", "none");
                $("#formTitle").text("See you soon!");
            }
        });
  }
</script>

<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">KNOCK KNOCK</a>
    <div style="width:100%;">
    </div>
    <a class="navbar-brand" href="#" style="right:0; font-size:15px">Hi John!</a>
    </nav>
    <p id="submitStatus"></p>
    <div class="outer">
      <div class="middle">
            <div id="contents" style='text-align:center'>
              <img id="l_left" src="assets/left.svg" height=30px onclick="light_switch()"/>
                <img id="l_img1" src="LightEnergy.png" width=550px />
                <img id="l_img2" src="HeatEnergy.png"  style="display: none;" width=550px/>
                <img id="l_img3" src="ACEnergy.png"  style="display: none;" width=550px/>
                <img id="l_img4" src="TotalEnergy.png"  style="display: none;" width=550px/>
              <img id="l_right" src="assets/right.svg" height=30px onclick="light_switch()"/>
          </div>
          <button id="mail" onclick="test()">Test</div>
        </div>
      </div>

    </div>

    <!-- <script>
      $("#mail").on("click",function(){alert("hi")})
    </script> -->
</body><!-- Footer -->
<footer class="page-footer font-small special-color-dark pt-4" style="bottom:0; position:absolute; text-align:centre; width:100%">
  <!-- Copyright -->
  <div class="footer-copyright text-center py-3" style="text-align:centre">2020 Hack Cambridge</div>
  <!-- Copyright -->
</footer>
</html>
