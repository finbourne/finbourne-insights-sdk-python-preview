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


class ResourceListWithHistogramOfAccessEvaluationLog(object):
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
        'histogram': 'Histogram',
        'values': 'list[AccessEvaluationLog]',
        'href': 'str',
        'next_page': 'str',
        'previous_page': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'histogram': 'histogram',
        'values': 'values',
        'href': 'href',
        'next_page': 'nextPage',
        'previous_page': 'previousPage',
        'links': 'links'
    }

    required_map = {
        'histogram': 'optional',
        'values': 'required',
        'href': 'optional',
        'next_page': 'optional',
        'previous_page': 'optional',
        'links': 'optional'
    }

    def __init__(self, histogram=None, values=None, href=None, next_page=None, previous_page=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ResourceListWithHistogramOfAccessEvaluationLog - a model defined in OpenAPI"
        
        :param histogram: 
        :type histogram: finbourne_insights.Histogram
        :param values:  (required)
        :type values: list[finbourne_insights.AccessEvaluationLog]
        :param href: 
        :type href: str
        :param next_page: 
        :type next_page: str
        :param previous_page: 
        :type previous_page: str
        :param links: 
        :type links: list[finbourne_insights.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._histogram = None
        self._values = None
        self._href = None
        self._next_page = None
        self._previous_page = None
        self._links = None
        self.discriminator = None

        if histogram is not None:
            self.histogram = histogram
        self.values = values
        self.href = href
        self.next_page = next_page
        self.previous_page = previous_page
        self.links = links

    @property
    def histogram(self):
        """Gets the histogram of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The histogram of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: finbourne_insights.Histogram
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param histogram: The histogram of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :type histogram: finbourne_insights.Histogram
        """

        self._histogram = histogram

    @property
    def values(self):
        """Gets the values of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The values of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: list[finbourne_insights.AccessEvaluationLog]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param values: The values of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :type values: list[finbourne_insights.AccessEvaluationLog]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def href(self):
        """Gets the href of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The href of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param href: The href of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def next_page(self):
        """Gets the next_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The next_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param next_page: The next_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :type next_page: str
        """

        self._next_page = next_page

    @property
    def previous_page(self):
        """Gets the previous_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The previous_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """Sets the previous_page of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param previous_page: The previous_page of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :type previous_page: str
        """

        self._previous_page = previous_page

    @property
    def links(self):
        """Gets the links of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501


        :return: The links of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
        :rtype: list[finbourne_insights.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResourceListWithHistogramOfAccessEvaluationLog.


        :param links: The links of this ResourceListWithHistogramOfAccessEvaluationLog.  # noqa: E501
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
        if not isinstance(other, ResourceListWithHistogramOfAccessEvaluationLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceListWithHistogramOfAccessEvaluationLog):
            return True

        return self.to_dict() != other.to_dict()
