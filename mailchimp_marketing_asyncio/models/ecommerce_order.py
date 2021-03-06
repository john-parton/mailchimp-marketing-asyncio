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


class EcommerceOrder(object):
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
        'customer': 'EcommerceCustomer',
        'store_id': 'str',
        'campaign_id': 'str',
        'landing_site': 'str',
        'financial_status': 'str',
        'fulfillment_status': 'str',
        'currency_code': 'str',
        'order_total': 'float',
        'order_url': 'str',
        'discount_total': 'float',
        'tax_total': 'float',
        'shipping_total': 'float',
        'tracking_code': 'str',
        'processed_at_foreign': 'datetime',
        'cancelled_at_foreign': 'datetime',
        'updated_at_foreign': 'datetime',
        'shipping_address': 'ShippingAddress',
        'billing_address': 'BillingAddress',
        'promos': 'list[OrdersPromos]',
        'lines': 'list[EcommerceOrderLineItem]',
        'outreach': 'Outreach',
        'tracking_number': 'str',
        'tracking_carrier': 'str',
        'tracking_url': 'str',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'customer': 'customer',
        'store_id': 'store_id',
        'campaign_id': 'campaign_id',
        'landing_site': 'landing_site',
        'financial_status': 'financial_status',
        'fulfillment_status': 'fulfillment_status',
        'currency_code': 'currency_code',
        'order_total': 'order_total',
        'order_url': 'order_url',
        'discount_total': 'discount_total',
        'tax_total': 'tax_total',
        'shipping_total': 'shipping_total',
        'tracking_code': 'tracking_code',
        'processed_at_foreign': 'processed_at_foreign',
        'cancelled_at_foreign': 'cancelled_at_foreign',
        'updated_at_foreign': 'updated_at_foreign',
        'shipping_address': 'shipping_address',
        'billing_address': 'billing_address',
        'promos': 'promos',
        'lines': 'lines',
        'outreach': 'outreach',
        'tracking_number': 'tracking_number',
        'tracking_carrier': 'tracking_carrier',
        'tracking_url': 'tracking_url',
        'links': '_links'
    }

    def __init__(self, id=None, customer=None, store_id=None, campaign_id=None, landing_site=None, financial_status=None, fulfillment_status=None, currency_code=None, order_total=None, order_url=None, discount_total=None, tax_total=None, shipping_total=None, tracking_code=None, processed_at_foreign=None, cancelled_at_foreign=None, updated_at_foreign=None, shipping_address=None, billing_address=None, promos=None, lines=None, outreach=None, tracking_number=None, tracking_carrier=None, tracking_url=None, links=None):  # noqa: E501
        """EcommerceOrder - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._customer = None
        self._store_id = None
        self._campaign_id = None
        self._landing_site = None
        self._financial_status = None
        self._fulfillment_status = None
        self._currency_code = None
        self._order_total = None
        self._order_url = None
        self._discount_total = None
        self._tax_total = None
        self._shipping_total = None
        self._tracking_code = None
        self._processed_at_foreign = None
        self._cancelled_at_foreign = None
        self._updated_at_foreign = None
        self._shipping_address = None
        self._billing_address = None
        self._promos = None
        self._lines = None
        self._outreach = None
        self._tracking_number = None
        self._tracking_carrier = None
        self._tracking_url = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if customer is not None:
            self.customer = customer
        if store_id is not None:
            self.store_id = store_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if landing_site is not None:
            self.landing_site = landing_site
        if financial_status is not None:
            self.financial_status = financial_status
        if fulfillment_status is not None:
            self.fulfillment_status = fulfillment_status
        if currency_code is not None:
            self.currency_code = currency_code
        if order_total is not None:
            self.order_total = order_total
        if order_url is not None:
            self.order_url = order_url
        if discount_total is not None:
            self.discount_total = discount_total
        if tax_total is not None:
            self.tax_total = tax_total
        if shipping_total is not None:
            self.shipping_total = shipping_total
        if tracking_code is not None:
            self.tracking_code = tracking_code
        if processed_at_foreign is not None:
            self.processed_at_foreign = processed_at_foreign
        if cancelled_at_foreign is not None:
            self.cancelled_at_foreign = cancelled_at_foreign
        if updated_at_foreign is not None:
            self.updated_at_foreign = updated_at_foreign
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if billing_address is not None:
            self.billing_address = billing_address
        if promos is not None:
            self.promos = promos
        if lines is not None:
            self.lines = lines
        if outreach is not None:
            self.outreach = outreach
        if tracking_number is not None:
            self.tracking_number = tracking_number
        if tracking_carrier is not None:
            self.tracking_carrier = tracking_carrier
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommerceOrder.  # noqa: E501

        A unique identifier for the order.  # noqa: E501

        :return: The id of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommerceOrder.

        A unique identifier for the order.  # noqa: E501

        :param id: The id of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this EcommerceOrder.  # noqa: E501


        :return: The customer of this EcommerceOrder.  # noqa: E501
        :rtype: EcommerceCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this EcommerceOrder.


        :param customer: The customer of this EcommerceOrder.  # noqa: E501
        :type: EcommerceCustomer
        """

        self._customer = customer

    @property
    def store_id(self):
        """Gets the store_id of this EcommerceOrder.  # noqa: E501

        The unique identifier for the store.  # noqa: E501

        :return: The store_id of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this EcommerceOrder.

        The unique identifier for the store.  # noqa: E501

        :param store_id: The store_id of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this EcommerceOrder.  # noqa: E501

        A string that uniquely identifies the campaign associated with an order.  # noqa: E501

        :return: The campaign_id of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this EcommerceOrder.

        A string that uniquely identifies the campaign associated with an order.  # noqa: E501

        :param campaign_id: The campaign_id of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def landing_site(self):
        """Gets the landing_site of this EcommerceOrder.  # noqa: E501

        The URL for the page where the buyer landed when entering the shop.  # noqa: E501

        :return: The landing_site of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._landing_site

    @landing_site.setter
    def landing_site(self, landing_site):
        """Sets the landing_site of this EcommerceOrder.

        The URL for the page where the buyer landed when entering the shop.  # noqa: E501

        :param landing_site: The landing_site of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._landing_site = landing_site

    @property
    def financial_status(self):
        """Gets the financial_status of this EcommerceOrder.  # noqa: E501

        The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).  # noqa: E501

        :return: The financial_status of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._financial_status

    @financial_status.setter
    def financial_status(self, financial_status):
        """Sets the financial_status of this EcommerceOrder.

        The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).  # noqa: E501

        :param financial_status: The financial_status of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._financial_status = financial_status

    @property
    def fulfillment_status(self):
        """Gets the fulfillment_status of this EcommerceOrder.  # noqa: E501

        The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).  # noqa: E501

        :return: The fulfillment_status of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, fulfillment_status):
        """Sets the fulfillment_status of this EcommerceOrder.

        The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).  # noqa: E501

        :param fulfillment_status: The fulfillment_status of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._fulfillment_status = fulfillment_status

    @property
    def currency_code(self):
        """Gets the currency_code of this EcommerceOrder.  # noqa: E501

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :return: The currency_code of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this EcommerceOrder.

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :param currency_code: The currency_code of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def order_total(self):
        """Gets the order_total of this EcommerceOrder.  # noqa: E501

        The order total associated with an order.  # noqa: E501

        :return: The order_total of this EcommerceOrder.  # noqa: E501
        :rtype: float
        """
        return self._order_total

    @order_total.setter
    def order_total(self, order_total):
        """Sets the order_total of this EcommerceOrder.

        The order total associated with an order.  # noqa: E501

        :param order_total: The order_total of this EcommerceOrder.  # noqa: E501
        :type: float
        """

        self._order_total = order_total

    @property
    def order_url(self):
        """Gets the order_url of this EcommerceOrder.  # noqa: E501

        The URL for the order.  # noqa: E501

        :return: The order_url of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_url

    @order_url.setter
    def order_url(self, order_url):
        """Sets the order_url of this EcommerceOrder.

        The URL for the order.  # noqa: E501

        :param order_url: The order_url of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._order_url = order_url

    @property
    def discount_total(self):
        """Gets the discount_total of this EcommerceOrder.  # noqa: E501

        The total amount of the discounts to be applied to the price of the order.  # noqa: E501

        :return: The discount_total of this EcommerceOrder.  # noqa: E501
        :rtype: float
        """
        return self._discount_total

    @discount_total.setter
    def discount_total(self, discount_total):
        """Sets the discount_total of this EcommerceOrder.

        The total amount of the discounts to be applied to the price of the order.  # noqa: E501

        :param discount_total: The discount_total of this EcommerceOrder.  # noqa: E501
        :type: float
        """

        self._discount_total = discount_total

    @property
    def tax_total(self):
        """Gets the tax_total of this EcommerceOrder.  # noqa: E501

        The tax total associated with an order.  # noqa: E501

        :return: The tax_total of this EcommerceOrder.  # noqa: E501
        :rtype: float
        """
        return self._tax_total

    @tax_total.setter
    def tax_total(self, tax_total):
        """Sets the tax_total of this EcommerceOrder.

        The tax total associated with an order.  # noqa: E501

        :param tax_total: The tax_total of this EcommerceOrder.  # noqa: E501
        :type: float
        """

        self._tax_total = tax_total

    @property
    def shipping_total(self):
        """Gets the shipping_total of this EcommerceOrder.  # noqa: E501

        The shipping total for the order.  # noqa: E501

        :return: The shipping_total of this EcommerceOrder.  # noqa: E501
        :rtype: float
        """
        return self._shipping_total

    @shipping_total.setter
    def shipping_total(self, shipping_total):
        """Sets the shipping_total of this EcommerceOrder.

        The shipping total for the order.  # noqa: E501

        :param shipping_total: The shipping_total of this EcommerceOrder.  # noqa: E501
        :type: float
        """

        self._shipping_total = shipping_total

    @property
    def tracking_code(self):
        """Gets the tracking_code of this EcommerceOrder.  # noqa: E501

        The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.  # noqa: E501

        :return: The tracking_code of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._tracking_code

    @tracking_code.setter
    def tracking_code(self, tracking_code):
        """Sets the tracking_code of this EcommerceOrder.

        The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.  # noqa: E501

        :param tracking_code: The tracking_code of this EcommerceOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["prec"]  # noqa: E501
        if tracking_code not in allowed_values:
            raise ValueError(
                "Invalid value for `tracking_code` ({0}), must be one of {1}"  # noqa: E501
                .format(tracking_code, allowed_values)
            )

        self._tracking_code = tracking_code

    @property
    def processed_at_foreign(self):
        """Gets the processed_at_foreign of this EcommerceOrder.  # noqa: E501

        The date and time the order was processed in ISO 8601 format.  # noqa: E501

        :return: The processed_at_foreign of this EcommerceOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._processed_at_foreign

    @processed_at_foreign.setter
    def processed_at_foreign(self, processed_at_foreign):
        """Sets the processed_at_foreign of this EcommerceOrder.

        The date and time the order was processed in ISO 8601 format.  # noqa: E501

        :param processed_at_foreign: The processed_at_foreign of this EcommerceOrder.  # noqa: E501
        :type: datetime
        """

        self._processed_at_foreign = processed_at_foreign

    @property
    def cancelled_at_foreign(self):
        """Gets the cancelled_at_foreign of this EcommerceOrder.  # noqa: E501

        The date and time the order was cancelled in ISO 8601 format.  # noqa: E501

        :return: The cancelled_at_foreign of this EcommerceOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled_at_foreign

    @cancelled_at_foreign.setter
    def cancelled_at_foreign(self, cancelled_at_foreign):
        """Sets the cancelled_at_foreign of this EcommerceOrder.

        The date and time the order was cancelled in ISO 8601 format.  # noqa: E501

        :param cancelled_at_foreign: The cancelled_at_foreign of this EcommerceOrder.  # noqa: E501
        :type: datetime
        """

        self._cancelled_at_foreign = cancelled_at_foreign

    @property
    def updated_at_foreign(self):
        """Gets the updated_at_foreign of this EcommerceOrder.  # noqa: E501

        The date and time the order was updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at_foreign of this EcommerceOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_foreign

    @updated_at_foreign.setter
    def updated_at_foreign(self, updated_at_foreign):
        """Sets the updated_at_foreign of this EcommerceOrder.

        The date and time the order was updated in ISO 8601 format.  # noqa: E501

        :param updated_at_foreign: The updated_at_foreign of this EcommerceOrder.  # noqa: E501
        :type: datetime
        """

        self._updated_at_foreign = updated_at_foreign

    @property
    def shipping_address(self):
        """Gets the shipping_address of this EcommerceOrder.  # noqa: E501


        :return: The shipping_address of this EcommerceOrder.  # noqa: E501
        :rtype: ShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this EcommerceOrder.


        :param shipping_address: The shipping_address of this EcommerceOrder.  # noqa: E501
        :type: ShippingAddress
        """

        self._shipping_address = shipping_address

    @property
    def billing_address(self):
        """Gets the billing_address of this EcommerceOrder.  # noqa: E501


        :return: The billing_address of this EcommerceOrder.  # noqa: E501
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this EcommerceOrder.


        :param billing_address: The billing_address of this EcommerceOrder.  # noqa: E501
        :type: BillingAddress
        """

        self._billing_address = billing_address

    @property
    def promos(self):
        """Gets the promos of this EcommerceOrder.  # noqa: E501

        The promo codes applied on the order  # noqa: E501

        :return: The promos of this EcommerceOrder.  # noqa: E501
        :rtype: list[OrdersPromos]
        """
        return self._promos

    @promos.setter
    def promos(self, promos):
        """Sets the promos of this EcommerceOrder.

        The promo codes applied on the order  # noqa: E501

        :param promos: The promos of this EcommerceOrder.  # noqa: E501
        :type: list[OrdersPromos]
        """

        self._promos = promos

    @property
    def lines(self):
        """Gets the lines of this EcommerceOrder.  # noqa: E501

        An array of the order's line items.  # noqa: E501

        :return: The lines of this EcommerceOrder.  # noqa: E501
        :rtype: list[EcommerceOrderLineItem]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this EcommerceOrder.

        An array of the order's line items.  # noqa: E501

        :param lines: The lines of this EcommerceOrder.  # noqa: E501
        :type: list[EcommerceOrderLineItem]
        """

        self._lines = lines

    @property
    def outreach(self):
        """Gets the outreach of this EcommerceOrder.  # noqa: E501


        :return: The outreach of this EcommerceOrder.  # noqa: E501
        :rtype: Outreach
        """
        return self._outreach

    @outreach.setter
    def outreach(self, outreach):
        """Sets the outreach of this EcommerceOrder.


        :param outreach: The outreach of this EcommerceOrder.  # noqa: E501
        :type: Outreach
        """

        self._outreach = outreach

    @property
    def tracking_number(self):
        """Gets the tracking_number of this EcommerceOrder.  # noqa: E501

        The tracking number associated with the order.  # noqa: E501

        :return: The tracking_number of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this EcommerceOrder.

        The tracking number associated with the order.  # noqa: E501

        :param tracking_number: The tracking_number of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def tracking_carrier(self):
        """Gets the tracking_carrier of this EcommerceOrder.  # noqa: E501

        The tracking carrier associated with the order.  # noqa: E501

        :return: The tracking_carrier of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._tracking_carrier

    @tracking_carrier.setter
    def tracking_carrier(self, tracking_carrier):
        """Sets the tracking_carrier of this EcommerceOrder.

        The tracking carrier associated with the order.  # noqa: E501

        :param tracking_carrier: The tracking_carrier of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._tracking_carrier = tracking_carrier

    @property
    def tracking_url(self):
        """Gets the tracking_url of this EcommerceOrder.  # noqa: E501

        The tracking URL associated with the order.  # noqa: E501

        :return: The tracking_url of this EcommerceOrder.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this EcommerceOrder.

        The tracking URL associated with the order.  # noqa: E501

        :param tracking_url: The tracking_url of this EcommerceOrder.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def links(self):
        """Gets the links of this EcommerceOrder.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommerceOrder.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommerceOrder.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommerceOrder.  # noqa: E501
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
        if issubclass(EcommerceOrder, dict):
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
        if not isinstance(other, EcommerceOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
