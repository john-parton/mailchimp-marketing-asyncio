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


class SignupForm(object):
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
        'header': 'SignupFormHeaderOptions',
        'contents': 'list[CollectionOfContentForListSignupForms]',
        'styles': 'list[CollectionOfElementStyleForListSignupForms]',
        'signup_form_url': 'str',
        'list_id': 'str',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'header': 'header',
        'contents': 'contents',
        'styles': 'styles',
        'signup_form_url': 'signup_form_url',
        'list_id': 'list_id',
        'links': '_links'
    }

    def __init__(self, header=None, contents=None, styles=None, signup_form_url=None, list_id=None, links=None):  # noqa: E501
        """SignupForm - a model defined in Swagger"""  # noqa: E501

        self._header = None
        self._contents = None
        self._styles = None
        self._signup_form_url = None
        self._list_id = None
        self._links = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if contents is not None:
            self.contents = contents
        if styles is not None:
            self.styles = styles
        if signup_form_url is not None:
            self.signup_form_url = signup_form_url
        if list_id is not None:
            self.list_id = list_id
        if links is not None:
            self.links = links

    @property
    def header(self):
        """Gets the header of this SignupForm.  # noqa: E501


        :return: The header of this SignupForm.  # noqa: E501
        :rtype: SignupFormHeaderOptions
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this SignupForm.


        :param header: The header of this SignupForm.  # noqa: E501
        :type: SignupFormHeaderOptions
        """

        self._header = header

    @property
    def contents(self):
        """Gets the contents of this SignupForm.  # noqa: E501

        The signup form body content.  # noqa: E501

        :return: The contents of this SignupForm.  # noqa: E501
        :rtype: list[CollectionOfContentForListSignupForms]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this SignupForm.

        The signup form body content.  # noqa: E501

        :param contents: The contents of this SignupForm.  # noqa: E501
        :type: list[CollectionOfContentForListSignupForms]
        """

        self._contents = contents

    @property
    def styles(self):
        """Gets the styles of this SignupForm.  # noqa: E501

        An array of objects, each representing an element style for the signup form.  # noqa: E501

        :return: The styles of this SignupForm.  # noqa: E501
        :rtype: list[CollectionOfElementStyleForListSignupForms]
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this SignupForm.

        An array of objects, each representing an element style for the signup form.  # noqa: E501

        :param styles: The styles of this SignupForm.  # noqa: E501
        :type: list[CollectionOfElementStyleForListSignupForms]
        """

        self._styles = styles

    @property
    def signup_form_url(self):
        """Gets the signup_form_url of this SignupForm.  # noqa: E501

        Signup form URL.  # noqa: E501

        :return: The signup_form_url of this SignupForm.  # noqa: E501
        :rtype: str
        """
        return self._signup_form_url

    @signup_form_url.setter
    def signup_form_url(self, signup_form_url):
        """Sets the signup_form_url of this SignupForm.

        Signup form URL.  # noqa: E501

        :param signup_form_url: The signup_form_url of this SignupForm.  # noqa: E501
        :type: str
        """

        self._signup_form_url = signup_form_url

    @property
    def list_id(self):
        """Gets the list_id of this SignupForm.  # noqa: E501

        The signup form's list id.  # noqa: E501

        :return: The list_id of this SignupForm.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this SignupForm.

        The signup form's list id.  # noqa: E501

        :param list_id: The list_id of this SignupForm.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def links(self):
        """Gets the links of this SignupForm.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this SignupForm.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SignupForm.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this SignupForm.  # noqa: E501
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
        if issubclass(SignupForm, dict):
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
        if not isinstance(other, SignupForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other