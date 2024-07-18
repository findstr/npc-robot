from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
import re

from actions import ChatApis

from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):

        # 访问图灵机器人API(闲聊)
        text = tracker.latest_message.get('text')
        message = ChatApis.get_response(text)
        if message is not None:
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message(response='utter_default')
        return [UserUtteranceReverted()]
