from __future__ import print_function
import math
import random
import string
import operator

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

        'shouldEndSession': should_end_session
    }
    
def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
            
    }
# ------- Skill specific  logic ------------------------------

GAME_LENGTH = 5

QUESTIONS=[
        {"10 divided by 5=?" : ["2"]},
        {"20 divided by 4=?" : ["5"]},
        {"20 divided by 5=?" : ["4"]},
        {"18 divided by 2=?" : ["9"]},
        {"18 divided by 6=?" : ["3"]},
        {"18 divided by 6=?": ["3"]},
        {"16 divided by8=?": ["2"]},
        {"16 divided by 8=?": ["4"]},
        {"15 divided by 3=?": ["5"]},
        {"14 divided by 7=?": ["2"]},
        {"14 divided by 14=?": ["1"]},
        {"12 divided by 6=?": ["2"]},
        {"12 divided by4=?": ["3"]},
        {"15 divided by 5=?": ["3"]},
        {"10 divided by 5=?": ["2"]},
        {"9 divided by 3=?": ["3"]},
        {"6 divided by 2=?": ["3"]},
        {"4 divided by2=?": ["2"]},
        {"2 divided by 2=?": ["1"]},
        {"21 divided by 7=?": ["3"]},
        {"22 divided by11=?": ["2"]},
        {"24 divided by 2=?": ["12"]},
        {"24 divided by 3=?": ["8"]},
        {"24 divided by 6=?": ["4"]},
        {"24 divided by 1=?": ["24"]},
        {"25 divided by5=?": ["5"]},
        {"26 divided by 2=?": ["13"]},
        {"27 divided by 3=?": ["9"]},
        {"27 divided by 9=?": ["3"]},
        {"28 divided by 14=?": ["2"]},
        {"28 divided by 4=?": ["7"]},
        {"28 divided by 2=?": ["14"]},
        {"30 divided by 3=?": ["10"]},
        {"30 divided by 5=?": ["6"]},
        {"30 divided by 1=?": ["30"]},
        {"32 divided by 2=?": ["16"]},
        {"32 divided by 4=?": ["8"]},
        {"32 divided by 8=?": ["4"]},
        {"33 divided by 3=?": ["11"]},
        {"34 divided by 17=?": ["2"]},
        {"35 divided by 7=?": ["5"]},
        {"36 divided by 4=?": ["9"]},
        {"36 divided by 6=?": ["6"]},
        {"38 divided by 2=?": ["19"]},
        {"39 divided by 3=?": ["13"]},
        {"40 divided by 2=?": ["20"]},
        {"40 divided by 4=?": ["10"]},
        {"40 divided by 5=?": ["8"]},
        {"42 divided by 2=?": ["21"]},
        {"42 divided by 14=?": ["3"]},
        {"42 divided by 6=?": ["7"]},
        {"44 divided by 4=?": ["11"]},
        {"44 divided by 22=?": ["2"]},
        {"45 divided by 5=?": ["9"]},
        {"45 divided by 9=?": ["5"]},
        {"46 divided by 2=?": ["23"]},
        {"47 divided by 47=?": ["1"]},
        {"48 divided by 4=?": ["12"]},
        {"48 divided by 6=?": ["8"]},
        {"48 divided by 8=?": ["6"]},
        {"48 divided by 2=?": ["24"]},
        {"49 divided by 7=?": ["7"]}

        
]

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Division Spot Quiz"
    speech_output = "Welcome to Division Spot Quiz. 'Are you ready to play the quiz'?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Are you ready to play the Quiz?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_get_help_request(intent, session):
    card_title = "Division Spot Quiz Help"
    attributes = {}
    speech_output = "For begin the quiz say 'begin quiz' "
    reprompt_text = "For begin the quiz say 'begin quiz' "
    should_end_session = False
    return build_response(attributes,build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def handle_repeat_request(intent, session):
    """
    Repeat the previous speech_output and reprompt_text from the session['attributes'].
    If available, else start a new game session.
    """
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return handle_get_help_request(intent, session)
    else:
        attributes = session['attributes']
        speech_output = attributes['speech_output']
        reprompt_text = attributes['reprompt_text']
        card_title = "Repeat Session"
        should_end_session = False
        return build_response( attributes,
            build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session) )

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Division Spot Quiz!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_quizlevel(intent, session):
    should_end_session = False
    card_title = "My Quiz"
    game_questions = populate_game_questions()
    starting_index = 0

    spoken_question = QUESTIONS[game_questions[starting_index]].keys()[0]
    
    speech_output = "Ok! let's go to Division Spot Quiz, " + spoken_question 
    reprompt_text = spoken_question + "<break time = \"5000ms\"/> "  \
                    " If you want to continue this then reply the answer or you can repeat it by saying 'repeat' or you can stop?" 
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": game_questions,
                  "score": 0,
                  "correct_answers": QUESTIONS[game_questions[starting_index]].values()[0]
                  }
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        

def populate_game_questions():
    game_questions = []
    index_list = []
    index = len(QUESTIONS)

    if GAME_LENGTH > index:
        raise ValueError("Invalid Game Length")

    for i in range(0, index):
        index_list.append(i)

    # Pick GAME_LENGTH random questions from the list to ask the user,
    # make sure there are no repeats
    for j in range(0, GAME_LENGTH):
        rand = int(math.floor(random.random() * index))
        index -= 1

        temp = index_list[index]
        index_list[index] = index_list[rand]
        index_list[rand] = temp
        game_questions.append(index_list[index])

    return game_questions

def handle_answer_request(intent, session):
    attributes = {}
    should_end_session = False
    answer = intent['slots'].get('Answer', {}).get('value')
    user_gave_up = intent['name']

    if  not answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
    else:
        game_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if answer and answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct. "
            #spoken_speech = '<say-as interpret-as="interjection">Bravo! </say-as>'
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            #spoken_speech = '<say-as interpret-as="interjection">Argh! </say-as>'

        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == GAME_LENGTH - 1:
            speech_output = "" if intent['name'] == "DontKnowIntent" else "This answer is "
            speech_output = ( speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, GAME_LENGTH) + 
                             " Do you want to continue? ")
            reprompt_text =  "Do you want to continue? "
            should_end_session = False
            card_title = "Final Score"
            return build_response(session['attributes'], build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
            """return build_response( session['attributes'],build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )"""

        else:
            current_questions_index += 1
            spoken_question = QUESTIONS[game_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_question

            speech_output = "" if user_gave_up == "DontKnowIntent" else "This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". Your score is " +
                             str(current_score) + '. ' + reprompt_text)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": game_questions,
                          "score": current_score,
                          "correct_answers": QUESTIONS[game_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
            """return build_response( attributes,build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )"""

def is_answer_slot_valid(intent):
    if 'Answer' in intent['slots'].keys() and 'value' in intent['slots']['Answer'].keys():
        return True
    else:
        return False

    
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
    
    if intent_name == "MyQuizIntent":
        return get_quizlevel(intent, session)
    elif intent_name == "AnswerIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AnswerOnlyIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return get_quizlevel(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_session_end_request()

    elif intent_name == "AMAZON.RepeatIntent":
        return handle_repeat_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_get_help_request(intent, session)
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
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
