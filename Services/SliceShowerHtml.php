<!DOCTYPE html>
<html>
<head>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link href="SliceShower.css" rel="stylesheet">
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

