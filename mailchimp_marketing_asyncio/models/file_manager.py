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


class FileManager(object):
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
        'files': 'list[GalleryFile]',
        'total_file_size': 'float',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'files': 'files',
        'total_file_size': 'total_file_size',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, files=None, total_file_size=None, total_items=None, links=None):  # noqa: E501
        """FileManager - a model defined in Swagger"""  # noqa: E501

        self._files = None
        self._total_file_size = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if files is not None:
            self.files = files
        if total_file_size is not None:
            self.total_file_size = total_file_size
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def files(self):
        """Gets the files of this FileManager.  # noqa: E501

         A list of files and images in an account.  # noqa: E501

        :return: The files of this FileManager.  # noqa: E501
        :rtype: list[GalleryFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this FileManager.

         A list of files and images in an account.  # noqa: E501

        :param files: The files of this FileManager.  # noqa: E501
        :type: list[GalleryFile]
        """

        self._files = files

    @property
    def total_file_size(self):
        """Gets the total_file_size of this FileManager.  # noqa: E501

        The total size of all File Manager files in bytes.  # noqa: E501

        :return: The total_file_size of this FileManager.  # noqa: E501
        :rtype: float
        """
        return self._total_file_size

    @total_file_size.setter
    def total_file_size(self, total_file_size):
        """Sets the total_file_size of this FileManager.

        The total size of all File Manager files in bytes.  # noqa: E501

        :param total_file_size: The total_file_size of this FileManager.  # noqa: E501
        :type: float
        """

        self._total_file_size = total_file_size

    @property
    def total_items(self):
        """Gets the total_items of this FileManager.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this FileManager.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this FileManager.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this FileManager.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this FileManager.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this FileManager.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FileManager.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this FileManager.  # noqa: E501
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
        if issubclass(FileManager, dict):
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
        if not isinstance(other, FileManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
