<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

</head>
<body>

<div class="slidecontainer">
  <input type="range" min="1" max="512" value="256" class="slider" id="myRangeFB">
  <p>Value: <span id="FB"></span></p>
  <p>Value: <span id="FBImg"></span></p>
</div>
<div class="slidecontainer">
  <input type="range" min="1" max="512" value="256" class="slider" id="myRangeLR">
  <p>Value: <span id="LR"></span></p>
  <p>Value: <span id="LRImg"></span></p>
</div>
<div class="slidecontainer">
  <input type="range" min="1" max="128" value="64" class="slider" id="myRangeTB">
  <p>Value: <span id="TB"></span></p>
  <p>Value: <span id="TBImg"></span></p>
</div>

<script>
var sliderFB = document.getElementById("myRangeFB");
var outputFB = document.getElementById("FB");
var imgFB = document.getElementById("FBImg");
outputFB.innerHTML = sliderFB.value;
sliderFB.oninput = function() {
    outputFB.innerHTML = sliderFB.value;
    if(sliderFB.value < 10)
        imgFB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/FrontBack/CTR_TRN_001_z00"+sliderFB.value+".png\" alt=\"\">";
    if(sliderFB.value < 100 && sliderFB.value > 9)
        imgFB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/FrontBack/CTR_TRN_001_z0"+sliderFB.value+".png\" alt=\"\">";
    if(sliderFB.value > 99)
    imgFB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/FrontBack/CTR_TRN_001_z"+sliderFB.value+".png\" alt=\"\">";
}

var sliderLR = document.getElementById("myRangeLR");
var outputLR = document.getElementById("LR");
var imgLR = document.getElementById("LRImg");
outputLR.innerHTML = sliderLR.value;
sliderLR.oninput = function() {
    outputLR.innerHTML = sliderLR.value;
    if(sliderLR.value < 10)
        imgLR.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/LeftRight/CTR_TRN_001_z00"+sliderLR.value+".png\" alt=\"\">";
    if(sliderLR.value < 100 && sliderLR.value > 9)
        imgLR.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/LeftRight/CTR_TRN_001_z0"+sliderLR.value+".png\" alt=\"\">";
    if(sliderLR.value > 99)
    imgLR.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/LeftRight/CTR_TRN_001_z"+sliderLR.value+".png\" alt=\"\">";
}

var sliderTB = document.getElementById("myRangeTB");
var outputTB = document.getElementById("TB");
var imgTB = document.getElementById("TBImg");
outputTB.innerHTML = sliderTB.value;
sliderTB.oninput = function() {
    outputTB.innerHTML = sliderTB.value;
    if(sliderTB.value < 10)
        imgTB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/TopBottom/CTR_TRN_001_z00"+sliderTB.value+".png\" alt=\"\">";
    if(sliderTB.value < 100 && sliderTB.value > 9)
        imgTB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/TopBottom/CTR_TRN_001_z0"+sliderTB.value+".png\" alt=\"\">";
    if(sliderTB.value > 99)
    imgTB.innerHTML = "<img class=\"prod_img\" src=\"CT_Scan/TopBottom/CTR_TRN_001_z"+sliderTB.value+".png\" alt=\"\">";
}
</script>

</body>