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


class EcommerceCart(object):
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
        'id': 'str',
        'customer': 'EcommerceCustomer',
        'campaign_id': 'str',
        'checkout_url': 'str',
        'currency_code': 'str',
        'order_total': 'float',
        'tax_total': 'float',
        'lines': 'list[EcommerceCartLineItem]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'customer': 'customer',
        'campaign_id': 'campaign_id',
        'checkout_url': 'checkout_url',
        'currency_code': 'currency_code',
        'order_total': 'order_total',
        'tax_total': 'tax_total',
        'lines': 'lines',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': '_links'
    }

    def __init__(self, id=None, customer=None, campaign_id=None, checkout_url=None, currency_code=None, order_total=None, tax_total=None, lines=None, created_at=None, updated_at=None, links=None):  # noqa: E501
        """EcommerceCart - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._customer = None
        self._campaign_id = None
        self._checkout_url = None
        self._currency_code = None
        self._order_total = None
        self._tax_total = None
        self._lines = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if customer is not None:
            self.customer = customer
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if checkout_url is not None:
            self.checkout_url = checkout_url
        if currency_code is not None:
            self.currency_code = currency_code
        if order_total is not None:
            self.order_total = order_total
        if tax_total is not None:
            self.tax_total = tax_total
        if lines is not None:
            self.lines = lines
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommerceCart.  # noqa: E501

        A unique identifier for the cart.  # noqa: E501

        :return: The id of this EcommerceCart.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommerceCart.

        A unique identifier for the cart.  # noqa: E501

        :param id: The id of this EcommerceCart.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this EcommerceCart.  # noqa: E501


        :return: The customer of this EcommerceCart.  # noqa: E501
        :rtype: EcommerceCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this EcommerceCart.


        :param customer: The customer of this EcommerceCart.  # noqa: E501
        :type: EcommerceCustomer
        """

        self._customer = customer

    @property
    def campaign_id(self):
        """Gets the campaign_id of this EcommerceCart.  # noqa: E501

        A string that uniquely identifies the campaign associated with a cart.  # noqa: E501

        :return: The campaign_id of this EcommerceCart.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this EcommerceCart.

        A string that uniquely identifies the campaign associated with a cart.  # noqa: E501

        :param campaign_id: The campaign_id of this EcommerceCart.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def checkout_url(self):
        """Gets the checkout_url of this EcommerceCart.  # noqa: E501

        The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-an-abandoned-cart-email/) automations.  # noqa: E501

        :return: The checkout_url of this EcommerceCart.  # noqa: E501
        :rtype: str
        """
        return self._checkout_url

    @checkout_url.setter
    def checkout_url(self, checkout_url):
        """Sets the checkout_url of this EcommerceCart.

        The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-an-abandoned-cart-email/) automations.  # noqa: E501

        :param checkout_url: The checkout_url of this EcommerceCart.  # noqa: E501
        :type: str
        """

        self._checkout_url = checkout_url

    @property
    def currency_code(self):
        """Gets the currency_code of this EcommerceCart.  # noqa: E501

        The three-letter ISO 4217 code for the currency that the cart uses.  # noqa: E501

        :return: The currency_code of this EcommerceCart.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this EcommerceCart.

        The three-letter ISO 4217 code for the currency that the cart uses.  # noqa: E501

        :param currency_code: The currency_code of this EcommerceCart.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def order_total(self):
        """Gets the order_total of this EcommerceCart.  # noqa: E501

        The order total for the cart.  # noqa: E501

        :return: The order_total of this EcommerceCart.  # noqa: E501
        :rtype: float
        """
        return self._order_total

    @order_total.setter
    def order_total(self, order_total):
        """Sets the order_total of this EcommerceCart.

        The order total for the cart.  # noqa: E501

        :param order_total: The order_total of this EcommerceCart.  # noqa: E501
        :type: float
        """

        self._order_total = order_total

    @property
    def tax_total(self):
        """Gets the tax_total of this EcommerceCart.  # noqa: E501

        The total tax for the cart.  # noqa: E501

        :return: The tax_total of this EcommerceCart.  # noqa: E501
        :rtype: float
        """
        return self._tax_total

    @tax_total.setter
    def tax_total(self, tax_total):
        """Sets the tax_total of this EcommerceCart.

        The total tax for the cart.  # noqa: E501

        :param tax_total: The tax_total of this EcommerceCart.  # noqa: E501
        :type: float
        """

        self._tax_total = tax_total

    @property
    def lines(self):
        """Gets the lines of this EcommerceCart.  # noqa: E501

        An array of the cart's line items.  # noqa: E501

        :return: The lines of this EcommerceCart.  # noqa: E501
        :rtype: list[EcommerceCartLineItem]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this EcommerceCart.

        An array of the cart's line items.  # noqa: E501

        :param lines: The lines of this EcommerceCart.  # noqa: E501
        :type: list[EcommerceCartLineItem]
        """

        self._lines = lines

    @property
    def created_at(self):
        """Gets the created_at of this EcommerceCart.  # noqa: E501

        The date and time the cart was created in ISO 8601 format.  # noqa: E501

        :return: The created_at of this EcommerceCart.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EcommerceCart.

        The date and time the cart was created in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this EcommerceCart.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EcommerceCart.  # noqa: E501

        The date and time the cart was last updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at of this EcommerceCart.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EcommerceCart.

        The date and time the cart was last updated in ISO 8601 format.  # noqa: E501

        :param updated_at: The updated_at of this EcommerceCart.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this EcommerceCart.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommerceCart.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommerceCart.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommerceCart.  # noqa: E501
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
        if issubclass(EcommerceCart, dict):
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
        if not isinstance(other, EcommerceCart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other