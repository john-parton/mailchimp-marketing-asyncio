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


class CollectionOfConversationMessages(object):
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
        'conversation_messages': 'list[ConversationMessage]',
        'conversation_id': 'str',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'conversation_messages': 'conversation_messages',
        'conversation_id': 'conversation_id',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, conversation_messages=None, conversation_id=None, total_items=None, links=None):  # noqa: E501
        """CollectionOfConversationMessages - a model defined in Swagger"""  # noqa: E501

        self._conversation_messages = None
        self._conversation_id = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if conversation_messages is not None:
            self.conversation_messages = conversation_messages
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def conversation_messages(self):
        """Gets the conversation_messages of this CollectionOfConversationMessages.  # noqa: E501

        An array of objects, each representing a conversation messages resources.  # noqa: E501

        :return: The conversation_messages of this CollectionOfConversationMessages.  # noqa: E501
        :rtype: list[ConversationMessage]
        """
        return self._conversation_messages

    @conversation_messages.setter
    def conversation_messages(self, conversation_messages):
        """Sets the conversation_messages of this CollectionOfConversationMessages.

        An array of objects, each representing a conversation messages resources.  # noqa: E501

        :param conversation_messages: The conversation_messages of this CollectionOfConversationMessages.  # noqa: E501
        :type: list[ConversationMessage]
        """

        self._conversation_messages = conversation_messages

    @property
    def conversation_id(self):
        """Gets the conversation_id of this CollectionOfConversationMessages.  # noqa: E501

        A string that identifies this conversation.  # noqa: E501

        :return: The conversation_id of this CollectionOfConversationMessages.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this CollectionOfConversationMessages.

        A string that identifies this conversation.  # noqa: E501

        :param conversation_id: The conversation_id of this CollectionOfConversationMessages.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def total_items(self):
        """Gets the total_items of this CollectionOfConversationMessages.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this CollectionOfConversationMessages.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this CollectionOfConversationMessages.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this CollectionOfConversationMessages.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this CollectionOfConversationMessages.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this CollectionOfConversationMessages.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionOfConversationMessages.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this CollectionOfConversationMessages.  # noqa: E501
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
        if issubclass(CollectionOfConversationMessages, dict):
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
        if not isinstance(other, CollectionOfConversationMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
