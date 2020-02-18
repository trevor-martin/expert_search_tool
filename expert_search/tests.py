from django.test import TestCase
from expert_search.models import Expert, Friendships

class ExpertTestCase(TestCase):

    def setUp(self):
        Expert.objects.create(name='expert001', personal_website_url='website001', shortened_personal_website_url='web001')
        Expert.objects.create(name='expert002', personal_website_url='website002', shortened_personal_website_url='web002')

    def test_expert_creation(self):
        expert = Expert.objects.get(name='expert001')
        
        self.assertEquals(expert.personal_website_url, 'website001')


class FriendshipsTestCase(TestCase):

    def setUp(self):
        Friendships.objects.create(expert_id_001=1, expert_id_002=2)

    def test_friendship_creation(self):
        friendship = Friendships.objects.get(expert_id_001=1)

        self.assertEquals(friendship.expert_id_001, 1)
        self.assertEquals(friendship.expert_id_002, 2)
