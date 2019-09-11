import yaml
from tests.utils.yapi import YAPI


class TestYandexTranslateAPI:
    """ Yandex Translate API test suite. """

    d = yaml.safe_load(open('../test_data.yml', encoding='utf-8'))  # Loading test data from 'test_data.yml'

    def test_translation_text1_en_ru(self):
        """
        Yandex Translate API returns correct en-ru translation of text1_en.
        """
        response = YAPI.get(self.d['text1_en'], 'en-ru')
        assert YAPI.get_returned_text(response) == self.d['text1_ru']

    def test_translation_text1_ru_en(self):
        """
        Yandex Translate API returns correct ru-en translation of text1_ru.
        """
        response = YAPI.get(self.d['text1_ru'], 'ru-en')
        assert YAPI.get_returned_text(response) == self.d['text1_en']

    def test_translation_text2_en_ru(self):
        """
        Yandex Translate API returns correct en-ru translation of text2_en.
        """
        response = YAPI.get(self.d['text2_en'], 'en-ru')
        assert YAPI.get_returned_text(response) == self.d['text2_ru']

    def test_translation_text2_ru_en(self):
        """
        Yandex Translate API returns correct ru-en translation of text2_ru.
        """
        response = YAPI.get(self.d['text2_ru'], 'ru-en')
        assert YAPI.get_returned_text(response) == self.d['text2_en']

    def test_sending_already_translated_rus_text_for_en_ru_translation(self):
        """
        Sending already translated russian text for english-russian translation.
        """
        response = YAPI.get(self.d['text1_ru'], 'en-ru')
        assert YAPI.get_returned_text(response) == self.d['text1_ru']

    def test_sending_special_symbols_set(self):
        """
        Sending full keyboard special symbols set for en-ru translation.
        Yandex Translate API shouldn't do something with special symbols.
        """
        response = YAPI.get(self.d['special_symbols'], 'en-ru')
        assert YAPI.get_returned_text(response) == self.d['special_symbols']

    def test_sending_empty_string(self):
        """
        Sending empty string for translation.
        """
        response = YAPI.get('', 'en-ru')
        assert 400 == response.status_code
        assert YAPI.get_error_message(response) == 'Invalid parameter: text'

    def test_sending_wrong_api_key(self):
        """
        Using wrong API-Key.
        """
        response = YAPI.get(self.d['text1_en'], 'en-ru', api_key='Wrong_Api_Key')
        assert 403 == response.status_code
        assert YAPI.get_error_message(response) == 'API key is invalid'

    def test_sending_wrong_language_parameter(self):
        """
        Using wrong language parameter.
        """
        response = YAPI.get(self.d['text1_en'], 'Wrong_Language')
        assert 400 == response.status_code
        assert YAPI.get_error_message(response) == 'Invalid parameter: lang'

    def test_wrong_request_method(self):
        """
        Using wrong http request method for translation.
        """
        response = YAPI.fake_delete_request(self.d['text1_en'], 'en-ru')
        assert 405 == response.status_code
        assert YAPI.get_error_message(response) == 'Method Not Allowed'

