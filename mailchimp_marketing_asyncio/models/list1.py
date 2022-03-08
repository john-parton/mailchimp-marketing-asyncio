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


class List1(object):
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
        'list_id': 'str',
        'store_id': 'str'
    }

    attribute_map = {
        'list_id': 'list_id',
        'store_id': 'store_id'
    }

    def __init__(self, list_id=None, store_id=None):  # noqa: E501
        """List1 - a model defined in Swagger"""  # noqa: E501

        self._list_id = None
        self._store_id = None
        self.discriminator = None

        if list_id is not None:
            self.list_id = list_id
        if store_id is not None:
            self.store_id = store_id

    @property
    def list_id(self):
        """Gets the list_id of this List1.  # noqa: E501

        The id of the List.  # noqa: E501

        :return: The list_id of this List1.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this List1.

        The id of the List.  # noqa: E501

        :param list_id: The list_id of this List1.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def store_id(self):
        """Gets the store_id of this List1.  # noqa: E501

        The id of the store.  # noqa: E501

        :return: The store_id of this List1.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this List1.

        The id of the store.  # noqa: E501

        :param store_id: The store_id of this List1.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

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
        if issubclass(List1, dict):
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
        if not isinstance(other, List1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other