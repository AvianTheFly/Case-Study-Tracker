<?php
// process.php

header('Content-Type: application/json');

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $medicineId = $_POST['medicine_id'];
        $trackingNumber = $_POST['tracking_number'];
        $location = $_POST['location'];
        $date = date("Y-m-d H:i:s"); // Capture current date and time

        // Connect to SQLite database
        $db = new PDO('sqlite:medicine_tracking.db');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Insert data into database
        $stmt = $db->prepare('INSERT INTO tracking (medicine_id, tracking_number, location, date) VALUES (?, ?, ?, ?)');
        $stmt->execute([$medicineId, $trackingNumber, $location, $date]);

        $response = ["message" => "Data saved successfully"];
    } else {
        $response = ["message" => "No data submitted"];
    }
} catch (PDOException $e) {
    $response = ["message" => "Database error: " . $e->getMessage()];
} catch (Exception $e) {
    $response = ["message" => "Error: " . $e->getMessage()];
}

echo json_encode($response);
?>
