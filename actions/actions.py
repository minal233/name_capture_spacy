from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import re

class ValidateFullName(Action):
    def name(self) -> Text:
        return "validate_full_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        extracted_name = tracker.get_slot("full_name")

        # If no name was extracted by NLU
        if not extracted_name:
            dispatcher.utter_message(response="utter_invalid_name")
            return [SlotSet("full_name", None)]

        name = extracted_name.strip().title()  # Clean and capitalize properly

        # Validation rules
        if len(name) < 3 or len(name) > 50:
            dispatcher.utter_message(response="utter_invalid_name")
            return [SlotSet("full_name", None)]

        if not re.match(r'^[A-Za-z\s\.\-]+$', name):
            dispatcher.utter_message(response="utter_invalid_name")
            return [SlotSet("full_name", None)]

        # Name is valid → store it properly and return NO SlotSet for null
        return [SlotSet("full_name", name)]