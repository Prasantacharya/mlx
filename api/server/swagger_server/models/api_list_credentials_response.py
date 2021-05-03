# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.api_credential import ApiCredential  # noqa: F401,E501
from swagger_server import util


class ApiListCredentialsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, credentials: List[ApiCredential]=None, total_size: int=None, next_page_token: str=None):  # noqa: E501
        """ApiListCredentialsResponse - a model defined in Swagger

        :param credentials: The credentials of this ApiListCredentialsResponse.  # noqa: E501
        :type credentials: List[ApiCredential]
        :param total_size: The total_size of this ApiListCredentialsResponse.  # noqa: E501
        :type total_size: int
        :param next_page_token: The next_page_token of this ApiListCredentialsResponse.  # noqa: E501
        :type next_page_token: str
        """
        self.swagger_types = {
            'credentials': List[ApiCredential],
            'total_size': int,
            'next_page_token': str
        }

        self.attribute_map = {
            'credentials': 'credentials',
            'total_size': 'total_size',
            'next_page_token': 'next_page_token'
        }

        self._credentials = credentials
        self._total_size = total_size
        self._next_page_token = next_page_token

    @classmethod
    def from_dict(cls, dikt) -> 'ApiListCredentialsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiListCredentialsResponse of this ApiListCredentialsResponse.  # noqa: E501
        :rtype: ApiListCredentialsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credentials(self) -> List[ApiCredential]:
        """Gets the credentials of this ApiListCredentialsResponse.


        :return: The credentials of this ApiListCredentialsResponse.
        :rtype: List[ApiCredential]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials: List[ApiCredential]):
        """Sets the credentials of this ApiListCredentialsResponse.


        :param credentials: The credentials of this ApiListCredentialsResponse.
        :type credentials: List[ApiCredential]
        """

        self._credentials = credentials

    @property
    def total_size(self) -> int:
        """Gets the total_size of this ApiListCredentialsResponse.


        :return: The total_size of this ApiListCredentialsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size: int):
        """Sets the total_size of this ApiListCredentialsResponse.


        :param total_size: The total_size of this ApiListCredentialsResponse.
        :type total_size: int
        """

        self._total_size = total_size

    @property
    def next_page_token(self) -> str:
        """Gets the next_page_token of this ApiListCredentialsResponse.


        :return: The next_page_token of this ApiListCredentialsResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token: str):
        """Sets the next_page_token of this ApiListCredentialsResponse.


        :param next_page_token: The next_page_token of this ApiListCredentialsResponse.
        :type next_page_token: str
        """

        self._next_page_token = next_page_token
