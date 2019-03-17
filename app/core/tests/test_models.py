from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import gender, race, ethnicity, education, religion, \
                        politics, age, income, polideology, usregion, \
                        usstates


def profile_gender(which='None'):
    # Find and return gender.
    return gender.objects.get(gender=which)


def profile_race(which='None'):
    # Find and return race.
    return race.objects.get(race=which)


def profile_ethnicity(which='None'):
    # Find and return ethnicity.
    return ethnicity.objects.get(ethnicity=which)


def profile_education(which='None'):
    # Find and return education.
    return education.objects.get(education=which)


def profile_religion(which='None'):
    # Find and return religion.
    return religion.objects.get(religion=which)


def profile_politics(which='None'):
    # Find and return politics.
    return politics.objects.get(politics=which)


def profile_age(which='None'):
    # Find and return age.
    return age.objects.get(age=which)


def profile_income(which='None'):
    # Find and return income.
    return income.objects.get(income=which)


def profile_polideology(which='None'):
    # Find and return polideology.
    return polideology.objects.get(politicalideology=which)


def profile_usregion(which='None'):
    # Find and return region.
    return usregion.objects.get(usregion=which)


def profile_usstate(which='NON-US LOCATION'):
    # Find and return state.
    return usstates.objects.get(usstate=which)


class ModelTests(TestCase):

    def setUp(self):
        # Preload all of the profile tables with their initial values.

        gender.objects.create(id=0, gender='None')
        gender.objects.create(id=1, gender='Male')
        gender.objects.create(id=2, gender='Female')
        gender.objects.create(id=3, gender='Trans')

        race.objects.create(id=0, race='None')
        race.objects.create(id=1, race='Alaskan Native')
        race.objects.create(id=2, race='Asian')
        race.objects.create(id=3, race='Black or African American')
        race.objects.create(id=4,
                            race='Native Hawaiian or Other Pacific Islander')
        race.objects.create(id=5, race='White')

        ethnicity.objects.create(id=0, ethnicity='None')
        ethnicity.objects.create(id=1, ethnicity='Hispanic or Latino')
        ethnicity.objects.create(id=2, ethnicity='Not Hispanic or Latino')

        education.objects.create(id=0, education='None')
        education.objects.create(id=1,
                                 education='Did not graduate High School')
        education.objects.create(id=2, education='High School Graduate')
        education.objects.create(id=3, education='Some College')
        education.objects.create(id=4, education='Associate Degree')
        education.objects.create(id=5, education='Bachlors Degree')
        education.objects.create(id=6, education='Masters Degree')
        education.objects.create(id=7, education='Professional Degree')
        education.objects.create(id=8, education='Doctorate')

        religion.objects.create(id=0, religion='None')
        religion.objects.create(id=1, religion='Unaffiliated')
        religion.objects.create(id=2, religion='Christianity')
        religion.objects.create(id=3, religion='Judiasm')
        religion.objects.create(id=4, religion='Islam')
        religion.objects.create(id=5, religion='Buddhism')
        religion.objects.create(id=6, religion='Hinduism')
        religion.objects.create(id=7, religion='Unitarian Universalism')
        religion.objects.create(id=8, religion='Wicca/Paganism/Druidry')

        age.objects.create(id=0, age='None')
        age.objects.create(id=1, age='Under 30')
        age.objects.create(id=2, age='30 to 39')
        age.objects.create(id=3, age='40 to 49')
        age.objects.create(id=4, age='50 to 59')
        age.objects.create(id=5, age='60 to 69')
        age.objects.create(id=6, age='70 to 79')
        age.objects.create(id=7, age='80 and older')

        politics.objects.create(id=0, politics='None')
        politics.objects.create(id=1, politics='Democrat')
        politics.objects.create(id=2, politics='Republican')
        politics.objects.create(id=3, politics='Libertarian')
        politics.objects.create(id=4, politics='Green')
        politics.objects.create(id=5, politics='Other')

        polideology.objects.create(id=0, politicalideology='None')
        polideology.objects.create(id=1, politicalideology='Conservatism')
        polideology.objects.create(id=2, politicalideology='Liberalism')
        polideology.objects.create(id=3, politicalideology='Libetarianism')
        polideology.objects.create(id=4, politicalideology='Socialism')
        polideology.objects.create(id=5, politicalideology='Communisim')
        polideology.objects.create(id=6, politicalideology='Anarchism')
        polideology.objects.create(id=7, politicalideology='Environmentalism')
        polideology.objects.create(id=8, politicalideology='Fascism')
        polideology.objects.create(id=9, politicalideology='Nationalism')

        income.objects.create(id=0, income='None')
        income.objects.create(id=1, income='$25K or less')
        income.objects.create(id=2, income='$25K to $50K')
        income.objects.create(id=3, income='$50K to $75K')
        income.objects.create(id=4, income='$75K to $100K')
        income.objects.create(id=5, income='$100K +')

        usregion.objects.create(id=0, usregion='None')
        usregion.objects.create(id=1, usregion='North East US')
        usregion.objects.create(id=2, usregion='South East US')
        usregion.objects.create(id=3, usregion='Mid West US')
        usregion.objects.create(id=4, usregion='South West US')
        usregion.objects.create(id=5, usregion='North West US')

        usstates.objects.create(id=0, usstate='NON-US LOCATION')
        usstates.objects.create(id=1, usstate='ALABAMA')
        usstates.objects.create(id=2, usstate='ALASKA')
        usstates.objects.create(id=3, usstate='ARIZONA')
        usstates.objects.create(id=4, usstate='ARKANSAS')
        usstates.objects.create(id=5, usstate='CALIFORNIA')
        usstates.objects.create(id=6, usstate='COLORADO')
        usstates.objects.create(id=7, usstate='CONNECTICUT')
        usstates.objects.create(id=8, usstate='DELAWARE')
        usstates.objects.create(id=9, usstate='FLORIDA')
        usstates.objects.create(id=10, usstate='GEORGIA')
        usstates.objects.create(id=11, usstate='HAWAII')
        usstates.objects.create(id=12, usstate='IDAHO')
        usstates.objects.create(id=13, usstate='ILLINOIS')
        usstates.objects.create(id=14, usstate='INDIANA')
        usstates.objects.create(id=15, usstate='IOWA')
        usstates.objects.create(id=16, usstate='KANSAS')
        usstates.objects.create(id=17, usstate='KENTUCKY')
        usstates.objects.create(id=18, usstate='LOUISIANA')
        usstates.objects.create(id=19, usstate='MAINE')
        usstates.objects.create(id=20, usstate='MARYLAND')
        usstates.objects.create(id=21, usstate='MASSACHUSETTS')
        usstates.objects.create(id=22, usstate='MICHIGAN')
        usstates.objects.create(id=23, usstate='MINNESOTA')
        usstates.objects.create(id=24, usstate='MISSISSIPPI')
        usstates.objects.create(id=25, usstate='MISSOURI')
        usstates.objects.create(id=26, usstate='MONTANA')
        usstates.objects.create(id=27, usstate='NEBRASKA')
        usstates.objects.create(id=28, usstate='NEVADA')
        usstates.objects.create(id=29, usstate='NEW HAMPSHIRE')
        usstates.objects.create(id=30, usstate='NEW JERSEY')
        usstates.objects.create(id=31, usstate='NEW MEXICO')
        usstates.objects.create(id=32, usstate='NEW YORK')
        usstates.objects.create(id=33, usstate='NORTH CAROLINA')
        usstates.objects.create(id=34, usstate='NORTH DAKOTA')
        usstates.objects.create(id=35, usstate='OHIO')
        usstates.objects.create(id=36, usstate='OKLAHOMA')
        usstates.objects.create(id=37, usstate='OREGON')
        usstates.objects.create(id=38, usstate='PENNSYLVANIA')
        usstates.objects.create(id=39, usstate='RHODE ISLAND')
        usstates.objects.create(id=40, usstate='SOUTH CAROLINA')
        usstates.objects.create(id=41, usstate='SOUTH DAKOTA')
        usstates.objects.create(id=42, usstate='TENNESSEE')
        usstates.objects.create(id=43, usstate='TEXAS')
        usstates.objects.create(id=44, usstate='UTAH')
        usstates.objects.create(id=45, usstate='VERMONT')
        usstates.objects.create(id=46, usstate='VIRGINIA')
        usstates.objects.create(id=47, usstate='WASHINGTON')
        usstates.objects.create(id=48, usstate='WEST VIRGINIA')
        usstates.objects.create(id=49, usstate='WISCONSIN')
        usstates.objects.create(id=50, usstate='WYOMING')
        usstates.objects.create(id=51, usstate='WASHINGTON DC')
        usstates.objects.create(id=52, usstate='PUERTO RICO')

    def test_create_user_with_email_successful(self):
        # Test creating a new user with an email is successful.
        email = 'test@simpoll.org'
        password = 'testpass123'
        gender = profile_gender(which='Female')
        race = profile_race(which='Asian')
        ethnicity = profile_ethnicity(which='Hispanic or Latino')
        education = profile_education(which='Bachlors Degree')
        religion = profile_religion(which='Christianity')
        politics = profile_politics(which='Republican')
        age = profile_age(which='60 to 69')
        income = profile_income(which='$100K +')
        polideology = profile_polideology(which='Conservatism')
        usregion = profile_usregion(which='North East US')
        usstate = profile_usstate(which='PENNSYLVANIA')
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            gender=gender,
            race=race,
            ethnicity=ethnicity,
            education=education,
            religion=religion,
            politics=politics,
            age=age,
            income=income,
            politicalideology=polideology,
            usregion=usregion,
            usstate=usstate
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.gender, gender)
        self.assertEqual(user.race, race)
        self.assertEqual(user.ethnicity, ethnicity)
        self.assertEqual(user.education, education)
        self.assertEqual(user.religion, religion)
        self.assertEqual(user.politics, politics)
        self.assertEqual(user.age, age)
        self.assertEqual(user.income, income)
        self.assertEqual(user.politicalideology, polideology)
        self.assertEqual(user.usstate, usstate)
        self.assertEqual(user.usregion, usregion)

    def test_new_user_email_normalized(self):
        # Test the email for a new user is normalized.
        email = 'test@simpoll.org'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email raises error.
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        # Test creating a new superuser.
        user = get_user_model().objects.create_superuser(
            'super@simpoll.org',
            'Test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
