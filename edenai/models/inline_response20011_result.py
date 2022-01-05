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

class InlineResponse20011Result(object):
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
        'file_name': 'str',
        'labels': 'list[str]',
        'confidences': 'list[float]',
        'x_mins': 'list[float]',
        'x_maxs': 'list[float]',
        'y_mins': 'list[float]',
        'y_maxs': 'list[float]'
    }

    attribute_map = {
        'file_name': 'file_name',
        'labels': 'labels',
        'confidences': 'confidences',
        'x_mins': 'x_mins',
        'x_maxs': 'x_maxs',
        'y_mins': 'y_mins',
        'y_maxs': 'y_maxs'
    }

    def __init__(self, file_name=None, labels=None, confidences=None, x_mins=None, x_maxs=None, y_mins=None, y_maxs=None):  # noqa: E501
        """InlineResponse20011Result - a model defined in Swagger"""  # noqa: E501
        self._file_name = None
        self._labels = None
        self._confidences = None
        self._x_mins = None
        self._x_maxs = None
        self._y_mins = None
        self._y_maxs = None
        self.discriminator = None
        if file_name is not None:
            self.file_name = file_name
        if labels is not None:
            self.labels = labels
        if confidences is not None:
            self.confidences = confidences
        if x_mins is not None:
            self.x_mins = x_mins
        if x_maxs is not None:
            self.x_maxs = x_maxs
        if y_mins is not None:
            self.y_mins = y_mins
        if y_maxs is not None:
            self.y_maxs = y_maxs

    @property
    def file_name(self):
        """Gets the file_name of this InlineResponse20011Result.  # noqa: E501


        :return: The file_name of this InlineResponse20011Result.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InlineResponse20011Result.


        :param file_name: The file_name of this InlineResponse20011Result.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def labels(self):
        """Gets the labels of this InlineResponse20011Result.  # noqa: E501


        :return: The labels of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this InlineResponse20011Result.


        :param labels: The labels of this InlineResponse20011Result.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def confidences(self):
        """Gets the confidences of this InlineResponse20011Result.  # noqa: E501


        :return: The confidences of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[float]
        """
        return self._confidences

    @confidences.setter
    def confidences(self, confidences):
        """Sets the confidences of this InlineResponse20011Result.


        :param confidences: The confidences of this InlineResponse20011Result.  # noqa: E501
        :type: list[float]
        """

        self._confidences = confidences

    @property
    def x_mins(self):
        """Gets the x_mins of this InlineResponse20011Result.  # noqa: E501


        :return: The x_mins of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[float]
        """
        return self._x_mins

    @x_mins.setter
    def x_mins(self, x_mins):
        """Sets the x_mins of this InlineResponse20011Result.


        :param x_mins: The x_mins of this InlineResponse20011Result.  # noqa: E501
        :type: list[float]
        """

        self._x_mins = x_mins

    @property
    def x_maxs(self):
        """Gets the x_maxs of this InlineResponse20011Result.  # noqa: E501


        :return: The x_maxs of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[float]
        """
        return self._x_maxs

    @x_maxs.setter
    def x_maxs(self, x_maxs):
        """Sets the x_maxs of this InlineResponse20011Result.


        :param x_maxs: The x_maxs of this InlineResponse20011Result.  # noqa: E501
        :type: list[float]
        """

        self._x_maxs = x_maxs

    @property
    def y_mins(self):
        """Gets the y_mins of this InlineResponse20011Result.  # noqa: E501


        :return: The y_mins of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[float]
        """
        return self._y_mins

    @y_mins.setter
    def y_mins(self, y_mins):
        """Sets the y_mins of this InlineResponse20011Result.


        :param y_mins: The y_mins of this InlineResponse20011Result.  # noqa: E501
        :type: list[float]
        """

        self._y_mins = y_mins

    @property
    def y_maxs(self):
        """Gets the y_maxs of this InlineResponse20011Result.  # noqa: E501


        :return: The y_maxs of this InlineResponse20011Result.  # noqa: E501
        :rtype: list[float]
        """
        return self._y_maxs

    @y_maxs.setter
    def y_maxs(self, y_maxs):
        """Sets the y_maxs of this InlineResponse20011Result.


        :param y_maxs: The y_maxs of this InlineResponse20011Result.  # noqa: E501
        :type: list[float]
        """

        self._y_maxs = y_maxs

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
        if issubclass(InlineResponse20011Result, dict):
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
        if not isinstance(other, InlineResponse20011Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
