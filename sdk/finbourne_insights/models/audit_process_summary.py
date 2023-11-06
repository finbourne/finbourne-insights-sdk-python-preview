# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.745
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_insights.configuration import Configuration


class AuditProcessSummary(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'process': 'AuditProcess',
        'latest_entry': 'AuditData',
        'summary': 'AuditDataSummary'
    }

    attribute_map = {
        'process': 'process',
        'latest_entry': 'latestEntry',
        'summary': 'summary'
    }

    required_map = {
        'process': 'optional',
        'latest_entry': 'optional',
        'summary': 'optional'
    }

    def __init__(self, process=None, latest_entry=None, summary=None, local_vars_configuration=None):  # noqa: E501
        """AuditProcessSummary - a model defined in OpenAPI"
        
        :param process: 
        :type process: finbourne_insights.AuditProcess
        :param latest_entry: 
        :type latest_entry: finbourne_insights.AuditData
        :param summary: 
        :type summary: finbourne_insights.AuditDataSummary

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._process = None
        self._latest_entry = None
        self._summary = None
        self.discriminator = None

        if process is not None:
            self.process = process
        if latest_entry is not None:
            self.latest_entry = latest_entry
        if summary is not None:
            self.summary = summary

    @property
    def process(self):
        """Gets the process of this AuditProcessSummary.  # noqa: E501


        :return: The process of this AuditProcessSummary.  # noqa: E501
        :rtype: finbourne_insights.AuditProcess
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this AuditProcessSummary.


        :param process: The process of this AuditProcessSummary.  # noqa: E501
        :type process: finbourne_insights.AuditProcess
        """

        self._process = process

    @property
    def latest_entry(self):
        """Gets the latest_entry of this AuditProcessSummary.  # noqa: E501


        :return: The latest_entry of this AuditProcessSummary.  # noqa: E501
        :rtype: finbourne_insights.AuditData
        """
        return self._latest_entry

    @latest_entry.setter
    def latest_entry(self, latest_entry):
        """Sets the latest_entry of this AuditProcessSummary.


        :param latest_entry: The latest_entry of this AuditProcessSummary.  # noqa: E501
        :type latest_entry: finbourne_insights.AuditData
        """

        self._latest_entry = latest_entry

    @property
    def summary(self):
        """Gets the summary of this AuditProcessSummary.  # noqa: E501


        :return: The summary of this AuditProcessSummary.  # noqa: E501
        :rtype: finbourne_insights.AuditDataSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AuditProcessSummary.


        :param summary: The summary of this AuditProcessSummary.  # noqa: E501
        :type summary: finbourne_insights.AuditDataSummary
        """

        self._summary = summary

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditProcessSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditProcessSummary):
            return True

        return self.to_dict() != other.to_dict()
