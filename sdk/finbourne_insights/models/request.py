# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.807
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


class Request(object):
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
        'headers': 'dict(str, list[str])',
        'content_length': 'int',
        'content_type': 'str',
        'body': 'str',
        'body_was_truncated': 'bool',
        'method': 'str',
        'url': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'headers': 'headers',
        'content_length': 'contentLength',
        'content_type': 'contentType',
        'body': 'body',
        'body_was_truncated': 'bodyWasTruncated',
        'method': 'method',
        'url': 'url',
        'links': 'links'
    }

    required_map = {
        'headers': 'optional',
        'content_length': 'optional',
        'content_type': 'optional',
        'body': 'optional',
        'body_was_truncated': 'optional',
        'method': 'optional',
        'url': 'optional',
        'links': 'optional'
    }

    def __init__(self, headers=None, content_length=None, content_type=None, body=None, body_was_truncated=None, method=None, url=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Request - a model defined in OpenAPI"
        
        :param headers:  The headers
        :type headers: dict(str, list[str])
        :param content_length:  The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Request.Body  (e.g. if actual Body is large, or not convertible to a string)
        :type content_length: int
        :param content_type:  The content type
        :type content_type: str
        :param body:  The recorded content.
        :type body: str
        :param body_was_truncated:  Determines if the recorded body was truncated.
        :type body_was_truncated: bool
        :param method:  Method called by the request
        :type method: str
        :param url:  URL of the request
        :type url: str
        :param links: 
        :type links: list[finbourne_insights.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._headers = None
        self._content_length = None
        self._content_type = None
        self._body = None
        self._body_was_truncated = None
        self._method = None
        self._url = None
        self._links = None
        self.discriminator = None

        self.headers = headers
        self.content_length = content_length
        self.content_type = content_type
        self.body = body
        if body_was_truncated is not None:
            self.body_was_truncated = body_was_truncated
        self.method = method
        self.url = url
        self.links = links

    @property
    def headers(self):
        """Gets the headers of this Request.  # noqa: E501

        The headers  # noqa: E501

        :return: The headers of this Request.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Request.

        The headers  # noqa: E501

        :param headers: The headers of this Request.  # noqa: E501
        :type headers: dict(str, list[str])
        """

        self._headers = headers

    @property
    def content_length(self):
        """Gets the content_length of this Request.  # noqa: E501

        The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Request.Body  (e.g. if actual Body is large, or not convertible to a string)  # noqa: E501

        :return: The content_length of this Request.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this Request.

        The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Request.Body  (e.g. if actual Body is large, or not convertible to a string)  # noqa: E501

        :param content_length: The content_length of this Request.  # noqa: E501
        :type content_length: int
        """

        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this Request.  # noqa: E501

        The content type  # noqa: E501

        :return: The content_type of this Request.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Request.

        The content type  # noqa: E501

        :param content_type: The content_type of this Request.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def body(self):
        """Gets the body of this Request.  # noqa: E501

        The recorded content.  # noqa: E501

        :return: The body of this Request.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Request.

        The recorded content.  # noqa: E501

        :param body: The body of this Request.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def body_was_truncated(self):
        """Gets the body_was_truncated of this Request.  # noqa: E501

        Determines if the recorded body was truncated.  # noqa: E501

        :return: The body_was_truncated of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._body_was_truncated

    @body_was_truncated.setter
    def body_was_truncated(self, body_was_truncated):
        """Sets the body_was_truncated of this Request.

        Determines if the recorded body was truncated.  # noqa: E501

        :param body_was_truncated: The body_was_truncated of this Request.  # noqa: E501
        :type body_was_truncated: bool
        """

        self._body_was_truncated = body_was_truncated

    @property
    def method(self):
        """Gets the method of this Request.  # noqa: E501

        Method called by the request  # noqa: E501

        :return: The method of this Request.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Request.

        Method called by the request  # noqa: E501

        :param method: The method of this Request.  # noqa: E501
        :type method: str
        """

        self._method = method

    @property
    def url(self):
        """Gets the url of this Request.  # noqa: E501

        URL of the request  # noqa: E501

        :return: The url of this Request.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Request.

        URL of the request  # noqa: E501

        :param url: The url of this Request.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def links(self):
        """Gets the links of this Request.  # noqa: E501


        :return: The links of this Request.  # noqa: E501
        :rtype: list[finbourne_insights.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Request.


        :param links: The links of this Request.  # noqa: E501
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
        if not isinstance(other, Request):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Request):
            return True

        return self.to_dict() != other.to_dict()
