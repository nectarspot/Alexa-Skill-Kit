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

QUIZ_LENGTH = 5
NORMAL_QUESTIONS = [
        {"3*1=?": ["3"]},
        {"2*3=?": ["6"]},
        {"2*7=?": ["14"]},
        {"2*9=?": ["18"]},
        {"2*5=?": ["10"]},
        {"3*3=?": ["9"]},
        {"3*4=?": ["12"]},
        {"3*6=?": ["18"]},
        {"3*7=?": ["21"]},
        {"3*9=?": ["27"]},
        {"4*2=?": ["8"]},
        {"4*4=?": ["16"]},
        {"4*6=?": ["24"]},
        {"4*8=?": ["32"]},
        {"4*10=?": ["40"]},
        {"4*0=?": ["0"]},
        {"5*3=?": ["15"]},
        {"5*2=?": ["10"]},
        {"5*5=?": ["25"]},
        {"5*4=?": ["20"]},
        {"5*7=?": ["35"]},
        {"5*9=?": ["45"]},
        {"6*1=?": ["6"]},
        {"6*2=?": ["12"]},
        {"6*4=?": ["24"]},
        {"6*5=?": ["30"]},
        {"6*6=?": ["36"]},
        {"6*8=?": ["48"]},
        {"6*9=?": ["54"]},
        {"7*2=?": ["14"]},
        {"7*3=?": ["21"]},
        {"7*4=?": ["28"]},
        {"7*6=?": ["42"]},
        {"7*7=?": ["49"]},
        {"7*9=?": ["63"]},
        {"8*0=?": ["0"]},
        {"8*2=?": ["16"]},
        {"8*3=?": ["24"]},
        {"8*5=?": ["40"]},
        {"8*6=?": ["48"]},
        {"8*7=?": ["56"]},
        {"8*8=?": ["64"]},
        {"9*1=?": ["9"]},
        {"9*2=?": ["18"]},
        {"9*4=?": ["36"]},
        {"9*6=?": ["54"]},
        {"9*7=?": ["63"]},
        {"9*8=?": ["72"]},
        {"9*9=?": ["81"]},
        {"10*1=?": ["10"]},
        {"10*6=?": ["60"]},
        {"10*7=?": ["70"]},
        {"7*5=?": ["35"]},
        {"8*4=?": ["32"]},
        {"7*8=?": ["56"]},
        {"7*9=?": ["63"]}        
]

HARD_QUESTIONS = [
    {"14*11=?": ["154"]}, 
    {"11*15=?": ["165"]},
    {"16*11=?": ["176"]},
    {"19*11=?": ["209"]},
    {"12*12=?": ["144"]},
    {"14*12=?": ["168"]},
    {"17*12=?": ["204"]},
    {"19*12=?": ["228"]},
    {"13*13=?": ["169"]},
    {"14*13=?": ["182"]},
    {"16*13=?": ["208"]},
    {"17*13=?": ["221"]},
    {"19*13=?": ["247"]},
    {"14*14=?": ["196"]},
    {"15*14=?": ["210"]},
    {"17*14=?": ["238"]},
    {"16*14=?": ["224"]},
    {"18*14=?": ["266"]},
    {"20*14=?": ["280"]},
    {"15*15=?": ["225"]},
    {"16*15=?": ["240"]},
    {"17*15=?": ["255"]},
    {"18*15=?": ["270"]},
    {"19*15=?": ["285"]},
    {"16*16=?": ["256"]},
    {"16*17=?": ["272"]},
    {"18*16=?": ["288"]},
    {"19*16=?": ["304"]},
    {"17*17=?": ["289"]},
    {"17*18=?": ["306"]},
    {"17*19=?": ["323"]},
    {"18*18=?": ["324"]},
    {"18*19=?": ["342"]},
    {"19*19=?": ["361"]},
    {"11*17=?": ["187"]},
    {"11*19=?": ["209"]},
    {"12*14=?": ["168"]},
    {"23*15=?": ["345"]},
    {"23*18=?": ["414"]},
    {"23*17=?": ["391"]},
    {"24*15=?": ["360"]},
    {"24*18=?": ["432"]},
    {"24*19=?": ["456"]},
    {"25*14=?": ["350"]},
    {"25*16=?": ["400"]},
    {"25*18=?": ["450"]}
]

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Advance Multiplication Spot Quiz"
    speech_output = "Welcome to Advance Multiplication Spot Quiz. Which level shall I open, for example, Normal or Hard."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Which level shall I open, for example, Normal or Hard."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_get_help_request(intent, session):
    card_title = "Advance Multiplication Spot Quiz Help"
    attributes = {}
    speech_output = "Which level shall I open, for example, Normal or Hard."
    reprompt_text = "Which level shall I open, for example, Normal or Hard."
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
        should_end_session = False
        return build_response( attributes,
            build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session) )

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Advance Multiplication Spot Quiz!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_re_enter(intent, session):
    card_title = "Re-enter to Quiz"
    attributes = {}
    speech_output = "Which level shall I open, for example, Normal or Hard."
                      
    reprompt_text = "Which level shall I open, for example, Normal or Hard."
    should_end_session = False
    return build_response(attributes,build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

        
#----------------------------------NORMAL LEVEL------------------------------------------------
    
def get_wait_normallevel(intent, session):
    card_title = "Waiting question"
    should_end_session= False
    normal_questions = populate_normal_questions()
    starting_index = 0
    spoken_normal_question = NORMAL_QUESTIONS[normal_questions[starting_index]].keys()[0]
    speech_output = spoken_normal_question 
    reprompt_text = spoken_normal_question + "<break time = \"5000ms\"/> " \
                    "Do you want to continue with the quiz?"
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": normal_questions,
                  "score": 0,
                  "correct_answers": NORMAL_QUESTIONS[normal_questions[starting_index]].values()[0]
                  }
    
    attributes ['wait_me'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
       

def get_normal_level(intent, session):
    card_title = "Normal Level"
    should_end_session= False
    normal_questions = populate_normal_questions()
    starting_index = 0
    spoken_normal_question = NORMAL_QUESTIONS[normal_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Normal Level. " + spoken_normal_question
    reprompt_text = spoken_normal_question + "<break time = \"5000ms\"/> " \
                    + spoken_normal_question + "<break time = \"5000ms\"/> " \
                    " Do you want more time?" 
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": normal_questions,
                  "score": 0,
                  "correct_answers": NORMAL_QUESTIONS[normal_questions[starting_index]].values()[0]
                  }
    attributes['user_prompted_to_continue'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_normal_questions():
    normal_questions = []
    index_list1 = []
    index1 = len(NORMAL_QUESTIONS)
    
    if QUIZ_LENGTH > index1:
        raise ValueError("Invalid Quiz Length")
        
    for a in range (0,index1):
        index_list1.append(a)
    for b in range (0, QUIZ_LENGTH):
        rand1 = int(math.floor(random.random()*index1))
        index1 -= 1
        temp1 = index_list1[index1]
        index_list1[index1] = index_list1[rand1]
        index_list1[rand1] = temp1
        normal_questions.append(index_list1[index1])
    return normal_questions

def get_normal_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    normal_answer = intent['slots'].get('NormalAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not normal_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        normal_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if normal_answer and normal_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech = '<say-as interpret-as="interjection">Bravo! </say-as>'
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = '<say-as interpret-as="interjection">Argh! </say-as>'
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == QUIZ_LENGTH - 1:
            
            if str(current_score) == "5":
                encouragement = '<say-as interpret-as="interjection">dynomite! </say-as>'
            elif str(current_score) == "4":
                encouragement = '<say-as interpret-as="interjection">hip hip hooray! </say-as>'
            elif str(current_score) == "3":
                encouragement = '<say-as interpret-as="interjection">well done! </say-as>'
            elif str(current_score) == "2":
                encouragement = '<say-as interpret-as="interjection">all righty!  </say-as>'
            elif str(current_score) == "1":
                encouragement = '<say-as interpret-as="interjection">okey! </say-as>'
            else:
                encouragement ='<say-as interpret-as="interjection">oh dear! </say-as>'
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Wrong , but don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "

            speech_output = "" if intent['name'] == "DontKnowIntent" else "This answer is "
            speech_output = (encouragement + speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, QUIZ_LENGTH) +last_encouragement +
                             " Do you want to continue the Quiz? ")
            reprompt_text =  "Do you want to continue the Quiz? "
            should_end_session = False
            card_title = "Final Score"
           
            return build_response( session['attributes'],build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )

            
        else:
            current_questions_index += 1
            spoken_normal_question = NORMAL_QUESTIONS[normal_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_normal_question +"<break time = \"5000ms\"/> " + spoken_normal_question

            speech_output = "" if user_gave_up == "DontKnowIntent" else "This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ". Your score is " +
                             str(current_score) + '. ' + spoken_normal_question )
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": normal_questions,
                          "score": current_score,
                          "correct_answers": NORMAL_QUESTIONS[normal_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            should_end_session = False
            
            return build_response( attributes,build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )


def is_normal_answer_slot_valid(intent):
    if 'NormalAnswer' in intent['slots'].keys() and 'value' in intent['slots']['NormalAnswer'].keys():
        return True
    else:
        return False

#----------------------------------HARD LEVEL---------------------------------------------------

def get_wait_hardlevel(intent, session):
    card_title = "wait"
    should_end_session= False
    hard_questions = populate_hard_questions()
    starting_index = 0
    spoken_hard_question = HARD_QUESTIONS[hard_questions[starting_index]].keys()[0]
    speech_output = spoken_hard_question
    reprompt_text = spoken_hard_question + "<break time = \"5000ms\"/> " \
                     "Do you want to continue with the quiz?"
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": hard_questions,
                  "score": 0,
                  "correct_answers": HARD_QUESTIONS[hard_questions[starting_index]].values()[0]
                  }
    attributes ['wait_hard'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        

def get_hard_level(intent, session):
    card_title = "Hard Level"
    should_end_session= False
    hard_questions = populate_hard_questions()
    starting_index = 0
    spoken_hard_question = HARD_QUESTIONS[hard_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to hard Level. " + spoken_hard_question
    reprompt_text = spoken_hard_question + "<break time = \"5000ms\"/> " \
                    + spoken_hard_question + "<break time = \"5000ms\"/> " \
                    " Do you want more time?"
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": hard_questions,
                  "score": 0,
                  "correct_answers": HARD_QUESTIONS[hard_questions[starting_index]].values()[0]
                  }
    attributes['user_prompted'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_hard_questions():
    hard_questions = []
    index_list2 = []
    index2 = len(HARD_QUESTIONS)
    
    if QUIZ_LENGTH > index2:
        raise ValueError("Invalid Quiz Length")
        
    for c in range (0,index2):
        index_list2.append(c)
    for d in range (0, QUIZ_LENGTH):
        rand2 = int(math.floor(random.random()*index2))
        index2 -= 1
        temp2 = index_list2[index2]
        index_list2[index2] = index_list2[rand2]
        index_list2[rand2] = temp2
        hard_questions.append(index_list2[index2])
    return hard_questions

def get_hard_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    hard_answer = intent['slots'].get('HardAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not hard_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        hard_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if hard_answer and hard_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct. "
            spoken_speech = '<say-as interpret-as="interjection">hurray! </say-as>'
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = '<say-as interpret-as="interjection">doh! </say-as>'
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == QUIZ_LENGTH - 1:
            
            if str(current_score) == "5":
                encouragement = '<say-as interpret-as="interjection">dynomite! </say-as>'
            elif str(current_score) == "4":
                encouragement = '<say-as interpret-as="interjection">hip hip hooray! </say-as>'
            elif str(current_score) == "3":
                encouragement = '<say-as interpret-as="interjection">well done! </say-as>'
            elif str(current_score) == "2":
                encouragement = '<say-as interpret-as="interjection">all righty!  </say-as>'
            elif str(current_score) == "1":
                encouragement = '<say-as interpret-as="interjection">okey! </say-as>'
            else:
                encouragement ='<say-as interpret-as="interjection">oh dear! </say-as>'
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Wrong , but don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "
                
            speech_output = "" if intent['name'] == "DontKnowIntent" else "This answer is "
            speech_output = (encouragement + speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, QUIZ_LENGTH) +last_encouragement +
                             " Do you want to continue the Quiz? ")
            reprompt_text =  "Do you want to continue the Quiz? "
            should_end_session = False
            card_title = "Final Score"
            """return build_response(session['attributes'], build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))"""
            return build_response( session['attributes'],build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )

        else:
            current_questions_index += 1
            spoken_hard_question = HARD_QUESTIONS[hard_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_hard_question + "<break time = \"5000ms\"/> " + spoken_hard_question

            speech_output = "" if user_gave_up == "DontKnowIntent" else "This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ". Your score is " +
                             str(current_score) + '. ' + spoken_hard_question )
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": hard_questions,
                          "score": current_score,
                          "correct_answers": HARD_QUESTIONS[hard_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            should_end_session = False
            """return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))"""
            return build_response( attributes,build_speechlet_response_without_card
                        (speech_output, reprompt_text, should_end_session) )


def is_hard_answer_slot_valid(intent):
    if 'HardAnswer' in intent['slots'].keys() and 'value' in intent['slots']['HardAnswer'].keys():
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
    if intent_name == "NormalLevelIntent":
        return get_normal_level(intent, session)
    elif intent_name == "NormalAnswerIntent":
        return get_normal_level_answer(intent,session)
    elif intent_name == "NormalAnswerOnlyIntent":
        return get_normal_level_answer(intent,session)
    
    elif intent_name == "HardLevelIntent":
        return get_hard_level(intent, session)
    elif intent_name == "HardAnswerIntent":
        return get_hard_level_answer(intent,session)
    elif intent_name == "HardAnswerOnlyIntent":
        return get_hard_level_answer(intent,session)
        
    elif intent_name == "AMAZON.YesIntent":
        if session.get('attributes', {}).get('user_prompted_to_continue'):
            return get_wait_normallevel(intent, session)
        elif session.get('attributes', {}).get('wait_me'):
            return get_re_enter(intent, session)
        elif session.get('attributes', {}).get('user_prompted'):
            return get_wait_hardlevel(intent, session)
        elif session.get('attributes', {}).get('wait_hard'):
            return get_re_enter(intent, session)
        return get_re_enter(intent, session)
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