# coding: utf-8

"""
    Eden AI API Documentation

    <a href=\"https://app.edenai.run/user/login\" target=\"_blank\"><img src=\"/static/images/welcome.png\"></a>. # Welcome  Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies: * Vision:  <a href=\"https://www.edenai.co/vision\" target=\"_blank\">www.edenai.co/vision</a>. * Text & NLP: <a href=\"https://www.edenai.co/text\" target=\"_blank\">www.edenai.co/text</a>. * Speech & Audio: <a href=\"https://www.edenai.co/speech\" target=\"_blank\">www.edenai.co/speech</a>. * OCR: <a href=\"https://www.edenai.co/ocr\" target=\"_blank\">www.edenai.co/ocr</a>. * Machine Translation: <a href=\"https://www.edenai.co/translation\" target=\"_blank\">www.edenai.co/translation</a>. * Prediction: <a href=\"https://www.edenai.co/prediction\" target=\"_blank\">www.edenai.co/prediction</a>.  For all the proposed technologies, we provide a single endpoint:  the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog  # Support & community  ### 1- Support If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.   ### 2- Community  You can interact personally with other people actively using and working with Eden AI and join our  <a href=\"https://join.slack.com/t/edenai/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w\" target=\"_blank\">Slack community</a>.  We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on Github: <a href=\"https://github.com/edenai\" target=\"_blank\">https://github.com/edenai</a>.  ### 3- Blog  We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: <a href=\"https://www.edenai.co/blog\" target=\"_blank\">https://www.edenai.co/blog</a>.   # Authentication  ## Create account ![Register](/static/images/register.png)  To create an account, please go to this link: <a href=\"https://app.edenai.run/user/login\" target=\"_blank\">app.edenai.run/user/login</a>. You can create an account with your email address or by using your account on available platforms (Gmail, Github, etc.).   By creating an account with your email address, you will receive a confirmation email with a link to click. Check your spam if needed and contact us if you have any problem: contact@edenai.co  ![Login](/static/images/login.png) ## API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will have access to your API key to start using the different AI engines offered by Eden AI.   ![api_key](/static/images/api_key.png) # Portal Guide  Eden AI provides a web portal that allows you to do several tasks:  ![portal](/static/images/portal.png)  ### 1- Benchmark and test The platform allows you to easily compare competing engines without having to code. By uploading your data, you have access to the prediction results of the different engines. This gives you a first overview of the performance of AI engines.   ![benchmark](/static/images/benchmark.png)  ### 2- Cost management The <a href=\"https://app.edenai.run/admin/cost-management\" target=\"_blank\">cost management page</a> also allows you to centralize the costs associated with the different engines with various filters to simplify the analysis.   This page also allows you to define monthly budget limits not to be exceeded to secure the use of different AI engines.   ![cost-management](/static/images/cost_management.png) ### 3- Account The <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">account page</a> allows you to change your information and password. It also gives you access to your API key that you can renew if needed.   This page also allows you to add a credit card and to buy with credits to use all the engines offered by Eden AI.   ![account](/static/images/account.png)   # API Guide  Eden AI API has different endpoints that refer to different AI services. The connected providers are thus parameters that the user can easily change.   # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@edenai.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edenai.api_client import ApiClient


class SpeechApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def asynchronous_speech_recognition(self, language, files, providers, **kwargs):  # noqa: E501
        """asynchronous_speech_recognition  # noqa: E501

        Speech recognition is technology that can recognize spoken words, which can then be converted to text. This endpoint allows you to launch asynchronous speech recognition jobs.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**English (US)**|`string`|`en-US`| |**English (GB)**|`string`|`en-GB`| |**French**|`string`|`fr-FR`| |**Spanish**|`string`|`es-ES`| |**Dutch (Netherlands)**|`string`|`nl-NL`| |**Japanese**|`string`|`ja-JP`| |**Russian**|`string`|`ru-RU`| |**Arabic**|`string`|`ar-SA`| |**Italian**|`string`|`it-IT`| |**Korean**|`string`|`ko-KR`| |**Portuguese**|`string`|`pt-PT`| |**Turkish**|`string`|`tr-TR`| |**Indonesian**|`string`|`id-ID`| |**Malay**|`string`|`ms-MY`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-speech-to-text)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-transcribe)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-speech-to-text)|`google`|`v1p1beta1`| |[**Deepgram**](https://www.edenai.co/catalog/deepgram)|`deepgram`|`v1`| |[**Assembly**](https://www.edenai.co/catalog/assembly-ai)|`assembly`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asynchronous_speech_recognition(language, files, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language: (required)
        :param str files: (required)
        :param str providers: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asynchronous_speech_recognition_with_http_info(language, files, providers, **kwargs)  # noqa: E501
        else:
            (data) = self.asynchronous_speech_recognition_with_http_info(language, files, providers, **kwargs)  # noqa: E501
            return data

    def asynchronous_speech_recognition_with_http_info(self, language, files, providers, **kwargs):  # noqa: E501
        """asynchronous_speech_recognition  # noqa: E501

        Speech recognition is technology that can recognize spoken words, which can then be converted to text. This endpoint allows you to launch asynchronous speech recognition jobs.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**English (US)**|`string`|`en-US`| |**English (GB)**|`string`|`en-GB`| |**French**|`string`|`fr-FR`| |**Spanish**|`string`|`es-ES`| |**Dutch (Netherlands)**|`string`|`nl-NL`| |**Japanese**|`string`|`ja-JP`| |**Russian**|`string`|`ru-RU`| |**Arabic**|`string`|`ar-SA`| |**Italian**|`string`|`it-IT`| |**Korean**|`string`|`ko-KR`| |**Portuguese**|`string`|`pt-PT`| |**Turkish**|`string`|`tr-TR`| |**Indonesian**|`string`|`id-ID`| |**Malay**|`string`|`ms-MY`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-speech-to-text)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-transcribe)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-speech-to-text)|`google`|`v1p1beta1`| |[**Deepgram**](https://www.edenai.co/catalog/deepgram)|`deepgram`|`v1`| |[**Assembly**](https://www.edenai.co/catalog/assembly-ai)|`assembly`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asynchronous_speech_recognition_with_http_info(language, files, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language: (required)
        :param str files: (required)
        :param str providers: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language', 'files', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asynchronous_speech_recognition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'language' is set
        if ('language' not in params or
                params['language'] is None):
            raise ValueError("Missing the required parameter `language` when calling `asynchronous_speech_recognition`")  # noqa: E501
        # verify the required parameter 'files' is set
        if ('files' not in params or
                params['files'] is None):
            raise ValueError("Missing the required parameter `files` when calling `asynchronous_speech_recognition`")  # noqa: E501
        # verify the required parameter 'providers' is set
        if ('providers' not in params or
                params['providers'] is None):
            raise ValueError("Missing the required parameter `providers` when calling `asynchronous_speech_recognition`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'language' in params:
            form_params.append(('language', params['language']))  # noqa: E501
        if 'files' in params:
            local_var_files['files'] = params['files']  # noqa: E501
        if 'providers' in params:
            form_params.append(('providers', params['providers']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/audio/speech_recognition_async', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asynchronous_speech_recognition_0(self, job_id, **kwargs):  # noqa: E501
        """asynchronous_speech_recognition_0  # noqa: E501

        This endpoint allows you to check the state of  your asynchronous speech recognition job and returns the results when they are ready.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asynchronous_speech_recognition_0(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asynchronous_speech_recognition_0_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.asynchronous_speech_recognition_0_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def asynchronous_speech_recognition_0_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """asynchronous_speech_recognition_0  # noqa: E501

        This endpoint allows you to check the state of  your asynchronous speech recognition job and returns the results when they are ready.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asynchronous_speech_recognition_0_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asynchronous_speech_recognition_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `asynchronous_speech_recognition_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/audio/speech_recognition_async/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def speech_recognition(self, language, files, providers, **kwargs):  # noqa: E501
        """speech_recognition  # noqa: E501

        Speech recognition is technology that can recognize spoken words, which can then be converted to text.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**English (US)**|`string`|`en-US`| |**English (GB)**|`string`|`en-GB`| |**French**|`string`|`fr-FR`| |**Spanish**|`string`|`es-ES`| |**Dutch (Netherlands)**|`string`|`nl-NL`| |**Japanese**|`string`|`ja-JP`| |**Russian**|`string`|`ru-RU`| |**Arabic**|`string`|`ar-SA`| |**Italian**|`string`|`it-IT`| |**Korean**|`string`|`ko-KR`| |**Portuguese**|`string`|`pt-PT`| |**Turkish**|`string`|`tr-TR`| |**Indonesian**|`string`|`id-ID`| |**Malay**|`string`|`ms-MY`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-speech-to-text)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-transcribe)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-speech-to-text)|`google`|`v1p1beta1`| |[**Deepgram**](https://www.edenai.co/catalog/deepgram)|`deepgram`|`v1`| |[**Assembly**](https://www.edenai.co/catalog/assembly-ai)|`assembly`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.speech_recognition(language, files, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language: (required)
        :param str files: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.speech_recognition_with_http_info(language, files, providers, **kwargs)  # noqa: E501
        else:
            (data) = self.speech_recognition_with_http_info(language, files, providers, **kwargs)  # noqa: E501
            return data

    def speech_recognition_with_http_info(self, language, files, providers, **kwargs):  # noqa: E501
        """speech_recognition  # noqa: E501

        Speech recognition is technology that can recognize spoken words, which can then be converted to text.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**English (US)**|`string`|`en-US`| |**English (GB)**|`string`|`en-GB`| |**French**|`string`|`fr-FR`| |**Spanish**|`string`|`es-ES`| |**Dutch (Netherlands)**|`string`|`nl-NL`| |**Japanese**|`string`|`ja-JP`| |**Russian**|`string`|`ru-RU`| |**Arabic**|`string`|`ar-SA`| |**Italian**|`string`|`it-IT`| |**Korean**|`string`|`ko-KR`| |**Portuguese**|`string`|`pt-PT`| |**Turkish**|`string`|`tr-TR`| |**Indonesian**|`string`|`id-ID`| |**Malay**|`string`|`ms-MY`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-speech-to-text)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-transcribe)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-speech-to-text)|`google`|`v1p1beta1`| |[**Deepgram**](https://www.edenai.co/catalog/deepgram)|`deepgram`|`v1`| |[**Assembly**](https://www.edenai.co/catalog/assembly-ai)|`assembly`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.speech_recognition_with_http_info(language, files, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str language: (required)
        :param str files: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['language', 'files', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method speech_recognition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'language' is set
        if ('language' not in params or
                params['language'] is None):
            raise ValueError("Missing the required parameter `language` when calling `speech_recognition`")  # noqa: E501
        # verify the required parameter 'files' is set
        if ('files' not in params or
                params['files'] is None):
            raise ValueError("Missing the required parameter `files` when calling `speech_recognition`")  # noqa: E501
        # verify the required parameter 'providers' is set
        if ('providers' not in params or
                params['providers'] is None):
            raise ValueError("Missing the required parameter `providers` when calling `speech_recognition`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'language' in params:
            form_params.append(('language', params['language']))  # noqa: E501
        if 'files' in params:
            local_var_files['files'] = params['files']  # noqa: E501
        if 'providers' in params:
            form_params.append(('providers', params['providers']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/audio/speech_recognition', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def text_to_speech(self, text, language, option, providers, **kwargs):  # noqa: E501
        """text_to_speech  # noqa: E501

        Text-to-speech (TTS) system converts normal language text into speech.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**Arabic**|`string`|`ar-XA`| |**Chinese**|`string`|`cmn-CN`| |**Danish**|`string`|`da-DK`| |**Dutch**|`string`|`nl-NL`| |**English (US)**|`string`|`en-US`| |**English (UK)**|`string`|`en-GB`| |**German**|`string`|`de-DE`| |**Italy**|`string`|`it-IT`| |**Japanese**|`string`|`ja-JP`| |**Portuguese (Brazil)**|`string`|`pt-BR`| |**Portuguese (Portugal)**|`string`|`pt-PT`| |**Russian**|`string`|`ru-RU`| |**Spanish**|`string`|`es-ES`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-text-to-speech)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-polly)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-text-to-speech)|`google`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_to_speech(text, language, option, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str language: (required)
        :param str option: (required)
        :param str providers: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.text_to_speech_with_http_info(text, language, option, providers, **kwargs)  # noqa: E501
        else:
            (data) = self.text_to_speech_with_http_info(text, language, option, providers, **kwargs)  # noqa: E501
            return data

    def text_to_speech_with_http_info(self, text, language, option, providers, **kwargs):  # noqa: E501
        """text_to_speech  # noqa: E501

        Text-to-speech (TTS) system converts normal language text into speech.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |----|----|-----| |**Arabic**|`string`|`ar-XA`| |**Chinese**|`string`|`cmn-CN`| |**Danish**|`string`|`da-DK`| |**Dutch**|`string`|`nl-NL`| |**English (US)**|`string`|`en-US`| |**English (UK)**|`string`|`en-GB`| |**German**|`string`|`de-DE`| |**Italy**|`string`|`it-IT`| |**Japanese**|`string`|`ja-JP`| |**Portuguese (Brazil)**|`string`|`pt-BR`| |**Portuguese (Portugal)**|`string`|`pt-PT`| |**Russian**|`string`|`ru-RU`| |**Spanish**|`string`|`es-ES`|  **AVAILABLE PROVIDERS**   |Name|Value|Version| |----|-----|-------| |[**Microsoft Azure**](https://www.edenai.co/catalog/azure-text-to-speech)|`microsoft`|`v1.0`| |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-polly)|`amazon`|`boto3 (v1.15.18)`| |[**Google Cloud**](https://www.edenai.co/catalog/google-cloud-text-to-speech)|`google`|`v1`|  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_to_speech_with_http_info(text, language, option, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str language: (required)
        :param str option: (required)
        :param str providers: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text', 'language', 'option', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method text_to_speech" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `text_to_speech`")  # noqa: E501
        # verify the required parameter 'language' is set
        if ('language' not in params or
                params['language'] is None):
            raise ValueError("Missing the required parameter `language` when calling `text_to_speech`")  # noqa: E501
        # verify the required parameter 'option' is set
        if ('option' not in params or
                params['option'] is None):
            raise ValueError("Missing the required parameter `option` when calling `text_to_speech`")  # noqa: E501
        # verify the required parameter 'providers' is set
        if ('providers' not in params or
                params['providers'] is None):
            raise ValueError("Missing the required parameter `providers` when calling `text_to_speech`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'text' in params:
            form_params.append(('text', params['text']))  # noqa: E501
        if 'language' in params:
            form_params.append(('language', params['language']))  # noqa: E501
        if 'option' in params:
            form_params.append(('option', params['option']))  # noqa: E501
        if 'providers' in params:
            form_params.append(('providers', params['providers']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/audio/text_to_speech', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
