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


class Statistics(object):
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
        'member_count': 'int',
        'total_contacts': 'int',
        'unsubscribe_count': 'int',
        'cleaned_count': 'int',
        'member_count_since_send': 'int',
        'unsubscribe_count_since_send': 'int',
        'cleaned_count_since_send': 'int',
        'campaign_count': 'int',
        'campaign_last_sent': 'datetime',
        'merge_field_count': 'int',
        'avg_sub_rate': 'float',
        'avg_unsub_rate': 'float',
        'target_sub_rate': 'float',
        'open_rate': 'float',
        'click_rate': 'float',
        'last_sub_date': 'datetime',
        'last_unsub_date': 'datetime'
    }

    attribute_map = {
        'member_count': 'member_count',
        'total_contacts': 'total_contacts',
        'unsubscribe_count': 'unsubscribe_count',
        'cleaned_count': 'cleaned_count',
        'member_count_since_send': 'member_count_since_send',
        'unsubscribe_count_since_send': 'unsubscribe_count_since_send',
        'cleaned_count_since_send': 'cleaned_count_since_send',
        'campaign_count': 'campaign_count',
        'campaign_last_sent': 'campaign_last_sent',
        'merge_field_count': 'merge_field_count',
        'avg_sub_rate': 'avg_sub_rate',
        'avg_unsub_rate': 'avg_unsub_rate',
        'target_sub_rate': 'target_sub_rate',
        'open_rate': 'open_rate',
        'click_rate': 'click_rate',
        'last_sub_date': 'last_sub_date',
        'last_unsub_date': 'last_unsub_date'
    }

    def __init__(self, member_count=None, total_contacts=None, unsubscribe_count=None, cleaned_count=None, member_count_since_send=None, unsubscribe_count_since_send=None, cleaned_count_since_send=None, campaign_count=None, campaign_last_sent=None, merge_field_count=None, avg_sub_rate=None, avg_unsub_rate=None, target_sub_rate=None, open_rate=None, click_rate=None, last_sub_date=None, last_unsub_date=None):  # noqa: E501
        """Statistics - a model defined in Swagger"""  # noqa: E501

        self._member_count = None
        self._total_contacts = None
        self._unsubscribe_count = None
        self._cleaned_count = None
        self._member_count_since_send = None
        self._unsubscribe_count_since_send = None
        self._cleaned_count_since_send = None
        self._campaign_count = None
        self._campaign_last_sent = None
        self._merge_field_count = None
        self._avg_sub_rate = None
        self._avg_unsub_rate = None
        self._target_sub_rate = None
        self._open_rate = None
        self._click_rate = None
        self._last_sub_date = None
        self._last_unsub_date = None
        self.discriminator = None

        if member_count is not None:
            self.member_count = member_count
        if total_contacts is not None:
            self.total_contacts = total_contacts
        if unsubscribe_count is not None:
            self.unsubscribe_count = unsubscribe_count
        if cleaned_count is not None:
            self.cleaned_count = cleaned_count
        if member_count_since_send is not None:
            self.member_count_since_send = member_count_since_send
        if unsubscribe_count_since_send is not None:
            self.unsubscribe_count_since_send = unsubscribe_count_since_send
        if cleaned_count_since_send is not None:
            self.cleaned_count_since_send = cleaned_count_since_send
        if campaign_count is not None:
            self.campaign_count = campaign_count
        if campaign_last_sent is not None:
            self.campaign_last_sent = campaign_last_sent
        if merge_field_count is not None:
            self.merge_field_count = merge_field_count
        if avg_sub_rate is not None:
            self.avg_sub_rate = avg_sub_rate
        if avg_unsub_rate is not None:
            self.avg_unsub_rate = avg_unsub_rate
        if target_sub_rate is not None:
            self.target_sub_rate = target_sub_rate
        if open_rate is not None:
            self.open_rate = open_rate
        if click_rate is not None:
            self.click_rate = click_rate
        if last_sub_date is not None:
            self.last_sub_date = last_sub_date
        if last_unsub_date is not None:
            self.last_unsub_date = last_unsub_date

    @property
    def member_count(self):
        """Gets the member_count of this Statistics.  # noqa: E501

        The number of active members in the list.  # noqa: E501

        :return: The member_count of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this Statistics.

        The number of active members in the list.  # noqa: E501

        :param member_count: The member_count of this Statistics.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def total_contacts(self):
        """Gets the total_contacts of this Statistics.  # noqa: E501

        The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed. Requires include_total_contacts query parameter to be included.  # noqa: E501

        :return: The total_contacts of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._total_contacts

    @total_contacts.setter
    def total_contacts(self, total_contacts):
        """Sets the total_contacts of this Statistics.

        The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed. Requires include_total_contacts query parameter to be included.  # noqa: E501

        :param total_contacts: The total_contacts of this Statistics.  # noqa: E501
        :type: int
        """

        self._total_contacts = total_contacts

    @property
    def unsubscribe_count(self):
        """Gets the unsubscribe_count of this Statistics.  # noqa: E501

        The number of members who have unsubscribed from the list.  # noqa: E501

        :return: The unsubscribe_count of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribe_count

    @unsubscribe_count.setter
    def unsubscribe_count(self, unsubscribe_count):
        """Sets the unsubscribe_count of this Statistics.

        The number of members who have unsubscribed from the list.  # noqa: E501

        :param unsubscribe_count: The unsubscribe_count of this Statistics.  # noqa: E501
        :type: int
        """

        self._unsubscribe_count = unsubscribe_count

    @property
    def cleaned_count(self):
        """Gets the cleaned_count of this Statistics.  # noqa: E501

        The number of members cleaned from the list.  # noqa: E501

        :return: The cleaned_count of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._cleaned_count

    @cleaned_count.setter
    def cleaned_count(self, cleaned_count):
        """Sets the cleaned_count of this Statistics.

        The number of members cleaned from the list.  # noqa: E501

        :param cleaned_count: The cleaned_count of this Statistics.  # noqa: E501
        :type: int
        """

        self._cleaned_count = cleaned_count

    @property
    def member_count_since_send(self):
        """Gets the member_count_since_send of this Statistics.  # noqa: E501

        The number of active members in the list since the last campaign was sent.  # noqa: E501

        :return: The member_count_since_send of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._member_count_since_send

    @member_count_since_send.setter
    def member_count_since_send(self, member_count_since_send):
        """Sets the member_count_since_send of this Statistics.

        The number of active members in the list since the last campaign was sent.  # noqa: E501

        :param member_count_since_send: The member_count_since_send of this Statistics.  # noqa: E501
        :type: int
        """

        self._member_count_since_send = member_count_since_send

    @property
    def unsubscribe_count_since_send(self):
        """Gets the unsubscribe_count_since_send of this Statistics.  # noqa: E501

        The number of members who have unsubscribed since the last campaign was sent.  # noqa: E501

        :return: The unsubscribe_count_since_send of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribe_count_since_send

    @unsubscribe_count_since_send.setter
    def unsubscribe_count_since_send(self, unsubscribe_count_since_send):
        """Sets the unsubscribe_count_since_send of this Statistics.

        The number of members who have unsubscribed since the last campaign was sent.  # noqa: E501

        :param unsubscribe_count_since_send: The unsubscribe_count_since_send of this Statistics.  # noqa: E501
        :type: int
        """

        self._unsubscribe_count_since_send = unsubscribe_count_since_send

    @property
    def cleaned_count_since_send(self):
        """Gets the cleaned_count_since_send of this Statistics.  # noqa: E501

        The number of members cleaned from the list since the last campaign was sent.  # noqa: E501

        :return: The cleaned_count_since_send of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._cleaned_count_since_send

    @cleaned_count_since_send.setter
    def cleaned_count_since_send(self, cleaned_count_since_send):
        """Sets the cleaned_count_since_send of this Statistics.

        The number of members cleaned from the list since the last campaign was sent.  # noqa: E501

        :param cleaned_count_since_send: The cleaned_count_since_send of this Statistics.  # noqa: E501
        :type: int
        """

        self._cleaned_count_since_send = cleaned_count_since_send

    @property
    def campaign_count(self):
        """Gets the campaign_count of this Statistics.  # noqa: E501

        The number of campaigns in any status that use this list.  # noqa: E501

        :return: The campaign_count of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._campaign_count

    @campaign_count.setter
    def campaign_count(self, campaign_count):
        """Sets the campaign_count of this Statistics.

        The number of campaigns in any status that use this list.  # noqa: E501

        :param campaign_count: The campaign_count of this Statistics.  # noqa: E501
        :type: int
        """

        self._campaign_count = campaign_count

    @property
    def campaign_last_sent(self):
        """Gets the campaign_last_sent of this Statistics.  # noqa: E501

        The date and time the last campaign was sent to this list in ISO 8601 format. This is updated when a campaign is sent to 10 or more recipients.  # noqa: E501

        :return: The campaign_last_sent of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._campaign_last_sent

    @campaign_last_sent.setter
    def campaign_last_sent(self, campaign_last_sent):
        """Sets the campaign_last_sent of this Statistics.

        The date and time the last campaign was sent to this list in ISO 8601 format. This is updated when a campaign is sent to 10 or more recipients.  # noqa: E501

        :param campaign_last_sent: The campaign_last_sent of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._campaign_last_sent = campaign_last_sent

    @property
    def merge_field_count(self):
        """Gets the merge_field_count of this Statistics.  # noqa: E501

        The number of merge fields ([audience field](https://mailchimp.com/help/getting-started-with-merge-tags/)) for this list (doesn't include EMAIL).  # noqa: E501

        :return: The merge_field_count of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._merge_field_count

    @merge_field_count.setter
    def merge_field_count(self, merge_field_count):
        """Sets the merge_field_count of this Statistics.

        The number of merge fields ([audience field](https://mailchimp.com/help/getting-started-with-merge-tags/)) for this list (doesn't include EMAIL).  # noqa: E501

        :param merge_field_count: The merge_field_count of this Statistics.  # noqa: E501
        :type: int
        """

        self._merge_field_count = merge_field_count

    @property
    def avg_sub_rate(self):
        """Gets the avg_sub_rate of this Statistics.  # noqa: E501

        The average number of subscriptions per month for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :return: The avg_sub_rate of this Statistics.  # noqa: E501
        :rtype: float
        """
        return self._avg_sub_rate

    @avg_sub_rate.setter
    def avg_sub_rate(self, avg_sub_rate):
        """Sets the avg_sub_rate of this Statistics.

        The average number of subscriptions per month for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :param avg_sub_rate: The avg_sub_rate of this Statistics.  # noqa: E501
        :type: float
        """

        self._avg_sub_rate = avg_sub_rate

    @property
    def avg_unsub_rate(self):
        """Gets the avg_unsub_rate of this Statistics.  # noqa: E501

        The average number of unsubscriptions per month for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :return: The avg_unsub_rate of this Statistics.  # noqa: E501
        :rtype: float
        """
        return self._avg_unsub_rate

    @avg_unsub_rate.setter
    def avg_unsub_rate(self, avg_unsub_rate):
        """Sets the avg_unsub_rate of this Statistics.

        The average number of unsubscriptions per month for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :param avg_unsub_rate: The avg_unsub_rate of this Statistics.  # noqa: E501
        :type: float
        """

        self._avg_unsub_rate = avg_unsub_rate

    @property
    def target_sub_rate(self):
        """Gets the target_sub_rate of this Statistics.  # noqa: E501

        The target number of subscriptions per month for the list to keep it growing (not returned if we haven't calculated it yet).  # noqa: E501

        :return: The target_sub_rate of this Statistics.  # noqa: E501
        :rtype: float
        """
        return self._target_sub_rate

    @target_sub_rate.setter
    def target_sub_rate(self, target_sub_rate):
        """Sets the target_sub_rate of this Statistics.

        The target number of subscriptions per month for the list to keep it growing (not returned if we haven't calculated it yet).  # noqa: E501

        :param target_sub_rate: The target_sub_rate of this Statistics.  # noqa: E501
        :type: float
        """

        self._target_sub_rate = target_sub_rate

    @property
    def open_rate(self):
        """Gets the open_rate of this Statistics.  # noqa: E501

        The average open rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :return: The open_rate of this Statistics.  # noqa: E501
        :rtype: float
        """
        return self._open_rate

    @open_rate.setter
    def open_rate(self, open_rate):
        """Sets the open_rate of this Statistics.

        The average open rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :param open_rate: The open_rate of this Statistics.  # noqa: E501
        :type: float
        """

        self._open_rate = open_rate

    @property
    def click_rate(self):
        """Gets the click_rate of this Statistics.  # noqa: E501

        The average click rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :return: The click_rate of this Statistics.  # noqa: E501
        :rtype: float
        """
        return self._click_rate

    @click_rate.setter
    def click_rate(self, click_rate):
        """Sets the click_rate of this Statistics.

        The average click rate (a percentage represented as a number between 0 and 100) per campaign for the list (not returned if we haven't calculated it yet).  # noqa: E501

        :param click_rate: The click_rate of this Statistics.  # noqa: E501
        :type: float
        """

        self._click_rate = click_rate

    @property
    def last_sub_date(self):
        """Gets the last_sub_date of this Statistics.  # noqa: E501

        The date and time of the last time someone subscribed to this list in ISO 8601 format.  # noqa: E501

        :return: The last_sub_date of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sub_date

    @last_sub_date.setter
    def last_sub_date(self, last_sub_date):
        """Sets the last_sub_date of this Statistics.

        The date and time of the last time someone subscribed to this list in ISO 8601 format.  # noqa: E501

        :param last_sub_date: The last_sub_date of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._last_sub_date = last_sub_date

    @property
    def last_unsub_date(self):
        """Gets the last_unsub_date of this Statistics.  # noqa: E501

        The date and time of the last time someone unsubscribed from this list in ISO 8601 format.  # noqa: E501

        :return: The last_unsub_date of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._last_unsub_date

    @last_unsub_date.setter
    def last_unsub_date(self, last_unsub_date):
        """Sets the last_unsub_date of this Statistics.

        The date and time of the last time someone unsubscribed from this list in ISO 8601 format.  # noqa: E501

        :param last_unsub_date: The last_unsub_date of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._last_unsub_date = last_unsub_date

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
        if issubclass(Statistics, dict):
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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
