# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.416
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


class AccessEvaluationLog(object):
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
        'timestamp': 'datetime',
        'application': 'str',
        'id': 'str',
        'request_id': 'str',
        'session_id': 'str',
        'user': 'str',
        'user_type': 'str',
        'duration': 'float',
        'result': 'str',
        'authoritative_role_id': 'str',
        'authoritative_policy_id': 'str',
        'authoritative_selector': 'str',
        'resource_type': 'str',
        'action': 'str',
        'resource': 'dict(str, str)',
        'resource_from_effective_date': 'str',
        'resource_to_effective_date': 'str',
        'resource_from_as_at': 'str',
        'resource_to_as_at': 'str',
        'access_execution_time': 'str',
        'access_as_at_time': 'str',
        'required_licence_policy_id': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'application': 'application',
        'id': 'id',
        'request_id': 'requestId',
        'session_id': 'sessionId',
        'user': 'user',
        'user_type': 'userType',
        'duration': 'duration',
        'result': 'result',
        'authoritative_role_id': 'authoritativeRoleId',
        'authoritative_policy_id': 'authoritativePolicyId',
        'authoritative_selector': 'authoritativeSelector',
        'resource_type': 'resourceType',
        'action': 'action',
        'resource': 'resource',
        'resource_from_effective_date': 'resourceFromEffectiveDate',
        'resource_to_effective_date': 'resourceToEffectiveDate',
        'resource_from_as_at': 'resourceFromAsAt',
        'resource_to_as_at': 'resourceToAsAt',
        'access_execution_time': 'accessExecutionTime',
        'access_as_at_time': 'accessAsAtTime',
        'required_licence_policy_id': 'requiredLicencePolicyId',
        'links': 'links'
    }

    required_map = {
        'timestamp': 'required',
        'application': 'required',
        'id': 'required',
        'request_id': 'optional',
        'session_id': 'optional',
        'user': 'required',
        'user_type': 'optional',
        'duration': 'required',
        'result': 'optional',
        'authoritative_role_id': 'optional',
        'authoritative_policy_id': 'optional',
        'authoritative_selector': 'optional',
        'resource_type': 'optional',
        'action': 'optional',
        'resource': 'optional',
        'resource_from_effective_date': 'optional',
        'resource_to_effective_date': 'optional',
        'resource_from_as_at': 'optional',
        'resource_to_as_at': 'optional',
        'access_execution_time': 'optional',
        'access_as_at_time': 'optional',
        'required_licence_policy_id': 'optional',
        'links': 'optional'
    }

    def __init__(self, timestamp=None, application=None, id=None, request_id=None, session_id=None, user=None, user_type=None, duration=None, result=None, authoritative_role_id=None, authoritative_policy_id=None, authoritative_selector=None, resource_type=None, action=None, resource=None, resource_from_effective_date=None, resource_to_effective_date=None, resource_from_as_at=None, resource_to_as_at=None, access_execution_time=None, access_as_at_time=None, required_licence_policy_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """AccessEvaluationLog - a model defined in OpenAPI"
        
        :param timestamp:  The timestamp of the access evaluation. (required)
        :type timestamp: datetime
        :param application:  The name of the application that the request was made from. (required)
        :type application: str
        :param id:  The ID of the access evaluation. (required)
        :type id: str
        :param request_id:  The identifier of the request.
        :type request_id: str
        :param session_id:  The identifier of the session that the request was made in.
        :type session_id: str
        :param user:  The user who made the request. (required)
        :type user: str
        :param user_type:  The type of the user who made the request.
        :type user_type: str
        :param duration:  The duration of the access evaluation. (required)
        :type duration: float
        :param result:  The result of the access evaluation.
        :type result: str
        :param authoritative_role_id:  The role that matched the access evaluation to provide a result.
        :type authoritative_role_id: str
        :param authoritative_policy_id:  The policy that matched the access evaluation to provide a result.
        :type authoritative_policy_id: str
        :param authoritative_selector:  The selector that matched the access evaluation to provide a result.
        :type authoritative_selector: str
        :param resource_type:  The type of the resource that the access evaluation is for.
        :type resource_type: str
        :param action:  The action key of the access evaluation.
        :type action: str
        :param resource:  The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \"resourceId\".
        :type resource: dict(str, str)
        :param resource_from_effective_date:  The From effective date of the resource.
        :type resource_from_effective_date: str
        :param resource_to_effective_date:  The To effective date of the resource.
        :type resource_to_effective_date: str
        :param resource_from_as_at:  The From AsAt date of the resource.
        :type resource_from_as_at: str
        :param resource_to_as_at:  The To AsAt date of the resource.
        :type resource_to_as_at: str
        :param access_execution_time:  The execution time of the entitlement.
        :type access_execution_time: str
        :param access_as_at_time:  The AsAt time of the entitlement.
        :type access_as_at_time: str
        :param required_licence_policy_id:  ID of the required licence policy.
        :type required_licence_policy_id: str
        :param links: 
        :type links: list[finbourne_insights.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._application = None
        self._id = None
        self._request_id = None
        self._session_id = None
        self._user = None
        self._user_type = None
        self._duration = None
        self._result = None
        self._authoritative_role_id = None
        self._authoritative_policy_id = None
        self._authoritative_selector = None
        self._resource_type = None
        self._action = None
        self._resource = None
        self._resource_from_effective_date = None
        self._resource_to_effective_date = None
        self._resource_from_as_at = None
        self._resource_to_as_at = None
        self._access_execution_time = None
        self._access_as_at_time = None
        self._required_licence_policy_id = None
        self._links = None
        self.discriminator = None

        self.timestamp = timestamp
        self.application = application
        self.id = id
        self.request_id = request_id
        self.session_id = session_id
        self.user = user
        self.user_type = user_type
        self.duration = duration
        self.result = result
        self.authoritative_role_id = authoritative_role_id
        self.authoritative_policy_id = authoritative_policy_id
        self.authoritative_selector = authoritative_selector
        self.resource_type = resource_type
        self.action = action
        self.resource = resource
        self.resource_from_effective_date = resource_from_effective_date
        self.resource_to_effective_date = resource_to_effective_date
        self.resource_from_as_at = resource_from_as_at
        self.resource_to_as_at = resource_to_as_at
        self.access_execution_time = access_execution_time
        self.access_as_at_time = access_as_at_time
        self.required_licence_policy_id = required_licence_policy_id
        self.links = links

    @property
    def timestamp(self):
        """Gets the timestamp of this AccessEvaluationLog.  # noqa: E501

        The timestamp of the access evaluation.  # noqa: E501

        :return: The timestamp of this AccessEvaluationLog.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AccessEvaluationLog.

        The timestamp of the access evaluation.  # noqa: E501

        :param timestamp: The timestamp of this AccessEvaluationLog.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def application(self):
        """Gets the application of this AccessEvaluationLog.  # noqa: E501

        The name of the application that the request was made from.  # noqa: E501

        :return: The application of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this AccessEvaluationLog.

        The name of the application that the request was made from.  # noqa: E501

        :param application: The application of this AccessEvaluationLog.  # noqa: E501
        :type application: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application is not None and len(application) < 1):
            raise ValueError("Invalid value for `application`, length must be greater than or equal to `1`")  # noqa: E501

        self._application = application

    @property
    def id(self):
        """Gets the id of this AccessEvaluationLog.  # noqa: E501

        The ID of the access evaluation.  # noqa: E501

        :return: The id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessEvaluationLog.

        The ID of the access evaluation.  # noqa: E501

        :param id: The id of this AccessEvaluationLog.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def request_id(self):
        """Gets the request_id of this AccessEvaluationLog.  # noqa: E501

        The identifier of the request.  # noqa: E501

        :return: The request_id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AccessEvaluationLog.

        The identifier of the request.  # noqa: E501

        :param request_id: The request_id of this AccessEvaluationLog.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def session_id(self):
        """Gets the session_id of this AccessEvaluationLog.  # noqa: E501

        The identifier of the session that the request was made in.  # noqa: E501

        :return: The session_id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this AccessEvaluationLog.

        The identifier of the session that the request was made in.  # noqa: E501

        :param session_id: The session_id of this AccessEvaluationLog.  # noqa: E501
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def user(self):
        """Gets the user of this AccessEvaluationLog.  # noqa: E501

        The user who made the request.  # noqa: E501

        :return: The user of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessEvaluationLog.

        The user who made the request.  # noqa: E501

        :param user: The user of this AccessEvaluationLog.  # noqa: E501
        :type user: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user is not None and len(user) < 1):
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `1`")  # noqa: E501

        self._user = user

    @property
    def user_type(self):
        """Gets the user_type of this AccessEvaluationLog.  # noqa: E501

        The type of the user who made the request.  # noqa: E501

        :return: The user_type of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this AccessEvaluationLog.

        The type of the user who made the request.  # noqa: E501

        :param user_type: The user_type of this AccessEvaluationLog.  # noqa: E501
        :type user_type: str
        """

        self._user_type = user_type

    @property
    def duration(self):
        """Gets the duration of this AccessEvaluationLog.  # noqa: E501

        The duration of the access evaluation.  # noqa: E501

        :return: The duration of this AccessEvaluationLog.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AccessEvaluationLog.

        The duration of the access evaluation.  # noqa: E501

        :param duration: The duration of this AccessEvaluationLog.  # noqa: E501
        :type duration: float
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def result(self):
        """Gets the result of this AccessEvaluationLog.  # noqa: E501

        The result of the access evaluation.  # noqa: E501

        :return: The result of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AccessEvaluationLog.

        The result of the access evaluation.  # noqa: E501

        :param result: The result of this AccessEvaluationLog.  # noqa: E501
        :type result: str
        """

        self._result = result

    @property
    def authoritative_role_id(self):
        """Gets the authoritative_role_id of this AccessEvaluationLog.  # noqa: E501

        The role that matched the access evaluation to provide a result.  # noqa: E501

        :return: The authoritative_role_id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._authoritative_role_id

    @authoritative_role_id.setter
    def authoritative_role_id(self, authoritative_role_id):
        """Sets the authoritative_role_id of this AccessEvaluationLog.

        The role that matched the access evaluation to provide a result.  # noqa: E501

        :param authoritative_role_id: The authoritative_role_id of this AccessEvaluationLog.  # noqa: E501
        :type authoritative_role_id: str
        """

        self._authoritative_role_id = authoritative_role_id

    @property
    def authoritative_policy_id(self):
        """Gets the authoritative_policy_id of this AccessEvaluationLog.  # noqa: E501

        The policy that matched the access evaluation to provide a result.  # noqa: E501

        :return: The authoritative_policy_id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._authoritative_policy_id

    @authoritative_policy_id.setter
    def authoritative_policy_id(self, authoritative_policy_id):
        """Sets the authoritative_policy_id of this AccessEvaluationLog.

        The policy that matched the access evaluation to provide a result.  # noqa: E501

        :param authoritative_policy_id: The authoritative_policy_id of this AccessEvaluationLog.  # noqa: E501
        :type authoritative_policy_id: str
        """

        self._authoritative_policy_id = authoritative_policy_id

    @property
    def authoritative_selector(self):
        """Gets the authoritative_selector of this AccessEvaluationLog.  # noqa: E501

        The selector that matched the access evaluation to provide a result.  # noqa: E501

        :return: The authoritative_selector of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._authoritative_selector

    @authoritative_selector.setter
    def authoritative_selector(self, authoritative_selector):
        """Sets the authoritative_selector of this AccessEvaluationLog.

        The selector that matched the access evaluation to provide a result.  # noqa: E501

        :param authoritative_selector: The authoritative_selector of this AccessEvaluationLog.  # noqa: E501
        :type authoritative_selector: str
        """

        self._authoritative_selector = authoritative_selector

    @property
    def resource_type(self):
        """Gets the resource_type of this AccessEvaluationLog.  # noqa: E501

        The type of the resource that the access evaluation is for.  # noqa: E501

        :return: The resource_type of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AccessEvaluationLog.

        The type of the resource that the access evaluation is for.  # noqa: E501

        :param resource_type: The resource_type of this AccessEvaluationLog.  # noqa: E501
        :type resource_type: str
        """

        self._resource_type = resource_type

    @property
    def action(self):
        """Gets the action of this AccessEvaluationLog.  # noqa: E501

        The action key of the access evaluation.  # noqa: E501

        :return: The action of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AccessEvaluationLog.

        The action key of the access evaluation.  # noqa: E501

        :param action: The action of this AccessEvaluationLog.  # noqa: E501
        :type action: str
        """

        self._action = action

    @property
    def resource(self):
        """Gets the resource of this AccessEvaluationLog.  # noqa: E501

        The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \"resourceId\".  # noqa: E501

        :return: The resource of this AccessEvaluationLog.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AccessEvaluationLog.

        The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \"resourceId\".  # noqa: E501

        :param resource: The resource of this AccessEvaluationLog.  # noqa: E501
        :type resource: dict(str, str)
        """

        self._resource = resource

    @property
    def resource_from_effective_date(self):
        """Gets the resource_from_effective_date of this AccessEvaluationLog.  # noqa: E501

        The From effective date of the resource.  # noqa: E501

        :return: The resource_from_effective_date of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_from_effective_date

    @resource_from_effective_date.setter
    def resource_from_effective_date(self, resource_from_effective_date):
        """Sets the resource_from_effective_date of this AccessEvaluationLog.

        The From effective date of the resource.  # noqa: E501

        :param resource_from_effective_date: The resource_from_effective_date of this AccessEvaluationLog.  # noqa: E501
        :type resource_from_effective_date: str
        """

        self._resource_from_effective_date = resource_from_effective_date

    @property
    def resource_to_effective_date(self):
        """Gets the resource_to_effective_date of this AccessEvaluationLog.  # noqa: E501

        The To effective date of the resource.  # noqa: E501

        :return: The resource_to_effective_date of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_to_effective_date

    @resource_to_effective_date.setter
    def resource_to_effective_date(self, resource_to_effective_date):
        """Sets the resource_to_effective_date of this AccessEvaluationLog.

        The To effective date of the resource.  # noqa: E501

        :param resource_to_effective_date: The resource_to_effective_date of this AccessEvaluationLog.  # noqa: E501
        :type resource_to_effective_date: str
        """

        self._resource_to_effective_date = resource_to_effective_date

    @property
    def resource_from_as_at(self):
        """Gets the resource_from_as_at of this AccessEvaluationLog.  # noqa: E501

        The From AsAt date of the resource.  # noqa: E501

        :return: The resource_from_as_at of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_from_as_at

    @resource_from_as_at.setter
    def resource_from_as_at(self, resource_from_as_at):
        """Sets the resource_from_as_at of this AccessEvaluationLog.

        The From AsAt date of the resource.  # noqa: E501

        :param resource_from_as_at: The resource_from_as_at of this AccessEvaluationLog.  # noqa: E501
        :type resource_from_as_at: str
        """

        self._resource_from_as_at = resource_from_as_at

    @property
    def resource_to_as_at(self):
        """Gets the resource_to_as_at of this AccessEvaluationLog.  # noqa: E501

        The To AsAt date of the resource.  # noqa: E501

        :return: The resource_to_as_at of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_to_as_at

    @resource_to_as_at.setter
    def resource_to_as_at(self, resource_to_as_at):
        """Sets the resource_to_as_at of this AccessEvaluationLog.

        The To AsAt date of the resource.  # noqa: E501

        :param resource_to_as_at: The resource_to_as_at of this AccessEvaluationLog.  # noqa: E501
        :type resource_to_as_at: str
        """

        self._resource_to_as_at = resource_to_as_at

    @property
    def access_execution_time(self):
        """Gets the access_execution_time of this AccessEvaluationLog.  # noqa: E501

        The execution time of the entitlement.  # noqa: E501

        :return: The access_execution_time of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._access_execution_time

    @access_execution_time.setter
    def access_execution_time(self, access_execution_time):
        """Sets the access_execution_time of this AccessEvaluationLog.

        The execution time of the entitlement.  # noqa: E501

        :param access_execution_time: The access_execution_time of this AccessEvaluationLog.  # noqa: E501
        :type access_execution_time: str
        """

        self._access_execution_time = access_execution_time

    @property
    def access_as_at_time(self):
        """Gets the access_as_at_time of this AccessEvaluationLog.  # noqa: E501

        The AsAt time of the entitlement.  # noqa: E501

        :return: The access_as_at_time of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._access_as_at_time

    @access_as_at_time.setter
    def access_as_at_time(self, access_as_at_time):
        """Sets the access_as_at_time of this AccessEvaluationLog.

        The AsAt time of the entitlement.  # noqa: E501

        :param access_as_at_time: The access_as_at_time of this AccessEvaluationLog.  # noqa: E501
        :type access_as_at_time: str
        """

        self._access_as_at_time = access_as_at_time

    @property
    def required_licence_policy_id(self):
        """Gets the required_licence_policy_id of this AccessEvaluationLog.  # noqa: E501

        ID of the required licence policy.  # noqa: E501

        :return: The required_licence_policy_id of this AccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._required_licence_policy_id

    @required_licence_policy_id.setter
    def required_licence_policy_id(self, required_licence_policy_id):
        """Sets the required_licence_policy_id of this AccessEvaluationLog.

        ID of the required licence policy.  # noqa: E501

        :param required_licence_policy_id: The required_licence_policy_id of this AccessEvaluationLog.  # noqa: E501
        :type required_licence_policy_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                required_licence_policy_id is not None and len(required_licence_policy_id) > 64):
            raise ValueError("Invalid value for `required_licence_policy_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                required_licence_policy_id is not None and len(required_licence_policy_id) < 1):
            raise ValueError("Invalid value for `required_licence_policy_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                required_licence_policy_id is not None and not re.search(r'^[a-zA-Z0-9\-_:\+]+$', required_licence_policy_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `required_licence_policy_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_:\+]+$/`")  # noqa: E501

        self._required_licence_policy_id = required_licence_policy_id

    @property
    def links(self):
        """Gets the links of this AccessEvaluationLog.  # noqa: E501


        :return: The links of this AccessEvaluationLog.  # noqa: E501
        :rtype: list[finbourne_insights.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AccessEvaluationLog.


        :param links: The links of this AccessEvaluationLog.  # noqa: E501
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
        if not isinstance(other, AccessEvaluationLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessEvaluationLog):
            return True

        return self.to_dict() != other.to_dict()
