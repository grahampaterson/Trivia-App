<?php

$input = fopen("triviaplaying.txt", "r");
$output = fopen("triviaconverted.txt", "w");

if ($input) {
    while (($line = fgets($input)) !== false) {
        // process the line read.
        fwrite($output, iconv("UTF-8", "ASCII//TRANSLIT", $line));
    }

    fclose($input);
} else {
    // error opening the file.
} 

fclose($output)


?>