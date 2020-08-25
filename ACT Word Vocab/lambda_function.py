from __future__ import print_function
import math
import random
import string

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
    
def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml':  "<speak>" + output + "</speak>"
        },

        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml':  "<speak>" + reprompt_text + "</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_without_reprompt(title, output,should_end_session):
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
    attributes = {}
    #card_title = "Welcome to First 100 High Frequency Words"
    speech_output = "Welcome to ACT Word Vocabulary."\
                    + "<break time = \"300ms\"/>"\
                    + " Are you ready to learn new word for the Day?"
                  
            
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    attributes['my_welcome']= True
    welcome_speech ="Are you ready to learn new word for the Day?"
                   
    reprompt_text = welcome_speech + "<break time = \"5000ms\"/> " \
                    + welcome_speech

    should_end_session = False
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )
 

def handle_session_end_request():
    card_title = "Thank You!"
    speech_output = "Thank you for using ACT Word Vocabulary."\
                    " See you soon!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response_without_reprompt(
        card_title, speech_output, should_end_session))

def handle_help_session():
    #card_title = "Help Session"
    attributes = {}
    speech_output = " To learn word for the day. "\
                    + "<break time = \"300ms\"/>"\
                    + " You can say , for example"\
                    + "<break time = \"300ms\"/>"\
                    + " begin word."
                    
    reprompt_text = " To learn word for the day. "\
                    + "<break time = \"300ms\"/>"\
                    + " You can say , for example"\
                    + "<break time = \"300ms\"/>"\
                    + " begin word."
                    
    attributes ['my_mine'] = True
    should_end_session = False
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )

#-----------------Error Session-------------------------
def handle_error_session():
    #card_title = "Please Specify"
    attributes = {}
    speech_output = "Please give an appropriate answer related with the session."\
                    + "<break time = \"500ms\"/> " \
                    +" Do you want to continue with the skill? "
                    
    reprompt_text = "Do you want to continue with skill?"
    attributes['my_error'] = True
    should_end_session = False
    return build_response(attributes,build_speechlet_response_without_card(
        speech_output, reprompt_text, should_end_session))
#---------------------------------------------------------------------------
def handle_spell_session(intent, session):
    #card_title = ""
    should_end_session = False
    attributes = {}
    speech_output = "Let's go to today's word for the day"\
                    + "<break time = \"400ms\"/> "\
                    + " SCRUPULOUS"\
                    + "<break time = \"800ms\"/> "\
                    + " SCRUPULOUS is spelled as "\
                    + "<break time = \"350ms\"/> "\
                    '<emphasis level="moderate"><say-as interpret-as="spell-out">SCRUPULOUS</say-as></emphasis>'\
                    + "<break time = \"800ms\"/> "\
                    + " SCRUPULOUS means"\
                    + "<break time = \"350ms\"/> "\
                    + " careful of small details. "\
                    + "<break time = \"800ms\"/> "\
                    + " Usage in sentence "\
                    + "<break time = \"400ms\"/> "\
                    + " If you want to keep your job, you need to be scrupulous about completing your work in the proper fashion."\
                    + "<break time = \"800ms\"/> "\
                    + " Do you want to take a test for better understanding of the word? "
                    
    reprompt_text = "Do you want to take a test for better understanding of the word?"\
                    + "<break time = \"500ms\"/> "\
                    + " Do you want to take a test for better understanding of the word?"
    attributes['my_spell_first']=True                   
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )

def handle_spell_word(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = " SCRUPULOUS is spelled as "\
                    + "<break time = \"300ms\"/> "\
                    + '<emphasis level="moderate"><say-as interpret-as="spell-out">SCROUPULOUS</say-as></emphasis>'\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
                    
    reprompt_text = " SCRUPULOUS is spelled as "\
                    + "<break time = \"300ms\"/> "\
                    + '<emphasis level="strong"><say-as interpret-as="spell-out">SCROUPULOUS</say-as></emphasis>'\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? " 
    attributes['spell_word'] = True                                
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )
                
def handle_spell_correctly(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">ding dong! </say-as>'\
                    " That's incorrect. "\
                    + "<break time = \"350ms\"/> "\
                    + " SCRUPULOUS spelled as  "\
                    + "<break time = \"250ms\"/> "\
                    + '<emphasis level="moderate"><say-as interpret-as="spell-out">SCRUPULOUS</say-as></emphasis>'\
                    + "<break time = \"500ms\"/> "\
                    + " Let's go for next test "\
                    + "<break time = \"300ms\"/> "\
                    + " SCRUPULOUS means someone who is aware of the right thing to do."\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
                    
    reprompt_text = " SCRUPULOUS means someone who is aware of the right thing to do. "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
    attributes['spell_yes_user']= True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) ) 
                
def handle_spell_wrong(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">bingo! </say-as>'\
                    " That's correct. "\
                    + "<break time = \"300ms\"/> "\
                    + " SCRUPULOUS spelled as "\
                    + "<break time = \"200ms\"/> "\
                    '<emphasis level="moderate"><say-as interpret-as="spell-out">SCRUPULOUS</say-as></emphasis>'\
                    + "<break time = \"500ms\"/> "\
                    + " Abstinence means someone who is aware of the right thing to do. "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
                    
    reprompt_text = "Abstinence means someone who is aware of the right thing to do. "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
    attributes['spell_no_by_user']= True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )   
                
def handle_meaning_correctly(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">bravo!</say-as>'\
                    " That's correct. "\
                    + "<break time = \"500ms\"/> "\
                    + " Let's go for next test. "\
                    + "<break time = \"300ms\"/> "\
                    + " Because Shannon is a scrupulous editor, she never misses errors when she proofreads a document."\
                    +"<break time = \"300ms\"/> "\
                    + " Is it a correct usage? "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
                    
    reprompt_text = " Because Shannon is a scrupulous editor, she never misses errors when she proofreads a document."\
                    + "<break time = \"300ms\"/> "\
                    + "Is it a correct usage?"\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
    attributes['mean_yes_user']= True                
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )   
                
def handle_meaning_wrong(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">argh!</say-as>'\
                    " That's incorrect. "\
                    + "<break time = \"500ms\"/> "\
                    + " Let's go for next test. "\
                    + "<break time = \"300ms\"/> "\
                    + " Because Shannon is a scrupulous editor, she never misses errors when she proofreads a document."\
                    +"<break time = \"300ms\"/> "\
                    + " Is it a correct usage? "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
                    
    reprompt_text = + " Because Shannon is a scrupulous editor, she never misses errors when she proofreads a document."\
                    +"<break time = \"300ms\"/> "\
                    + " Is it a correct usage? "\
                    + "<break time = \"200ms\"/> "\
                    + " Yes or No ? "
    attributes['mean_no'] = True                
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )                   
                
def handle_usage_correctly(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">wahoo! </say-as>'\
                    " That's correct. "\
                    + "<break time = \"300ms\"/> "\
                    + " You have completed todays word of the day."\
                    + "<break time = \"200ms\"/> "\
                    + " Come tomorrow for new word. "\
                    + "<break time = \"300ms\"/> "\
                    + " would you like to continue with the skill again ? "
                    
    reprompt_text = " would you like to continue with the skill again ? "
    attributes['usage_yes_user']= True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )  
                
def handle_usage_wrong(intent, session):
    attributes = {}
    should_end_session = False
    speech_output = '<say-as interpret-as="interjection">uh ho! </say-as>'\
                    " That's incorrect. "\
                    + "<break time = \"300ms\"/> "\
                    + " You have completed todays word of the day."\
                    + "<break time = \"200ms\"/> "\
                    + " Come tomorrow for new word. "\
                    + "<break time = \"300ms\"/> "\
                    + " would you like to continue with the skill again ? "
                    
    reprompt_text = " would you like to continue with the skill again ? "
    attributes['usage_no']= True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) ) 
                
# --------------- Events ----------------------------------------------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):

    #Called when the user launches the skill without specifying what they want

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
    
    if intent_name == "MyErrorIntent":
        if session.get('attributes', {}).get('my_welcome'):
            return handle_help_session()
        elif session.get('attributes', {}).get('my_error'):
            return  handle_help_session()
        elif session.get('attributes', {}).get('spell_word'):
            return  handle_spell_correctly(intent, session)
        elif session.get('attributes', {}).get('spell_yes_user'):
            return handle_meaning_wrong(intent, session)
        elif session.get('attributes', {}).get('spell_no_by_user'):
            return handle_meaning_wrong(intent, session)
        elif session.get('attributes', {}).get('mean_yes_user'):
            return handle_usage_wrong(intent, session)
        elif session.get('attributes', {}).get('mean_no'):
            return handle_usage_wrong(intent, session)
        else:
            return handle_error_session()
        return handle_error_session()
            
    elif intent_name == "AMAZON.YesIntent":
        if session.get('attributes', {}).get('my_welcome'):
            return handle_spell_session(intent, session)
        elif session.get('attributes', {}).get('my_spell_first'):
            return handle_spell_word(intent, session)
        elif session.get('attributes', {}).get('spell_word'):
            return handle_spell_correctly(intent, session)
        elif session.get('attributes', {}).get('spell_yes_user'):
            return handle_meaning_correctly(intent, session)
        elif session.get('attributes', {}).get('spell_no_by_user'):
            return handle_meaning_correctly(intent, session)
        elif session.get('attributes', {}).get('mean_yes_user'):
            return handle_usage_correctly(intent, session)
        elif session.get('attributes', {}).get('mean_no'):
            return handle_usage_correctly(intent, session)
        elif session.get('attributes', {}).get('usage_yes_user'):
            return handle_spell_session(intent, session)
        elif session.get('attributes', {}).get('usage_no'):
            return handle_spell_session(intent, session)
        elif session.get('attributes', {}).get('my_error'):
            return handle_spell_session(intent, session)
        elif session.get('attributes', {}).get('my_mine'):
            return handle_spell_session(intent, session)
        else:
            return handle_error_session()
        return handle_error_session()
    
    elif intent_name == "AMAZON.NoIntent":
        if session.get('attributes', {}).get('my_welcome'):
            return handle_help_session()
        elif session.get('attributes', {}).get('spell_word'):
            return handle_spell_wrong(intent, session)
        elif session.get('attributes', {}).get('spell_yes_user'):
            return handle_meaning_wrong(intent, session)
        elif session.get('attributes', {}).get('spell_no_by_user'):
            return handle_meaning_wrong(intent, session)
        elif session.get('attributes', {}).get('mean_yes_user'):
            return handle_usage_wrong(intent, session)
        elif session.get('attributes', {}).get('mean_no'):
            return handle_usage_wrong(intent, session)
        #elif session.get('attributes', {}).get(''):
        else:
            return handle_session_end_request()
        return handle_session_end_request()
        
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_session()
    elif intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.CancelIntent":
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
    try:
        
        print("event.session.application.applicationId=" +
              event['session']['application']['applicationId'])
    
        """
        Uncomment this if statement and populate with your skill's application ID to
        prevent someone else from configuring a skill that sends requests to this
        function.
        """
        #if (event['session']['application']['applicationId'] !=
        #        "amzn1.echo-sdk-ams.app.[unique-value-here]"):
        #    raise ValueError("Invalid Application ID")
    
        
        if event['session']['new']:
            on_session_started({'requestId': event['request']['requestId']},
                               event['session'])
    
        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])
    
    except Exception, e:
        raise e
    return handle_error_session

