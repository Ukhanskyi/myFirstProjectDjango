from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import posts_list, post_detail, tags_list, tag_detail


class TestUrls(SimpleTestCase):

    def test_posts_list_url_is_resolved(self):
        url = reverse('posts_list_url')
        self.assertEquals(resolve(url).func, posts_list)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail_url', args=['some-slug'])
        self.assertEquals(resolve(url).func, post_detail)

    def test_tags_list_url_is_resolved(self):
        url = reverse('tags_list_url')
        self.assertEquals(resolve(url).func, tags_list)

    def test_tag_detail_url_is_resolved(self):
        url = reverse('tag_detail_url', args=['some-slug'])
        self.assertEquals(resolve(url).func, tag_detail)
