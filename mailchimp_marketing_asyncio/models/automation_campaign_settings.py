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


class AutomationCampaignSettings(object):
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
        'from_name': 'str',
        'reply_to': 'str',
        'use_conversation': 'bool',
        'to_name': 'str',
        'authenticate': 'bool',
        'auto_footer': 'bool',
        'inline_css': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'from_name': 'from_name',
        'reply_to': 'reply_to',
        'use_conversation': 'use_conversation',
        'to_name': 'to_name',
        'authenticate': 'authenticate',
        'auto_footer': 'auto_footer',
        'inline_css': 'inline_css'
    }

    def __init__(self, title=None, from_name=None, reply_to=None, use_conversation=None, to_name=None, authenticate=None, auto_footer=None, inline_css=None):  # noqa: E501
        """AutomationCampaignSettings - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._from_name = None
        self._reply_to = None
        self._use_conversation = None
        self._to_name = None
        self._authenticate = None
        self._auto_footer = None
        self._inline_css = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if from_name is not None:
            self.from_name = from_name
        if reply_to is not None:
            self.reply_to = reply_to
        if use_conversation is not None:
            self.use_conversation = use_conversation
        if to_name is not None:
            self.to_name = to_name
        if authenticate is not None:
            self.authenticate = authenticate
        if auto_footer is not None:
            self.auto_footer = auto_footer
        if inline_css is not None:
            self.inline_css = inline_css

    @property
    def title(self):
        """Gets the title of this AutomationCampaignSettings.  # noqa: E501

        The title of the Automation.  # noqa: E501

        :return: The title of this AutomationCampaignSettings.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AutomationCampaignSettings.

        The title of the Automation.  # noqa: E501

        :param title: The title of this AutomationCampaignSettings.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def from_name(self):
        """Gets the from_name of this AutomationCampaignSettings.  # noqa: E501

        The 'from' name for the Automation (not an email address).  # noqa: E501

        :return: The from_name of this AutomationCampaignSettings.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this AutomationCampaignSettings.

        The 'from' name for the Automation (not an email address).  # noqa: E501

        :param from_name: The from_name of this AutomationCampaignSettings.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def reply_to(self):
        """Gets the reply_to of this AutomationCampaignSettings.  # noqa: E501

        The reply-to email address for the Automation.  # noqa: E501

        :return: The reply_to of this AutomationCampaignSettings.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this AutomationCampaignSettings.

        The reply-to email address for the Automation.  # noqa: E501

        :param reply_to: The reply_to of this AutomationCampaignSettings.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def use_conversation(self):
        """Gets the use_conversation of this AutomationCampaignSettings.  # noqa: E501

        Whether to use Mailchimp Conversation feature to manage replies  # noqa: E501

        :return: The use_conversation of this AutomationCampaignSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_conversation

    @use_conversation.setter
    def use_conversation(self, use_conversation):
        """Sets the use_conversation of this AutomationCampaignSettings.

        Whether to use Mailchimp Conversation feature to manage replies  # noqa: E501

        :param use_conversation: The use_conversation of this AutomationCampaignSettings.  # noqa: E501
        :type: bool
        """

        self._use_conversation = use_conversation

    @property
    def to_name(self):
        """Gets the to_name of this AutomationCampaignSettings.  # noqa: E501

        The Automation's custom 'To' name, typically the first name [audience field](https://mailchimp.com/help/getting-started-with-merge-tags/).  # noqa: E501

        :return: The to_name of this AutomationCampaignSettings.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this AutomationCampaignSettings.

        The Automation's custom 'To' name, typically the first name [audience field](https://mailchimp.com/help/getting-started-with-merge-tags/).  # noqa: E501

        :param to_name: The to_name of this AutomationCampaignSettings.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

    @property
    def authenticate(self):
        """Gets the authenticate of this AutomationCampaignSettings.  # noqa: E501

        Whether Mailchimp [authenticated](https://mailchimp.com/help/about-email-authentication/) the Automation. Defaults to `true`.  # noqa: E501

        :return: The authenticate of this AutomationCampaignSettings.  # noqa: E501
        :rtype: bool
        """
        return self._authenticate

    @authenticate.setter
    def authenticate(self, authenticate):
        """Sets the authenticate of this AutomationCampaignSettings.

        Whether Mailchimp [authenticated](https://mailchimp.com/help/about-email-authentication/) the Automation. Defaults to `true`.  # noqa: E501

        :param authenticate: The authenticate of this AutomationCampaignSettings.  # noqa: E501
        :type: bool
        """

        self._authenticate = authenticate

    @property
    def auto_footer(self):
        """Gets the auto_footer of this AutomationCampaignSettings.  # noqa: E501

        Whether to automatically append Mailchimp's [default footer](https://mailchimp.com/help/about-campaign-footers/) to the Automation.  # noqa: E501

        :return: The auto_footer of this AutomationCampaignSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_footer

    @auto_footer.setter
    def auto_footer(self, auto_footer):
        """Sets the auto_footer of this AutomationCampaignSettings.

        Whether to automatically append Mailchimp's [default footer](https://mailchimp.com/help/about-campaign-footers/) to the Automation.  # noqa: E501

        :param auto_footer: The auto_footer of this AutomationCampaignSettings.  # noqa: E501
        :type: bool
        """

        self._auto_footer = auto_footer

    @property
    def inline_css(self):
        """Gets the inline_css of this AutomationCampaignSettings.  # noqa: E501

        Whether to automatically inline the CSS included with the Automation content.  # noqa: E501

        :return: The inline_css of this AutomationCampaignSettings.  # noqa: E501
        :rtype: bool
        """
        return self._inline_css

    @inline_css.setter
    def inline_css(self, inline_css):
        """Sets the inline_css of this AutomationCampaignSettings.

        Whether to automatically inline the CSS included with the Automation content.  # noqa: E501

        :param inline_css: The inline_css of this AutomationCampaignSettings.  # noqa: E501
        :type: bool
        """

        self._inline_css = inline_css

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
        if issubclass(AutomationCampaignSettings, dict):
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
        if not isinstance(other, AutomationCampaignSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other