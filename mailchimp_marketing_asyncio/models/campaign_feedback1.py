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


class CampaignFeedback1(object):
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
        'block_id': 'int',
        'message': 'str',
        'is_complete': 'bool'
    }

    attribute_map = {
        'block_id': 'block_id',
        'message': 'message',
        'is_complete': 'is_complete'
    }

    def __init__(self, block_id=None, message=None, is_complete=None):  # noqa: E501
        """CampaignFeedback1 - a model defined in Swagger"""  # noqa: E501

        self._block_id = None
        self._message = None
        self._is_complete = None
        self.discriminator = None

        if block_id is not None:
            self.block_id = block_id
        self.message = message
        if is_complete is not None:
            self.is_complete = is_complete

    @property
    def block_id(self):
        """Gets the block_id of this CampaignFeedback1.  # noqa: E501

        The block id for the editable block that the feedback addresses.  # noqa: E501

        :return: The block_id of this CampaignFeedback1.  # noqa: E501
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this CampaignFeedback1.

        The block id for the editable block that the feedback addresses.  # noqa: E501

        :param block_id: The block_id of this CampaignFeedback1.  # noqa: E501
        :type: int
        """

        self._block_id = block_id

    @property
    def message(self):
        """Gets the message of this CampaignFeedback1.  # noqa: E501

        The content of the feedback.  # noqa: E501

        :return: The message of this CampaignFeedback1.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CampaignFeedback1.

        The content of the feedback.  # noqa: E501

        :param message: The message of this CampaignFeedback1.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def is_complete(self):
        """Gets the is_complete of this CampaignFeedback1.  # noqa: E501

        The status of feedback.  # noqa: E501

        :return: The is_complete of this CampaignFeedback1.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this CampaignFeedback1.

        The status of feedback.  # noqa: E501

        :param is_complete: The is_complete of this CampaignFeedback1.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

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
        if issubclass(CampaignFeedback1, dict):
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
        if not isinstance(other, CampaignFeedback1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
