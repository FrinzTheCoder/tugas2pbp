from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_html, show_xml, show_json

class TestUrls(SimpleTestCase):

    def test_show_mywatchlist_html(self):
        url = reverse('show_html')
        self.assertEquals(resolve(url).func, show_html)

    def test_show_mywatchlist_xml(self):
        url = reverse('show_xml')
        self.assertEquals(resolve(url).func, show_xml)

    def test_show_mywatchlist_json(self):
        url = reverse('show_json')
        self.assertEquals(resolve(url).func, show_json)

    



# acknowledgment: https://www.youtube.com/watch?v=0MrgsYswT1c