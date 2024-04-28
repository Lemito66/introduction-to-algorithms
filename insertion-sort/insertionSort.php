<?php
function insertionSort($arr)
{
    for ($i = 1; $i < count($arr); $i++) {
        $j = $i;
        while ($j > 0 && $arr[$j] < $arr[$j - 1]) {
            $temp = $arr[$j];
            $arr[$j] = $arr[$j - 1];
            $arr[$j - 1] = $temp;
            $j--;
        }
    }
    return $arr;
}
