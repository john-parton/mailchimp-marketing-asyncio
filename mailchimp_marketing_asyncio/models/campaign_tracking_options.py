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


class CampaignTrackingOptions(object):
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
        'opens': 'bool',
        'html_clicks': 'bool',
        'text_clicks': 'bool',
        'goal_tracking': 'bool',
        'ecomm360': 'bool',
        'google_analytics': 'str',
        'clicktale': 'str',
        'salesforce': 'SalesforceCRMTracking',
        'capsule': 'CapsuleCRMTracking1'
    }

    attribute_map = {
        'opens': 'opens',
        'html_clicks': 'html_clicks',
        'text_clicks': 'text_clicks',
        'goal_tracking': 'goal_tracking',
        'ecomm360': 'ecomm360',
        'google_analytics': 'google_analytics',
        'clicktale': 'clicktale',
        'salesforce': 'salesforce',
        'capsule': 'capsule'
    }

    def __init__(self, opens=None, html_clicks=None, text_clicks=None, goal_tracking=None, ecomm360=None, google_analytics=None, clicktale=None, salesforce=None, capsule=None):  # noqa: E501
        """CampaignTrackingOptions - a model defined in Swagger"""  # noqa: E501

        self._opens = None
        self._html_clicks = None
        self._text_clicks = None
        self._goal_tracking = None
        self._ecomm360 = None
        self._google_analytics = None
        self._clicktale = None
        self._salesforce = None
        self._capsule = None
        self.discriminator = None

        if opens is not None:
            self.opens = opens
        if html_clicks is not None:
            self.html_clicks = html_clicks
        if text_clicks is not None:
            self.text_clicks = text_clicks
        if goal_tracking is not None:
            self.goal_tracking = goal_tracking
        if ecomm360 is not None:
            self.ecomm360 = ecomm360
        if google_analytics is not None:
            self.google_analytics = google_analytics
        if clicktale is not None:
            self.clicktale = clicktale
        if salesforce is not None:
            self.salesforce = salesforce
        if capsule is not None:
            self.capsule = capsule

    @property
    def opens(self):
        """Gets the opens of this CampaignTrackingOptions.  # noqa: E501

        Whether to [track opens](https://mailchimp.com/help/about-open-tracking/). Defaults to `true`.  # noqa: E501

        :return: The opens of this CampaignTrackingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this CampaignTrackingOptions.

        Whether to [track opens](https://mailchimp.com/help/about-open-tracking/). Defaults to `true`.  # noqa: E501

        :param opens: The opens of this CampaignTrackingOptions.  # noqa: E501
        :type: bool
        """

        self._opens = opens

    @property
    def html_clicks(self):
        """Gets the html_clicks of this CampaignTrackingOptions.  # noqa: E501

        Whether to [track clicks](https://mailchimp.com/help/enable-and-view-click-tracking/) in the HTML version of the campaign. Defaults to `true`.  # noqa: E501

        :return: The html_clicks of this CampaignTrackingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._html_clicks

    @html_clicks.setter
    def html_clicks(self, html_clicks):
        """Sets the html_clicks of this CampaignTrackingOptions.

        Whether to [track clicks](https://mailchimp.com/help/enable-and-view-click-tracking/) in the HTML version of the campaign. Defaults to `true`.  # noqa: E501

        :param html_clicks: The html_clicks of this CampaignTrackingOptions.  # noqa: E501
        :type: bool
        """

        self._html_clicks = html_clicks

    @property
    def text_clicks(self):
        """Gets the text_clicks of this CampaignTrackingOptions.  # noqa: E501

        Whether to [track clicks](https://mailchimp.com/help/enable-and-view-click-tracking/) in the plain-text version of the campaign. Defaults to `true`.  # noqa: E501

        :return: The text_clicks of this CampaignTrackingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._text_clicks

    @text_clicks.setter
    def text_clicks(self, text_clicks):
        """Sets the text_clicks of this CampaignTrackingOptions.

        Whether to [track clicks](https://mailchimp.com/help/enable-and-view-click-tracking/) in the plain-text version of the campaign. Defaults to `true`.  # noqa: E501

        :param text_clicks: The text_clicks of this CampaignTrackingOptions.  # noqa: E501
        :type: bool
        """

        self._text_clicks = text_clicks

    @property
    def goal_tracking(self):
        """Gets the goal_tracking of this CampaignTrackingOptions.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The goal_tracking of this CampaignTrackingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._goal_tracking

    @goal_tracking.setter
    def goal_tracking(self, goal_tracking):
        """Sets the goal_tracking of this CampaignTrackingOptions.

        Deprecated  # noqa: E501

        :param goal_tracking: The goal_tracking of this CampaignTrackingOptions.  # noqa: E501
        :type: bool
        """

        self._goal_tracking = goal_tracking

    @property
    def ecomm360(self):
        """Gets the ecomm360 of this CampaignTrackingOptions.  # noqa: E501

        Whether to enable e-commerce tracking.  # noqa: E501

        :return: The ecomm360 of this CampaignTrackingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ecomm360

    @ecomm360.setter
    def ecomm360(self, ecomm360):
        """Sets the ecomm360 of this CampaignTrackingOptions.

        Whether to enable e-commerce tracking.  # noqa: E501

        :param ecomm360: The ecomm360 of this CampaignTrackingOptions.  # noqa: E501
        :type: bool
        """

        self._ecomm360 = ecomm360

    @property
    def google_analytics(self):
        """Gets the google_analytics of this CampaignTrackingOptions.  # noqa: E501

        The custom slug for [Google Analytics](https://mailchimp.com/help/integrate-google-analytics-with-mailchimp/) tracking (max of 50 bytes).  # noqa: E501

        :return: The google_analytics of this CampaignTrackingOptions.  # noqa: E501
        :rtype: str
        """
        return self._google_analytics

    @google_analytics.setter
    def google_analytics(self, google_analytics):
        """Sets the google_analytics of this CampaignTrackingOptions.

        The custom slug for [Google Analytics](https://mailchimp.com/help/integrate-google-analytics-with-mailchimp/) tracking (max of 50 bytes).  # noqa: E501

        :param google_analytics: The google_analytics of this CampaignTrackingOptions.  # noqa: E501
        :type: str
        """

        self._google_analytics = google_analytics

    @property
    def clicktale(self):
        """Gets the clicktale of this CampaignTrackingOptions.  # noqa: E501

        The custom slug for [Click Tale](https://mailchimp.com/help/additional-tracking-options-for-campaigns/) tracking (max of 50 bytes).  # noqa: E501

        :return: The clicktale of this CampaignTrackingOptions.  # noqa: E501
        :rtype: str
        """
        return self._clicktale

    @clicktale.setter
    def clicktale(self, clicktale):
        """Sets the clicktale of this CampaignTrackingOptions.

        The custom slug for [Click Tale](https://mailchimp.com/help/additional-tracking-options-for-campaigns/) tracking (max of 50 bytes).  # noqa: E501

        :param clicktale: The clicktale of this CampaignTrackingOptions.  # noqa: E501
        :type: str
        """

        self._clicktale = clicktale

    @property
    def salesforce(self):
        """Gets the salesforce of this CampaignTrackingOptions.  # noqa: E501


        :return: The salesforce of this CampaignTrackingOptions.  # noqa: E501
        :rtype: SalesforceCRMTracking
        """
        return self._salesforce

    @salesforce.setter
    def salesforce(self, salesforce):
        """Sets the salesforce of this CampaignTrackingOptions.


        :param salesforce: The salesforce of this CampaignTrackingOptions.  # noqa: E501
        :type: SalesforceCRMTracking
        """

        self._salesforce = salesforce

    @property
    def capsule(self):
        """Gets the capsule of this CampaignTrackingOptions.  # noqa: E501


        :return: The capsule of this CampaignTrackingOptions.  # noqa: E501
        :rtype: CapsuleCRMTracking1
        """
        return self._capsule

    @capsule.setter
    def capsule(self, capsule):
        """Sets the capsule of this CampaignTrackingOptions.


        :param capsule: The capsule of this CampaignTrackingOptions.  # noqa: E501
        :type: CapsuleCRMTracking1
        """

        self._capsule = capsule

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
        if issubclass(CampaignTrackingOptions, dict):
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
        if not isinstance(other, CampaignTrackingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
