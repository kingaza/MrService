

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.actions import Action
from rasa_core.events import SlotSet

logger = logging.getLogger(__name__)



class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Please save the log files asap, ")
        dispatcher.utter_message("and provide it to local customer service.")
        return []


class ActionTicket(Action):
    def name(self):
        return 'action_ticket'

    def run(self, dispatcher, tracker, domain): 
        dispatcher.utter_message("I will submit a ticket of this incident for you.")
        return []