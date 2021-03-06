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


class ConversationMessage(object):
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
        'id': 'str',
        'conversation_id': 'str',
        'list_id': 'int',
        'from_label': 'str',
        'from_email': 'str',
        'subject': 'str',
        'message': 'str',
        'read': 'bool',
        'timestamp': 'datetime',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'conversation_id': 'conversation_id',
        'list_id': 'list_id',
        'from_label': 'from_label',
        'from_email': 'from_email',
        'subject': 'subject',
        'message': 'message',
        'read': 'read',
        'timestamp': 'timestamp',
        'links': '_links'
    }

    def __init__(self, id=None, conversation_id=None, list_id=None, from_label=None, from_email=None, subject=None, message=None, read=None, timestamp=None, links=None):  # noqa: E501
        """ConversationMessage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._conversation_id = None
        self._list_id = None
        self._from_label = None
        self._from_email = None
        self._subject = None
        self._message = None
        self._read = None
        self._timestamp = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if list_id is not None:
            self.list_id = list_id
        if from_label is not None:
            self.from_label = from_label
        if from_email is not None:
            self.from_email = from_email
        if subject is not None:
            self.subject = subject
        if message is not None:
            self.message = message
        if read is not None:
            self.read = read
        if timestamp is not None:
            self.timestamp = timestamp
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ConversationMessage.  # noqa: E501

        A string that uniquely identifies this message  # noqa: E501

        :return: The id of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversationMessage.

        A string that uniquely identifies this message  # noqa: E501

        :param id: The id of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this ConversationMessage.  # noqa: E501

        A string that identifies this message's conversation  # noqa: E501

        :return: The conversation_id of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this ConversationMessage.

        A string that identifies this message's conversation  # noqa: E501

        :param conversation_id: The conversation_id of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def list_id(self):
        """Gets the list_id of this ConversationMessage.  # noqa: E501

        The list's web ID  # noqa: E501

        :return: The list_id of this ConversationMessage.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this ConversationMessage.

        The list's web ID  # noqa: E501

        :param list_id: The list_id of this ConversationMessage.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

    @property
    def from_label(self):
        """Gets the from_label of this ConversationMessage.  # noqa: E501

        A label representing the sender of this message  # noqa: E501

        :return: The from_label of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._from_label

    @from_label.setter
    def from_label(self, from_label):
        """Sets the from_label of this ConversationMessage.

        A label representing the sender of this message  # noqa: E501

        :param from_label: The from_label of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._from_label = from_label

    @property
    def from_email(self):
        """Gets the from_email of this ConversationMessage.  # noqa: E501

        A label representing the email of the sender of this message  # noqa: E501

        :return: The from_email of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this ConversationMessage.

        A label representing the email of the sender of this message  # noqa: E501

        :param from_email: The from_email of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def subject(self):
        """Gets the subject of this ConversationMessage.  # noqa: E501

        The subject of this message  # noqa: E501

        :return: The subject of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ConversationMessage.

        The subject of this message  # noqa: E501

        :param subject: The subject of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def message(self):
        """Gets the message of this ConversationMessage.  # noqa: E501

        The plain-text content of the message  # noqa: E501

        :return: The message of this ConversationMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConversationMessage.

        The plain-text content of the message  # noqa: E501

        :param message: The message of this ConversationMessage.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def read(self):
        """Gets the read of this ConversationMessage.  # noqa: E501

        Whether this message has been marked as read  # noqa: E501

        :return: The read of this ConversationMessage.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this ConversationMessage.

        Whether this message has been marked as read  # noqa: E501

        :param read: The read of this ConversationMessage.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def timestamp(self):
        """Gets the timestamp of this ConversationMessage.  # noqa: E501

        The date and time the message was either sent or received in ISO 8601 format.  # noqa: E501

        :return: The timestamp of this ConversationMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ConversationMessage.

        The date and time the message was either sent or received in ISO 8601 format.  # noqa: E501

        :param timestamp: The timestamp of this ConversationMessage.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def links(self):
        """Gets the links of this ConversationMessage.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this ConversationMessage.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConversationMessage.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this ConversationMessage.  # noqa: E501
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
        if issubclass(ConversationMessage, dict):
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
        if not isinstance(other, ConversationMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
