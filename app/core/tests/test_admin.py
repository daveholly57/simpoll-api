from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import gender, race, ethnicity, education, religion, \
                        politics, age, income, polideology, usregion, \
                        usstates


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@simpoll.org',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@simpoll.org',
            password='test123',
            name='Test User Full Name'
        )

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

    def test_users_listed(self):
        # Test that users are listed on user page.
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        # Test that the user edit page works.
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        # Test that the create user page works.
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
