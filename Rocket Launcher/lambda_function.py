from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
        },
        'card': {
            'type' : 'Standard',
            'title':  title,
            'text' : output
        },

        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml':  "<speak>" + reprompt_text + "</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_with_card_only(title, card_text, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml':  "<speak>" + output + "</speak>"
        },
        'card': {
            'type' : 'Standard',
            'title':  title,
            'text' : card_text
        },

        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml':  "<speak>" + reprompt_text + "</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_without_reprompt(title, output,  should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
        },
        'card': {
            'type' : 'Standard',
            'title':  title,
            'text' : output
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
    card_title = ""
    card_text = "Welcome to Rocket Launcher."
    speech_output = "Welcome to Rocket Launcher. " \
                    "Let me know for which time would you like me to countdown from 100 to 0 "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please let me know for which time would you like me to countdown from 100 to 0, for example, start from 5"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_with_card_only(
        card_title, card_text,  speech_output, reprompt_text, should_end_session))
        
def get_help_response():
    session_attributes = {}
    card_title = "Help Session"
    card_text = "From 100 to 0"
    speech_output = "Please clarify for which time would you like me to countdown from 100 to 0, for example, start from 5"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_with_card_only(
        card_title, card_text,  speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Rocket Launcher. See you soon!" 
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response_without_reprompt(
        card_title, speech_output, should_end_session))


def get_count_table_response(intent, session):
    session_attributes = {}
    card_title = ""
    card_text = ""
    speech_output = " "
    
    time = intent["slots"]["Time"]["value"]
    session_attributes = create_time_attributes(time)
    card_text = "Countdown from " + time
    if time == "1":
        speech_output = " 1," + "<break time = \".5s\"/> " +  "0. " + "<break time = \".5s\"/> "\
                        +  " Do you want to repeat?"  
        reprompt_text = "Do you want to repeat?"
    elif time == "2":
        speech_output = " 2 ," + "<break time = \".5s\"/> " +  " 1 , " + "<break time = \".5s\"/> "\
                        +  "0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "3":
        speech_output = " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> "\
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> "\
                        +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "4":
        speech_output = " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> "\
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0." + "<break time = \".5s\"/> " +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "5":
        speech_output = " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0." + "<break time = \".5s\"/> "\
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "6":
        speech_output = " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0." + "<break time = \".5s\"/> " +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "7":
        speech_output = " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0." + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "8":
        speech_output = "8, " + "<break time = \".5s\"/> " +  "7, " + "<break time = \".5s\"/> " \
                        +  "6, " + "<break time = \".5s\"/> " +  "5, " + "<break time = \".5s\"/> " \
                        +  "4, " + "<break time = \".5s\"/> " +  "3, " + "<break time = \".5s\"/> " \
                        +  "2, " + "<break time = \".5s\"/> " +  "1, " + "<break time = \".5s\"/> " \
                        +  "0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "9":
        speech_output = " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
						+  " 1 ," + "<break time = \".5s\"/> " +  " 0." + "<break time = \".5s\"/> " \
                        +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "10":
        speech_output = " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "11":
        speech_output = " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0." + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "12":
        speech_output = " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "13":
        speech_output = " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0." + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "14":
        speech_output = " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "15":
        speech_output = " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "16":
        speech_output = " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6 ," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "17":
        speech_output = " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "18":
        speech_output = " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "19":
        speech_output = " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "20":
        speech_output = " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "21":
        speech_output = " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "22":
        speech_output = " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "23":
        speech_output = " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "24":
        speech_output = " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "25":
        speech_output = " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "26":
        speech_output = " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "27":
        speech_output = " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "28":
        speech_output = " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "29":
        speech_output = " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "30":
        speech_output = " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "31":
        speech_output = " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "32":
        speech_output = " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "33":
        speech_output = " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "34":
        speech_output = " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "35":
        speech_output = " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "36":
        speech_output = " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "37":
        speech_output = " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "38":
        speech_output = " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "39":
        speech_output = " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "40":
        speech_output = " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "41":
        speech_output = " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "42":
        speech_output = " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "43":
        speech_output = " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "44":
        speech_output = " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "45":
        speech_output = " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "46":
        speech_output = " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "47":
        speech_output = " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "48":
        speech_output = " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "49":
        speech_output = " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "50":
        speech_output = " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "51":
        speech_output = " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "52":
        speech_output = " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "53":
        speech_output = " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "54":
        speech_output = " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "55":
        speech_output = " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "56":
        speech_output = " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "57":
        speech_output = " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "58":
        speech_output = " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "59":
        speech_output = " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "60":
        speech_output = " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "61":
        speech_output = " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "62":
        speech_output = " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "63":
        speech_output = " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "64":
        speech_output = " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "65":
        speech_output = " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "66":
        speech_output = " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "67":
        speech_output = " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"    
    elif time == "68":
        speech_output = " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "69":
        speech_output = " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "70":
        speech_output = " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "71":
        speech_output = " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "72":
        speech_output = " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "73":
        speech_output = " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "74":
        speech_output = " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "75":
        speech_output = " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "76":
        speech_output = " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "77":
        speech_output = " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "78":
        speech_output = " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"

        reprompt_text = "Do you want to repeat?"
    elif time == "79":
        speech_output = " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "80":
        speech_output = " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"

        reprompt_text = "Do you want to repeat?"
    elif time == "81":
        speech_output = " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "82":
        speech_output = " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"

        reprompt_text = "Do you want to repeat?"
    elif time == "83":
        speech_output = " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 

        reprompt_text = "Do you want to repeat?"
    elif time == "84":
        speech_output = " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"

        reprompt_text = "Do you want to repeat?"
    elif time == "85":
        speech_output = " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?" 
        reprompt_text = "Do you want to repeat?"
    elif time == "86":
        speech_output = " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"

        reprompt_text = "Do you want to repeat?"
    elif time == "87":
        speech_output = " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"         
        reprompt_text = "Do you want to repeat?"
    elif time == "88":
        speech_output = " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "89":
        speech_output = " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"         
        reprompt_text = "Do you want to repeat?"
    elif time == "90":
        speech_output = " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "91":
        speech_output = " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                        +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"         
        reprompt_text = "Do you want to repeat?"
    elif time == "92":
        speech_output = " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                        +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "93":
        speech_output = " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                        +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                        +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"         
        reprompt_text = "Do you want to repeat?"
    elif time == "94":
        speech_output = " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                        +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                        +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "95":
        speech_output = " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                        +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                        +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                        +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"         
        reprompt_text = "Do you want to repeat?"
    elif time == "96":
        speech_output = " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                        +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                        +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                        +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "97":
        speech_output = " 97 ," + "<break time = \".5s\"/> " +  " 96 ," + "<break time = \".5s\"/> " \
                        +  " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                        +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                        +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                        +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "98":
        speech_output = " 98 ," + "<break time = \".5s\"/> " +  " 97 ," + "<break time = \".5s\"/> " \
                        +  " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                        +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                        +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                        +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "99":
        speech_output = " 99 ," + "<break time = \".5s\"/> " +  " 98 ," + "<break time = \".5s\"/> " \
                        +  " 97 ," + "<break time = \".5s\"/> " +  " 96 ," + "<break time = \".5s\"/> " \
                        +  " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                        +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                        +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                        +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                        +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                        +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                        +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                        +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                        +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                        +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                        +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                        +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                        +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                        +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                        +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                        +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                        +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                        +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                        +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                        +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                        +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                        +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                        +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                        +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                        +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                        +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                        +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                        +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                        +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                        +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                        +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                        +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                        +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                        +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                        +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                        +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                        +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                        +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                        +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                        +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                        +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                        +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                        +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                        +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                        +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                        +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                        +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                        +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " + "<break time = \".5s\"/> " \
                        +  "  Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    elif time == "100":
        speech_output = " 100 , " + "<break time = \".5s\"/> " +  " 99 ," + "<break time = \".5s\"/> " \
                        +  " 98 ," + "<break time = \".5s\"/> " +  " 97 ," + "<break time = \".5s\"/> " \
                        +  " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                        +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                        +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                        +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                        +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                        +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                        +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                        +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                        +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                        +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                        +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                        +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                        +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                        +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                        +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                        +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                        +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                        +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                        +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                        +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                        +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                        +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                        +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                        +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                        +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                        +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                        +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                        +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                        +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                        +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                        +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                        +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                        +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                        +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                        +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                        +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                        +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                        +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                        +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                        +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                        +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                        +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                        +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                        +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                        +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                        +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                        +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                        +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                        +  " 0. " + "<break time = \".5s\"/> " +  " Do you want to repeat?"
        reprompt_text = "Do you want to repeat?"
    else:
        speech_output = "Please make sure time should be in between from 100 to 0."
        reprompt_text = "Please make sure time should be in between from 100 to 0."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_with_card_only(
        card_title, card_text,  speech_output, reprompt_text, should_end_session))

def create_time_attributes(time):
    return {"favtime": time}


def get_repeat_response(intent, session):
    session_attributes = {}
    card_title = ""
    card_text = ""
    
    if session.get('attributes', {}) and "favtime" in session.get('attributes', {}):
        time = session['attributes']['favtime']
        card_text = "Countdown from " + time
        if time == "1":
            speech_output = " 1," + "<break time = \".5s\"/> " +  "0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "2":
            speech_output = " 2 ," + "<break time = \".5s\"/> " +  " 1 , " + "<break time = \".5s\"/> "+  "0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "3":
            speech_output = " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> "\
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "4":
            speech_output = " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> "\
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0." 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "5":
            speech_output = " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0."
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "6":
            speech_output = " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " \
                            +  " 0." 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "7":
            speech_output = " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0." 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "8":
            speech_output = "8, " + "<break time = \".5s\"/> " +  "7, " + "<break time = \".5s\"/> " \
                            +  "6, " + "<break time = \".5s\"/> " +  "5, " + "<break time = \".5s\"/> " \
                            +  "4, " + "<break time = \".5s\"/> " +  "3, " + "<break time = \".5s\"/> " \
                            +  "2, " + "<break time = \".5s\"/> " +  "1, " + "<break time = \".5s\"/> " + "0."
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "9":
            speech_output = " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
							+  " 1 ," + "<break time = \".5s\"/> " +  " 0 ."
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "10":
            speech_output = " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " + " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "11":
            speech_output = " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0." 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "12":
            speech_output = " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "13":
            speech_output = " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0." 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "14":
            speech_output = " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "15":
            speech_output = " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6," + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "16":
            speech_output = " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6 ," + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "17":
            speech_output = " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "18":
            speech_output = " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " + " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "19":
            speech_output = " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "20":
            speech_output = " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "21":
            speech_output = " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "22":
            speech_output = " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "23":
            speech_output = " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "24":
            speech_output = " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " + " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "25":
            speech_output = " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "26":
            speech_output = " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "27":
            speech_output = " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "28":
            speech_output = " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "29":
            speech_output = " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "30":
            speech_output = " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "31":
            speech_output = " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "32":
            speech_output = " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "33":
            speech_output = " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "34":
            speech_output = " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "35":
            speech_output = " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "36":
            speech_output = " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0."
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "37":
            speech_output = " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "38":
            speech_output = " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "39":
            speech_output = " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "40":
            speech_output = " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "41":
            speech_output = " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "42":
            speech_output = " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "43":
            speech_output = " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "44":
            speech_output = " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "45":
            speech_output = " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "46":
            speech_output = " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "47":
            speech_output = " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "48":
            speech_output = " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "49":
            speech_output = " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "50":
            speech_output = " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "51":
            speech_output = " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "52":
            speech_output = " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "53":
            speech_output = " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "54":
            speech_output = " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "55":
            speech_output = " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "56":
            speech_output = " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "57":
            speech_output = " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "58":
            speech_output = " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0."
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "59":
            speech_output = " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "60":
            speech_output = " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "61":
            speech_output = " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "62":
            speech_output = " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "63":
            speech_output = " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "64":
            speech_output = " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "65":
            speech_output = " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "66":
            speech_output = " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "67":
            speech_output = " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"    
        elif time == "68":
            speech_output = " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "69":
            speech_output = " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "70":
            speech_output = " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "71":
            speech_output = " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "72":
            speech_output = " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "73":
            speech_output = " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "74":
            speech_output = " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "75":
            speech_output = " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "76":
            speech_output = " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "77":
            speech_output = " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "78":
            speech_output = " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+ " 0. "
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "79":
            speech_output = " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "80":
            speech_output = " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+ " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "81":
            speech_output = " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "82":
            speech_output = " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+ " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "83":
            speech_output = " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "  
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "84":
            speech_output = " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "85":
            speech_output = " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "86":
            speech_output = " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. "
    
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "87":
            speech_output = " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "          
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "88":
            speech_output = " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!" 
        elif time == "89":
            speech_output = " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "         
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "90":
            speech_output = " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "91":
            speech_output = " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                            +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "         
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "92":
            speech_output = " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                            +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +" 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "93":
            speech_output = " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                            +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                            +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "         
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "94":
            speech_output = " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                            +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                            +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+" 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "95":
            speech_output = " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                            +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                            +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                            +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "       
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "96":
            speech_output = " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                            +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                            +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                            +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+" 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "97":
            speech_output = " 97 ," + "<break time = \".5s\"/> " +  " 96 ," + "<break time = \".5s\"/> " \
                            +  " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                            +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                            +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                            +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "98":
            speech_output = " 98 ," + "<break time = \".5s\"/> " +  " 97 ," + "<break time = \".5s\"/> " \
                            +  " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                            +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                            +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                            +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> "+" 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "99":
            speech_output = " 99 ," + "<break time = \".5s\"/> " +  " 98 ," + "<break time = \".5s\"/> " \
                            +  " 97 ," + "<break time = \".5s\"/> " +  " 96 ," + "<break time = \".5s\"/> " \
                            +  " 95 ," + "<break time = \".5s\"/> " +  " 94 ," + "<break time = \".5s\"/> " \
                            +  " 93 ," + "<break time = \".5s\"/> " +  " 92 ," + "<break time = \".5s\"/> " \
                            +  " 91 ," + "<break time = \".5s\"/> " +  " 90 ," + "<break time = \".5s\"/> " \
                            +  " 89 ," + "<break time = \".5s\"/> " +  " 88 ," + "<break time = \".5s\"/> " \
                            +  " 87 ," + "<break time = \".5s\"/> " +  " 86 ," + "<break time = \".5s\"/> " \
                            +  " 85 ," + "<break time = \".5s\"/> " +  " 84 ," + "<break time = \".5s\"/> " \
                            +  " 83 ," + "<break time = \".5s\"/> " +  " 82 ," + "<break time = \".5s\"/> " \
                            +  " 81 ," + "<break time = \".5s\"/> " +  " 80 ," + "<break time = \".5s\"/> " \
                            +  " 79 ," + "<break time = \".5s\"/> " +  " 78 ," + "<break time = \".5s\"/> " \
                            +  " 77 ," + "<break time = \".5s\"/> " +  " 76 ," + "<break time = \".5s\"/> " \
                            +  " 75 ," + "<break time = \".5s\"/> " +  " 74 ," + "<break time = \".5s\"/> " \
                            +  " 73 ," + "<break time = \".5s\"/> " +  " 72 ," + "<break time = \".5s\"/> " \
                            +  " 71 ," + "<break time = \".5s\"/> " +  " 70 ," + "<break time = \".5s\"/> " \
                            +  " 69 ," + "<break time = \".5s\"/> " +  " 68 ," + "<break time = \".5s\"/> " \
                            +  " 67 ," + "<break time = \".5s\"/> " +  " 66 ," + "<break time = \".5s\"/> " \
                            +  " 65 ," + "<break time = \".5s\"/> " +  " 64 ," + "<break time = \".5s\"/> " \
                            +  " 63 ," + "<break time = \".5s\"/> " +  " 62 ," + "<break time = \".5s\"/> " \
                            +  " 61 ," + "<break time = \".5s\"/> " +  " 60 ," + "<break time = \".5s\"/> " \
                            +  " 59 ," + "<break time = \".5s\"/> " +  " 58 ," + "<break time = \".5s\"/> " \
                            +  " 57 ," + "<break time = \".5s\"/> " +  " 56 ," + "<break time = \".5s\"/> " \
                            +  " 55 ," + "<break time = \".5s\"/> " +  " 54 ," + "<break time = \".5s\"/> " \
                            +  " 53 ," + "<break time = \".5s\"/> " +  " 52 ," + "<break time = \".5s\"/> " \
                            +  " 51 ," + "<break time = \".5s\"/> " +  " 50 ," + "<break time = \".5s\"/> " \
                            +  " 49 ," + "<break time = \".5s\"/> " +  " 48 ," + "<break time = \".5s\"/> " \
                            +  " 47 ," + "<break time = \".5s\"/> " +  " 46 ," + "<break time = \".5s\"/> " \
                            +  " 45 ," + "<break time = \".5s\"/> " +  " 44 ," + "<break time = \".5s\"/> " \
                            +  " 43 ," + "<break time = \".5s\"/> " +  " 42 ," + "<break time = \".5s\"/> " \
                            +  " 41 ," + "<break time = \".5s\"/> " +  " 40 ," + "<break time = \".5s\"/> " \
                            +  " 39 ," + "<break time = \".5s\"/> " +  " 38 ," + "<break time = \".5s\"/> " \
                            +  " 37 ," + "<break time = \".5s\"/> " +  " 36 ," + "<break time = \".5s\"/> " \
                            +  " 35 ," + "<break time = \".5s\"/> " +  " 34 ," + "<break time = \".5s\"/> " \
                            +  " 33 ," + "<break time = \".5s\"/> " +  " 32 ," + "<break time = \".5s\"/> " \
                            +  " 31 , " + "<break time = \".5s\"/> " +  "  30, " + "<break time = \".5s\"/> " \
                            +  " 29 ," + "<break time = \".5s\"/> " +  "  28 ," + "<break time = \".5s\"/> " \
                            +  " 27 ," + "<break time = \".5s\"/> " +  "  26 ," + "<break time = \".5s\"/> " \
                            +  " 25 ," + "<break time = \".5s\"/> " +  " 24 ," + "<break time = \".5s\"/> "\
                            +  " 23 ," + "<break time = \".5s\"/> " +  " 22 ," + "<break time = \".5s\"/> " \
                            +  " 21 ," + "<break time = \".5s\"/> " +  " 20 ," + "<break time = \".5s\"/> " \
                            +  " 19 ," + "<break time = \".5s\"/> " +  " 18 ," + "<break time = \".5s\"/> " \
                            +  " 17 ," + "<break time = \".5s\"/> " +  " 16 ," + "<break time = \".5s\"/> " \
                            +  " 15 ," + "<break time = \".5s\"/> " +  " 14 ," + "<break time = \".5s\"/> " \
                            +  " 13 ," + "<break time = \".5s\"/> " +  " 12 ," + "<break time = \".5s\"/> " \
                            +  " 11 ," + "<break time = \".5s\"/> " +  " 10 ," + "<break time = \".5s\"/> " \
                            +  " 9 ," + "<break time = \".5s\"/> " +  " 8 ," + "<break time = \".5s\"/> " \
                            +  " 7 ," + "<break time = \".5s\"/> " +  " 6, " + "<break time = \".5s\"/> " \
                            +  " 5 ," + "<break time = \".5s\"/> " +  " 4 ," + "<break time = \".5s\"/> " \
                            +  " 3 ," + "<break time = \".5s\"/> " +  " 2 ," + "<break time = \".5s\"/> " \
                            +  " 1 ," + "<break time = \".5s\"/> " +  " 0. " 
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        elif time == "100":
            speech_output = " 100 , " + "<break time = \".5s\"/> " +  " 99 ," + "<break time = \".5s\"/> " \
                            +  " 98 ," + "<break time = \".5s\"/> " +  " 97 ," + "<break time = \".5s\"/> " \
                            +  " 96 ," + "<break time = \".5s\"/> " +  " 95 ," + "<break time = \".5s\"/> " \
                            +  " 94 ," + "<break time = \".5s\"/> " +  " 93 ," + "<break time = \".5s\"/> " \
                            +  " 92 ," + "<break time = \".5s\"/> " +  " 91 ," + "<break time = \".5s\"/> " \
                            +  " 90 ," + "<break time = \".5s\"/> " +  " 89 ," + "<break time = \".5s\"/> " \
                            +  " 88 ," + "<break time = \".5s\"/> " +  " 87 ," + "<break time = \".5s\"/> " \
                            +  " 86 ," + "<break time = \".5s\"/> " +  " 85 ," + "<break time = \".5s\"/> " \
                            +  " 84 ," + "<break time = \".5s\"/> " +  " 83 ," + "<break time = \".5s\"/> " \
                            +  " 82 ," + "<break time = \".5s\"/> " +  " 81 ," + "<break time = \".5s\"/> " \
                            +  " 80 ," + "<break time = \".5s\"/> " +  " 79 ," + "<break time = \".5s\"/> " \
                            +  " 78 ," + "<break time = \".5s\"/> " +  " 77 ," + "<break time = \".5s\"/> " \
                            +  " 76 ," + "<break time = \".5s\"/> " +  " 75 ," + "<break time = \".5s\"/> " \
                            +  " 74 ," + "<break time = \".5s\"/> " +  " 73 ," + "<break time = \".5s\"/> " \
                            +  " 72 ," + "<break time = \".5s\"/> " +  " 71 ," + "<break time = \".5s\"/> " \
                            +  " 70 ," + "<break time = \".5s\"/> " +  " 69 ," + "<break time = \".5s\"/> " \
                            +  " 68 ," + "<break time = \".5s\"/> " +  " 67 ," + "<break time = \".5s\"/> " \
                            +  " 66 ," + "<break time = \".5s\"/> " +  " 65 ," + "<break time = \".5s\"/> " \
                            +  " 64 ," + "<break time = \".5s\"/> " +  " 63 ," + "<break time = \".5s\"/> " \
                            +  " 62 ," + "<break time = \".5s\"/> " +  " 61 ," + "<break time = \".5s\"/> " \
                            +  " 60 ," + "<break time = \".5s\"/> " +  " 59 ," + "<break time = \".5s\"/> " \
                            +  " 58 ," + "<break time = \".5s\"/> " +  " 57 ," + "<break time = \".5s\"/> " \
                            +  " 56 ," + "<break time = \".5s\"/> " +  " 55 ," + "<break time = \".5s\"/> " \
                            +  " 54 ," + "<break time = \".5s\"/> " +  " 53 ," + "<break time = \".5s\"/> " \
                            +  " 52 ," + "<break time = \".5s\"/> " +  " 51 ," + "<break time = \".5s\"/> " \
                            +  " 50 ," + "<break time = \".5s\"/> " +  " 49 ," + "<break time = \".5s\"/> " \
                            +  " 48 ," + "<break time = \".5s\"/> " +  " 47 ," + "<break time = \".5s\"/> " \
                            +  " 46 ," + "<break time = \".5s\"/> " +  " 45 ," + "<break time = \".5s\"/> " \
                            +  " 44 ," + "<break time = \".5s\"/> " +  " 43 ," + "<break time = \".5s\"/> " \
                            +  " 42 ," + "<break time = \".5s\"/> " +  " 41 ," + "<break time = \".5s\"/> " \
                            +  " 40 ," + "<break time = \".5s\"/> " +  " 39 ," + "<break time = \".5s\"/> " \
                            +  " 38 ," + "<break time = \".5s\"/> " +  " 37 ," + "<break time = \".5s\"/> " \
                            +  " 36 ," + "<break time = \".5s\"/> " +  " 35 ," + "<break time = \".5s\"/> " \
                            +  " 34 ," + "<break time = \".5s\"/> " +  " 33 ," + "<break time = \".5s\"/> " \
                            +  " 32 ," + "<break time = \".5s\"/> " +  " 31 ," + "<break time = \".5s\"/> " \
                            +  " 30, " + "<break time = \".5s\"/> " +  "  29 ," + "<break time = \".5s\"/> " \
                            +  " 28 ," + "<break time = \".5s\"/> " +  "  27 ," + "<break time = \".5s\"/> " \
                            +  " 26 ," + "<break time = \".5s\"/> " +  "  25 ," + "<break time = \".5s\"/> " \
                            +  " 24 ," + "<break time = \".5s\"/> " +  "  23 ," + "<break time = \".5s\"/> " \
                            +  " 22 ," + "<break time = \".5s\"/> " +  " 21 ," + "<break time = \".5s\"/> " \
                            +  " 20 ," + "<break time = \".5s\"/> " +  " 19 ," + "<break time = \".5s\"/> " \
                            +  " 18 ," + "<break time = \".5s\"/> " +  " 17 ," + "<break time = \".5s\"/> " \
                            +  " 16 ," + "<break time = \".5s\"/> " +  " 15 ," + "<break time = \".5s\"/> " \
                            +  " 14 ," + "<break time = \".5s\"/> " +  " 13 ," + "<break time = \".5s\"/> " \
                            +  " 12 ," + "<break time = \".5s\"/> " +  " 11 ," + "<break time = \".5s\"/> " \
                            +  " 10 ," + "<break time = \".5s\"/> " +  " 9 ," + "<break time = \".5s\"/> " \
                            +  " 8 ," + "<break time = \".5s\"/> " +  " 7 ," + "<break time = \".5s\"/> " \
                            +  " 6, " + "<break time = \".5s\"/> " +  " 5 ," + "<break time = \".5s\"/> " \
                            +  " 4 ," + "<break time = \".5s\"/> " +  " 3 ," + "<break time = \".5s\"/> " \
                            +  " 2 ," + "<break time = \".5s\"/> " +  " 1 ," + "<break time = \".5s\"/> " +  " 0. "
            reprompt_text = "Thank you for using Rocket Launcher. See you soon!"
        else:
            speech_output = "Please make sure time should be in between from 100 to 0."
            reprompt_text = "Thank you for using Rocket Launcher! See you soon!"

        
        should_end_session = True
    else:
        return get_help_response()
        should_end_session = False
        
    return build_response(session_attributes, build_speechlet_response_with_card_only(
        card_title, card_text,  speech_output, reprompt_text, should_end_session))


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
        return get_count_table_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.FallbackIntent":
        return get_help_response()
    elif intent_name == "AMAZON.YesIntent":
        return get_repeat_response(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_session_end_request()    
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.StopIntent":
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
