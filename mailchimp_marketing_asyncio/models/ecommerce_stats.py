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


class EcommerceStats(object):
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
        'total_revenue': 'float',
        'number_of_orders': 'float',
        'currency_code': 'str'
    }

    attribute_map = {
        'total_revenue': 'total_revenue',
        'number_of_orders': 'number_of_orders',
        'currency_code': 'currency_code'
    }

    def __init__(self, total_revenue=None, number_of_orders=None, currency_code=None):  # noqa: E501
        """EcommerceStats - a model defined in Swagger"""  # noqa: E501

        self._total_revenue = None
        self._number_of_orders = None
        self._currency_code = None
        self.discriminator = None

        if total_revenue is not None:
            self.total_revenue = total_revenue
        if number_of_orders is not None:
            self.number_of_orders = number_of_orders
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def total_revenue(self):
        """Gets the total_revenue of this EcommerceStats.  # noqa: E501

        The total revenue the list member has brought in.  # noqa: E501

        :return: The total_revenue of this EcommerceStats.  # noqa: E501
        :rtype: float
        """
        return self._total_revenue

    @total_revenue.setter
    def total_revenue(self, total_revenue):
        """Sets the total_revenue of this EcommerceStats.

        The total revenue the list member has brought in.  # noqa: E501

        :param total_revenue: The total_revenue of this EcommerceStats.  # noqa: E501
        :type: float
        """

        self._total_revenue = total_revenue

    @property
    def number_of_orders(self):
        """Gets the number_of_orders of this EcommerceStats.  # noqa: E501

        The total number of orders placed by the list member.  # noqa: E501

        :return: The number_of_orders of this EcommerceStats.  # noqa: E501
        :rtype: float
        """
        return self._number_of_orders

    @number_of_orders.setter
    def number_of_orders(self, number_of_orders):
        """Sets the number_of_orders of this EcommerceStats.

        The total number of orders placed by the list member.  # noqa: E501

        :param number_of_orders: The number_of_orders of this EcommerceStats.  # noqa: E501
        :type: float
        """

        self._number_of_orders = number_of_orders

    @property
    def currency_code(self):
        """Gets the currency_code of this EcommerceStats.  # noqa: E501

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :return: The currency_code of this EcommerceStats.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this EcommerceStats.

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :param currency_code: The currency_code of this EcommerceStats.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if issubclass(EcommerceStats, dict):
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
        if not isinstance(other, EcommerceStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
