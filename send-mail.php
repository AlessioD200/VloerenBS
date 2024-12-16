<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $message = htmlspecialchars($_POST['message']);

    $to = "alessio.depreytere@icloud.com"; // Replace with your email
    $subject = "Nieuwe offerte aanvraag van $name";
    $body = "Naam: $name\nE-mail: $email\nTelefoonnummer: $phone\nBericht:\n$message";

    $headers = "From: $email\r\nReply-To: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Bedankt! Uw aanvraag is verzonden.";
    } else {
        echo "Er is een probleem opgetreden. Probeer het later opnieuw.";
    }
} else {
    echo "Ongeldige verzoekmethode.";
}
?>
