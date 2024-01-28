<?php
// process.php

header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $medicineId = $_POST['medicine_id'];
    $trackingNumber = $_POST['tracking_number'];
    $location = $_POST['location'];
    $date = date("Y-m-d H:i:s"); // Capture current date and time

    $data = [
        'medicine_id' => $medicineId,
        'tracking_number' => $trackingNumber,
        'location' => $location,
        'date' => $date
    ];

    // Convert to JSON and append to file
    file_put_contents("data.txt", json_encode($data) . "\n", FILE_APPEND);

    echo json_encode(["message" => "Data saved successfully"]);
} else {
    echo json_encode(["message" => "No data submitted"]);
}
?>
