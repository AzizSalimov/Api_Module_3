import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from django.db import transaction

from api.models import Category


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n + 1}')


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    owner = factory.SubFactory(UserFactory)


@transaction.atomic
def create_categories():
    for _ in range(10000):
        CategoryFactory.create()


# Call the create_categories function to create and save 1000 instances of Category
create_categories()
