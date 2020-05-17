<!DOCTYPE html>
<html>
<head>
     <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div id = "chenar">
 <div><h2>Underneath are shown the CT scans, sliced along the 3 axes.</h2></div>
 <div><hr></div>
    <div class = "ContainerMajor">
    <div class="slidecontainer">
     <h3>Front to back</h3>
     <input type="range" min="1" max="512" value="256" class="slider" id="myRangeFB">
     <p>Choose the CT :<span id="FB"></span></p>
     <p> <span id="FBImg"></span> </p>
    </div>

    <div class="slidecontainer">
        <h3>Left to Right</h3>
         <input type="range" min="1" max="512" value="256" class="slider" id="myRangeLR">
         <p>Choose the CT : <span id="LR"></span></p>
         <p> <span id="LRImg"></span></p><br>
     </div>

    <div class="slidecontainer">
     <h3>Top to Bottom</h3>
         <input type="range" min="1" max="128" value="64" class="slider" id="myRangeTB">
         <p>Choose the CT : <span id="TB"></span> </p>
         <p> <span id="TBImg"></span></p>
      </div>
    </div>
    </div>
    </body>
<style>
#chenar{
    border-radius:10px;
    margin-left:40px;
    margin-right:40px;
    padding-left:15px;
    padding-right:15px;
    background-color:  #f4f4f4;
}
h2{
    text-align:center;
    padding-top:15px;
}
hr{
    width:95%;
}


body{
    background-color:  white;
}
.ContainerMajor{
    display: flex;
    height:auto;
    flex-direction:row;
    justify-content:center;
    text-align:center;
    /*border: 1px solid rgba(187, 187, 206, 0.787);*/
    border-radius:10px;
    padding:20px;
    padding-top: 0px;
    /*background-color: rgb(247, 247, 255);*/

}
.slider {
  -webkit-appearance: none;
  width: 70%;
  border-radius: 5px;  
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
  cursor:pointer;
}

.prod_img{
    width:340px;
    height:340px;
    border-radius:15px;
    margin-left:15px;
    margin-right:15px;
    border: 1px solid black;
}

@media (min-width:1850px){
    .prod_img{
    width:512px;
    height:512px;
    border-radius:15px;
    margin-left:55px;
    margin-right:55px
    }
}
@media (min-width:859px)and (max-width:1212px){
    .prod_img{
        width:250px;
        height:250px;
        margin-left:10px;
        margin-right:10px;
    }
    .ContainerMajor{
        padding: 5px;
    }
    #chenar{
        margin:15px;
    }
    
}
@media (min-width:660px)and (max-width:858px){
    .prod_img{
        width:200px;
        height:200px;
        margin-left:5px;
        margin-right:5px;
    }
    .ContainerMajor{
        padding: 5px;
    }
    #chenar{
        margin:5px;
    }
    
}
@media (min-width:300px)and (max-width:660px){
    .ContainerMajor{
    flex-direction:column;
    padding: 5px;
}
.prod_img{
        width:250px;
        height:250px;
        margin:0px;
    }
    #chenar{
        margin:5px;
    }
}
</style>
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
