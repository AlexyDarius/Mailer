def generate_success_php(directory_path, main_domain, website, full_body_tag):
    php_code = f'''<!DOCTYPE html>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <meta name="robots" content="noindex, nofollow">
    <title>{website} - Message envoyé</title>
</head>

{full_body_tag}

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <section style="margin-top: 24px;margin-bottom: 24px;">
        <div class="container">
            <div class="row">
                <div class="col-md-12" style="text-align: center;">
                    <h1 style="font-family: 'Lato-Bold', sans-serif;font-size: 48px;">Message envoyé avec succès !</h1>
                    <p><a class="btn ms-auto ms-md-2" role="button" data-bss-hover-animate="pulse" href="https://www.{main_domain}" style="background: var(--bs-secondary);color: var(--bs-body-bg);text-shadow: 0px 0px 8px var(--bs-black);">Revenir au site</a></p>
                </div>
            </div>
        </div>
    </section>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/mailer/success.php", "w") as php_file:
        php_file.write(php_code)
        print("success.php generated !")
