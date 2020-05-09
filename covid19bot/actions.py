# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests


class ActionSearchNoPatients(Action):

    def name(self) -> Text:
        return "action_search_no_patients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('location')

        loc = str(loc).lower()
        # Spelling correction

        params = {
  			'loc': loc
		}

        data = requests.get("http://127.0.0.1:8000/getstatecases", params)

        data = data.json()

        name = data['name']
        confirmed = data['confirmed']
        recovered = data['recovered'] 
        deceased = data['deceased']
        active = data['active']
        date = data['date']

        response = """As of {} in {}. Confirmed cases: {}, Recovered cases: {}, Deceased cases: {}, Active cases:{}""".format(date,name, confirmed, recovered, deceased, active)

        dispatcher.utter_message(response)


        return []

class ActionSearchCasesOnDate(Action):

    def name(self) -> Text:
        return "action_search_cases_ondate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot('date')

        params = {
  			'date': date
		}

        data = requests.get("http://127.0.0.1:8000/totalcases", params)

        data = data.json()

        confirmed = data['confirmed']
        recovered = data['recovered'] 
        deceased = data['deceased']
        date = data['date']

        response = """As of {} in {}. Confirmed cases: {}, Recovered cases: {}, Deceased cases: {}.""".format(date,"INDIA", confirmed, recovered, deceased)

        dispatcher.utter_message(response)


        return []

class ActionSearchGrowthRate(Action):

    def name(self) -> Text:
        return "action_search_growth_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('location')

        loc = str(loc).lower()
        # Spelling correction

        params = {
  			'loc': loc
		}

        data = requests.get("http://127.0.0.1:8000/growthrate", params)

        data = data.json()

        name = data['name']
        growthrate = data['growthrate'] 
    

        response = """ Growth rate in {} is {}""".format(name,growthrate)

        dispatcher.utter_message(response)

        return []

class ActionSearchHightestRate(Action):

    def name(self) -> Text:
        return "action_search_highest_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #loc = tracker.get_slot('location')

        #params = {
  		#	'loc': loc
		#}

        data = requests.get("http://127.0.0.1:8000/highestgrowthrate")

        data = data.json()

        name = data['name']
        date = data['date'] 
    

        response = """ Highest Growth rate is in {} as of {}""".format(name,date)

        dispatcher.utter_message(response)

        return []

class ActionCheckZone(Action):

    def name(self) -> Text:
        return "action_check_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('location')

        loc = str(loc).lower()
        # Spelling correction

        params = {
  			'loc': loc
		}

        data = requests.get("http://127.0.0.1:8000/getzonetype",params)

        data = data.json()

        name = data['district']
        date = data['updatedate'] 
        zone = data['zone']

        response = """ {} is {} zone since {}""".format(name,zone,date)

        dispatcher.utter_message(response)

        return []

