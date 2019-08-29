import yaml
from tests.utils.yapi import Yapi


class TestYandexTranslateApi:
    """ Yandex Translate Api test suite. """

    d = yaml.safe_load(open('../test_data.yml', encoding='utf-8'))  # Loading test data from 'test_data.yml'

    def test_positive_answer(self):
        """
        Yandex Translate Api returns positive answer test.
        """
        request = Yapi.get(self.d['text1_en'], self.d['lang'])
        assert 200 == request.status_code

    def test_api_returns_string(self):
        """
        Yandex Translate Api returns string test.
        """
        request = Yapi.get(self.d['text1_en'], self.d['lang'])
        assert type(request.text) == str

    def test_api_returns_non_empty_string(self):
        """
        Yandex Translate Api returns not empty string test.
        """
        request = Yapi.get(self.d['text1_en'], self.d['lang'])
        assert request.text != ""

    def test_api_returns_different_text(self):
        """
        Yandex Translate Api returned text, that not equal sent text.
        """
        request = Yapi.get(self.d['text1_en'], self.d['lang'])
        assert Yapi.get_returned_text(request) != self.d['text1_en']

    def test_translation_1(self):
        """
        Yandex Translate Api returns right translation of text1_en test.
        """
        request = Yapi.get(self.d['text1_en'], self.d['lang'])
        assert Yapi.get_returned_text(request) == self.d['text1_ru']

    def test_translation_2(self):
        """
        Yandex Translate Api returns right translation of text2_en test.
        """
        request = Yapi.get(self.d['text2_en'], self.d['lang'])
        assert Yapi.get_returned_text(request) == self.d['text2_ru']

    def test_sending_already_translated_text(self):
        """
        Sending already translated text to Yandex Translate Api test.
        """
        request = Yapi.get(self.d['text1_ru'], self.d['lang'])
        assert Yapi.get_returned_text(request) == self.d['text1_ru']

    def test_special_symbols(self):
        """
        Testing special symbols set translation.
        """
        request = Yapi.get(self.d['special_symbols'], self.d['lang'])
        assert Yapi.get_returned_text(request) == self.d['special_symbols']

    def test_sending_empty_string(self):
        """
        Sending empty string to Yandex Translate Api.
        """
        request = Yapi.get('', self.d['lang'])
        assert 400 == request.status_code
        assert Yapi.get_error_message(request) == 'Invalid parameter: text'

    def test_sending_wrong_api_key(self):
        """
        Sending wrong api-key to Yandex Translate Api.
        """
        request = Yapi.get(self.d['text1_en'],  self.d['lang'], api_key='Wrong_Api_Key')
        assert 403 == request.status_code
        assert Yapi.get_error_message(request) == 'API key is invalid'

    def test_sending_wrong_language(self):
        """
        Sending wrong language to Yandex Translate Api.
        """
        request = Yapi.get(self.d['text1_en'], 'Wrong_Language')
        assert 400 == request.status_code
        assert Yapi.get_error_message(request) == 'Invalid parameter: lang'

    def test_using_wrong_method(self):
        """
        Using wrong http request method for translation.
        """
        request = Yapi.fake_delete(self.d['text1_en'], self.d['lang'])
        assert 405 == request.status_code
        assert Yapi.get_error_message(request) == 'Method Not Allowed'

