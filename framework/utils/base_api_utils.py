import requests
from requests import Response

from framework.logger.logger import Logger


class BaseApiRequests:

    @staticmethod
    def get(url: str) -> Response:
        """
        :param url: url value
        :return: get api method response
        """
        response = requests.get(url)
        Logger.get_log().info(f"Send 'GET' request to {url}")
        Logger.get_log().info(f"Get response with status code: {response.status_code}")
        return response

    @staticmethod
    def post(url: str, **kwargs) -> Response:
        """
        :param url:
        :param kwargs: data for post api method
        :return: post api method response
        """
        response = requests.post(url, **kwargs)
        Logger.get_log().info(f"Send 'POST' request to {url} with kwargs={kwargs}")
        Logger.get_log().info(f"Get response with status code: {response.status_code}")
        return response
