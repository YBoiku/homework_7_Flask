from flask import Flask
from faker import Faker
from random import choice
import csv

fake = Faker()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Aleksanr, it\'s my homework'


@app.route('/requirements')
def requirements():
    with open('anacondaz.txt', 'r') as file:
        song = str(file.read())
        song_1 = song.split('\n')
        return "<p>".join(song_1)


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
            fake_name = []
            fake_first_and_last_name = fake.name()
            fake_name += [''.join(fake_first_and_last_name.split(' ')[0])]
            list_fake_name.append(fake_name)
            for each_name in fake_name:
                name = each_name.lower()
                create_fake_email = []
                create_fake_email += [f'{name}_{choice(numbers)}@{choice(domain_name)}.com']
                list_fake_email.append(create_fake_email)
        writer.writeheader()
        for each_fake_name in list_fake_name:
            for each_fake_email in list_fake_email:
                writer.writerow({"Name": each_fake_name, "E-mail": each_fake_email})
    with open('some.csv', 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            file_1 = []
            file_1 += row['Name'], row['E-mail']
    return " ".join(file_1)


if __name__ == '__main__':
    app.run()
