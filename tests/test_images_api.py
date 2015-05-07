import sys
import os
import unittest
import requests

from threading import Thread
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from twisted_test import app


WARMUP_TIMEOUT = 2
UNKNOWN_IMAGE_ID = 'fake-image-id'
PORT = 9090


def get_url(url):
    return 'http://127.0.0.1:{port}/{url}'.format(
        port=PORT,
        url=url.lstrip('/')
    )


class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thread = Thread(target=app.start, args=[PORT])
        thread.daemon = True
        thread.start()
        sleep(WARMUP_TIMEOUT)

    @classmethod
    def tearDownClass(cls):
        app.stop()

    def test_get_static_files(self):
        response = requests.get(get_url('/index.html'))
        self.assertEqual(response.status_code, 200)

    def test_get_unknown_image(self):
        response = requests.get(
            get_url('/api/images/get/{}'.format(UNKNOWN_IMAGE_ID))
        )
        self.assertEqual(response.status_code, 404)

    def test_get_images(self):
        for extension in ('png', 'jpeg', 'bmp', 'gif'):
            path_to_image = self._get_image_path(extension)
            image_id = self._add_new_image(path_to_image)

            response = requests.get(
                get_url('/api/images/get/{}'.format(image_id))
            )
            self.assertEqual(response.status_code, 200)
            
    def test_get_flipped_images(self):
        for extension in ('png', 'jpeg', 'bmp', 'gif'):
            path_to_image = self._get_image_path(extension)
            image_id = self._add_new_image(path_to_image)

            response = requests.get(
                get_url('/api/images/get/{}/flip'.format(image_id))
            )
            self.assertEqual(response.status_code, 200)

            
    def _get_image_path(self, extension):
            return os.path.join(
                os.path.dirname(__file__),
                'samples',
                'sample_1.{}'.format(extension)
            )

    def _add_new_image(self, path_to_image):
        response = requests.post(
            get_url('/api/images/add'),
            files={'image': open(path_to_image, 'rb')}
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn('success', response.json)
        self.assertEqual(True, response.json['success'])

        self.assertIn('data', response.json)
        self.assertIn('id', response.json['data'])
        image_id = response.json['data']['id']
        
        return image_id


if __name__ == '__main__':
    unittest.main()
