# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.269
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


class AuditProcess(object):
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
        'name': 'str',
        'run_id': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'succeeded': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'run_id': 'runId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'succeeded': 'succeeded'
    }

    required_map = {
        'name': 'required',
        'run_id': 'required',
        'start_time': 'required',
        'end_time': 'optional',
        'succeeded': 'optional'
    }

    def __init__(self, name=None, run_id=None, start_time=None, end_time=None, succeeded=None, local_vars_configuration=None):  # noqa: E501
        """AuditProcess - a model defined in OpenAPI"
        
        :param name:  (required)
        :type name: str
        :param run_id:  (required)
        :type run_id: str
        :param start_time:  (required)
        :type start_time: datetime
        :param end_time: 
        :type end_time: datetime
        :param succeeded: 
        :type succeeded: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._run_id = None
        self._start_time = None
        self._end_time = None
        self._succeeded = None
        self.discriminator = None

        self.name = name
        self.run_id = run_id
        self.start_time = start_time
        self.end_time = end_time
        self.succeeded = succeeded

    @property
    def name(self):
        """Gets the name of this AuditProcess.  # noqa: E501


        :return: The name of this AuditProcess.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditProcess.


        :param name: The name of this AuditProcess.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def run_id(self):
        """Gets the run_id of this AuditProcess.  # noqa: E501


        :return: The run_id of this AuditProcess.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this AuditProcess.


        :param run_id: The run_id of this AuditProcess.  # noqa: E501
        :type run_id: str
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def start_time(self):
        """Gets the start_time of this AuditProcess.  # noqa: E501


        :return: The start_time of this AuditProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AuditProcess.


        :param start_time: The start_time of this AuditProcess.  # noqa: E501
        :type start_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AuditProcess.  # noqa: E501


        :return: The end_time of this AuditProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AuditProcess.


        :param end_time: The end_time of this AuditProcess.  # noqa: E501
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def succeeded(self):
        """Gets the succeeded of this AuditProcess.  # noqa: E501


        :return: The succeeded of this AuditProcess.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this AuditProcess.


        :param succeeded: The succeeded of this AuditProcess.  # noqa: E501
        :type succeeded: bool
        """

        self._succeeded = succeeded

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
        if not isinstance(other, AuditProcess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditProcess):
            return True

        return self.to_dict() != other.to_dict()
