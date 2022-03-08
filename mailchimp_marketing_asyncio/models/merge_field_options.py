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


class MergeFieldOptions(object):
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
        'default_country': 'int',
        'phone_format': 'str',
        'date_format': 'str',
        'choices': 'list[str]',
        'size': 'int'
    }

    attribute_map = {
        'default_country': 'default_country',
        'phone_format': 'phone_format',
        'date_format': 'date_format',
        'choices': 'choices',
        'size': 'size'
    }

    def __init__(self, default_country=None, phone_format=None, date_format=None, choices=None, size=None):  # noqa: E501
        """MergeFieldOptions - a model defined in Swagger"""  # noqa: E501

        self._default_country = None
        self._phone_format = None
        self._date_format = None
        self._choices = None
        self._size = None
        self.discriminator = None

        if default_country is not None:
            self.default_country = default_country
        if phone_format is not None:
            self.phone_format = phone_format
        if date_format is not None:
            self.date_format = date_format
        if choices is not None:
            self.choices = choices
        if size is not None:
            self.size = size

    @property
    def default_country(self):
        """Gets the default_country of this MergeFieldOptions.  # noqa: E501

        In an address field, the default country code if none supplied.  # noqa: E501

        :return: The default_country of this MergeFieldOptions.  # noqa: E501
        :rtype: int
        """
        return self._default_country

    @default_country.setter
    def default_country(self, default_country):
        """Sets the default_country of this MergeFieldOptions.

        In an address field, the default country code if none supplied.  # noqa: E501

        :param default_country: The default_country of this MergeFieldOptions.  # noqa: E501
        :type: int
        """

        self._default_country = default_country

    @property
    def phone_format(self):
        """Gets the phone_format of this MergeFieldOptions.  # noqa: E501

        In a phone field, the phone number type: US or International.  # noqa: E501

        :return: The phone_format of this MergeFieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._phone_format

    @phone_format.setter
    def phone_format(self, phone_format):
        """Sets the phone_format of this MergeFieldOptions.

        In a phone field, the phone number type: US or International.  # noqa: E501

        :param phone_format: The phone_format of this MergeFieldOptions.  # noqa: E501
        :type: str
        """

        self._phone_format = phone_format

    @property
    def date_format(self):
        """Gets the date_format of this MergeFieldOptions.  # noqa: E501

        In a date or birthday field, the format of the date.  # noqa: E501

        :return: The date_format of this MergeFieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this MergeFieldOptions.

        In a date or birthday field, the format of the date.  # noqa: E501

        :param date_format: The date_format of this MergeFieldOptions.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def choices(self):
        """Gets the choices of this MergeFieldOptions.  # noqa: E501

        In a radio or dropdown non-group field, the available options for contacts to pick from.  # noqa: E501

        :return: The choices of this MergeFieldOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """Sets the choices of this MergeFieldOptions.

        In a radio or dropdown non-group field, the available options for contacts to pick from.  # noqa: E501

        :param choices: The choices of this MergeFieldOptions.  # noqa: E501
        :type: list[str]
        """

        self._choices = choices

    @property
    def size(self):
        """Gets the size of this MergeFieldOptions.  # noqa: E501

        In a text field, the default length of the text field.  # noqa: E501

        :return: The size of this MergeFieldOptions.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MergeFieldOptions.

        In a text field, the default length of the text field.  # noqa: E501

        :param size: The size of this MergeFieldOptions.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(MergeFieldOptions, dict):
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
        if not isinstance(other, MergeFieldOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other