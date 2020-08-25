from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Standard',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Reverse Counter. " \
                    "Let me know for which time would you like me to countdown from 60 to 0 "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please let me know for which time would you like me to countdown from 60 to 0, for example, start from 5"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "Please clarify for which time would you like me to countdown from 60 to 0, for example, start from 5"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Reverse Counter. "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_count_table_response(intent_request):
    session_attributes = {}
    card_title = "Counting time"
    speech_output = " "
    time = intent_request["intent"]["slots"]["Time"]["value"]

    if time == "1":
        speech_output = " 1 , 0.  For which time would you like me to count back again from 60 to 0"  
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "2":
        speech_output = " 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "3":
        speech_output = " 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "4":
        speech_output = " 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "5":
        speech_output = " 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "6":
        speech_output = " 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "7":
        speech_output = " 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "8":
        speech_output = " 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "9":
        speech_output = " 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "10":
        speech_output = " 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "11":
        speech_output = " 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "12":
        speech_output = " 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "13":
        speech_output = " 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "14":
        speech_output = " 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "15":
        speech_output = " 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "16":
        speech_output = " 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "17":
        speech_output = " 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "18":
        speech_output = " 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "19":
        speech_output = " 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "20":
        speech_output = " 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "21":
        speech_output = " 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "22":
        speech_output = " 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "23":
        speech_output = " 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "24":
        speech_output = " 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "25":
        speech_output = " 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "26":
        speech_output = " 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0. For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "27":
        speech_output = " 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "28":
        speech_output = " 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "29":
        speech_output = " 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "30":
        speech_output = " 30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "31":
        speech_output = " 31 , 30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "32":
        speech_output = " 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "33":
        speech_output = " 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "34":
        speech_output = " 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "35":
        speech_output = " 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "36":
        speech_output = " 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "37":
        speech_output = " 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "38":
        speech_output = " 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "39":
        speech_output = " 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "40":
        speech_output = " 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "41":
        speech_output = " 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "42":
        speech_output = " 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "43":
        speech_output = " 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "44":
        speech_output = " 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "45":
        speech_output = " 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "46":
        speech_output = " 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "47":
        speech_output = " 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "48":
        speech_output = " 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "49":
        speech_output = " 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "50":
        speech_output = " 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "51":
        speech_output = " 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "52":
        speech_output = " 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "53":
        speech_output = " 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "54":
        speech_output = " 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 ,0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "55":
        speech_output = " 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0. For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "56":
        speech_output = " 56 , 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "57":
        speech_output = " 57 , 56 , 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "58":
        speech_output = " 58 , 57 , 56 , 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "59":
        speech_output = " 59 , 58 , 57 , 56 , 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    elif time == "60":
        speech_output = " 60 , 59 , 58 , 57 , 56 , 55 , 54 , 53 , 52 , 51 , 50 , 49 , 48 , 47 , 46 , 45 , 44 , 43 , 42 , 41 , 40 , 39 , 38 , 37 , 36 , 35 , 34 , 33 , 32 , 31 ,30, 29 , 28 , 27 , 26 , 25 , 24 , 23 , 22 , 21 , 20 , 19 , 18 , 17 , 16 , 15 , 14 , 13 , 12 , 11 , 10 , 9 , 8 , 7 , 6, 5 , 4 , 3 , 2 , 1 , 0.  For which time would you like me to count back again from 60 to 0"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    else:
        speech_output = "Please let me know for which time would you like me to countdown from 60 to 0, for example, start from 5"
        reprompt_text = "Let me know for which time Would you like me to count back again from 60 to 0 or want to stop."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyCountIntent":
        return get_count_table_response(intent_request)
    elif intent_name == "MyHelpIntent":
        return get_help_response() 
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
