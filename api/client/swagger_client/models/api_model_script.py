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


class ApiModelScript(object):
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
        'pipeline_stage': 'str',
        'execution_platform': 'str',
        'script_code': 'str'
    }

    attribute_map = {
        'pipeline_stage': 'pipeline_stage',
        'execution_platform': 'execution_platform',
        'script_code': 'script_code'
    }

    def __init__(self, pipeline_stage=None, execution_platform=None, script_code=None):  # noqa: E501
        """ApiModelScript - a model defined in Swagger"""  # noqa: E501

        self._pipeline_stage = None
        self._execution_platform = None
        self._script_code = None
        self.discriminator = None

        self.pipeline_stage = pipeline_stage
        self.execution_platform = execution_platform
        self.script_code = script_code

    @property
    def pipeline_stage(self):
        """Gets the pipeline_stage of this ApiModelScript.  # noqa: E501

        pipeline stage that this code sample applies to, either 'train' or 'serve'  # noqa: E501

        :return: The pipeline_stage of this ApiModelScript.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_stage

    @pipeline_stage.setter
    def pipeline_stage(self, pipeline_stage):
        """Sets the pipeline_stage of this ApiModelScript.

        pipeline stage that this code sample applies to, either 'train' or 'serve'  # noqa: E501

        :param pipeline_stage: The pipeline_stage of this ApiModelScript.  # noqa: E501
        :type: str
        """
        if pipeline_stage is None:
            raise ValueError("Invalid value for `pipeline_stage`, must not be `None`")  # noqa: E501

        self._pipeline_stage = pipeline_stage

    @property
    def execution_platform(self):
        """Gets the execution_platform of this ApiModelScript.  # noqa: E501

        execution platform that this code sample applies to, i.e. 'kubernetes', 'knative'  # noqa: E501

        :return: The execution_platform of this ApiModelScript.  # noqa: E501
        :rtype: str
        """
        return self._execution_platform

    @execution_platform.setter
    def execution_platform(self, execution_platform):
        """Sets the execution_platform of this ApiModelScript.

        execution platform that this code sample applies to, i.e. 'kubernetes', 'knative'  # noqa: E501

        :param execution_platform: The execution_platform of this ApiModelScript.  # noqa: E501
        :type: str
        """
        if execution_platform is None:
            raise ValueError("Invalid value for `execution_platform`, must not be `None`")  # noqa: E501

        self._execution_platform = execution_platform

    @property
    def script_code(self):
        """Gets the script_code of this ApiModelScript.  # noqa: E501

        the source code to run the model in a pipeline stage  # noqa: E501

        :return: The script_code of this ApiModelScript.  # noqa: E501
        :rtype: str
        """
        return self._script_code

    @script_code.setter
    def script_code(self, script_code):
        """Sets the script_code of this ApiModelScript.

        the source code to run the model in a pipeline stage  # noqa: E501

        :param script_code: The script_code of this ApiModelScript.  # noqa: E501
        :type: str
        """
        if script_code is None:
            raise ValueError("Invalid value for `script_code`, must not be `None`")  # noqa: E501

        self._script_code = script_code

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
        if issubclass(ApiModelScript, dict):
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
        if not isinstance(other, ApiModelScript):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
