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


class Body2(object):
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
        'test_emails': 'list[str]',
        'send_type': 'str'
    }

    attribute_map = {
        'test_emails': 'test_emails',
        'send_type': 'send_type'
    }

    def __init__(self, test_emails=None, send_type=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501

        self._test_emails = None
        self._send_type = None
        self.discriminator = None

        self.test_emails = test_emails
        self.send_type = send_type

    @property
    def test_emails(self):
        """Gets the test_emails of this Body2.  # noqa: E501

        An array of email addresses to send the test email to.  # noqa: E501

        :return: The test_emails of this Body2.  # noqa: E501
        :rtype: list[str]
        """
        return self._test_emails

    @test_emails.setter
    def test_emails(self, test_emails):
        """Sets the test_emails of this Body2.

        An array of email addresses to send the test email to.  # noqa: E501

        :param test_emails: The test_emails of this Body2.  # noqa: E501
        :type: list[str]
        """
        if test_emails is None:
            raise ValueError("Invalid value for `test_emails`, must not be `None`")  # noqa: E501

        self._test_emails = test_emails

    @property
    def send_type(self):
        """Gets the send_type of this Body2.  # noqa: E501

        Choose the type of test email to send.  # noqa: E501

        :return: The send_type of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._send_type

    @send_type.setter
    def send_type(self, send_type):
        """Sets the send_type of this Body2.

        Choose the type of test email to send.  # noqa: E501

        :param send_type: The send_type of this Body2.  # noqa: E501
        :type: str
        """
        if send_type is None:
            raise ValueError("Invalid value for `send_type`, must not be `None`")  # noqa: E501
        allowed_values = ["html", "plaintext"]  # noqa: E501
        if send_type not in allowed_values:
            raise ValueError(
                "Invalid value for `send_type` ({0}), must be one of {1}"  # noqa: E501
                .format(send_type, allowed_values)
            )

        self._send_type = send_type

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
        if issubclass(Body2, dict):
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
        if not isinstance(other, Body2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
