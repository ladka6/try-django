import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','deneme_proje.settings')

import django
django.setup()


from deneme_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N = 5):

    for people in range(N):

        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_name = fake_name.split(' ')
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]

        usr = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating complete")
