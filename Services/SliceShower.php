<script type="text/javascript">
window.addEventListener('error', function(notFound) {
    alert("Slice was not processed yet, please wait...");
}, true);
</script>

<?php
          if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $ct_path = $_POST['path_to_ct'];

            $ct_path = str_replace("\\", "\\\\", $ct_path);
            $output = '';
            pclose(popen("start /B ". "C:\\Python\\python.exe C:\\xampp\\htdocs\\Software-Engineering2020\\Scripts\\PreProcessingScripts\\nii_to_png_All_Slices.py "
            . $ct_path, "r")); 

        }

 ?>
 

<html>
<head>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link href="../Styles/SliceShower.css" rel="stylesheet">
</head>
<body>
<div id = "chenar">
 <div><h2>Underneath are shown the CT scans, sliced along the 3 axes.</h2></div>
 <div><hr></div>
    <div class = "ContainerMajor">
    <div class="slidecontainer">
     <h3>Front to back</h3>
     <input type="range" min="101" max="380" value="256" class="slider" id="myRangeFB">
     <p>Choose the slice number :<span id="FB"></span></p>
     <p> <span id="FBImg"></span> </p>
    </div>

    <div class="slidecontainer">
        <h3>Left to Right</h3>
         <input type="range" min="66" max="435" value="256" class="slider" id="myRangeLR">
         <p>Choose the slice number : <span id="LR"></span></p>
         <p> <span id="LRImg"></span></p><br>
     </div>

    <div class="slidecontainer">
     <h3>Top to Bottom</h3>
         <input type="range" min="16" max="100" value="64" class="slider" id="myRangeTB">
         <p>Choose the sclice number : <span id="TB"></span> </p>
         <p> <span id="TBImg"></span></p>
      </div>
    </div>
    </div>
</body>


 
 <script type="text/javascript">
    var strFilePath = <?php echo json_encode($_POST['path_to_ct']); ?>;
    var filenameEXT = strFilePath.replace(/^.*[\\\/]/, '');
    var filename = filenameEXT.split(".")[0];
    var sliderFB = document.getElementById("myRangeFB");
    var outputFB = document.getElementById("FB");
    var imgFB = document.getElementById("FBImg");
    outputFB.innerHTML = sliderFB.value;
    
    sliderFB.oninput = function() {
        outputFB.innerHTML = sliderFB.value;
        try{
            if(sliderFB.value < 10)
                imgFB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/FrontBack/" + filename +"_z00"+sliderFB.value+".png\" alt=\"\">";
            if(sliderFB.value < 100 && sliderFB.value > 9)
                imgFB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/FrontBack/" + filename +"_z0"+sliderFB.value+".png\" alt=\"\">";
            if(sliderFB.value > 99)
                imgFB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/FrontBack/" + filename +"_z"+sliderFB.value+".png\" alt=\"\">";
        }
        catch(err){
            alert("Slice was not yet processed, please wait...")
        }
    }

    var sliderLR = document.getElementById("myRangeLR");
    var outputLR = document.getElementById("LR");
    var imgLR = document.getElementById("LRImg");
    outputLR.innerHTML = sliderLR.value;
    sliderLR.oninput = function() {
        outputLR.innerHTML = sliderLR.value;
        try{
            if(sliderLR.value < 10)
                imgLR.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/LeftRight/" + filename +"_z00"+sliderLR.value+".png\" alt=\"\">";
            if(sliderLR.value < 100 && sliderLR.value > 9)
                imgLR.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/LeftRight/" + filename +"_z0"+sliderLR.value+".png\" alt=\"\">";
            if(sliderLR.value > 99)
                imgLR.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/LeftRight/" + filename +"_z"+sliderLR.value+".png\" alt=\"\">";
        }
        catch(err){
            alert("Slice was not yet processed, please wait...")
        }
    }

    var sliderTB = document.getElementById("myRangeTB");
    var outputTB = document.getElementById("TB");
    var imgTB = document.getElementById("TBImg");
    outputTB.innerHTML = sliderTB.value;
    sliderTB.oninput = function() {
        outputTB.innerHTML = sliderTB.value;
        try{
            if(sliderTB.value < 10)
                imgTB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/TopBottom/" + filename +"_z00"+sliderTB.value+".png\" alt=\"\">";
            if(sliderTB.value < 100 && sliderTB.value > 9)
                imgTB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/TopBottom/" + filename +"_z0"+sliderTB.value+".png\" alt=\"\">";
            if(sliderTB.value > 99)
                imgTB.innerHTML = "<img class=\"prod_img\" src=\"../ProcessedPatients/"+ filename + "/CT Scan/All/TopBottom/" + filename +"_z00"+sliderTB.value+".png\" alt=\"\">";
        }
        catch(err){
            alert("Slice was not yet processed, please wait...")
        }
}
</script>


