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


class TemplateContent(object):
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
        'id': 'int',
        'sections': 'object'
    }

    attribute_map = {
        'id': 'id',
        'sections': 'sections'
    }

    def __init__(self, id=None, sections=None):  # noqa: E501
        """TemplateContent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._sections = None
        self.discriminator = None

        self.id = id
        if sections is not None:
            self.sections = sections

    @property
    def id(self):
        """Gets the id of this TemplateContent.  # noqa: E501

        The id of the template to use.  # noqa: E501

        :return: The id of this TemplateContent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateContent.

        The id of the template to use.  # noqa: E501

        :param id: The id of this TemplateContent.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def sections(self):
        """Gets the sections of this TemplateContent.  # noqa: E501

        Content for the sections of the template. Each key should be the unique [mc:edit area](https://mailchimp.com/help/create-editable-content-areas-with-mailchimps-template-language/) name from the template.  # noqa: E501

        :return: The sections of this TemplateContent.  # noqa: E501
        :rtype: object
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this TemplateContent.

        Content for the sections of the template. Each key should be the unique [mc:edit area](https://mailchimp.com/help/create-editable-content-areas-with-mailchimps-template-language/) name from the template.  # noqa: E501

        :param sections: The sections of this TemplateContent.  # noqa: E501
        :type: object
        """

        self._sections = sections

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
        if issubclass(TemplateContent, dict):
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
        if not isinstance(other, TemplateContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other