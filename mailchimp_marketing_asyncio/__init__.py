# coding: utf-8

# flake8: noqa

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.74
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from mailchimp_marketing_asyncio.api.account_export_api import AccountExportApi
from mailchimp_marketing_asyncio.api.account_exports_api import AccountExportsApi
from mailchimp_marketing_asyncio.api.activity_feed_api import ActivityFeedApi
from mailchimp_marketing_asyncio.api.authorized_apps_api import AuthorizedAppsApi
from mailchimp_marketing_asyncio.api.automations_api import AutomationsApi
from mailchimp_marketing_asyncio.api.batch_webhooks_api import BatchWebhooksApi
from mailchimp_marketing_asyncio.api.batches_api import BatchesApi
from mailchimp_marketing_asyncio.api.campaign_folders_api import CampaignFoldersApi
from mailchimp_marketing_asyncio.api.campaigns_api import CampaignsApi
from mailchimp_marketing_asyncio.api.connected_sites_api import ConnectedSitesApi
from mailchimp_marketing_asyncio.api.conversations_api import ConversationsApi
from mailchimp_marketing_asyncio.api.customer_journeys_api import CustomerJourneysApi
from mailchimp_marketing_asyncio.api.ecommerce_api import EcommerceApi
from mailchimp_marketing_asyncio.api.facebook_ads_api import FacebookAdsApi
from mailchimp_marketing_asyncio.api.file_manager_api import FileManagerApi
from mailchimp_marketing_asyncio.api.landing_pages_api import LandingPagesApi
from mailchimp_marketing_asyncio.api.lists_api import ListsApi
from mailchimp_marketing_asyncio.api.ping_api import PingApi
from mailchimp_marketing_asyncio.api.reporting_api import ReportingApi
from mailchimp_marketing_asyncio.api.reports_api import ReportsApi
from mailchimp_marketing_asyncio.api.root_api import RootApi
from mailchimp_marketing_asyncio.api.search_campaigns_api import SearchCampaignsApi
from mailchimp_marketing_asyncio.api.search_members_api import SearchMembersApi
from mailchimp_marketing_asyncio.api.template_folders_api import TemplateFoldersApi
from mailchimp_marketing_asyncio.api.templates_api import TemplatesApi
from mailchimp_marketing_asyncio.api.verified_domains_api import VerifiedDomainsApi


from mailchimp_marketing_asyncio.api_client import ApiClient
from mailchimp_marketing_asyncio.configuration import Configuration

class Client(object):
  def __init__(self, config = {}):
    self.api_client = ApiClient(config)

    self.accountExport = AccountExportApi(self.api_client)
    self.accountExports = AccountExportsApi(self.api_client)
    self.activityFeed = ActivityFeedApi(self.api_client)
    self.authorizedApps = AuthorizedAppsApi(self.api_client)
    self.automations = AutomationsApi(self.api_client)
    self.batchWebhooks = BatchWebhooksApi(self.api_client)
    self.batches = BatchesApi(self.api_client)
    self.campaignFolders = CampaignFoldersApi(self.api_client)
    self.campaigns = CampaignsApi(self.api_client)
    self.connectedSites = ConnectedSitesApi(self.api_client)
    self.conversations = ConversationsApi(self.api_client)
    self.customerJourneys = CustomerJourneysApi(self.api_client)
    self.ecommerce = EcommerceApi(self.api_client)
    self.facebookAds = FacebookAdsApi(self.api_client)
    self.fileManager = FileManagerApi(self.api_client)
    self.landingPages = LandingPagesApi(self.api_client)
    self.lists = ListsApi(self.api_client)
    self.ping = PingApi(self.api_client)
    self.reporting = ReportingApi(self.api_client)
    self.reports = ReportsApi(self.api_client)
    self.root = RootApi(self.api_client)
    self.searchCampaigns = SearchCampaignsApi(self.api_client)
    self.searchMembers = SearchMembersApi(self.api_client)
    self.templateFolders = TemplateFoldersApi(self.api_client)
    self.templates = TemplatesApi(self.api_client)
    self.verifiedDomains = VerifiedDomainsApi(self.api_client)
    

  def set_config(self, config = {}):
    self.api_client.set_config(config)
