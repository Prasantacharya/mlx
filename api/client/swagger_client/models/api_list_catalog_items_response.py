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

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.25-related-assets
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiListCatalogItemsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'components': 'list[ApiComponent]',
        'datasets': 'list[ApiDataset]',
        'models': 'list[ApiModel]',
        'notebooks': 'list[ApiNotebook]',
        'pipelines': 'list[ApiPipeline]',
        'total_size': 'int',
        'next_page_token': 'str'
    }

    attribute_map = {
        'components': 'components',
        'datasets': 'datasets',
        'models': 'models',
        'notebooks': 'notebooks',
        'pipelines': 'pipelines',
        'total_size': 'total_size',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, components=None, datasets=None, models=None, notebooks=None, pipelines=None, total_size=None, next_page_token=None):  # noqa: E501
        """ApiListCatalogItemsResponse - a model defined in Swagger"""  # noqa: E501

        self._components = None
        self._datasets = None
        self._models = None
        self._notebooks = None
        self._pipelines = None
        self._total_size = None
        self._next_page_token = None
        self.discriminator = None

        if components is not None:
            self.components = components
        if datasets is not None:
            self.datasets = datasets
        if models is not None:
            self.models = models
        if notebooks is not None:
            self.notebooks = notebooks
        if pipelines is not None:
            self.pipelines = pipelines
        if total_size is not None:
            self.total_size = total_size
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def components(self):
        """Gets the components of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The components of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: list[ApiComponent]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ApiListCatalogItemsResponse.


        :param components: The components of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: list[ApiComponent]
        """

        self._components = components

    @property
    def datasets(self):
        """Gets the datasets of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The datasets of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: list[ApiDataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ApiListCatalogItemsResponse.


        :param datasets: The datasets of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: list[ApiDataset]
        """

        self._datasets = datasets

    @property
    def models(self):
        """Gets the models of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The models of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: list[ApiModel]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ApiListCatalogItemsResponse.


        :param models: The models of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: list[ApiModel]
        """

        self._models = models

    @property
    def notebooks(self):
        """Gets the notebooks of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The notebooks of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: list[ApiNotebook]
        """
        return self._notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        """Sets the notebooks of this ApiListCatalogItemsResponse.


        :param notebooks: The notebooks of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: list[ApiNotebook]
        """

        self._notebooks = notebooks

    @property
    def pipelines(self):
        """Gets the pipelines of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The pipelines of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: list[ApiPipeline]
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ApiListCatalogItemsResponse.


        :param pipelines: The pipelines of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: list[ApiPipeline]
        """

        self._pipelines = pipelines

    @property
    def total_size(self):
        """Gets the total_size of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The total_size of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ApiListCatalogItemsResponse.


        :param total_size: The total_size of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ApiListCatalogItemsResponse.  # noqa: E501


        :return: The next_page_token of this ApiListCatalogItemsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ApiListCatalogItemsResponse.


        :param next_page_token: The next_page_token of this ApiListCatalogItemsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiListCatalogItemsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiListCatalogItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
