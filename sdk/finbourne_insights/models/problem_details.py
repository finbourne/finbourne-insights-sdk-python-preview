# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.799
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


class ProblemDetails(object):
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
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance'
    }

    required_map = {
        'type': 'optional',
        'title': 'optional',
        'status': 'optional',
        'detail': 'optional',
        'instance': 'optional'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, local_vars_configuration=None):  # noqa: E501
        """ProblemDetails - a model defined in OpenAPI"
        
        :param type: 
        :type type: str
        :param title: 
        :type title: str
        :param status: 
        :type status: int
        :param detail: 
        :type detail: str
        :param instance: 
        :type instance: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self.discriminator = None

        self.type = type
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance

    @property
    def type(self):
        """Gets the type of this ProblemDetails.  # noqa: E501


        :return: The type of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetails.


        :param type: The type of this ProblemDetails.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this ProblemDetails.  # noqa: E501


        :return: The title of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetails.


        :param title: The title of this ProblemDetails.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this ProblemDetails.  # noqa: E501


        :return: The status of this ProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetails.


        :param status: The status of this ProblemDetails.  # noqa: E501
        :type status: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ProblemDetails.  # noqa: E501


        :return: The detail of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetails.


        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type detail: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetails.  # noqa: E501


        :return: The instance of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetails.


        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

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
        if not isinstance(other, ProblemDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProblemDetails):
            return True

        return self.to_dict() != other.to_dict()
