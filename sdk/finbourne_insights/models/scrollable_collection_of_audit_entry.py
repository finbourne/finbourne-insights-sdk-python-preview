# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.340
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


class ScrollableCollectionOfAuditEntry(object):
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
        'data': 'list[AuditEntry]',
        'state': 'str'
    }

    attribute_map = {
        'data': 'data',
        'state': 'state'
    }

    required_map = {
        'data': 'optional',
        'state': 'optional'
    }

    def __init__(self, data=None, state=None, local_vars_configuration=None):  # noqa: E501
        """ScrollableCollectionOfAuditEntry - a model defined in OpenAPI"
        
        :param data: 
        :type data: list[finbourne_insights.AuditEntry]
        :param state: 
        :type state: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._state = None
        self.discriminator = None

        self.data = data
        self.state = state

    @property
    def data(self):
        """Gets the data of this ScrollableCollectionOfAuditEntry.  # noqa: E501


        :return: The data of this ScrollableCollectionOfAuditEntry.  # noqa: E501
        :rtype: list[finbourne_insights.AuditEntry]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ScrollableCollectionOfAuditEntry.


        :param data: The data of this ScrollableCollectionOfAuditEntry.  # noqa: E501
        :type data: list[finbourne_insights.AuditEntry]
        """

        self._data = data

    @property
    def state(self):
        """Gets the state of this ScrollableCollectionOfAuditEntry.  # noqa: E501


        :return: The state of this ScrollableCollectionOfAuditEntry.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ScrollableCollectionOfAuditEntry.


        :param state: The state of this ScrollableCollectionOfAuditEntry.  # noqa: E501
        :type state: str
        """

        self._state = state

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
        if not isinstance(other, ScrollableCollectionOfAuditEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScrollableCollectionOfAuditEntry):
            return True

        return self.to_dict() != other.to_dict()
