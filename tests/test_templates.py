from django.template.loader import render_to_string
from django.test import SimpleTestCase


class SuperSuperTests(SimpleTestCase):

    def test_super_super(self):
        rendered = render_to_string('top.html', {})
        self.assertIn('THIS IS VERY KEWL', rendered)

    def test_super(self):
        rendered = render_to_string('top.html', {})
        self.assertIn('not kewl12', rendered)

    def test_super_skipped(self):
        rendered = render_to_string('top.html', {})
        self.assertIn('not so kewl...', rendered)
