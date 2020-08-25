from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type' : 'Standard',
            'title':  title,
            'text' : output
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
    speech_output = "Welcome to Skip Counting. " \
                    "Let me know for Which number shall I start skip counting ?  "
    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please Let me know for Which number shall I start skip counting ?For example you can say 3 "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_count_table_response(intent_request):
    session_attributes = {}
    card_title = "Skip Counting"
    speech_output = " "
    table = intent_request["intent"]["slots"]["Table"]["value"]

    if table == "1":
        speech_output = "Starting Skip count for 1 :  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "2":
        speech_output = "Starting Skip count for 2 :  2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "3":
        speech_output = "Starting Skip count for 3 :  3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "4":
        speech_output = "Starting Skip count for 4 :  4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "5":
        speech_output = "Starting Skip count for 5 :  5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90 ,95 ,100. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "6":
        speech_output = "Starting Skip count for 6 :  6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "7":
        speech_output = "Starting Skip count for 7 :  7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98. Please tell me for Which number shall I repeat skip counting ?"
    elif table == "8":
        speech_output = "Starting Skip count for 8 :  8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Please tell me for Which number shall I repeat skip counting ?"
    elif table == "9":
        speech_output = "Starting Skip count for 9 :  9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99. Please tell me for Which number shall I repeat skip counting ? "
    elif table == "10":
        speech_output = "Starting Skip count for 10 : 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Please tell me for Which number shall I repeat skip counting ? "
    else:
        speech_output = "Please tell me for which number shall I start skip counting from 1 to 10 ? for example you can say 5"
    should_end_session = False
    reprompt_text = speech_output
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))
  
  
def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = "Please tell me for which number shall I start skip counting from 1 to 10 ? for example you can say 5"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

  
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Skip Counting."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
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
    
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()    
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    
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
