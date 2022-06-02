@app.route('/generate-users/<int:number>')
def fake_email(number):
    with open('some.csv', 'w') as file:
        names = ['Name', 'E-mail']
        writer = csv.DictWriter(file, fieldnames=names)
        list_fake_name = []
        list_fake_email = []
        domain_name = ['gmail', 'yahoo']
        numbers = range(100)
        for _ in range(number):
            fake_first_and_last_name = fake.first_name()
            list_fake_name += [f'<p>{fake_first_and_last_name}']
            name = fake_first_and_last_name.lower()
            list_fake_email += [f'{name}_{choice(numbers)}@{choice(domain_name)}.com<p>']
        writer.writeheader()
        for each_fake_name in list_fake_name:
            for each_fake_email in list_fake_email:
                writer.writerow({"Name": each_fake_name, "E-mail": each_fake_email})
    with open('some.csv', 'r') as file:
        read = csv.DictReader(file)
        file_1 = []
        for row in read:
            file_1 += row['Name'], row['E-mail']
        file.close()
    return " ".join(file_1)