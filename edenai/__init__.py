# coding: utf-8

# flake8: noqa

"""
    Eden AI API Documentation

    <a href=\"https://app.edenai.run/user/login\" target=\"_blank\"><img src=\"/static/images/welcome.png\"></a>. # Welcome  Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies: * Vision:  <a href=\"https://www.edenai.co/vision\" target=\"_blank\">www.edenai.co/vision</a>. * Text & NLP: <a href=\"https://www.edenai.co/text\" target=\"_blank\">www.edenai.co/text</a>. * Speech & Audio: <a href=\"https://www.edenai.co/speech\" target=\"_blank\">www.edenai.co/speech</a>. * OCR: <a href=\"https://www.edenai.co/ocr\" target=\"_blank\">www.edenai.co/ocr</a>. * Machine Translation: <a href=\"https://www.edenai.co/translation\" target=\"_blank\">www.edenai.co/translation</a>. * Prediction: <a href=\"https://www.edenai.co/prediction\" target=\"_blank\">www.edenai.co/prediction</a>.  For all the proposed technologies, we provide a single endpoint:  the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog  # Support & community  ### 1- Support If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.   ### 2- Community  You can interact personally with other people actively using and working with Eden AI and join our  <a href=\"https://join.slack.com/t/edenai/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w\" target=\"_blank\">Slack community</a>.  We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on Github: <a href=\"https://github.com/edenai\" target=\"_blank\">https://github.com/edenai</a>.  ### 3- Blog  We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: <a href=\"https://www.edenai.co/blog\" target=\"_blank\">https://www.edenai.co/blog</a>.   # Authentication  ## Create account ![Register](/static/images/register.png)  To create an account, please go to this link: <a href=\"https://app.edenai.run/user/login\" target=\"_blank\">app.edenai.run/user/login</a>. You can create an account with your email address or by using your account on available platforms (Gmail, Github, etc.).   By creating an account with your email address, you will receive a confirmation email with a link to click. Check your spam if needed and contact us if you have any problem: contact@edenai.co  ![Login](/static/images/login.png) ## API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will have access to your API key to start using the different AI engines offered by Eden AI.   ![api_key](/static/images/api_key.png) # Portal Guide  Eden AI provides a web portal that allows you to do several tasks:  ![portal](/static/images/portal.png)  ### 1- Benchmark and test The platform allows you to easily compare competing engines without having to code. By uploading your data, you have access to the prediction results of the different engines. This gives you a first overview of the performance of AI engines.   ![benchmark](/static/images/benchmark.png)  ### 2- Cost management The <a href=\"https://app.edenai.run/admin/cost-management\" target=\"_blank\">cost management page</a> also allows you to centralize the costs associated with the different engines with various filters to simplify the analysis.   This page also allows you to define monthly budget limits not to be exceeded to secure the use of different AI engines.   ![cost-management](/static/images/cost_management.png) ### 3- Account The <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">account page</a> allows you to change your information and password. It also gives you access to your API key that you can renew if needed.   This page also allows you to add a credit card and to buy with credits to use all the engines offered by Eden AI.   ![account](/static/images/account.png)   # API Guide  Eden AI API has different endpoints that refer to different AI services. The connected providers are thus parameters that the user can easily change.   # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@edenai.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from edenai.api.auto_ml_text_data_api import AutoMLTextDataApi
from edenai.api.eden_ai_tools_api import EdenAIToolsApi
from edenai.api.ocr_api import OCRApi
from edenai.api.pipelines_api import PipelinesApi
from edenai.api.speech_api import SpeechApi
from edenai.api.text_api import TextApi
from edenai.api.translation_api import TranslationApi
from edenai.api.vision_api import VisionApi
# import ApiClient
from edenai.api_client import ApiClient
from edenai.configuration import Configuration
# import models into sdk package
from edenai.models.audio_speech_recognition_async_body import AudioSpeechRecognitionAsyncBody
from edenai.models.audio_speech_recognition_body import AudioSpeechRecognitionBody
from edenai.models.audio_text_to_speech_body import AudioTextToSpeechBody
from edenai.models.inline_response200 import InlineResponse200
from edenai.models.inline_response2001 import InlineResponse2001
from edenai.models.inline_response20010 import InlineResponse20010
from edenai.models.inline_response20010_result import InlineResponse20010Result
from edenai.models.inline_response20010_result1 import InlineResponse20010Result1
from edenai.models.inline_response20010_result_landmarks import InlineResponse20010ResultLandmarks
from edenai.models.inline_response20011 import InlineResponse20011
from edenai.models.inline_response20011_result import InlineResponse20011Result
from edenai.models.inline_response20011_result1 import InlineResponse20011Result1
from edenai.models.inline_response20012 import InlineResponse20012
from edenai.models.inline_response20012_result import InlineResponse20012Result
from edenai.models.inline_response2001_result import InlineResponse2001Result
from edenai.models.inline_response2001_result1 import InlineResponse2001Result1
from edenai.models.inline_response2001_result_bounding_boxes import InlineResponse2001ResultBoundingBoxes
from edenai.models.inline_response2002 import InlineResponse2002
from edenai.models.inline_response2002_customer_information import InlineResponse2002CustomerInformation
from edenai.models.inline_response2002_item_lines import InlineResponse2002ItemLines
from edenai.models.inline_response2002_locale import InlineResponse2002Locale
from edenai.models.inline_response2002_merchant_information import InlineResponse2002MerchantInformation
from edenai.models.inline_response2002_result import InlineResponse2002Result
from edenai.models.inline_response2002_result1 import InlineResponse2002Result1
from edenai.models.inline_response2002_results import InlineResponse2002Results
from edenai.models.inline_response2003 import InlineResponse2003
from edenai.models.inline_response2003_result import InlineResponse2003Result
from edenai.models.inline_response2003_result1 import InlineResponse2003Result1
from edenai.models.inline_response2004 import InlineResponse2004
from edenai.models.inline_response2004_result import InlineResponse2004Result
from edenai.models.inline_response2004_result1 import InlineResponse2004Result1
from edenai.models.inline_response2005 import InlineResponse2005
from edenai.models.inline_response2005_result import InlineResponse2005Result
from edenai.models.inline_response2005_result1 import InlineResponse2005Result1
from edenai.models.inline_response2006 import InlineResponse2006
from edenai.models.inline_response2006_result import InlineResponse2006Result
from edenai.models.inline_response2006_result1 import InlineResponse2006Result1
from edenai.models.inline_response2007 import InlineResponse2007
from edenai.models.inline_response2007_result import InlineResponse2007Result
from edenai.models.inline_response2007_result1 import InlineResponse2007Result1
from edenai.models.inline_response2008 import InlineResponse2008
from edenai.models.inline_response2008_result import InlineResponse2008Result
from edenai.models.inline_response2008_result1 import InlineResponse2008Result1
from edenai.models.inline_response2009 import InlineResponse2009
from edenai.models.inline_response2009_result import InlineResponse2009Result
from edenai.models.inline_response2009_result1 import InlineResponse2009Result1
from edenai.models.inline_response201 import InlineResponse201
from edenai.models.inline_response2011 import InlineResponse2011
from edenai.models.inline_response2011_result import InlineResponse2011Result
from edenai.models.inline_response2011_result1 import InlineResponse2011Result1
from edenai.models.inline_response201_result import InlineResponse201Result
from edenai.models.inline_response201_result1 import InlineResponse201Result1
from edenai.models.ocr_ocr_body import OcrOcrBody
from edenai.models.ocr_ocr_invoice_body import OcrOcrInvoiceBody
from edenai.models.pipelines_body import PipelinesBody
from edenai.models.project_id_train_body import ProjectIdTrainBody
from edenai.models.project_project_id_body import ProjectProjectIdBody
from edenai.models.text_keyword_extraction_body import TextKeywordExtractionBody
from edenai.models.text_named_entity_recognition_body import TextNamedEntityRecognitionBody
from edenai.models.text_project_body import TextProjectBody
from edenai.models.text_sentiment_analysis_body import TextSentimentAnalysisBody
from edenai.models.text_syntax_analysis_body import TextSyntaxAnalysisBody
from edenai.models.tools_search_body import ToolsSearchBody
from edenai.models.tools_search_body1 import ToolsSearchBody1
from edenai.models.train_id_prediction_body import TrainIdPredictionBody
from edenai.models.translation_automatic_translation_body import TranslationAutomaticTranslationBody
from edenai.models.translation_language_detection_body import TranslationLanguageDetectionBody
from edenai.models.vision_explicit_content_detection_body import VisionExplicitContentDetectionBody
from edenai.models.vision_face_detection_body import VisionFaceDetectionBody
from edenai.models.vision_object_detection_body import VisionObjectDetectionBody
from edenai.simplify import *
