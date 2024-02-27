import tkinter as tk
from tkinter import filedialog
from generate_arbo import generate_arbo
from generate_send_email_php import generate_send_email_php
from generate_success_php import generate_success_php
from generate_fail_php import generate_fail_php
from generate_form_php import generate_form_php

def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()
    mail = mail_entry.get()
    full_body_tag = full_body_tag_entry.get("1.0", "end-1c")

    parts = main_domain.split(".")
    website = parts[0]

    if all([directory_path, main_domain, mail, full_body_tag]):
        # Generate tree path
        generate_arbo(directory_path)
        generate_send_email_php(directory_path, main_domain, mail)
        generate_success_php(directory_path, main_domain, website, full_body_tag)
        generate_fail_php(directory_path, main_domain, website, full_body_tag, mail)
        generate_form_php(directory_path)
        
        result_label.config(text="Mailer files have been generated.")

        print("Mailer files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

app = tk.Tk()
app.title("DariusDev Mailer Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

main_domain_label = tk.Label(app, text="Enter the main domain (e.g. dariusdev.fr, without www. !) :")
main_domain_label.pack()
main_domain_entry = tk.Entry(app)
main_domain_entry.pack()

mail_label = tk.Label(app, text="Enter the destination mail for the form (e.g. contact@dariusdev.fr) :")
mail_label.pack()
mail_entry = tk.Entry(app)
mail_entry.pack()

full_body_tag_label = tk.Label(app, text="Full Body tag (e.g. <body style=...>) :")
full_body_tag_label.pack()
full_body_tag_entry = tk.Text(app, width=50, height=5)
full_body_tag_entry.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
