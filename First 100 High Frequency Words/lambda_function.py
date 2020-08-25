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
    speech_output = "Welcome to First 100 High Frequency Words."\
                    " Which High Frequency Word List you want to listen from first to"\
                    " fifth word list,"\
                    + "<break time = \"300ms\"/> " \
                    + " For example you can say, 'first word list'."
            
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    
    reprompt_text = " Which High Frequency Word List you want to listen from first to"\
                    " fifth word list, For example you can say,"\
                    '<say-as interpret-as="interjection"> first word list.</say-as>'

    should_end_session = False
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )
 

def handle_session_end_request():
    card_title = "Thank You!"
    speech_output = "Thank you for using First 100 High Frequency Words."\
                    " See you soon!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response_without_reprompt(
        card_title, speech_output, should_end_session))

def handle_help_session():
    card_title = "Help Session"
    attributes = {}
    speech_output = "Which High Frequency Word list you want to listen from"\
                    " first to fifth word list, for example you can say, first word list."
    reprompt_text = "Which High Frequency Word list you want to listen from"\
                    " first to fifth word list, for example you can say, first word list."
    attributes ['my_mine'] = True
    should_end_session = False
    card_title = "Help Session"
    return build_response(attributes,build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def handle_error_session():
    #card_title = "Please Specify"
    attributes = {}
    speech_output = "Please give a exact word list number from"\
                    " first to fifth"\
                    + "<break time = \"300ms\"/> " \
                    +" for example you can say, first word list."
                    
    reprompt_text = "Do you want to listen a set of High Frequency Word List?"
    attributes['my_error'] = True
    should_end_session = False
    return build_response(attributes,build_speechlet_response_without_card(
        speech_output, reprompt_text, should_end_session))
        

def handle_reenter_response(intent, session):
    attributes = {}
    speech_output = " Which High Frequency Word List you want to listen from first to"\
                    " fifth word list, For example you can say,"\
                    '<say-as interpret-as="interjection"> first word list.</say-as>'

    reprompt_text =" Which High Frequency Word List you want to listen from first to"\
                    " fifth word list, For example you can say,"\
                    '<say-as interpret-as="interjection"> first word list.</say-as>'

    should_end_session = False
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )


"""def handle_repeat_request(intent, session):
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return get_welcome_response()
    else:
        attributes = session['attributes']
        speech_output = attributes['speech_output']
        reprompt_text = attributes['reprompt_text']
        should_end_session = False
        return build_response(attributes,build_speechlet_response_without_card(
            speech_output, reprompt_text, should_end_session))
    """          
   
#-----------------------------1- Word set------------------------------------------------

def handle_word_first_set(intent, session):
    attributes = {}
    should_end_session = False
    
    first_spoken_speech = " ".join([FIRST_WORD[random.randrange(0, len(FIRST_WORD))] for i in range(5)])
    speech_output = "Let's hear 1st set of High Frequency Word list." \
                    " The words are - " + "<break time = \"700ms\"/> " \
                    + first_spoken_speech + "<break time = \"500ms\"/> " \
                    + ". Do you want to hear next set of High Frequency Word List? "
    reprompt_text = first_spoken_speech + "<break time = \"400ms\"/> " \
                    " Do you want to hear next set of High Frequency word List? "
    
    attributes['my_first'] = True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )


def handle_word_second_set(intent, session):
    attributes = {}
    should_end_session = False
    
    second_spoken_speech = " ".join([SECOND_WORD[random.randrange(0, len(SECOND_WORD))] for j in range(5)])
    speech_output = "Let's hear 2nd set of High Frequency Word list." \
                    " The words are - " + "<break time = \"700ms\"/> " \
                    + second_spoken_speech + "<break time = \"500ms\"/> " \
                    + ". Do you want to hear next set of High Frequency Word List? "
    reprompt_text = second_spoken_speech + "<break time = \"400ms\"/> " \
                    " Do you want to hear next set of High Frequency Word List? "
    attributes['my_second'] = True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )


def handle_word_third_set(intent, session):
    attributes = {}
    should_end_session = False
    
    third_spoken_speech = " ".join([THIRD_WORD[random.randrange(0, len(THIRD_WORD))] for k in range(5)])
    speech_output = "Let's hear 3rd set of High Frequency Word list." \
                    " The words are - " + "<break time = \"700ms\"/> " \
                    + third_spoken_speech + "<break time = \"500ms\"/> " \
                    + ". Do you want to hear next set of High Frequency Word List? "
    reprompt_text = third_spoken_speech + "<break time = \"400ms\"/> " \
                    " Do you want to hear next set of High Frequency Word List? "
    attributes['my_third'] = True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )


def handle_word_set4(intent, session):
    attributes = {}
    should_end_session = False
    
    fourth_spoken_speech = " ".join([WORD4[random.randrange(0, len(WORD4))] for l in range(5)])
    speech_output = "Let's hear 4th set of High Frequency Word list." \
                    " The words are - " + "<break time = \"700ms\"/> " \
                    + fourth_spoken_speech + "<break time = \"500ms\"/> " \
                    + ". Do you want to hear next set of High Frequency Word list? "
    reprompt_text = fourth_spoken_speech + "<break time = \"400ms\"/> " \
                    " Do you want to hear next set of High Frequency Word list? "
    attributes['my_fourth'] = True
    return build_response( attributes, build_speechlet_response_without_card(
                speech_output, reprompt_text, should_end_session) )
                

def handle_word_set5(intent, session):
    attributes = {}
    should_end_session = False
    
    fifth_spoken_speech = " ".join([WORD4[random.randrange(0, len(WORD4))] for l in range(5)])
    word_day = " ".join([WORD_Day[random.randrange(0, len(WORD_Day))] for p in range(1)])

    speech_output = "Let's hear 5th set of High Frequency Word list." \
                    " The words are - " + "<break time = \"700ms\"/> "\
                    + fifth_spoken_speech + "<break time = \"500ms\"/> "\
                    "Do you want to again hear set of High Frequency Word list?"
    
    reprompt_text ="Do you want to again hear set of High Frequency Word list? "
    attributes['my_fifth']= True
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
    
    if intent_name == "MyFirstWordIntent" :   
        return handle_word_first_set(intent, session)
    elif intent_name == "MySecondWordIntent":
        return handle_word_second_set(intent, session)
    elif intent_name == "MyThirdWordIntent":
        return handle_word_third_set(intent, session)
    elif intent_name == "MyFourthWordIntent":
        return handle_word_set4(intent, session)
    elif intent_name == "MyFifthWordIntent":
        return handle_word_set5(intent, session)
    
    elif intent_name == "MyReenterIntent":
        return handle_reenter_response(intent, session)   
    
    elif intent_name == "MyErrorIntent":
        return handle_error_session()
    
    elif intent_name == "AMAZON.YesIntent":
        if session.get('attributes', {}).get('my_first'):
            return handle_word_second_set(intent,session)
        elif session.get('attributes', {}).get('my_second'):
            return handle_word_third_set(intent,session)
        elif session.get('attributes', {}).get('my_third'):
            return handle_word_set4(intent, session)
        elif session.get('attributes', {}).get('my_fourth'):
            return handle_word_set5(intent, session)
        elif session.get('attributes', {}).get('my_fifth'):
            return handle_reenter_response(intent, session)
            
        elif session.get('attributes', {}).get('my_error'):
            return handle_reenter_response(intent, session)
        else:
            handle_error_session()
        return handle_error_session()
    
    elif intent_name == "AMAZON.NoIntent":
        return handle_session_end_request()
    elif intent_name == "AMAZON.RepeatIntent":
        return handle_repeat_request(intent, session)
    
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
#-----------------------------Word list-------------------------------------
#---------set 1(words)-------------------
FIRST_WORD =[
    "A"  +  "<break t`ime = \"100ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">A</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Am" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Am</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "An" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">An</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "And" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">And</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "At" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">At</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Can" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Can</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Do" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Do</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Go" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Go</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "He" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">He</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "I" + "<break time = \"100ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">I</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "In" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">In</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Is" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Is</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "It" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">It</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Like" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Like</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Me" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Me</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "My" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">My</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "No" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">No</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "On" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">On</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "See" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">See</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "The" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">The</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "To" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">To</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Up" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Up</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "We" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">We</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "You" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">You</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "All" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">All</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Be" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Be</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Big" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Big</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Has" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Has</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "How"+ "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">How</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Who" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Who</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "What" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">What</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Have" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Have</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "When" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">When</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "This" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">This</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Our" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Our</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mine" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Mine</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "That" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">That</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "She" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">She</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Him" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Him</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
   ]

   
 #---------set 2(words)-------------------

SECOND_WORD =[
    "If" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">If</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",    
    
    "For"+ "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">For</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Like" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Like</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Me" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Me</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "My" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">My</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Not" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Not</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "As" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">As</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",

    "Back" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Back</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "By" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">By</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Come" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Come</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Came" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Came</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Did" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Did</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Get" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Get</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Had" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Had</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Have" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Have</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Her" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">Her</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "His" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">His</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Look" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Look</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Make" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Make</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Now" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Now</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Of" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Of</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Off" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Off</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "One" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">One</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Or" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Or</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Out" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Out</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Was" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Was</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Are" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Are</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "But" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">But</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "From" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">From</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Here" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Here</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Into" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Into</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Little" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Little</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Man" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Man</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Put" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Put</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Cut" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Cut</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Cat" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Cat</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Hat" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Hat</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Hot" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Hot</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Saw" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Saw</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Us" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Us</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    ]
     
#---------set 3(words)-------------------

THIRD_WORD =[
    "Away" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Away</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Been" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Been</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Play" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Play</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Very" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Very</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Your" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Your</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "After" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">After</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mother"+ "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mother</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Father" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Father</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Brother" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Brother</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Sister" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Sister</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Over" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Over</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Then" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Then</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "There" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">There</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
     
    "They" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">They</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "This" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">This</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Too" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Too</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "That" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">That</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Said" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Said</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Two" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Two</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Went" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Went</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Were" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Were</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "When" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">When</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Will" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Will</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "With" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">With</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Add" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Add</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Air" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Air</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Baby" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Baby</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Dry" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Dry</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Shy" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Shy</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Feel" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Feel</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Was" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Was</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "See" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">See</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Big" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Big</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Small" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Small</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "These" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">These</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Those" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Those</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Our" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Our</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Not" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Not</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Real" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Real</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Full" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Full</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Fool" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Fool</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    ]
    
    
    #---------set 4(words)-------------------

WORD4 =[
    "Full" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Full</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Uncle" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Uncle</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Miss" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Miss</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mind" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mind</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Nice" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Nice</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Old" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Old</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "New" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">New</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Of" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Of</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "It" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">It</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Can" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Can</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "There" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">There</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Out" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Out</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Went" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Went</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Some" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Some</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Little" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Little</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "As" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">As</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "No" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">No</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mum" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mum</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Them" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Them</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Do" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Do</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Down" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Down</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Dad" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Dad</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "See" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">See</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Look" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Look</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Very" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Very</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Come" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Come</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Will" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Will</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Into" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Into</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Back" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Back</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "From" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">From</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Children" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Children</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Him" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Him</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mr" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mr</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mrs" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mrs</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Get" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Get</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Just" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Just</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Now" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Now</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Came"+ "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Came</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Child" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Child</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Baby" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Baby</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Other" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Other</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    ]
   
   #---------set 5(words)-------------------

WORD5 =[
    "Me" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Me</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Because" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Because</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Before" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Before</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Cloud" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Cloud</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Going" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Going</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Just" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Just</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Where" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Where</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Oh" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Oh</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "About" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">About</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Got" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Got</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Their" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Their</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "People" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">People</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Your" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Your</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Put" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Put</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Can" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Can</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Could" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Could</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "House" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">House</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Old" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Old</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Too" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Too</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "By" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">By</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Day" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Day</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Made" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Made</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Time" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Time</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Am" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Am</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "If" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">If</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Help" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Help</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Mrs" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Mrs</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Called" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Called</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Here" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Here</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Off" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Off</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Asked" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Asked</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Saw" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Saw</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Make" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Make</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "An" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">An</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "From" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">From</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Way" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Way</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Could" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Could</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "May" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">May</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Made" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Made</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "Part" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Part</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    "About" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">About</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    ]
   
#-------------------------WORD OF THE DAY------------------------
WORD_Day = [
    "A"  +  "<break t`ime = \"100ms\"/> "\
    " is spelled as "\
    '<emphasis level="moderate"><say-as interpret-as="spell-out">A</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",  
    
    "Part" + "<break time = \"200ms\"/> "\
    " is spelled as "\
    '<emphasis level="strong"><say-as interpret-as="spell-out">Part</say-as></emphasis>'\
    + "<break time = \"500ms\"/> ",
    
    ]
