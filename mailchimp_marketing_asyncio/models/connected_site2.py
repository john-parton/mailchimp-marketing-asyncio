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


class ConnectedSite2(object):
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
        'site_foreign_id': 'str',
        'site_script': 'Script1'
    }

    attribute_map = {
        'site_foreign_id': 'site_foreign_id',
        'site_script': 'site_script'
    }

    def __init__(self, site_foreign_id=None, site_script=None):  # noqa: E501
        """ConnectedSite2 - a model defined in Swagger"""  # noqa: E501

        self._site_foreign_id = None
        self._site_script = None
        self.discriminator = None

        if site_foreign_id is not None:
            self.site_foreign_id = site_foreign_id
        if site_script is not None:
            self.site_script = site_script

    @property
    def site_foreign_id(self):
        """Gets the site_foreign_id of this ConnectedSite2.  # noqa: E501

        The unique identifier for the connected site.  # noqa: E501

        :return: The site_foreign_id of this ConnectedSite2.  # noqa: E501
        :rtype: str
        """
        return self._site_foreign_id

    @site_foreign_id.setter
    def site_foreign_id(self, site_foreign_id):
        """Sets the site_foreign_id of this ConnectedSite2.

        The unique identifier for the connected site.  # noqa: E501

        :param site_foreign_id: The site_foreign_id of this ConnectedSite2.  # noqa: E501
        :type: str
        """

        self._site_foreign_id = site_foreign_id

    @property
    def site_script(self):
        """Gets the site_script of this ConnectedSite2.  # noqa: E501


        :return: The site_script of this ConnectedSite2.  # noqa: E501
        :rtype: Script1
        """
        return self._site_script

    @site_script.setter
    def site_script(self, site_script):
        """Sets the site_script of this ConnectedSite2.


        :param site_script: The site_script of this ConnectedSite2.  # noqa: E501
        :type: Script1
        """

        self._site_script = site_script

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
        if issubclass(ConnectedSite2, dict):
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
        if not isinstance(other, ConnectedSite2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
