import factory
from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password

from accounts.models import MemberProfile, Account
from geo_id.models import GeoLocation


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GeoLocation

    id = factory.Sequence(lambda n: n+1)
    name = factory.Faker('city')
    parent = None


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('password'))
    is_active = True


class SuperUserFactory(UserFactory):
    class Meta:
        model = Account

    is_superuser = True
    is_staff = True


@factory.django.mute_signals(post_save)
class MemberProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MemberProfile

    phone_number = factory.Faker('phone_number')
    address = factory.Faker('address')
    location = factory.SubFactory(LocationFactory)
    account = factory.SubFactory("model_factory.factories.MemberUserFactory", profile=None)


@factory.django.mute_signals(post_save)
class MemberUserFactory(UserFactory):
    class Meta:
        model = Account

    is_member = True
    profile = factory.RelatedFactory(
        MemberProfileFactory,
        factory_related_name="account",
    )
