from django.conf import settings
from django.test import TestCase

class ShortcutTests(TestCase):
    def setUp(self):
        self.old_STATIC_URL = settings.STATIC_URL
        self.old_TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS

        settings.STATIC_URL = '/path/to/static/media'
        settings.TEMPLATE_CONTEXT_PROCESSORS = (
            'django.core.context_processors.static'
        )

    def tearDown(self):
        settings.STATIC_URL = self.old_STATIC_URL
        settings.TEMPLATE_CONTEXT_PROCESSORS = self.old_TEMPLATE_CONTEXT_PROCESSORS

    def test_render_to_response(self):
        response = self.client.get('/views/shortcuts/render_to_response/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR..\n')
        self.assertEquals(response['Content-Type'], 'text/html; charset=utf-8')

    def test_render_to_response_with_request_context(self):
        response = self.client.get('/views/shortcuts/render_to_response/request_context/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR../path/to/static/media\n')
        self.assertEquals(response['Content-Type'], 'text/html; charset=utf-8')

    def test_render_to_response_with_mimetype(self):
        response = self.client.get('/views/shortcuts/render_to_response/mimetype/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR..\n')
        self.assertEquals(response['Content-Type'], 'application/x-rendertest')

    def test_render(self):
        response = self.client.get('/views/shortcuts/render/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR../path/to/static/media\n')
        self.assertEquals(response['Content-Type'], 'text/html; charset=utf-8')

    def test_render_with_base_context(self):
        response = self.client.get('/views/shortcuts/render/base_context/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR..\n')
        self.assertEquals(response['Content-Type'], 'text/html; charset=utf-8')

    def test_render_with_mimetype(self):
        response = self.client.get('/views/shortcuts/render/mimetype/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'FOO.BAR../path/to/static/media\n')
        self.assertEquals(response['Content-Type'], 'application/x-rendertest')

