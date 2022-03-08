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


class LandingPage(object):
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
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'template_id': 'int',
        'status': 'str',
        'list_id': 'str',
        'store_id': 'str',
        'web_id': 'int',
        'created_by_source': 'str',
        'url': 'str',
        'created_at': 'datetime',
        'published_at': 'datetime',
        'unpublished_at': 'datetime',
        'updated_at': 'datetime',
        'tracking': 'TrackingSettings',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'template_id': 'template_id',
        'status': 'status',
        'list_id': 'list_id',
        'store_id': 'store_id',
        'web_id': 'web_id',
        'created_by_source': 'created_by_source',
        'url': 'url',
        'created_at': 'created_at',
        'published_at': 'published_at',
        'unpublished_at': 'unpublished_at',
        'updated_at': 'updated_at',
        'tracking': 'tracking',
        'links': '_links'
    }

    def __init__(self, id=None, name=None, title=None, description=None, template_id=None, status=None, list_id=None, store_id=None, web_id=None, created_by_source=None, url=None, created_at=None, published_at=None, unpublished_at=None, updated_at=None, tracking=None, links=None):  # noqa: E501
        """LandingPage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._title = None
        self._description = None
        self._template_id = None
        self._status = None
        self._list_id = None
        self._store_id = None
        self._web_id = None
        self._created_by_source = None
        self._url = None
        self._created_at = None
        self._published_at = None
        self._unpublished_at = None
        self._updated_at = None
        self._tracking = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if template_id is not None:
            self.template_id = template_id
        if status is not None:
            self.status = status
        if list_id is not None:
            self.list_id = list_id
        if store_id is not None:
            self.store_id = store_id
        if web_id is not None:
            self.web_id = web_id
        if created_by_source is not None:
            self.created_by_source = created_by_source
        if url is not None:
            self.url = url
        if created_at is not None:
            self.created_at = created_at
        if published_at is not None:
            self.published_at = published_at
        if unpublished_at is not None:
            self.unpublished_at = unpublished_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tracking is not None:
            self.tracking = tracking
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this LandingPage.  # noqa: E501

        A string that uniquely identifies this landing page.  # noqa: E501

        :return: The id of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LandingPage.

        A string that uniquely identifies this landing page.  # noqa: E501

        :param id: The id of this LandingPage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LandingPage.  # noqa: E501

        The name of this landing page.  # noqa: E501

        :return: The name of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LandingPage.

        The name of this landing page.  # noqa: E501

        :param name: The name of this LandingPage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this LandingPage.  # noqa: E501

        The title of this landing page seen in the browser's title bar.  # noqa: E501

        :return: The title of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LandingPage.

        The title of this landing page seen in the browser's title bar.  # noqa: E501

        :param title: The title of this LandingPage.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this LandingPage.  # noqa: E501

        The description of this landing page.  # noqa: E501

        :return: The description of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LandingPage.

        The description of this landing page.  # noqa: E501

        :param description: The description of this LandingPage.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def template_id(self):
        """Gets the template_id of this LandingPage.  # noqa: E501

        The template_id of this landing page.  # noqa: E501

        :return: The template_id of this LandingPage.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this LandingPage.

        The template_id of this landing page.  # noqa: E501

        :param template_id: The template_id of this LandingPage.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def status(self):
        """Gets the status of this LandingPage.  # noqa: E501

        The status of this landing page.  # noqa: E501

        :return: The status of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LandingPage.

        The status of this landing page.  # noqa: E501

        :param status: The status of this LandingPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["published", "unpublished", "draft"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def list_id(self):
        """Gets the list_id of this LandingPage.  # noqa: E501

        The list's ID associated with this landing page.  # noqa: E501

        :return: The list_id of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this LandingPage.

        The list's ID associated with this landing page.  # noqa: E501

        :param list_id: The list_id of this LandingPage.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def store_id(self):
        """Gets the store_id of this LandingPage.  # noqa: E501

        The ID of the store associated with this landing page.  # noqa: E501

        :return: The store_id of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this LandingPage.

        The ID of the store associated with this landing page.  # noqa: E501

        :param store_id: The store_id of this LandingPage.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def web_id(self):
        """Gets the web_id of this LandingPage.  # noqa: E501

        The ID used in the Mailchimp web application.  # noqa: E501

        :return: The web_id of this LandingPage.  # noqa: E501
        :rtype: int
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """Sets the web_id of this LandingPage.

        The ID used in the Mailchimp web application.  # noqa: E501

        :param web_id: The web_id of this LandingPage.  # noqa: E501
        :type: int
        """

        self._web_id = web_id

    @property
    def created_by_source(self):
        """Gets the created_by_source of this LandingPage.  # noqa: E501

        Created by mobile or web  # noqa: E501

        :return: The created_by_source of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._created_by_source

    @created_by_source.setter
    def created_by_source(self, created_by_source):
        """Sets the created_by_source of this LandingPage.

        Created by mobile or web  # noqa: E501

        :param created_by_source: The created_by_source of this LandingPage.  # noqa: E501
        :type: str
        """

        self._created_by_source = created_by_source

    @property
    def url(self):
        """Gets the url of this LandingPage.  # noqa: E501

        The url of the published landing page.  # noqa: E501

        :return: The url of this LandingPage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LandingPage.

        The url of the published landing page.  # noqa: E501

        :param url: The url of this LandingPage.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def created_at(self):
        """Gets the created_at of this LandingPage.  # noqa: E501

        The time this landing page was created.  # noqa: E501

        :return: The created_at of this LandingPage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LandingPage.

        The time this landing page was created.  # noqa: E501

        :param created_at: The created_at of this LandingPage.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def published_at(self):
        """Gets the published_at of this LandingPage.  # noqa: E501

        The time this landing page was published.  # noqa: E501

        :return: The published_at of this LandingPage.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this LandingPage.

        The time this landing page was published.  # noqa: E501

        :param published_at: The published_at of this LandingPage.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def unpublished_at(self):
        """Gets the unpublished_at of this LandingPage.  # noqa: E501

        The time this landing page was unpublished.  # noqa: E501

        :return: The unpublished_at of this LandingPage.  # noqa: E501
        :rtype: datetime
        """
        return self._unpublished_at

    @unpublished_at.setter
    def unpublished_at(self, unpublished_at):
        """Sets the unpublished_at of this LandingPage.

        The time this landing page was unpublished.  # noqa: E501

        :param unpublished_at: The unpublished_at of this LandingPage.  # noqa: E501
        :type: datetime
        """

        self._unpublished_at = unpublished_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LandingPage.  # noqa: E501

        The time this landing page was updated at.  # noqa: E501

        :return: The updated_at of this LandingPage.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LandingPage.

        The time this landing page was updated at.  # noqa: E501

        :param updated_at: The updated_at of this LandingPage.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def tracking(self):
        """Gets the tracking of this LandingPage.  # noqa: E501


        :return: The tracking of this LandingPage.  # noqa: E501
        :rtype: TrackingSettings
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this LandingPage.


        :param tracking: The tracking of this LandingPage.  # noqa: E501
        :type: TrackingSettings
        """

        self._tracking = tracking

    @property
    def links(self):
        """Gets the links of this LandingPage.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this LandingPage.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LandingPage.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this LandingPage.  # noqa: E501
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
        if issubclass(LandingPage, dict):
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
        if not isinstance(other, LandingPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other