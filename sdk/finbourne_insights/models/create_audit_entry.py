# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.368
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


class CreateAuditEntry(object):
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
        'data': 'AuditData'
    }

    attribute_map = {
        'process': 'process',
        'data': 'data'
    }

    required_map = {
        'process': 'required',
        'data': 'required'
    }

    def __init__(self, process=None, data=None, local_vars_configuration=None):  # noqa: E501
        """CreateAuditEntry - a model defined in OpenAPI"
        
        :param process:  (required)
        :type process: finbourne_insights.AuditProcess
        :param data:  (required)
        :type data: finbourne_insights.AuditData

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._process = None
        self._data = None
        self.discriminator = None

        self.process = process
        self.data = data

    @property
    def process(self):
        """Gets the process of this CreateAuditEntry.  # noqa: E501


        :return: The process of this CreateAuditEntry.  # noqa: E501
        :rtype: finbourne_insights.AuditProcess
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this CreateAuditEntry.


        :param process: The process of this CreateAuditEntry.  # noqa: E501
        :type process: finbourne_insights.AuditProcess
        """
        if self.local_vars_configuration.client_side_validation and process is None:  # noqa: E501
            raise ValueError("Invalid value for `process`, must not be `None`")  # noqa: E501

        self._process = process

    @property
    def data(self):
        """Gets the data of this CreateAuditEntry.  # noqa: E501


        :return: The data of this CreateAuditEntry.  # noqa: E501
        :rtype: finbourne_insights.AuditData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateAuditEntry.


        :param data: The data of this CreateAuditEntry.  # noqa: E501
        :type data: finbourne_insights.AuditData
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, CreateAuditEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAuditEntry):
            return True

        return self.to_dict() != other.to_dict()
