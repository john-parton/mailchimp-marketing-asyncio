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


class InlineResponse2009Content(object):
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
        'title': 'str',
        'link_url': 'str',
        'message': 'str',
        'description': 'str',
        'image_url': 'str',
        'call_to_action': 'str',
        'attachments': 'list[InlineResponse2009ContentAttachments]'
    }

    attribute_map = {
        'title': 'title',
        'link_url': 'link_url',
        'message': 'message',
        'description': 'description',
        'image_url': 'image_url',
        'call_to_action': 'call_to_action',
        'attachments': 'attachments'
    }

    def __init__(self, title=None, link_url=None, message=None, description=None, image_url=None, call_to_action=None, attachments=None):  # noqa: E501
        """InlineResponse2009Content - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._link_url = None
        self._message = None
        self._description = None
        self._image_url = None
        self._call_to_action = None
        self._attachments = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if link_url is not None:
            self.link_url = link_url
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description
        if image_url is not None:
            self.image_url = image_url
        if call_to_action is not None:
            self.call_to_action = call_to_action
        if attachments is not None:
            self.attachments = attachments

    @property
    def title(self):
        """Gets the title of this InlineResponse2009Content.  # noqa: E501


        :return: The title of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse2009Content.


        :param title: The title of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def link_url(self):
        """Gets the link_url of this InlineResponse2009Content.  # noqa: E501


        :return: The link_url of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this InlineResponse2009Content.


        :param link_url: The link_url of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._link_url = link_url

    @property
    def message(self):
        """Gets the message of this InlineResponse2009Content.  # noqa: E501


        :return: The message of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2009Content.


        :param message: The message of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def description(self):
        """Gets the description of this InlineResponse2009Content.  # noqa: E501


        :return: The description of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2009Content.


        :param description: The description of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_url(self):
        """Gets the image_url of this InlineResponse2009Content.  # noqa: E501


        :return: The image_url of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this InlineResponse2009Content.


        :param image_url: The image_url of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def call_to_action(self):
        """Gets the call_to_action of this InlineResponse2009Content.  # noqa: E501


        :return: The call_to_action of this InlineResponse2009Content.  # noqa: E501
        :rtype: str
        """
        return self._call_to_action

    @call_to_action.setter
    def call_to_action(self, call_to_action):
        """Sets the call_to_action of this InlineResponse2009Content.


        :param call_to_action: The call_to_action of this InlineResponse2009Content.  # noqa: E501
        :type: str
        """

        self._call_to_action = call_to_action

    @property
    def attachments(self):
        """Gets the attachments of this InlineResponse2009Content.  # noqa: E501


        :return: The attachments of this InlineResponse2009Content.  # noqa: E501
        :rtype: list[InlineResponse2009ContentAttachments]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this InlineResponse2009Content.


        :param attachments: The attachments of this InlineResponse2009Content.  # noqa: E501
        :type: list[InlineResponse2009ContentAttachments]
        """

        self._attachments = attachments

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
        if issubclass(InlineResponse2009Content, dict):
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
        if not isinstance(other, InlineResponse2009Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
