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


class OpenActivity(object):
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
        'campaign_id': 'str',
        'list_id': 'str',
        'list_is_active': 'bool',
        'contact_status': 'str',
        'email_id': 'str',
        'email_address': 'str',
        'merge_fields': 'dict(str, object)',
        'vip': 'bool',
        'opens_count': 'int',
        'opens': 'list[MemberActivity1]',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'campaign_id': 'campaign_id',
        'list_id': 'list_id',
        'list_is_active': 'list_is_active',
        'contact_status': 'contact_status',
        'email_id': 'email_id',
        'email_address': 'email_address',
        'merge_fields': 'merge_fields',
        'vip': 'vip',
        'opens_count': 'opens_count',
        'opens': 'opens',
        'links': '_links'
    }

    def __init__(self, campaign_id=None, list_id=None, list_is_active=None, contact_status=None, email_id=None, email_address=None, merge_fields=None, vip=None, opens_count=None, opens=None, links=None):  # noqa: E501
        """OpenActivity - a model defined in Swagger"""  # noqa: E501

        self._campaign_id = None
        self._list_id = None
        self._list_is_active = None
        self._contact_status = None
        self._email_id = None
        self._email_address = None
        self._merge_fields = None
        self._vip = None
        self._opens_count = None
        self._opens = None
        self._links = None
        self.discriminator = None

        if campaign_id is not None:
            self.campaign_id = campaign_id
        if list_id is not None:
            self.list_id = list_id
        if list_is_active is not None:
            self.list_is_active = list_is_active
        if contact_status is not None:
            self.contact_status = contact_status
        if email_id is not None:
            self.email_id = email_id
        if email_address is not None:
            self.email_address = email_address
        if merge_fields is not None:
            self.merge_fields = merge_fields
        if vip is not None:
            self.vip = vip
        if opens_count is not None:
            self.opens_count = opens_count
        if opens is not None:
            self.opens = opens
        if links is not None:
            self.links = links

    @property
    def campaign_id(self):
        """Gets the campaign_id of this OpenActivity.  # noqa: E501

        The unique id for the campaign.  # noqa: E501

        :return: The campaign_id of this OpenActivity.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this OpenActivity.

        The unique id for the campaign.  # noqa: E501

        :param campaign_id: The campaign_id of this OpenActivity.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def list_id(self):
        """Gets the list_id of this OpenActivity.  # noqa: E501

        The unique id for the list.  # noqa: E501

        :return: The list_id of this OpenActivity.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this OpenActivity.

        The unique id for the list.  # noqa: E501

        :param list_id: The list_id of this OpenActivity.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def list_is_active(self):
        """Gets the list_is_active of this OpenActivity.  # noqa: E501

        The status of the list used, namely if it's deleted or disabled.  # noqa: E501

        :return: The list_is_active of this OpenActivity.  # noqa: E501
        :rtype: bool
        """
        return self._list_is_active

    @list_is_active.setter
    def list_is_active(self, list_is_active):
        """Sets the list_is_active of this OpenActivity.

        The status of the list used, namely if it's deleted or disabled.  # noqa: E501

        :param list_is_active: The list_is_active of this OpenActivity.  # noqa: E501
        :type: bool
        """

        self._list_is_active = list_is_active

    @property
    def contact_status(self):
        """Gets the contact_status of this OpenActivity.  # noqa: E501

        The status of the member, namely if they are subscribed, unsubscribed, deleted, non-subscribed, transactional, pending, or need reconfirmation.  # noqa: E501

        :return: The contact_status of this OpenActivity.  # noqa: E501
        :rtype: str
        """
        return self._contact_status

    @contact_status.setter
    def contact_status(self, contact_status):
        """Sets the contact_status of this OpenActivity.

        The status of the member, namely if they are subscribed, unsubscribed, deleted, non-subscribed, transactional, pending, or need reconfirmation.  # noqa: E501

        :param contact_status: The contact_status of this OpenActivity.  # noqa: E501
        :type: str
        """

        self._contact_status = contact_status

    @property
    def email_id(self):
        """Gets the email_id of this OpenActivity.  # noqa: E501

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :return: The email_id of this OpenActivity.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this OpenActivity.

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :param email_id: The email_id of this OpenActivity.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def email_address(self):
        """Gets the email_address of this OpenActivity.  # noqa: E501

        Email address for a subscriber.  # noqa: E501

        :return: The email_address of this OpenActivity.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this OpenActivity.

        Email address for a subscriber.  # noqa: E501

        :param email_address: The email_address of this OpenActivity.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def merge_fields(self):
        """Gets the merge_fields of this OpenActivity.  # noqa: E501

        A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.  # noqa: E501

        :return: The merge_fields of this OpenActivity.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._merge_fields

    @merge_fields.setter
    def merge_fields(self, merge_fields):
        """Sets the merge_fields of this OpenActivity.

        A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.  # noqa: E501

        :param merge_fields: The merge_fields of this OpenActivity.  # noqa: E501
        :type: dict(str, object)
        """

        self._merge_fields = merge_fields

    @property
    def vip(self):
        """Gets the vip of this OpenActivity.  # noqa: E501

        [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.  # noqa: E501

        :return: The vip of this OpenActivity.  # noqa: E501
        :rtype: bool
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this OpenActivity.

        [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.  # noqa: E501

        :param vip: The vip of this OpenActivity.  # noqa: E501
        :type: bool
        """

        self._vip = vip

    @property
    def opens_count(self):
        """Gets the opens_count of this OpenActivity.  # noqa: E501

        The total number of times the this campaign was opened by the list member.  # noqa: E501

        :return: The opens_count of this OpenActivity.  # noqa: E501
        :rtype: int
        """
        return self._opens_count

    @opens_count.setter
    def opens_count(self, opens_count):
        """Sets the opens_count of this OpenActivity.

        The total number of times the this campaign was opened by the list member.  # noqa: E501

        :param opens_count: The opens_count of this OpenActivity.  # noqa: E501
        :type: int
        """

        self._opens_count = opens_count

    @property
    def opens(self):
        """Gets the opens of this OpenActivity.  # noqa: E501

        An array of timestamps for each time a list member opened the campaign. If a list member opens an email multiple times, this will return a separate timestamp for each open event.  # noqa: E501

        :return: The opens of this OpenActivity.  # noqa: E501
        :rtype: list[MemberActivity1]
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this OpenActivity.

        An array of timestamps for each time a list member opened the campaign. If a list member opens an email multiple times, this will return a separate timestamp for each open event.  # noqa: E501

        :param opens: The opens of this OpenActivity.  # noqa: E501
        :type: list[MemberActivity1]
        """

        self._opens = opens

    @property
    def links(self):
        """Gets the links of this OpenActivity.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this OpenActivity.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OpenActivity.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this OpenActivity.  # noqa: E501
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
        if issubclass(OpenActivity, dict):
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
        if not isinstance(other, OpenActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
