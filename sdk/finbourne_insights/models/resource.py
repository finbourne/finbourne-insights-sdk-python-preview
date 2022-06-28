# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.299
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


class Resource(object):
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
        'type': 'str',
        'identifier': 'str'
    }

    attribute_map = {
        'type': 'type',
        'identifier': 'identifier'
    }

    required_map = {
        'type': 'optional',
        'identifier': 'optional'
    }

    def __init__(self, type=None, identifier=None, local_vars_configuration=None):  # noqa: E501
        """Resource - a model defined in OpenAPI"
        
        :param type: 
        :type type: str
        :param identifier: 
        :type identifier: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._identifier = None
        self.discriminator = None

        self.type = type
        self.identifier = identifier

    @property
    def type(self):
        """Gets the type of this Resource.  # noqa: E501


        :return: The type of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.


        :param type: The type of this Resource.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 64):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 0):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

    @property
    def identifier(self):
        """Gets the identifier of this Resource.  # noqa: E501


        :return: The identifier of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Resource.


        :param identifier: The identifier of this Resource.  # noqa: E501
        :type identifier: str
        """
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) > 128):
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) < 0):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `0`")  # noqa: E501

        self._identifier = identifier

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
        if not isinstance(other, Resource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Resource):
            return True

        return self.to_dict() != other.to_dict()
