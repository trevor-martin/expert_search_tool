from django.test import TestCase
from expert_search.models import Expert, Friendships

class ExpertTestCase(TestCase):

    def setUp(self):
        pass

    def test001(self):
        self.assertEquals(1, 1)


class FriendshipsTestCase(TestCase):

    def setUp(self):
        pass

    def test002(self):
        self.assertEquals(2, 2)
