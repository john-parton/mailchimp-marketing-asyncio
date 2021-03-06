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


class EcommerceCartLineItem(object):
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
        'product_id': 'str',
        'product_title': 'str',
        'product_variant_id': 'str',
        'product_variant_title': 'str',
        'quantity': 'int',
        'price': 'float',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'product_id': 'product_id',
        'product_title': 'product_title',
        'product_variant_id': 'product_variant_id',
        'product_variant_title': 'product_variant_title',
        'quantity': 'quantity',
        'price': 'price',
        'links': '_links'
    }

    def __init__(self, id=None, product_id=None, product_title=None, product_variant_id=None, product_variant_title=None, quantity=None, price=None, links=None):  # noqa: E501
        """EcommerceCartLineItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._product_id = None
        self._product_title = None
        self._product_variant_id = None
        self._product_variant_title = None
        self._quantity = None
        self._price = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if product_title is not None:
            self.product_title = product_title
        if product_variant_id is not None:
            self.product_variant_id = product_variant_id
        if product_variant_title is not None:
            self.product_variant_title = product_variant_title
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommerceCartLineItem.  # noqa: E501

        A unique identifier for the cart line item.  # noqa: E501

        :return: The id of this EcommerceCartLineItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommerceCartLineItem.

        A unique identifier for the cart line item.  # noqa: E501

        :param id: The id of this EcommerceCartLineItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def product_id(self):
        """Gets the product_id of this EcommerceCartLineItem.  # noqa: E501

        A unique identifier for the product associated with the cart line item.  # noqa: E501

        :return: The product_id of this EcommerceCartLineItem.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this EcommerceCartLineItem.

        A unique identifier for the product associated with the cart line item.  # noqa: E501

        :param product_id: The product_id of this EcommerceCartLineItem.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def product_title(self):
        """Gets the product_title of this EcommerceCartLineItem.  # noqa: E501

        The name of the product for the cart line item.  # noqa: E501

        :return: The product_title of this EcommerceCartLineItem.  # noqa: E501
        :rtype: str
        """
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        """Sets the product_title of this EcommerceCartLineItem.

        The name of the product for the cart line item.  # noqa: E501

        :param product_title: The product_title of this EcommerceCartLineItem.  # noqa: E501
        :type: str
        """

        self._product_title = product_title

    @property
    def product_variant_id(self):
        """Gets the product_variant_id of this EcommerceCartLineItem.  # noqa: E501

        A unique identifier for the product variant associated with the cart line item.  # noqa: E501

        :return: The product_variant_id of this EcommerceCartLineItem.  # noqa: E501
        :rtype: str
        """
        return self._product_variant_id

    @product_variant_id.setter
    def product_variant_id(self, product_variant_id):
        """Sets the product_variant_id of this EcommerceCartLineItem.

        A unique identifier for the product variant associated with the cart line item.  # noqa: E501

        :param product_variant_id: The product_variant_id of this EcommerceCartLineItem.  # noqa: E501
        :type: str
        """

        self._product_variant_id = product_variant_id

    @property
    def product_variant_title(self):
        """Gets the product_variant_title of this EcommerceCartLineItem.  # noqa: E501

        The name of the product variant for the cart line item.  # noqa: E501

        :return: The product_variant_title of this EcommerceCartLineItem.  # noqa: E501
        :rtype: str
        """
        return self._product_variant_title

    @product_variant_title.setter
    def product_variant_title(self, product_variant_title):
        """Sets the product_variant_title of this EcommerceCartLineItem.

        The name of the product variant for the cart line item.  # noqa: E501

        :param product_variant_title: The product_variant_title of this EcommerceCartLineItem.  # noqa: E501
        :type: str
        """

        self._product_variant_title = product_variant_title

    @property
    def quantity(self):
        """Gets the quantity of this EcommerceCartLineItem.  # noqa: E501

        The quantity of a cart line item.  # noqa: E501

        :return: The quantity of this EcommerceCartLineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this EcommerceCartLineItem.

        The quantity of a cart line item.  # noqa: E501

        :param quantity: The quantity of this EcommerceCartLineItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this EcommerceCartLineItem.  # noqa: E501

        The price of a cart line item.  # noqa: E501

        :return: The price of this EcommerceCartLineItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this EcommerceCartLineItem.

        The price of a cart line item.  # noqa: E501

        :param price: The price of this EcommerceCartLineItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def links(self):
        """Gets the links of this EcommerceCartLineItem.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommerceCartLineItem.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommerceCartLineItem.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommerceCartLineItem.  # noqa: E501
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
        if issubclass(EcommerceCartLineItem, dict):
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
        if not isinstance(other, EcommerceCartLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
