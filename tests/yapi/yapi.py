import json
import requests


class YAPI:
    """
    Tools for working with Yandex Translate API.
    """
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get(self, text, lang, api_key=None):
        """
        Sending http GET reguest to Yandex Translate API.
        """
        text = text
        lang = lang
        if api_key is None:
            api_key = self.api_key
        
        params = {'key': api_key, 'lang': lang, 'text': text}
        response = requests.get(self.api_url, params=params)

        return response

    def get_returned_text(self, api_response):
        """
        Getting returned text from Yandex Translate API response.
        """
        response = api_response
        assert 200 == response.status_code
        
        returned_json = json.loads(response.text)
        returned_text = returned_json['text'][0]

        return returned_text

    def get_error_message(self, api_response):
        """
        Getting returned error message Yandex Translate API response.
        """
        response = api_response

        assert 400 <= response.status_code

        returned_json = json.loads(response.text)
        returned_error_message = returned_json['message']

        return returned_error_message

    def fake_delete_request(self, text, lang, api_key=None):
        """
        Sending http fake DELETE reguest to Yandex Translate API.
        """
        text = text
        lang = lang
        if api_key is None:
            api_key = self.api_key

        params = {'key': api_key, 'lang': lang, 'text': text}
        response = requests.delete(self.api_url, params=params)

        return response
