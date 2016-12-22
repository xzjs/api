<?php
require_once("php_python.php"); //框架提供的程序脚本

try {
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $city = $_POST['city'];
        if ($city) {
            $servername = '192.168.4.96';
            $username = 'root';
            $password = '123';
            $dbname = 'spider';

            // 创建连接
            $conn = new mysqli($servername, $username, $password, $dbname);
// 检测连接
            if ($conn->connect_error) {
                die("连接失败: " . $conn->connect_error);
            }
            mysqli_set_charset($conn,"utf8");
            $sql = "SELECT time FROM spider.advice where city=$city ORDER BY time DESC ";
            $result = $conn->query($sql);
            $num=$result->num_rows;
            if ($result->num_rows == 0) {
                $ret = ppython("weather::start", $city);
                echo $ret;
            }
            if(time() - mysqli_fetch_array($result)['time'] > 3600){
                $ret = ppython("weather::start", $city);
                echo $ret;
            }
            $sql = "SELECT today,advice FROM spider.advice where city=$city ORDER BY time DESC";
            $result = $conn->query($sql);
            $data['advice'] = mysqli_fetch_object($result);
            $sql = "SELECT pm10,pm2_5,no2,so2,co,o3 FROM spider.aqi where city=$city ORDER BY time DESC";
            $result = $conn->query($sql);
            $data['aqi'] = mysqli_fetch_object($result);
            $sql = "SELECT * FROM (select date,pollute,temp,weather from spider.future where city=$city order by time desc) as db limit 15";
            $result = $conn->query($sql);
            $data['future']=mysqli_fetch_all($result,MYSQLI_ASSOC);
print_r($data);
            $sql = "SELECT update_time,weather,tempmax,tempmin,wind,pollute,warning FROM spider.today where city=$city order by time desc";
            $result = $conn->query($sql);
            $data['today'] = mysqli_fetch_object($result);
            echo json_encode($data,JSON_UNESCAPED_UNICODE);
            $conn->close();
        }
    } else {
        echo '请使用post提交';
    }
}catch (Exception $exception){
    echo $exception->getMessage();
}
