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


class AutomationWorkflow1(object):
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
        'recipients': 'List1',
        'settings': 'AutomationCampaignSettings1',
        'trigger_settings': 'AutomationTrigger1'
    }

    attribute_map = {
        'recipients': 'recipients',
        'settings': 'settings',
        'trigger_settings': 'trigger_settings'
    }

    def __init__(self, recipients=None, settings=None, trigger_settings=None):  # noqa: E501
        """AutomationWorkflow1 - a model defined in Swagger"""  # noqa: E501

        self._recipients = None
        self._settings = None
        self._trigger_settings = None
        self.discriminator = None

        self.recipients = recipients
        if settings is not None:
            self.settings = settings
        self.trigger_settings = trigger_settings

    @property
    def recipients(self):
        """Gets the recipients of this AutomationWorkflow1.  # noqa: E501


        :return: The recipients of this AutomationWorkflow1.  # noqa: E501
        :rtype: List1
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this AutomationWorkflow1.


        :param recipients: The recipients of this AutomationWorkflow1.  # noqa: E501
        :type: List1
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def settings(self):
        """Gets the settings of this AutomationWorkflow1.  # noqa: E501


        :return: The settings of this AutomationWorkflow1.  # noqa: E501
        :rtype: AutomationCampaignSettings1
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AutomationWorkflow1.


        :param settings: The settings of this AutomationWorkflow1.  # noqa: E501
        :type: AutomationCampaignSettings1
        """

        self._settings = settings

    @property
    def trigger_settings(self):
        """Gets the trigger_settings of this AutomationWorkflow1.  # noqa: E501


        :return: The trigger_settings of this AutomationWorkflow1.  # noqa: E501
        :rtype: AutomationTrigger1
        """
        return self._trigger_settings

    @trigger_settings.setter
    def trigger_settings(self, trigger_settings):
        """Sets the trigger_settings of this AutomationWorkflow1.


        :param trigger_settings: The trigger_settings of this AutomationWorkflow1.  # noqa: E501
        :type: AutomationTrigger1
        """
        if trigger_settings is None:
            raise ValueError("Invalid value for `trigger_settings`, must not be `None`")  # noqa: E501

        self._trigger_settings = trigger_settings

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
        if issubclass(AutomationWorkflow1, dict):
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
        if not isinstance(other, AutomationWorkflow1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
