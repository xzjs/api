<?php
/**
 * Created by PhpStorm.
 * User: xzjs
 * Date: 2017/1/9
 * Time: 上午9:46
 */
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $str='{"name":"BeJson","url":"http://www.bejson.com","page":88,"isNonProfit":true,"address":{"street":"科技园路.","city":"江苏苏州","country":"中国"},"links":[{"name":"Google","url":"http://www.google.com"},{"name":"Baidu","url":"http://www.baidu.com"},{"name":"SoSo","url":"http://www.SoSo.com"}]}';
    $img=file_get_contents('1.mp3');
    $result=$str.'|'.$img;
    echo $result;
}