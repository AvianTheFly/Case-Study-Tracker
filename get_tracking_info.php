<?php
// get_tracking_info.php

header('Content-Type: text/html; charset=utf-8');

if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST['tracking_number_query'])) {
    $trackingNumber = $_POST['tracking_number_query'];

    // Connect to SQLite database
    $db = new PDO('sqlite:medicine_tracking.db');

    // Query the database
    $stmt = $db->prepare('SELECT medicine_id, location, date FROM tracking WHERE tracking_number = ?');
    $stmt->execute([$trackingNumber]);
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (count($results) > 0) {
        echo "<ul>";
        foreach ($results as $row) {
            echo "<li>" . htmlspecialchars($row['date']) . ": " . htmlspecialchars($row['location']) . " (Medicine ID: " . htmlspecialchars($row['medicine_id']) . ")</li>";
        }
        echo "</ul>";
    } else {
        echo "No records found for this tracking number.";
    }
} else {
    echo "No tracking number provided.";
}
?>
