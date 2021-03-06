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


class CollectionOfMemberActivityEvents(object):
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
        'goals': 'list[Goal]',
        'list_id': 'str',
        'email_id': 'str',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'goals': 'goals',
        'list_id': 'list_id',
        'email_id': 'email_id',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, goals=None, list_id=None, email_id=None, total_items=None, links=None):  # noqa: E501
        """CollectionOfMemberActivityEvents - a model defined in Swagger"""  # noqa: E501

        self._goals = None
        self._list_id = None
        self._email_id = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if goals is not None:
            self.goals = goals
        if list_id is not None:
            self.list_id = list_id
        if email_id is not None:
            self.email_id = email_id
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def goals(self):
        """Gets the goals of this CollectionOfMemberActivityEvents.  # noqa: E501

        The last 50 Goal events triggered by a member.  # noqa: E501

        :return: The goals of this CollectionOfMemberActivityEvents.  # noqa: E501
        :rtype: list[Goal]
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """Sets the goals of this CollectionOfMemberActivityEvents.

        The last 50 Goal events triggered by a member.  # noqa: E501

        :param goals: The goals of this CollectionOfMemberActivityEvents.  # noqa: E501
        :type: list[Goal]
        """

        self._goals = goals

    @property
    def list_id(self):
        """Gets the list_id of this CollectionOfMemberActivityEvents.  # noqa: E501

        The list id.  # noqa: E501

        :return: The list_id of this CollectionOfMemberActivityEvents.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this CollectionOfMemberActivityEvents.

        The list id.  # noqa: E501

        :param list_id: The list_id of this CollectionOfMemberActivityEvents.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def email_id(self):
        """Gets the email_id of this CollectionOfMemberActivityEvents.  # noqa: E501

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :return: The email_id of this CollectionOfMemberActivityEvents.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this CollectionOfMemberActivityEvents.

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :param email_id: The email_id of this CollectionOfMemberActivityEvents.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def total_items(self):
        """Gets the total_items of this CollectionOfMemberActivityEvents.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this CollectionOfMemberActivityEvents.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this CollectionOfMemberActivityEvents.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this CollectionOfMemberActivityEvents.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this CollectionOfMemberActivityEvents.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this CollectionOfMemberActivityEvents.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionOfMemberActivityEvents.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this CollectionOfMemberActivityEvents.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

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
        if issubclass(CollectionOfMemberActivityEvents, dict):
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
        if not isinstance(other, CollectionOfMemberActivityEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
