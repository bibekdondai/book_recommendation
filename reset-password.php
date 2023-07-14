<?php
session_start();

// Function to send the verification code to the user's email address
function sendVerificationCode($email, $code) {
    // SMTP configuration
    $smtpHost = 'smtp.example.com';
    $smtpPort = 587;
    $smtpUsername = 'bibekp8000@gmail.com'; // Replace with your email address
    $smtpPassword = 'your_password'; // Replace with your email password

    // Create a message
    $subject = 'Reset Password Verification Code';
    $message = "Your verification code is: " . $code;

    // Set additional headers
    $headers = "From: $smtpUsername" . "\r\n";
    $headers .= "Reply-To: $smtpUsername" . "\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    // Send the email
    mail($email, $subject, $message, $headers);
}

// Function to generate a random verification code
function generateVerificationCode() {
    // Generate a random code (e.g., 6 digits)
    return rand(100000, 999999);
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the submitted email address
    $email = $_POST["email"];

    // Generate a verification code
    $code = generateVerificationCode();

    // Store the verification code in a session variable
    $_SESSION["verification_code"] = $code;

    // Send the verification code to the user's email address
    sendVerificationCode($email, $code);

    // Redirect the user to a separate PHP file where they can enter the verification code
    header("Location: verify_code.php");
    exit();
}
?>


