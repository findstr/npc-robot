from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLeaveWorld(Action):

    def name(self) -> Text:
        return "action_leave"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        begin_time = tracker.get_slot("begin_time")
        duration = tracker.get_slot("duration")
        leave_type = tracker.get_slot("leave_type")
        print(f"请假参数信息，开始时间：{begin_time}, 时长：{duration}，类型：{leave_type}")
        dispatcher.utter_message(text=f"您从{begin_time}开始，为期{duration}天的{leave_type}申请已提交，请关注审批进度")
        return []
