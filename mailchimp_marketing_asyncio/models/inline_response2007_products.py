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


class InlineResponse2007Products(object):
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
        'sku': 'str',
        'image_url': 'str',
        'total_revenue': 'float',
        'total_purchased': 'float',
        'currency_code': 'str',
        'recommendation_total': 'int',
        'recommendation_purchased': 'int'
    }

    attribute_map = {
        'title': 'title',
        'sku': 'sku',
        'image_url': 'image_url',
        'total_revenue': 'total_revenue',
        'total_purchased': 'total_purchased',
        'currency_code': 'currency_code',
        'recommendation_total': 'recommendation_total',
        'recommendation_purchased': 'recommendation_purchased'
    }

    def __init__(self, title=None, sku=None, image_url=None, total_revenue=None, total_purchased=None, currency_code=None, recommendation_total=None, recommendation_purchased=None):  # noqa: E501
        """InlineResponse2007Products - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._sku = None
        self._image_url = None
        self._total_revenue = None
        self._total_purchased = None
        self._currency_code = None
        self._recommendation_total = None
        self._recommendation_purchased = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if sku is not None:
            self.sku = sku
        if image_url is not None:
            self.image_url = image_url
        if total_revenue is not None:
            self.total_revenue = total_revenue
        if total_purchased is not None:
            self.total_purchased = total_purchased
        if currency_code is not None:
            self.currency_code = currency_code
        if recommendation_total is not None:
            self.recommendation_total = recommendation_total
        if recommendation_purchased is not None:
            self.recommendation_purchased = recommendation_purchased

    @property
    def title(self):
        """Gets the title of this InlineResponse2007Products.  # noqa: E501


        :return: The title of this InlineResponse2007Products.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineResponse2007Products.


        :param title: The title of this InlineResponse2007Products.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def sku(self):
        """Gets the sku of this InlineResponse2007Products.  # noqa: E501


        :return: The sku of this InlineResponse2007Products.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this InlineResponse2007Products.


        :param sku: The sku of this InlineResponse2007Products.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def image_url(self):
        """Gets the image_url of this InlineResponse2007Products.  # noqa: E501


        :return: The image_url of this InlineResponse2007Products.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this InlineResponse2007Products.


        :param image_url: The image_url of this InlineResponse2007Products.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def total_revenue(self):
        """Gets the total_revenue of this InlineResponse2007Products.  # noqa: E501


        :return: The total_revenue of this InlineResponse2007Products.  # noqa: E501
        :rtype: float
        """
        return self._total_revenue

    @total_revenue.setter
    def total_revenue(self, total_revenue):
        """Sets the total_revenue of this InlineResponse2007Products.


        :param total_revenue: The total_revenue of this InlineResponse2007Products.  # noqa: E501
        :type: float
        """

        self._total_revenue = total_revenue

    @property
    def total_purchased(self):
        """Gets the total_purchased of this InlineResponse2007Products.  # noqa: E501


        :return: The total_purchased of this InlineResponse2007Products.  # noqa: E501
        :rtype: float
        """
        return self._total_purchased

    @total_purchased.setter
    def total_purchased(self, total_purchased):
        """Sets the total_purchased of this InlineResponse2007Products.


        :param total_purchased: The total_purchased of this InlineResponse2007Products.  # noqa: E501
        :type: float
        """

        self._total_purchased = total_purchased

    @property
    def currency_code(self):
        """Gets the currency_code of this InlineResponse2007Products.  # noqa: E501


        :return: The currency_code of this InlineResponse2007Products.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this InlineResponse2007Products.


        :param currency_code: The currency_code of this InlineResponse2007Products.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def recommendation_total(self):
        """Gets the recommendation_total of this InlineResponse2007Products.  # noqa: E501


        :return: The recommendation_total of this InlineResponse2007Products.  # noqa: E501
        :rtype: int
        """
        return self._recommendation_total

    @recommendation_total.setter
    def recommendation_total(self, recommendation_total):
        """Sets the recommendation_total of this InlineResponse2007Products.


        :param recommendation_total: The recommendation_total of this InlineResponse2007Products.  # noqa: E501
        :type: int
        """

        self._recommendation_total = recommendation_total

    @property
    def recommendation_purchased(self):
        """Gets the recommendation_purchased of this InlineResponse2007Products.  # noqa: E501


        :return: The recommendation_purchased of this InlineResponse2007Products.  # noqa: E501
        :rtype: int
        """
        return self._recommendation_purchased

    @recommendation_purchased.setter
    def recommendation_purchased(self, recommendation_purchased):
        """Sets the recommendation_purchased of this InlineResponse2007Products.


        :param recommendation_purchased: The recommendation_purchased of this InlineResponse2007Products.  # noqa: E501
        :type: int
        """

        self._recommendation_purchased = recommendation_purchased

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
        if issubclass(InlineResponse2007Products, dict):
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
        if not isinstance(other, InlineResponse2007Products):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
