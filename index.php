<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="stylesheet.css" />
  <meta charset="UTF-8" />
  <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
</head>

<?php
$message = shell_exec('python3 retrieve.py');
echo $message;
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
    count = (count+1) % 4;
  }
  function test() {
    var x = $.ajax({
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
                return state;
            }
        });
  }
</script>

<body style="background-color:rgb(211,211,211)">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <table style="width: 100%">
      <tr >
        <td><a class="navbar-brand" href="#">KNOCK KNOCK</a></td>
        <td style="text-align:right"><a class="navbar-brand" href="#" style="right:0; font-size:15px">User's Name</a></td>
      </tr>
    </table>
    </nav>
    <p id="submitStatus"></p>
    <div class="outer">
      <div class="middle">
        <div style='padding: 10px; background-color: #FFFFFF; border: 5px; height: 80%; width: 1000px; margin:auto;'>
          <h2>Hi User.</h2>
          <p>Let's check your usage for the past week.</p>
          <ul>
            <li>x% of your energy was wasted.</li>


          </ul>
          <!-- <h4>Let's check your energy usage for the past week!</h3> -->
            <div id="contents" style='text-align:center;'>
              <img id="l_left" src="assets/left.svg" height=30px margin-right=10px onclick="light_switch()"/>
                <img id="l_img1" src="LightEnergy.png" width=400px style="border-radius: 5px;"/>
                <img id="l_img2" src="HeatEnergy.png"  style="border-radius: 5px;display: none;" width=400px/>
                <img id="l_img3" src="ACEnergy.png" style="border-radius: 5px;display: none;" width=400px/>
                <img id="l_img4" src="TotalEnergy.png"  style="border-radius: 5px;display: none;" width=400px/>
              <img id="l_right" src="assets/right.svg" height=30px margin-left=10px onclick="light_switch()"/>
          </div>

        <div>
          <p>Want to turn your lights off now?</p>
          <div id="contents" style='text-align:center; padding-top: 10px;'>
            <button id="mail" onclick="test()" style="text-align:center; border: none; background-color: #FFFFFF; color: #111111; border-color: black; border-radius: 5px;">LIGHTS OUT</div>
          <div>
      </div>

    </div>
    <div style='padding: 10px; z-index: -1; background-color: #111111; border: 5px; height: 80%; width: 1000px; position: absolute; top: 115px; margin:auto;'></div>
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
