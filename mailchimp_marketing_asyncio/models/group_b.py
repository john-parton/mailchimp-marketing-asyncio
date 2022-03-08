# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.74
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GroupB(object):
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
        'total_clicks_b': 'int',
        'click_percentage_b': 'float',
        'unique_clicks_b': 'int',
        'unique_click_percentage_b': 'float'
    }

    attribute_map = {
        'total_clicks_b': 'total_clicks_b',
        'click_percentage_b': 'click_percentage_b',
        'unique_clicks_b': 'unique_clicks_b',
        'unique_click_percentage_b': 'unique_click_percentage_b'
    }

    def __init__(self, total_clicks_b=None, click_percentage_b=None, unique_clicks_b=None, unique_click_percentage_b=None):  # noqa: E501
        """GroupB - a model defined in Swagger"""  # noqa: E501

        self._total_clicks_b = None
        self._click_percentage_b = None
        self._unique_clicks_b = None
        self._unique_click_percentage_b = None
        self.discriminator = None

        if total_clicks_b is not None:
            self.total_clicks_b = total_clicks_b
        if click_percentage_b is not None:
            self.click_percentage_b = click_percentage_b
        if unique_clicks_b is not None:
            self.unique_clicks_b = unique_clicks_b
        if unique_click_percentage_b is not None:
            self.unique_click_percentage_b = unique_click_percentage_b

    @property
    def total_clicks_b(self):
        """Gets the total_clicks_b of this GroupB.  # noqa: E501

        The total number of clicks for Group B.  # noqa: E501

        :return: The total_clicks_b of this GroupB.  # noqa: E501
        :rtype: int
        """
        return self._total_clicks_b

    @total_clicks_b.setter
    def total_clicks_b(self, total_clicks_b):
        """Sets the total_clicks_b of this GroupB.

        The total number of clicks for Group B.  # noqa: E501

        :param total_clicks_b: The total_clicks_b of this GroupB.  # noqa: E501
        :type: int
        """

        self._total_clicks_b = total_clicks_b

    @property
    def click_percentage_b(self):
        """Gets the click_percentage_b of this GroupB.  # noqa: E501

        The percentage of total clicks for Group B.  # noqa: E501

        :return: The click_percentage_b of this GroupB.  # noqa: E501
        :rtype: float
        """
        return self._click_percentage_b

    @click_percentage_b.setter
    def click_percentage_b(self, click_percentage_b):
        """Sets the click_percentage_b of this GroupB.

        The percentage of total clicks for Group B.  # noqa: E501

        :param click_percentage_b: The click_percentage_b of this GroupB.  # noqa: E501
        :type: float
        """

        self._click_percentage_b = click_percentage_b

    @property
    def unique_clicks_b(self):
        """Gets the unique_clicks_b of this GroupB.  # noqa: E501

        The number of unique clicks for Group B.  # noqa: E501

        :return: The unique_clicks_b of this GroupB.  # noqa: E501
        :rtype: int
        """
        return self._unique_clicks_b

    @unique_clicks_b.setter
    def unique_clicks_b(self, unique_clicks_b):
        """Sets the unique_clicks_b of this GroupB.

        The number of unique clicks for Group B.  # noqa: E501

        :param unique_clicks_b: The unique_clicks_b of this GroupB.  # noqa: E501
        :type: int
        """

        self._unique_clicks_b = unique_clicks_b

    @property
    def unique_click_percentage_b(self):
        """Gets the unique_click_percentage_b of this GroupB.  # noqa: E501

        The percentage of unique clicks for Group B.  # noqa: E501

        :return: The unique_click_percentage_b of this GroupB.  # noqa: E501
        :rtype: float
        """
        return self._unique_click_percentage_b

    @unique_click_percentage_b.setter
    def unique_click_percentage_b(self, unique_click_percentage_b):
        """Sets the unique_click_percentage_b of this GroupB.

        The percentage of unique clicks for Group B.  # noqa: E501

        :param unique_click_percentage_b: The unique_click_percentage_b of this GroupB.  # noqa: E501
        :type: float
        """

        self._unique_click_percentage_b = unique_click_percentage_b

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
        if issubclass(GroupB, dict):
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
        if not isinstance(other, GroupB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other