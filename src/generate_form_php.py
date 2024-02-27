def generate_form_php(directory_path):
    php_code = f'''<section class="position-relative" style="margin-top: 24px;margin-bottom: 12px;">
    <div class="container position-relative">
        <div class="row" style="margin-bottom: 6px;">
            <div class="col d-flex justify-content-center">
                <h2 style="font-family: Lato-Bold;">Écrivez-nous via ce formulaire</h2>
            </div>
        </div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                <div class="card" style="border-width: 4px;border-color: var(--bs-primary);border-radius: 12px;margin-bottom: 12px;">
                    <div class="card-body p-sm-5">
                        <h3 class="text-center mb-4" style="font-family: Lato-Bold;">Écrivez-nous ici</h3>
                        <form method="post">
                            <div class="mb-3"><input class="form-control" type="text" id="name-2" name="name" placeholder="Nom" style="color: var(--bs-primary);"></div>
                            <div class="mb-3"><input class="form-control" type="email" id="email-2" name="email" placeholder="Email" style="color: var(--bs-primary);"></div>
                            <div class="mb-3"><textarea class="form-control" id="message-2" name="message" rows="6" placeholder="Message" style="color: var(--bs-primary);"></textarea></div>
                            <div><button class="btn d-block w-100" type="submit" style="background: var(--bs-secondary);color: var(--bs-body-bg);text-shadow: 0px 0px 8px var(--bs-black);">Envoyer</button></div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
'''

    with open(f"{directory_path}/form.php", "w") as php_file:
        php_file.write(php_code)
        print("form.php generated !")
