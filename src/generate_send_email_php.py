def generate_send_email_php(directory_path, main_domain, mail):
    php_code = f'''<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {{
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Set up email headers
    $to = "{mail}"; // Replace with your email address
    $subject = "Nouveau message sur {main_domain} !";
    $headers = "From: " . $email . "\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    // Compose the email body (you can use HTML here)
    $email_body = "<h1>Nouveau message sur {main_domain} !</h1>";
    $email_body .= "<p>Nom: " . $name . "</p>";
    $email_body .= "<p>Email: " . $email . "</p>";
    $email_body .= "<p>Message: " . $message . "</p>";

    // Send the email
    if (mail($to, $subject, $email_body, $headers)) {{
        header('Location: https://www.{main_domain}/modules/mailer/success.php');
        exit;
        echo "Email sent successfully!";
    }} else {{
        header('Location: https://www.{main_domain}/modules/mailer/fail.php');
        exit;
        echo "Failed to send email. Please try again later.";
    }}
}}
?>
'''

    with open(f"{directory_path}/mailer/send-email.php.php", "w") as php_file:
        php_file.write(php_code)
        print("send-email.php generated !")
