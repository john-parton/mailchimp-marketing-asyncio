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


class ProblemDetailDocument(object):
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
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None):  # noqa: E501
        """ProblemDetailDocument - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self.discriminator = None

        self.type = type
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance

    @property
    def type(self):
        """Gets the type of this ProblemDetailDocument.  # noqa: E501

        An absolute URI that identifies the problem type. When dereferenced, it should provide human-readable documentation for the problem type.  # noqa: E501

        :return: The type of this ProblemDetailDocument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetailDocument.

        An absolute URI that identifies the problem type. When dereferenced, it should provide human-readable documentation for the problem type.  # noqa: E501

        :param type: The type of this ProblemDetailDocument.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this ProblemDetailDocument.  # noqa: E501

        A short, human-readable summary of the problem type. It shouldn't change based on the occurrence of the problem, except for purposes of localization.  # noqa: E501

        :return: The title of this ProblemDetailDocument.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetailDocument.

        A short, human-readable summary of the problem type. It shouldn't change based on the occurrence of the problem, except for purposes of localization.  # noqa: E501

        :param title: The title of this ProblemDetailDocument.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def status(self):
        """Gets the status of this ProblemDetailDocument.  # noqa: E501

        The HTTP status code (RFC2616, Section 6) generated by the origin server for this occurrence of the problem.  # noqa: E501

        :return: The status of this ProblemDetailDocument.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetailDocument.

        The HTTP status code (RFC2616, Section 6) generated by the origin server for this occurrence of the problem.  # noqa: E501

        :param status: The status of this ProblemDetailDocument.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ProblemDetailDocument.  # noqa: E501

        A human-readable explanation specific to this occurrence of the problem. [Learn more about errors](/developer/guides/get-started-with-mailchimp-api-3/#Errors).  # noqa: E501

        :return: The detail of this ProblemDetailDocument.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetailDocument.

        A human-readable explanation specific to this occurrence of the problem. [Learn more about errors](/developer/guides/get-started-with-mailchimp-api-3/#Errors).  # noqa: E501

        :param detail: The detail of this ProblemDetailDocument.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetailDocument.  # noqa: E501

        A string that identifies this specific occurrence of the problem. Please provide this ID when contacting support.  # noqa: E501

        :return: The instance of this ProblemDetailDocument.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetailDocument.

        A string that identifies this specific occurrence of the problem. Please provide this ID when contacting support.  # noqa: E501

        :param instance: The instance of this ProblemDetailDocument.  # noqa: E501
        :type: str
        """
        if instance is None:
            raise ValueError("Invalid value for `instance`, must not be `None`")  # noqa: E501

        self._instance = instance

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
        if issubclass(ProblemDetailDocument, dict):
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
        if not isinstance(other, ProblemDetailDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
