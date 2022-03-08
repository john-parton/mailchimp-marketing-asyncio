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


class InlineResponse20011AudienceActivity(object):
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
        'clicks': 'list[InlineResponse20011AudienceActivityClicks]',
        'impressions': 'list[InlineResponse20011AudienceActivityImpressions]',
        'revenue': 'list[InlineResponse20011AudienceActivityRevenue]'
    }

    attribute_map = {
        'clicks': 'clicks',
        'impressions': 'impressions',
        'revenue': 'revenue'
    }

    def __init__(self, clicks=None, impressions=None, revenue=None):  # noqa: E501
        """InlineResponse20011AudienceActivity - a model defined in Swagger"""  # noqa: E501

        self._clicks = None
        self._impressions = None
        self._revenue = None
        self.discriminator = None

        if clicks is not None:
            self.clicks = clicks
        if impressions is not None:
            self.impressions = impressions
        if revenue is not None:
            self.revenue = revenue

    @property
    def clicks(self):
        """Gets the clicks of this InlineResponse20011AudienceActivity.  # noqa: E501


        :return: The clicks of this InlineResponse20011AudienceActivity.  # noqa: E501
        :rtype: list[InlineResponse20011AudienceActivityClicks]
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this InlineResponse20011AudienceActivity.


        :param clicks: The clicks of this InlineResponse20011AudienceActivity.  # noqa: E501
        :type: list[InlineResponse20011AudienceActivityClicks]
        """

        self._clicks = clicks

    @property
    def impressions(self):
        """Gets the impressions of this InlineResponse20011AudienceActivity.  # noqa: E501


        :return: The impressions of this InlineResponse20011AudienceActivity.  # noqa: E501
        :rtype: list[InlineResponse20011AudienceActivityImpressions]
        """
        return self._impressions

    @impressions.setter
    def impressions(self, impressions):
        """Sets the impressions of this InlineResponse20011AudienceActivity.


        :param impressions: The impressions of this InlineResponse20011AudienceActivity.  # noqa: E501
        :type: list[InlineResponse20011AudienceActivityImpressions]
        """

        self._impressions = impressions

    @property
    def revenue(self):
        """Gets the revenue of this InlineResponse20011AudienceActivity.  # noqa: E501


        :return: The revenue of this InlineResponse20011AudienceActivity.  # noqa: E501
        :rtype: list[InlineResponse20011AudienceActivityRevenue]
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this InlineResponse20011AudienceActivity.


        :param revenue: The revenue of this InlineResponse20011AudienceActivity.  # noqa: E501
        :type: list[InlineResponse20011AudienceActivityRevenue]
        """

        self._revenue = revenue

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
        if issubclass(InlineResponse20011AudienceActivity, dict):
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
        if not isinstance(other, InlineResponse20011AudienceActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other