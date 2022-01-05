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

class InlineResponse2002Results(object):
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
        'word_text': 'str',
        'left': 'float',
        'top': 'float',
        'width': 'float',
        'hight': 'float',
        'customer_information': 'InlineResponse2002CustomerInformation',
        'merchant_information': 'InlineResponse2002MerchantInformation',
        'invoice_total': 'str',
        'subtotal': 'str',
        '_date': 'str',
        'due_date': 'str',
        'invoice_number': 'str',
        'taxes': 'str',
        'locale': 'InlineResponse2002Locale',
        'item_lines': 'list[InlineResponse2002ItemLines]'
    }

    attribute_map = {
        'word_text': 'word_text',
        'left': 'left',
        'top': 'top',
        'width': 'width',
        'hight': 'hight',
        'customer_information': 'customer_information',
        'merchant_information': 'merchant_information',
        'invoice_total': 'invoice_total',
        'subtotal': 'subtotal',
        '_date': 'date',
        'due_date': 'due_date',
        'invoice_number': 'invoice_number',
        'taxes': 'taxes',
        'locale': 'locale',
        'item_lines': 'item_lines'
    }

    def __init__(self, word_text=None, left=None, top=None, width=None, hight=None, customer_information=None, merchant_information=None, invoice_total=None, subtotal=None, _date=None, due_date=None, invoice_number=None, taxes=None, locale=None, item_lines=None):  # noqa: E501
        """InlineResponse2002Results - a model defined in Swagger"""  # noqa: E501
        self._word_text = None
        self._left = None
        self._top = None
        self._width = None
        self._hight = None
        self._customer_information = None
        self._merchant_information = None
        self._invoice_total = None
        self._subtotal = None
        self.__date = None
        self._due_date = None
        self._invoice_number = None
        self._taxes = None
        self._locale = None
        self._item_lines = None
        self.discriminator = None
        if word_text is not None:
            self.word_text = word_text
        if left is not None:
            self.left = left
        if top is not None:
            self.top = top
        if width is not None:
            self.width = width
        if hight is not None:
            self.hight = hight
        if customer_information is not None:
            self.customer_information = customer_information
        if merchant_information is not None:
            self.merchant_information = merchant_information
        if invoice_total is not None:
            self.invoice_total = invoice_total
        if subtotal is not None:
            self.subtotal = subtotal
        if _date is not None:
            self._date = _date
        if due_date is not None:
            self.due_date = due_date
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if taxes is not None:
            self.taxes = taxes
        if locale is not None:
            self.locale = locale
        if item_lines is not None:
            self.item_lines = item_lines

    @property
    def word_text(self):
        """Gets the word_text of this InlineResponse2002Results.  # noqa: E501


        :return: The word_text of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._word_text

    @word_text.setter
    def word_text(self, word_text):
        """Sets the word_text of this InlineResponse2002Results.


        :param word_text: The word_text of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._word_text = word_text

    @property
    def left(self):
        """Gets the left of this InlineResponse2002Results.  # noqa: E501


        :return: The left of this InlineResponse2002Results.  # noqa: E501
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this InlineResponse2002Results.


        :param left: The left of this InlineResponse2002Results.  # noqa: E501
        :type: float
        """

        self._left = left

    @property
    def top(self):
        """Gets the top of this InlineResponse2002Results.  # noqa: E501


        :return: The top of this InlineResponse2002Results.  # noqa: E501
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this InlineResponse2002Results.


        :param top: The top of this InlineResponse2002Results.  # noqa: E501
        :type: float
        """

        self._top = top

    @property
    def width(self):
        """Gets the width of this InlineResponse2002Results.  # noqa: E501


        :return: The width of this InlineResponse2002Results.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this InlineResponse2002Results.


        :param width: The width of this InlineResponse2002Results.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def hight(self):
        """Gets the hight of this InlineResponse2002Results.  # noqa: E501


        :return: The hight of this InlineResponse2002Results.  # noqa: E501
        :rtype: float
        """
        return self._hight

    @hight.setter
    def hight(self, hight):
        """Sets the hight of this InlineResponse2002Results.


        :param hight: The hight of this InlineResponse2002Results.  # noqa: E501
        :type: float
        """

        self._hight = hight

    @property
    def customer_information(self):
        """Gets the customer_information of this InlineResponse2002Results.  # noqa: E501


        :return: The customer_information of this InlineResponse2002Results.  # noqa: E501
        :rtype: InlineResponse2002CustomerInformation
        """
        return self._customer_information

    @customer_information.setter
    def customer_information(self, customer_information):
        """Sets the customer_information of this InlineResponse2002Results.


        :param customer_information: The customer_information of this InlineResponse2002Results.  # noqa: E501
        :type: InlineResponse2002CustomerInformation
        """

        self._customer_information = customer_information

    @property
    def merchant_information(self):
        """Gets the merchant_information of this InlineResponse2002Results.  # noqa: E501


        :return: The merchant_information of this InlineResponse2002Results.  # noqa: E501
        :rtype: InlineResponse2002MerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """Sets the merchant_information of this InlineResponse2002Results.


        :param merchant_information: The merchant_information of this InlineResponse2002Results.  # noqa: E501
        :type: InlineResponse2002MerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def invoice_total(self):
        """Gets the invoice_total of this InlineResponse2002Results.  # noqa: E501


        :return: The invoice_total of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._invoice_total

    @invoice_total.setter
    def invoice_total(self, invoice_total):
        """Sets the invoice_total of this InlineResponse2002Results.


        :param invoice_total: The invoice_total of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._invoice_total = invoice_total

    @property
    def subtotal(self):
        """Gets the subtotal of this InlineResponse2002Results.  # noqa: E501


        :return: The subtotal of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this InlineResponse2002Results.


        :param subtotal: The subtotal of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._subtotal = subtotal

    @property
    def _date(self):
        """Gets the _date of this InlineResponse2002Results.  # noqa: E501


        :return: The _date of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InlineResponse2002Results.


        :param _date: The _date of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def due_date(self):
        """Gets the due_date of this InlineResponse2002Results.  # noqa: E501


        :return: The due_date of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this InlineResponse2002Results.


        :param due_date: The due_date of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this InlineResponse2002Results.  # noqa: E501


        :return: The invoice_number of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this InlineResponse2002Results.


        :param invoice_number: The invoice_number of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def taxes(self):
        """Gets the taxes of this InlineResponse2002Results.  # noqa: E501


        :return: The taxes of this InlineResponse2002Results.  # noqa: E501
        :rtype: str
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this InlineResponse2002Results.


        :param taxes: The taxes of this InlineResponse2002Results.  # noqa: E501
        :type: str
        """

        self._taxes = taxes

    @property
    def locale(self):
        """Gets the locale of this InlineResponse2002Results.  # noqa: E501


        :return: The locale of this InlineResponse2002Results.  # noqa: E501
        :rtype: InlineResponse2002Locale
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this InlineResponse2002Results.


        :param locale: The locale of this InlineResponse2002Results.  # noqa: E501
        :type: InlineResponse2002Locale
        """

        self._locale = locale

    @property
    def item_lines(self):
        """Gets the item_lines of this InlineResponse2002Results.  # noqa: E501


        :return: The item_lines of this InlineResponse2002Results.  # noqa: E501
        :rtype: list[InlineResponse2002ItemLines]
        """
        return self._item_lines

    @item_lines.setter
    def item_lines(self, item_lines):
        """Sets the item_lines of this InlineResponse2002Results.


        :param item_lines: The item_lines of this InlineResponse2002Results.  # noqa: E501
        :type: list[InlineResponse2002ItemLines]
        """

        self._item_lines = item_lines

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
        if issubclass(InlineResponse2002Results, dict):
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
        if not isinstance(other, InlineResponse2002Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
