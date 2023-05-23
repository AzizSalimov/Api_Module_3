import factory


class ParentCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Category'

    name = factory.Faker("word")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.Category'

    name = factory.Faker("word")
    parent = factory.SubFactory(ParentCategoryFactory)


