# coding: utf-8

"""
    Eden AI API Documentation

    <a href=\"https://app.edenai.run/user/login\" target=\"_blank\"><img src=\"/static/images/welcome.png\"></a>. # Welcome  Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies: * Vision:  <a href=\"https://www.edenai.co/vision\" target=\"_blank\">www.edenai.co/vision</a>. * Text & NLP: <a href=\"https://www.edenai.co/text\" target=\"_blank\">www.edenai.co/text</a>. * Speech & Audio: <a href=\"https://www.edenai.co/speech\" target=\"_blank\">www.edenai.co/speech</a>. * OCR: <a href=\"https://www.edenai.co/ocr\" target=\"_blank\">www.edenai.co/ocr</a>. * Machine Translation: <a href=\"https://www.edenai.co/translation\" target=\"_blank\">www.edenai.co/translation</a>. * Prediction: <a href=\"https://www.edenai.co/prediction\" target=\"_blank\">www.edenai.co/prediction</a>.  For all the proposed technologies, we provide a single endpoint:  the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog  # Support & community  ### 1- Support If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.   ### 2- Community  You can interact personally with other people actively using and working with Eden AI and join our  <a href=\"https://join.slack.com/t/edenai/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w\" target=\"_blank\">Slack community</a>.  We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on Github: <a href=\"https://github.com/edenai\" target=\"_blank\">https://github.com/edenai</a>.  ### 3- Blog  We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: <a href=\"https://www.edenai.co/blog\" target=\"_blank\">https://www.edenai.co/blog</a>.   # Authentication  ## Create account ![Register](/static/images/register.png)  To create an account, please go to this link: <a href=\"https://app.edenai.run/user/login\" target=\"_blank\">app.edenai.run/user/login</a>. You can create an account with your email address or by using your account on available platforms (Gmail, Github, etc.).   By creating an account with your email address, you will receive a confirmation email with a link to click. Check your spam if needed and contact us if you have any problem: contact@edenai.co  ![Login](/static/images/login.png) ## API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will have access to your API key to start using the different AI engines offered by Eden AI.   ![api_key](/static/images/api_key.png) # Portal Guide  Eden AI provides a web portal that allows you to do several tasks:  ![portal](/static/images/portal.png)  ### 1- Benchmark and test The platform allows you to easily compare competing engines without having to code. By uploading your data, you have access to the prediction results of the different engines. This gives you a first overview of the performance of AI engines.   ![benchmark](/static/images/benchmark.png)  ### 2- Cost management The <a href=\"https://app.edenai.run/admin/cost-management\" target=\"_blank\">cost management page</a> also allows you to centralize the costs associated with the different engines with various filters to simplify the analysis.   This page also allows you to define monthly budget limits not to be exceeded to secure the use of different AI engines.   ![cost-management](/static/images/cost_management.png) ### 3- Account The <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">account page</a> allows you to change your information and password. It also gives you access to your API key that you can renew if needed.   This page also allows you to add a credit card and to buy with credits to use all the engines offered by Eden AI.   ![account](/static/images/account.png)   # API Guide  Eden AI API has different endpoints that refer to different AI services. The connected providers are thus parameters that the user can easily change.   # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@edenai.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2005Result1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'solution_name': 'str',
        'provider': 'str',
        'status': 'str',
        'execution_time': 'float',
        'original_result': 'object',
        'result': 'InlineResponse2005Result'
    }

    attribute_map = {
        'solution_name': 'solution_name',
        'provider': 'provider',
        'status': 'status',
        'execution_time': 'execution_time',
        'original_result': 'original_result',
        'result': 'result'
    }

    def __init__(self, solution_name=None, provider=None, status=None, execution_time=None, original_result=None, result=None):  # noqa: E501
        """InlineResponse2005Result1 - a model defined in Swagger"""  # noqa: E501
        self._solution_name = None
        self._provider = None
        self._status = None
        self._execution_time = None
        self._original_result = None
        self._result = None
        self.discriminator = None
        if solution_name is not None:
            self.solution_name = solution_name
        if provider is not None:
            self.provider = provider
        if status is not None:
            self.status = status
        if execution_time is not None:
            self.execution_time = execution_time
        if original_result is not None:
            self.original_result = original_result
        if result is not None:
            self.result = result

    @property
    def solution_name(self):
        """Gets the solution_name of this InlineResponse2005Result1.  # noqa: E501


        :return: The solution_name of this InlineResponse2005Result1.  # noqa: E501
        :rtype: str
        """
        return self._solution_name

    @solution_name.setter
    def solution_name(self, solution_name):
        """Sets the solution_name of this InlineResponse2005Result1.


        :param solution_name: The solution_name of this InlineResponse2005Result1.  # noqa: E501
        :type: str
        """

        self._solution_name = solution_name

    @property
    def provider(self):
        """Gets the provider of this InlineResponse2005Result1.  # noqa: E501


        :return: The provider of this InlineResponse2005Result1.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this InlineResponse2005Result1.


        :param provider: The provider of this InlineResponse2005Result1.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def status(self):
        """Gets the status of this InlineResponse2005Result1.  # noqa: E501


        :return: The status of this InlineResponse2005Result1.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2005Result1.


        :param status: The status of this InlineResponse2005Result1.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def execution_time(self):
        """Gets the execution_time of this InlineResponse2005Result1.  # noqa: E501


        :return: The execution_time of this InlineResponse2005Result1.  # noqa: E501
        :rtype: float
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this InlineResponse2005Result1.


        :param execution_time: The execution_time of this InlineResponse2005Result1.  # noqa: E501
        :type: float
        """

        self._execution_time = execution_time

    @property
    def original_result(self):
        """Gets the original_result of this InlineResponse2005Result1.  # noqa: E501


        :return: The original_result of this InlineResponse2005Result1.  # noqa: E501
        :rtype: object
        """
        return self._original_result

    @original_result.setter
    def original_result(self, original_result):
        """Sets the original_result of this InlineResponse2005Result1.


        :param original_result: The original_result of this InlineResponse2005Result1.  # noqa: E501
        :type: object
        """

        self._original_result = original_result

    @property
    def result(self):
        """Gets the result of this InlineResponse2005Result1.  # noqa: E501


        :return: The result of this InlineResponse2005Result1.  # noqa: E501
        :rtype: InlineResponse2005Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse2005Result1.


        :param result: The result of this InlineResponse2005Result1.  # noqa: E501
        :type: InlineResponse2005Result
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2005Result1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2005Result1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
