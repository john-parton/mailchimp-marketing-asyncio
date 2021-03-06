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


class IndustryStats(object):
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
        'open_rate': 'float',
        'bounce_rate': 'float',
        'click_rate': 'float'
    }

    attribute_map = {
        'open_rate': 'open_rate',
        'bounce_rate': 'bounce_rate',
        'click_rate': 'click_rate'
    }

    def __init__(self, open_rate=None, bounce_rate=None, click_rate=None):  # noqa: E501
        """IndustryStats - a model defined in Swagger"""  # noqa: E501

        self._open_rate = None
        self._bounce_rate = None
        self._click_rate = None
        self.discriminator = None

        if open_rate is not None:
            self.open_rate = open_rate
        if bounce_rate is not None:
            self.bounce_rate = bounce_rate
        if click_rate is not None:
            self.click_rate = click_rate

    @property
    def open_rate(self):
        """Gets the open_rate of this IndustryStats.  # noqa: E501

        The average unique open rate for all campaigns in the account's specified industry.  # noqa: E501

        :return: The open_rate of this IndustryStats.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this IndustryStats.

        The average unique open rate for all campaigns in the account's specified industry.  # noqa: E501

        :param open_rate: The open_rate of this IndustryStats.  # noqa: E501
        :type: float
        """

        self._open_rate = open_rate

    @property
    def bounce_rate(self):
        """Gets the bounce_rate of this IndustryStats.  # noqa: E501

        The average bounce rate for all campaigns in the account's specified industry.  # noqa: E501

        :return: The bounce_rate of this IndustryStats.  # noqa: E501
        :rtype: float
        """
        return self._bounce_rate

    @bounce_rate.setter
    def bounce_rate(self, bounce_rate):
        """Sets the bounce_rate of this IndustryStats.

        The average bounce rate for all campaigns in the account's specified industry.  # noqa: E501

        :param bounce_rate: The bounce_rate of this IndustryStats.  # noqa: E501
        :type: float
        """

        self._bounce_rate = bounce_rate

    @property
    def click_rate(self):
        """Gets the click_rate of this IndustryStats.  # noqa: E501

        The average unique click rate for all campaigns in the account's specified industry.  # noqa: E501

        :return: The click_rate of this IndustryStats.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this IndustryStats.

        The average unique click rate for all campaigns in the account's specified industry.  # noqa: E501

        :param click_rate: The click_rate of this IndustryStats.  # noqa: E501
        :type: float
        """

        self._click_rate = click_rate

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
        if issubclass(IndustryStats, dict):
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
        if not isinstance(other, IndustryStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
