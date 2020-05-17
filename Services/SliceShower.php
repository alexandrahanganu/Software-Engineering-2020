<?php
          include __DIR__ . '\SliceShowerHtml.php' ;
         
          if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $ct_path = $_POST['path_to_ct'];
            $ct_path = str_replace("\\", "\\\\", $ct_path);
            
            $mask_path = $_POST['path_to_mask'];
            $mask_path = str_replace("\\", "\\\\", $mask_path);
            exec("python nii_to_png_script3.0.py $ct_path $mask_path");
        }  
 ?>
 
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
