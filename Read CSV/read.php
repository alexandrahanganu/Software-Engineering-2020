
<?php

$row = 1;
if (($handle = fopen("C:\Users\Ioana\Downloads\wetransfer-65cf87\TBC Right\TBC_Results_Right.csv", "r")) !== FALSE) {
   // La fopen se modifica csv-ul din calculatorul vostru
    echo '<table border="1">';
   
    while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
        $num = count($data);
        if ($row == 1) {
            echo '<thead><tr>';
        }else{
            echo '<tr>';
        }
       
        for ($c=0; $c < $num; $c++) {
            //echo $data[$c] . "<br />\n";
            if(empty($data[$c])) {
               $value = "&nbsp;";
            }else{
               $value = $data[$c];
            }
            if ($row == 1) {
                echo '<th>'.$value.'</th>';
            }else{
                echo '<td>'.$value.'</td>';
            }
        }
       
        if ($row == 1) {
            echo '</tr></thead><tbody>';
        }else{
            echo '</tr>';
        }
        $row++;
    }
   
    echo '</tbody></table>';
    fclose($handle);
}


?>