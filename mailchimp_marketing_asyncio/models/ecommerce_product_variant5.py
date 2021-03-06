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


class EcommerceProductVariant5(object):
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
        'url': 'str',
        'sku': 'str',
        'price': 'float',
        'inventory_quantity': 'int',
        'image_url': 'str',
        'backorders': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'sku': 'sku',
        'price': 'price',
        'inventory_quantity': 'inventory_quantity',
        'image_url': 'image_url',
        'backorders': 'backorders',
        'visibility': 'visibility'
    }

    def __init__(self, title=None, url=None, sku=None, price=None, inventory_quantity=None, image_url=None, backorders=None, visibility=None):  # noqa: E501
        """EcommerceProductVariant5 - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._url = None
        self._sku = None
        self._price = None
        self._inventory_quantity = None
        self._image_url = None
        self._backorders = None
        self._visibility = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if sku is not None:
            self.sku = sku
        if price is not None:
            self.price = price
        if inventory_quantity is not None:
            self.inventory_quantity = inventory_quantity
        if image_url is not None:
            self.image_url = image_url
        if backorders is not None:
            self.backorders = backorders
        if visibility is not None:
            self.visibility = visibility

    @property
    def title(self):
        """Gets the title of this EcommerceProductVariant5.  # noqa: E501

        The title of a product variant.  # noqa: E501

        :return: The title of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EcommerceProductVariant5.

        The title of a product variant.  # noqa: E501

        :param title: The title of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this EcommerceProductVariant5.  # noqa: E501

        The URL for a product variant.  # noqa: E501

        :return: The url of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EcommerceProductVariant5.

        The URL for a product variant.  # noqa: E501

        :param url: The url of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def sku(self):
        """Gets the sku of this EcommerceProductVariant5.  # noqa: E501

        The stock keeping unit (SKU) of a product variant.  # noqa: E501

        :return: The sku of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this EcommerceProductVariant5.

        The stock keeping unit (SKU) of a product variant.  # noqa: E501

        :param sku: The sku of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def price(self):
        """Gets the price of this EcommerceProductVariant5.  # noqa: E501

        The price of a product variant.  # noqa: E501

        :return: The price of this EcommerceProductVariant5.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this EcommerceProductVariant5.

        The price of a product variant.  # noqa: E501

        :param price: The price of this EcommerceProductVariant5.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def inventory_quantity(self):
        """Gets the inventory_quantity of this EcommerceProductVariant5.  # noqa: E501

        The inventory quantity of a product variant.  # noqa: E501

        :return: The inventory_quantity of this EcommerceProductVariant5.  # noqa: E501
        :rtype: int
        """
        return self._inventory_quantity

    @inventory_quantity.setter
    def inventory_quantity(self, inventory_quantity):
        """Sets the inventory_quantity of this EcommerceProductVariant5.

        The inventory quantity of a product variant.  # noqa: E501

        :param inventory_quantity: The inventory_quantity of this EcommerceProductVariant5.  # noqa: E501
        :type: int
        """

        self._inventory_quantity = inventory_quantity

    @property
    def image_url(self):
        """Gets the image_url of this EcommerceProductVariant5.  # noqa: E501

        The image URL for a product variant.  # noqa: E501

        :return: The image_url of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this EcommerceProductVariant5.

        The image URL for a product variant.  # noqa: E501

        :param image_url: The image_url of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def backorders(self):
        """Gets the backorders of this EcommerceProductVariant5.  # noqa: E501

        The backorders of a product variant.  # noqa: E501

        :return: The backorders of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._backorders

    @backorders.setter
    def backorders(self, backorders):
        """Sets the backorders of this EcommerceProductVariant5.

        The backorders of a product variant.  # noqa: E501

        :param backorders: The backorders of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._backorders = backorders

    @property
    def visibility(self):
        """Gets the visibility of this EcommerceProductVariant5.  # noqa: E501

        The visibility of a product variant.  # noqa: E501

        :return: The visibility of this EcommerceProductVariant5.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this EcommerceProductVariant5.

        The visibility of a product variant.  # noqa: E501

        :param visibility: The visibility of this EcommerceProductVariant5.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

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
        if issubclass(EcommerceProductVariant5, dict):
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
        if not isinstance(other, EcommerceProductVariant5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
