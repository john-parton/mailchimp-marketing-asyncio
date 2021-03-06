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


class List7(object):
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
        'name': 'str',
        'member_count': 'int',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'options': 'Conditions',
        'list_id': 'str',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'member_count': 'member_count',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'options': 'options',
        'list_id': 'list_id',
        'links': '_links'
    }

    def __init__(self, id=None, name=None, member_count=None, type=None, created_at=None, updated_at=None, options=None, list_id=None, links=None):  # noqa: E501
        """List7 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._member_count = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._options = None
        self._list_id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if member_count is not None:
            self.member_count = member_count
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if options is not None:
            self.options = options
        if list_id is not None:
            self.list_id = list_id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this List7.  # noqa: E501

        The unique id for the segment.  # noqa: E501

        :return: The id of this List7.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this List7.

        The unique id for the segment.  # noqa: E501

        :param id: The id of this List7.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this List7.  # noqa: E501

        The name of the segment.  # noqa: E501

        :return: The name of this List7.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this List7.

        The name of the segment.  # noqa: E501

        :param name: The name of this List7.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def member_count(self):
        """Gets the member_count of this List7.  # noqa: E501

        The number of active subscribers currently included in the segment.  # noqa: E501

        :return: The member_count of this List7.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this List7.

        The number of active subscribers currently included in the segment.  # noqa: E501

        :param member_count: The member_count of this List7.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def type(self):
        """Gets the type of this List7.  # noqa: E501

        The type of segment. Static segments are now known as tags. Learn more about [tags](https://mailchimp.com/help/getting-started-tags?utm_source=mc-api&utm_medium=docs&utm_campaign=apidocs).  # noqa: E501

        :return: The type of this List7.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this List7.

        The type of segment. Static segments are now known as tags. Learn more about [tags](https://mailchimp.com/help/getting-started-tags?utm_source=mc-api&utm_medium=docs&utm_campaign=apidocs).  # noqa: E501

        :param type: The type of this List7.  # noqa: E501
        :type: str
        """
        allowed_values = ["saved", "static", "fuzzy"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this List7.  # noqa: E501

        The date and time the segment was created in ISO 8601 format.  # noqa: E501

        :return: The created_at of this List7.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this List7.

        The date and time the segment was created in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this List7.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this List7.  # noqa: E501

        The date and time the segment was last updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at of this List7.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this List7.

        The date and time the segment was last updated in ISO 8601 format.  # noqa: E501

        :param updated_at: The updated_at of this List7.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def options(self):
        """Gets the options of this List7.  # noqa: E501


        :return: The options of this List7.  # noqa: E501
        :rtype: Conditions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this List7.


        :param options: The options of this List7.  # noqa: E501
        :type: Conditions
        """

        self._options = options

    @property
    def list_id(self):
        """Gets the list_id of this List7.  # noqa: E501

        The list id.  # noqa: E501

        :return: The list_id of this List7.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this List7.

        The list id.  # noqa: E501

        :param list_id: The list_id of this List7.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def links(self):
        """Gets the links of this List7.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this List7.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this List7.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this List7.  # noqa: E501
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
        if issubclass(List7, dict):
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
        if not isinstance(other, List7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
