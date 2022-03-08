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


class OpenDetailReport(object):
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
        'members': 'list[OpenActivity]',
        'campaign_id': 'str',
        'total_opens': 'int',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'members': 'members',
        'campaign_id': 'campaign_id',
        'total_opens': 'total_opens',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, members=None, campaign_id=None, total_opens=None, total_items=None, links=None):  # noqa: E501
        """OpenDetailReport - a model defined in Swagger"""  # noqa: E501

        self._members = None
        self._campaign_id = None
        self._total_opens = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if total_opens is not None:
            self.total_opens = total_opens
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def members(self):
        """Gets the members of this OpenDetailReport.  # noqa: E501

        An array of objects, each representing a list member who opened a campaign email. Each members object will contain information about the number of total opens by a single member, as well as timestamps for each open event.  # noqa: E501

        :return: The members of this OpenDetailReport.  # noqa: E501
        :rtype: list[OpenActivity]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this OpenDetailReport.

        An array of objects, each representing a list member who opened a campaign email. Each members object will contain information about the number of total opens by a single member, as well as timestamps for each open event.  # noqa: E501

        :param members: The members of this OpenDetailReport.  # noqa: E501
        :type: list[OpenActivity]
        """

        self._members = members

    @property
    def campaign_id(self):
        """Gets the campaign_id of this OpenDetailReport.  # noqa: E501

        The campaign id.  # noqa: E501

        :return: The campaign_id of this OpenDetailReport.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this OpenDetailReport.

        The campaign id.  # noqa: E501

        :param campaign_id: The campaign_id of this OpenDetailReport.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def total_opens(self):
        """Gets the total_opens of this OpenDetailReport.  # noqa: E501

        The total number of opens matching the query regardless of pagination.  # noqa: E501

        :return: The total_opens of this OpenDetailReport.  # noqa: E501
        :rtype: int
        """
        return self._total_opens

    @total_opens.setter
    def total_opens(self, total_opens):
        """Sets the total_opens of this OpenDetailReport.

        The total number of opens matching the query regardless of pagination.  # noqa: E501

        :param total_opens: The total_opens of this OpenDetailReport.  # noqa: E501
        :type: int
        """

        self._total_opens = total_opens

    @property
    def total_items(self):
        """Gets the total_items of this OpenDetailReport.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this OpenDetailReport.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this OpenDetailReport.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this OpenDetailReport.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this OpenDetailReport.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this OpenDetailReport.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OpenDetailReport.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this OpenDetailReport.  # noqa: E501
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
        if issubclass(OpenDetailReport, dict):
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
        if not isinstance(other, OpenDetailReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other