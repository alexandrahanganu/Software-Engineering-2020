<?php

use PHPUnit\Framework\Constraint\IsTrue;
use PHPUnit\Framework\TestCase;
$filename = '/path/to/foo.txt';

class Test extends PHPUnit\Framework\TestCase   //PHPUnit_Framework_TestCase
{

    public function fileType() //must me .nii
    {
        $path = new ..\Services\SliceShower;
        $this->assertSame('.nii', substr($path,-4));

        if ( 0 == filesize( $path ) ) // file can't be empty
        {
            $this->false;
        }
    }
}
?>


