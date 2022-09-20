# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.362
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


class VendorLog(object):
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
        'id': 'str',
        'provider': 'str',
        'timestamp': 'datetime',
        'type': 'str',
        'destination_url': 'str',
        'operation': 'str',
        'outcome': 'str',
        'duration': 'float',
        'http_status_code': 'int',
        'user_id': 'str',
        'request_id': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'provider': 'provider',
        'timestamp': 'timestamp',
        'type': 'type',
        'destination_url': 'destinationUrl',
        'operation': 'operation',
        'outcome': 'outcome',
        'duration': 'duration',
        'http_status_code': 'httpStatusCode',
        'user_id': 'userId',
        'request_id': 'requestId',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'provider': 'required',
        'timestamp': 'required',
        'type': 'required',
        'destination_url': 'required',
        'operation': 'required',
        'outcome': 'required',
        'duration': 'required',
        'http_status_code': 'required',
        'user_id': 'required',
        'request_id': 'required',
        'links': 'optional'
    }

    def __init__(self, id=None, provider=None, timestamp=None, type=None, destination_url=None, operation=None, outcome=None, duration=None, http_status_code=None, user_id=None, request_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """VendorLog - a model defined in OpenAPI"
        
        :param id:  The identifier of a log entry. (required)
        :type id: str
        :param provider:  The provider or service name. (required)
        :type provider: str
        :param timestamp:  Timestamp of when the log was generated. (required)
        :type timestamp: datetime
        :param type:  Type of log. Possible values: HttpResponse. (required)
        :type type: str
        :param destination_url:  The destination URL of the task. (required)
        :type destination_url: str
        :param operation:  The operation performed. Possible values: Evaluate. (required)
        :type operation: str
        :param outcome:  The outcome of the operation. Possible values: Success, Failure. (required)
        :type outcome: str
        :param duration:  The duration of the operation in ms. (required)
        :type duration: float
        :param http_status_code:  The status code of the operation. (required)
        :type http_status_code: int
        :param user_id:  The user that made the request to LUSID. (required)
        :type user_id: str
        :param request_id:  The ID of the request to LUSID. (required)
        :type request_id: str
        :param links: 
        :type links: list[finbourne_insights.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._provider = None
        self._timestamp = None
        self._type = None
        self._destination_url = None
        self._operation = None
        self._outcome = None
        self._duration = None
        self._http_status_code = None
        self._user_id = None
        self._request_id = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.provider = provider
        self.timestamp = timestamp
        self.type = type
        self.destination_url = destination_url
        self.operation = operation
        self.outcome = outcome
        self.duration = duration
        self.http_status_code = http_status_code
        self.user_id = user_id
        self.request_id = request_id
        self.links = links

    @property
    def id(self):
        """Gets the id of this VendorLog.  # noqa: E501

        The identifier of a log entry.  # noqa: E501

        :return: The id of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VendorLog.

        The identifier of a log entry.  # noqa: E501

        :param id: The id of this VendorLog.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def provider(self):
        """Gets the provider of this VendorLog.  # noqa: E501

        The provider or service name.  # noqa: E501

        :return: The provider of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VendorLog.

        The provider or service name.  # noqa: E501

        :param provider: The provider of this VendorLog.  # noqa: E501
        :type provider: str
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def timestamp(self):
        """Gets the timestamp of this VendorLog.  # noqa: E501

        Timestamp of when the log was generated.  # noqa: E501

        :return: The timestamp of this VendorLog.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VendorLog.

        Timestamp of when the log was generated.  # noqa: E501

        :param timestamp: The timestamp of this VendorLog.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this VendorLog.  # noqa: E501

        Type of log. Possible values: HttpResponse.  # noqa: E501

        :return: The type of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VendorLog.

        Type of log. Possible values: HttpResponse.  # noqa: E501

        :param type: The type of this VendorLog.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def destination_url(self):
        """Gets the destination_url of this VendorLog.  # noqa: E501

        The destination URL of the task.  # noqa: E501

        :return: The destination_url of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._destination_url

    @destination_url.setter
    def destination_url(self, destination_url):
        """Sets the destination_url of this VendorLog.

        The destination URL of the task.  # noqa: E501

        :param destination_url: The destination_url of this VendorLog.  # noqa: E501
        :type destination_url: str
        """
        if self.local_vars_configuration.client_side_validation and destination_url is None:  # noqa: E501
            raise ValueError("Invalid value for `destination_url`, must not be `None`")  # noqa: E501

        self._destination_url = destination_url

    @property
    def operation(self):
        """Gets the operation of this VendorLog.  # noqa: E501

        The operation performed. Possible values: Evaluate.  # noqa: E501

        :return: The operation of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this VendorLog.

        The operation performed. Possible values: Evaluate.  # noqa: E501

        :param operation: The operation of this VendorLog.  # noqa: E501
        :type operation: str
        """
        if self.local_vars_configuration.client_side_validation and operation is None:  # noqa: E501
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def outcome(self):
        """Gets the outcome of this VendorLog.  # noqa: E501

        The outcome of the operation. Possible values: Success, Failure.  # noqa: E501

        :return: The outcome of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this VendorLog.

        The outcome of the operation. Possible values: Success, Failure.  # noqa: E501

        :param outcome: The outcome of this VendorLog.  # noqa: E501
        :type outcome: str
        """
        if self.local_vars_configuration.client_side_validation and outcome is None:  # noqa: E501
            raise ValueError("Invalid value for `outcome`, must not be `None`")  # noqa: E501

        self._outcome = outcome

    @property
    def duration(self):
        """Gets the duration of this VendorLog.  # noqa: E501

        The duration of the operation in ms.  # noqa: E501

        :return: The duration of this VendorLog.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this VendorLog.

        The duration of the operation in ms.  # noqa: E501

        :param duration: The duration of this VendorLog.  # noqa: E501
        :type duration: float
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def http_status_code(self):
        """Gets the http_status_code of this VendorLog.  # noqa: E501

        The status code of the operation.  # noqa: E501

        :return: The http_status_code of this VendorLog.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this VendorLog.

        The status code of the operation.  # noqa: E501

        :param http_status_code: The http_status_code of this VendorLog.  # noqa: E501
        :type http_status_code: int
        """
        if self.local_vars_configuration.client_side_validation and http_status_code is None:  # noqa: E501
            raise ValueError("Invalid value for `http_status_code`, must not be `None`")  # noqa: E501

        self._http_status_code = http_status_code

    @property
    def user_id(self):
        """Gets the user_id of this VendorLog.  # noqa: E501

        The user that made the request to LUSID.  # noqa: E501

        :return: The user_id of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this VendorLog.

        The user that made the request to LUSID.  # noqa: E501

        :param user_id: The user_id of this VendorLog.  # noqa: E501
        :type user_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def request_id(self):
        """Gets the request_id of this VendorLog.  # noqa: E501

        The ID of the request to LUSID.  # noqa: E501

        :return: The request_id of this VendorLog.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this VendorLog.

        The ID of the request to LUSID.  # noqa: E501

        :param request_id: The request_id of this VendorLog.  # noqa: E501
        :type request_id: str
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def links(self):
        """Gets the links of this VendorLog.  # noqa: E501


        :return: The links of this VendorLog.  # noqa: E501
        :rtype: list[finbourne_insights.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VendorLog.


        :param links: The links of this VendorLog.  # noqa: E501
        :type links: list[finbourne_insights.Link]
        """

        self._links = links

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
        if not isinstance(other, VendorLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VendorLog):
            return True

        return self.to_dict() != other.to_dict()
