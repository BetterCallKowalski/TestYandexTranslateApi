import requests
import json


class TestYandexTranslateApiSimple:
    """ Yandex Translate Api test suite for en-ru translation. """

    text1_en = 'cat'
    text1_ru = 'кошка'
    text2_en = 'London is the capital of great Britain'
    text2_ru = 'Лондон является столицей Великобритании'
    special_symbols = '~`!@#$%^&*()_+-={}[]\\|:;\'"<>,.?/'
    lang = 'en-ru'
    api_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    api_key = 'Enter-Your-Yandex-Translate-Api-Key-Here'

    def test_positive_answer(self):
        """
        Yandex Translate Api returns positive answer test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        assert 200 == request.status_code

    def test_api_returns_string(self):
        """
        Yandex Translate Api returns string test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        assert type(request.text) == str

    def test_api_returns_non_empty_string(self):
        """
        Yandex Translate Api returns not empty string test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        assert request.text != ""

    def test_api_returns_different_text(self):
        """
        Yandex Translate Api returned text, that not equal sent text.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        returned_json = json.loads(request.text)
        returned_text = returned_json['text'][0]
        assert returned_text != self.text1_en

    def test_translation_1(self):
        """
        Yandex Translate Api returns right translation of text1_en test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        returned_json = json.loads(request.text)
        returned_text = returned_json['text'][0]
        assert returned_text == self.text1_ru

    def test_translation_2(self):
        """
        Yandex Translate Api returns right translation of text2_en test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text2_en}

        request = requests.get(self.api_url, params=params)
        returned_json = json.loads(request.text)
        returned_text = returned_json['text'][0]
        assert returned_text == self.text2_ru

    def test_sending_already_translated_text(self):
        """
        Sending already translated text to Yandex Translate Api test.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_ru}

        request = requests.get(self.api_url, params=params)
        returned_json = json.loads(request.text)
        returned_text = returned_json['text'][0]
        assert returned_text == self.text1_ru

    def test_special_symbols(self):
        """
        Testing special symbols set translation.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.special_symbols}

        request = requests.get(self.api_url, params=params)
        returned_json = json.loads(request.text)
        returned_text = returned_json['text'][0]
        assert returned_text == self.special_symbols

    def test_sending_empty_string(self):
        """
        Sending empty string to Yandex Translate Api.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': ''}

        request = requests.get(self.api_url, params=params)
        assert 400 == request.status_code

        returned_json = json.loads(request.text)
        returned_error_message = returned_json['message']
        assert returned_error_message == 'Invalid parameter: text'

    def test_sending_wrong_api_key(self):
        """
        Sending wrong api-key to Yandex Translate Api.
        """
        params = {'key': 'this-is-not-key', 'lang': self.lang, 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        assert 403 == request.status_code

        returned_json = json.loads(request.text)
        returned_error_message = returned_json['message']
        assert returned_error_message == 'API key is invalid'

    def test_sending_wrong_language(self):
        """
        Sending wrong language to Yandex Translate Api.
        """
        params = {'key': self.api_key, 'lang': 'this-is-not-real-lang', 'text': self.text1_en}

        request = requests.get(self.api_url, params=params)
        assert 400 == request.status_code

        returned_json = json.loads(request.text)
        returned_error_message = returned_json['message']
        assert returned_error_message == 'Invalid parameter: lang'

    def test_using_wrong_method(self):
        """
        Using wrong http request method for translation.
        """
        params = {'key': self.api_key, 'lang': self.lang, 'text': self.text1_ru}

        request = requests.delete(self.api_url, params=params)
        assert 405 == request.status_code

        returned_json = json.loads(request.text)
        returned_error_message = returned_json['message']
        assert returned_error_message == 'Method Not Allowed'
