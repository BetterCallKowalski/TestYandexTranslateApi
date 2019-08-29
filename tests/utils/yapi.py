import yaml
import json
import requests


class Yapi:
    """
    Tools for working with Yandex Translate Api.
    """
    api_conf = yaml.safe_load(open('../api_config.yml', encoding='utf-8'))

    @staticmethod
    def get(text, lang, api_key=api_conf['api-key']):
        """
        Sending http GET reguest to Yandex Translate Api.
        """
        text = text
        lang = lang
        api_key = api_key

        params = {'key': api_key, 'lang': lang, 'text': text}
        request = requests.get(Yapi.api_conf['api-url'], params=params)

        return request

    @staticmethod
    def fake_delete(text, lang, api_key=api_conf['api-key']):
        """
        Sending http fake DELETE reguest to Yandex Translate Api.
        """
        text = text
        lang = lang
        api_key = api_key

        params = {'key': api_key, 'lang': lang, 'text': text}
        request = requests.delete(Yapi.api_conf['api-url'], params=params)

        return request

    @staticmethod
    def get_returned_text(api_response):
        """
        Getting returned text from Yandex Translate Api response.
        """
        response = api_response

        returned_json = json.loads(response.text)
        returned_text = returned_json['text'][0]

        return returned_text

    @staticmethod
    def get_error_message(api_response):
        """
        Getting returned error message Yandex Translate Api response.
        """
        response = api_response

        assert 400 <= response.status_code

        returned_json = json.loads(response.text)
        returned_error_message = returned_json['message']

        return returned_error_message

