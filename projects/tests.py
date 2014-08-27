from django.core.urlresolvers import resolve
from django.test import TestCase


class HomePageTest(TestCase):

    def test_root_url_resolves_to_projects_index(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'projects:index')
