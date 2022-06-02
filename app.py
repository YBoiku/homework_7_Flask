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
        list_fake_email = []
        domain_name = ['gmail', 'yahoo']
        numbers = range(100)
        for _ in range(number):
            fake_first_and_last_name = fake.first_name()
            name = fake_first_and_last_name.lower()
            list_fake_email += [{"Name": f'<p>{fake_first_and_last_name}: ',
                                 "E-mail": f'{name}_{choice(numbers)}@{choice(domain_name)}.com</p>'}]
        writer.writeheader()
        for each_fake_name in list_fake_email:
            writer.writerow(each_fake_name)
    with open('some.csv', 'r') as file:
        read = csv.DictReader(file)
        file_1 = []
        for row in read:
            file_1 += row['Name'], row['E-mail']
        file.close()
    return " ".join(file_1)


if __name__ == '__main__':
    app.run()
