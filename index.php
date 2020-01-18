<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="stylesheet.css" />
  <meta charset="UTF-8" />
</head>
<script>
  let light_total = false
  function light_switch() {
    if (!light_total) {
      document.getElementById("l_img1").style.display='none';
      document.getElementById("l_img2").style.display='inline';
    } else {
      document.getElementById("l_img1").style.display='inline';
      document.getElementById("l_img2").style.display='none';
    }
    light_total = !light_total
    console.log(light_total)
  }
</script>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">KNOCK KNOCK</a>
    </nav>

    <div id="contents">
      <div style="text-align: center">
        <h3>Light Consumption</h1>
        <div id="contents">
          <img id="l_left" src="assets/left.svg" height=30px onclick="light_switch()"/>
          <img id="l_img1" src="graph.png" />
          <img id="l_img2" src="" style="display: none;"/>
          <img id="l_right" src="assets/right.svg" height=30px onclick="light_switch()"/>
        </div>
      </div>


      <div style="text-align: center">
        <h3>Heat Consumption</h1>

        <div id="contents">

          <img src="graph.png" />
        </div>
      </div>
    </div>


</body><!-- Footer -->
<footer class="page-footer font-small special-color-dark pt-4">
  <!-- Copyright -->
  <div class="footer-copyright text-center py-3">2020 Hack Cambridge</div>
  <!-- Copyright -->
</footer>
</html>
