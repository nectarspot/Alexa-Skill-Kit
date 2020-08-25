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
    
def build_speechlet_response_without_reprompt(title, output, reprompt_text, should_end_session):
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
    
    session_attributes = {}
    card_title = "Subtraction Spot Quiz for Fourth Graders"
            
    speech_output = "Welcome to Subtraction Spot Quiz for Fourth Graders. Which level shall i open, for example, level 1 or 2 ?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Which level shall i open, for example, level 1 to 5 ?"
    should_end_session = False
    return build_response(session_attributes,build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Subtraction Spot Quiz for Fourth Graders!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response_without_reprompt({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def handle_help_session():
    card_title = "Help Session"
    attributes = {}
    speech_output = "To start the quiz, you can say 'Start'."
    reprompt_text = "To start the quiz, you can say 'Start'."
    should_end_session = False
    return build_response(attributes,build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def handle_repeat_request(intent, session):
    """
    Repeat the previous speech_output and reprompt_text from the session['attributes'].
    If available, else start a new game session.
    """
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return handle_help_session()
    else:
        attributes = session['attributes']
        speech_output = attributes['speech_output']
        reprompt_text = attributes['reprompt_text']
        should_end_session = False
        card_title = "Repeat Session"
        return build_response( attributes,
            build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session) )

  
#---------------First Level----------------------------------------------------------------

def get_first_level(intent, session):
    card_title = "Level 1"
    should_end_session= False
    first_questions = populate_first_questions()
    starting_index = 0
    spoken_first_question = FIRST_LEVEL_QUESTIONS[first_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Level 1. " + spoken_first_question 
    reprompt_text = spoken_first_question + "<break time = \"6000ms\"/> " \
                    +spoken_first_question + "<break time = \"6000ms\"/> " \
                    +spoken_first_question 
                    
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": first_questions,
                  "score": 0,
                  "correct_answers": FIRST_LEVEL_QUESTIONS[first_questions[starting_index]].values()[0]
                  }
    attributes['user_first'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_first_questions():
    first_questions = []
    index_list1 = []
    index1 = len(FIRST_LEVEL_QUESTIONS)
    
    if LEVEL_LENGTH > index1:
        raise ValueError("Invalid Quiz Length")
        
    for a in range (0,index1):
        index_list1.append(a)
    for b in range (0, LEVEL_LENGTH):
        rand1 = int(math.floor(random.random()*index1))
        index1 -= 1
        temp1 = index_list1[index1]
        index_list1[index1] = index_list1[rand1]
        index_list1[rand1] = temp1
        first_questions.append(index_list1[index1])
    return first_questions

def get_first_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    first_answer = intent['slots'].get('FirstAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not first_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        reprompt_text = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        first_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if first_answer and first_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech = "Bravo!" 
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = "Argh! "
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == LEVEL_LENGTH - 1:
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "
                
            speech_output = "" if intent['name'] == "DontKnowIntent" else " This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, LEVEL_LENGTH) + last_encouragement +
                             " Do you want continue to next level? ")
            reprompt_text =  "Do you want continue to next level? "
            should_end_session = False
            card_title = "Level 1 Final Score"
            attributes['user_prompted_to_continue'] = True
            return build_response(attributes, build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
        else:
            current_questions_index += 1
            spoken_first_question = FIRST_LEVEL_QUESTIONS[first_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_first_question+ "<break time = \"6000ms\"/> " \
                            + spoken_first_question + "<break time = \"6000ms\"/> " \
                            + spoken_first_question
                            
            speech_output = "" if user_gave_up == "DontKnowIntent" else " This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ".. " + spoken_first_question)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": first_questions,
                          "score": current_score,
                          "correct_answers": FIRST_LEVEL_QUESTIONS[first_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            attributes['user_first_answer'] = True
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))


def is_first_answer_slot_valid(intent):
    if 'FirstAnswer' in intent['slots'].keys() and 'value' in intent['slots']['FirstAnswer'].keys():
        return True
    else:
        return False

            
#---------------Second Level----------------------------------------------------------------

def get_second_level(intent, session):
    card_title = "Level- 2"
    should_end_session= False
    second_questions = populate_second_questions()
    starting_index = 0
    spoken_second_question = SECOND_LEVEL_QUESTIONS[second_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Level-2. " + spoken_second_question
    reprompt_text = spoken_second_question  + "<break time = \"6000ms\"/> " \
                    +spoken_second_question + "<break time = \"6000ms\"/> " \
                    +spoken_second_question 
                    
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": second_questions,
                  "score": 0,
                  "correct_answers": SECOND_LEVEL_QUESTIONS[second_questions[starting_index]].values()[0]
                  }
    attributes['user_second'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_second_questions():
    second_questions = []
    index_list2 = []
    index2 = len(SECOND_LEVEL_QUESTIONS)
    
    if LEVEL_LENGTH > index2:
        raise ValueError("Invalid Quiz Length")
        
    for c in range (0,index2):
        index_list2.append(c)
    for d in range (0, LEVEL_LENGTH):
        rand2 = int(math.floor(random.random()*index2))
        index2 -= 1
        temp2 = index_list2[index2]
        index_list2[index2] = index_list2[rand2]
        index_list2[rand2] = temp2
        second_questions.append(index_list2[index2])
    return second_questions

def get_second_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    second_answer = intent['slots'].get('SecondAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not second_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        second_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if second_answer and second_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech ="Bravo! "
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = "Argh! "
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == LEVEL_LENGTH - 1:
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "


            speech_output = "" if intent['name'] == "DontKnowIntent" else " This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, LEVEL_LENGTH) + last_encouragement +
                             "  Do you want continue to next level? ")
            reprompt_text =  "Do you want continue to next level? "
            should_end_session = False
            card_title = "Level 2 Final Score"
            attributes['user_prompted_continue'] = True
            return build_response(attributes, build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
        else:
            current_questions_index += 1
            spoken_second_question = SECOND_LEVEL_QUESTIONS[second_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_second_question + "<break time = \"6000ms\"/> " \
                            + spoken_second_question + "<break time = \"6000ms\"/> " \
                            + spoken_second_question
            speech_output = "" if user_gave_up == "DontKnowIntent" else " This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ".. " + spoken_second_question)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": second_questions,
                          "score": current_score,
                          "correct_answers": SECOND_LEVEL_QUESTIONS[second_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            attributes['user_second_answer'] = True
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))


def is_second_answer_slot_valid(intent):
    if 'SecondAnswer' in intent['slots'].keys() and 'value' in intent['slots']['SecondAnswer'].keys():
        return True
    else:
        return False

#---------------Third Level----------------------------------------------------------------

def get_third_level(intent, session):
    card_title = "Level- 3"
    should_end_session= False
    third_questions = populate_third_questions()
    starting_index = 0
    spoken_third_question = THIRD_LEVEL_QUESTIONS[third_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Level-3. " + spoken_third_question
    reprompt_text = spoken_third_question+ "<break time = \"6000ms\"/> " \
                    +spoken_third_question + "<break time = \"6000ms\"/> " \
                    +spoken_third_question
                    
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": third_questions,
                  "score": 0,
                  "correct_answers": THIRD_LEVEL_QUESTIONS[third_questions[starting_index]].values()[0]
                  }
    attributes['user_third'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_third_questions():
    third_questions = []
    index_list3 = []
    index3 = len(THIRD_LEVEL_QUESTIONS)
    
    if LEVEL_LENGTH > index3:
        raise ValueError("Invalid Quiz Length")
        
    for e in range (0,index3):
        index_list3.append(e)
    for f in range (0, LEVEL_LENGTH):
        rand3 = int(math.floor(random.random()*index3))
        index3 -= 1
        temp3 = index_list3[index3]
        index_list3[index3] = index_list3[rand3]
        index_list3[rand3] = temp3
        third_questions.append(index_list3[index3])
    return third_questions

def get_third_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    third_answer = intent['slots'].get('ThirdAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not third_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        third_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if third_answer and third_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech = "Bravo! "
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = "Argh! "
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == LEVEL_LENGTH - 1:
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "
                
            speech_output = "" if intent['name'] == "DontKnowIntent" else " This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, LEVEL_LENGTH) + last_encouragement +
                             " Do you want to continue the next level? ")
            reprompt_text =  "Do you want to continue the next level? "
            should_end_session = False
            card_title = "Level 3 Final Score"
            attributes['user_prompted_fourth'] = True
            return build_response(attributes, build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
        else:
            current_questions_index += 1
            spoken_third_question = THIRD_LEVEL_QUESTIONS[third_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_third_question  + "<break time = \"6000ms\"/> " \
                            + spoken_third_question + "<break time = \"6000ms\"/> " \
                            + spoken_third_question
                            
            speech_output = "" if user_gave_up == "DontKnowIntent" else " This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ".. " + spoken_third_question)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": third_questions,
                          "score": current_score,
                          "correct_answers": THIRD_LEVEL_QUESTIONS[third_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            attributes['user_third_answer'] = True
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))


def is_third_answer_slot_valid(intent):
    if 'ThirdAnswer' in intent['slots'].keys() and 'value' in intent['slots']['ThirdAnswer'].keys():
        return True
    else:
        return False

#---------------Fourth Level----------------------------------------------------------------

def get_fourth_level(intent, session):
    card_title = "Level- 4"
    should_end_session= False
    fourth_questions = populate_fourth_questions()
    starting_index = 0
    spoken_fourth_question = FOURTH_LEVEL_QUESTIONS[fourth_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Level-4. " + spoken_fourth_question
    reprompt_text = spoken_fourth_question + "<break time = \"6000ms\"/> " \
                    +spoken_fourth_question + "<break time = \"6000ms\"/> " \
                    +spoken_fourth_question
                    
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": fourth_questions,
                  "score": 0,
                  "correct_answers": FOURTH_LEVEL_QUESTIONS[fourth_questions[starting_index]].values()[0]
                  }
    attributes['user_fourth'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_fourth_questions():
    fourth_questions = []
    index_list4 = []
    index4 = len(FOURTH_LEVEL_QUESTIONS)
    
    if LEVEL_LENGTH > index4:
        raise ValueError("Invalid Quiz Length")
        
    for g in range (0,index4):
        index_list4.append(g)
    for h in range (0, LEVEL_LENGTH):
        rand4 = int(math.floor(random.random()*index4))
        index4 -= 1
        temp4 = index_list4[index4]
        index_list4[index4] = index_list4[rand4]
        index_list4[rand4] = temp4
        fourth_questions.append(index_list4[index4])
    return fourth_questions

def get_fourth_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    fourth_answer = intent['slots'].get('FourthAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not fourth_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        fourth_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if fourth_answer and fourth_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech = "Bravo! "
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = "Argh! "
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == LEVEL_LENGTH - 1:
        
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "
                
            speech_output = "" if intent['name'] == "DontKnowIntent" else " This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, LEVEL_LENGTH) + last_encouragement +
                             " Do you want continue to next level? ")
            reprompt_text =  "Do you want continue to next level? "
            should_end_session = False
            card_title = "Level 4 Final Score"
            attributes['user_prompted_fifth'] = True
            return build_response(attributes, build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
        else:
            current_questions_index += 1
            spoken_fourth_question = FOURTH_LEVEL_QUESTIONS[fourth_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_fourth_question + "<break time = \"6000ms\"/> " \
                            + spoken_fourth_question + "<break time = \"6000ms\"/> " \
                            + spoken_fourth_question
                            
            speech_output = "" if user_gave_up == "DontKnowIntent" else " This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ".. " + spoken_fourth_question)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": fourth_questions,
                          "score": current_score,
                          "correct_answers": FOURTH_LEVEL_QUESTIONS[fourth_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            attributes['user_fourth_answer'] = True
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))


def is_fourth_answer_slot_valid(intent):
    if 'FourthAnswer' in intent['slots'].keys() and 'value' in intent['slots']['FourthAnswer'].keys():
        return True
    else:
        return False
    
#---------------Fifth Level----------------------------------------------------------------

def get_fifth_level(intent, session):
    card_title = "Level- 5"
    should_end_session= False
    fifth_questions = populate_fifth_questions()
    starting_index = 0
    spoken_fifth_question = FIFTH_LEVEL_QUESTIONS[fifth_questions[starting_index]].keys()[0]
    speech_output = "Ok, Let's go to Level-5. " + spoken_fifth_question
    reprompt_text = spoken_fifth_question + "<break time = \"6000ms\"/> " \
                    +spoken_fifth_question + "<break time = \"6000ms\"/> " \
                    +spoken_fifth_question
                    
    attributes = {"speech_output": speech_output,
                  "reprompt_text": reprompt_text,
                  "current_questions_index": starting_index,
                  "questions": fifth_questions,
                  "score": 0,
                  "correct_answers": FIFTH_LEVEL_QUESTIONS[fifth_questions[starting_index]].values()[0]
                  }
    attributes['user_fifth'] = True
    return build_response(attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def populate_fifth_questions():
    fifth_questions = []
    index_list5 = []
    index5 = len(FIFTH_LEVEL_QUESTIONS)
    
    if LEVEL_LENGTH > index5:
        raise ValueError("Invalid Quiz Length")
        
    for i in range (0,index5):
        index_list5.append(i)
    for j in range (0, LEVEL_LENGTH):
        rand5 = int(math.floor(random.random()*index5))
        index5 -= 1
        temp5 = index_list5[index5]
        index_list5[index5] = index_list5[rand5]
        index_list5[rand5] = temp5
        fifth_questions.append(index_list5[index5])
    return fifth_questions

def get_fifth_level_answer(intent,session):
    attributes ={}
    should_end_session =False
    fifth_answer = intent['slots'].get('FifthAnswer', {}).get('value')
    user_gave_up = intent['name']
    
    if  not fifth_answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        card_title = "User guide"
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(session['attributes'], build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))
                
    else:
        fifth_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if fifth_answer and fifth_answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct"
            spoken_speech = "Bravo! "
                       
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "not correct. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])
            spoken_speech = "Argh! "
            
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == LEVEL_LENGTH - 1:
            
            if str(current_score) == "5":
                last_encouragement = "You are super star! "
            elif str(current_score) == "4":
                last_encouragement = "You are Star! "
            elif str(current_score) == "3":
                last_encouragement = "very good keep it up! "
            elif str(current_score) == "2":
                last_encouragement = "You need to practice more!  "
            elif str(current_score) == "1":
                last_encouragement = "Don't give up! "
            else:
                last_encouragement = "You need to work really really hard! "
                
            speech_output = "" if intent['name'] == "DontKnowIntent" else " This answer is "
            speech_output = (speech_output + speech_output_analysis +
                             ". You got {} out of {} correct. ".format(current_score, LEVEL_LENGTH) +  last_encouragement +
                             " Do you want continue to quiz? ")
            reprompt_text =  "Do you want continue to quiz? "
            should_end_session = False
            card_title = "Level 5 Final Score"
            attributes['user_prompted_re_enter'] = True
            return build_response(attributes, build_speechlet_response(
                    card_title, speech_output, reprompt_text, should_end_session))
        else:
            current_questions_index += 1
            spoken_fifth_question = FIFTH_LEVEL_QUESTIONS[fifth_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_fifth_question + "<break time = \"6000ms\"/> " \
                            + spoken_fifth_question + "<break time = \"6000ms\"/> " \
                            + spoken_fifth_question
                            
            speech_output = "" if user_gave_up == "DontKnowIntent" else " This answer is "
            speech_output = (spoken_speech + speech_output + speech_output_analysis +
                             ".. " + spoken_fifth_question)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": fifth_questions,
                          "score": current_score,
                          "correct_answers": FIFTH_LEVEL_QUESTIONS[fifth_questions[current_questions_index]].values()[0]  # noqa
                          }
            card_title ="Score"
            attributes['user_fifth_answer'] = True
            should_end_session = False
            return build_response(attributes,build_speechlet_response(
                card_title, speech_output, reprompt_text, should_end_session))


def is_fifth_answer_slot_valid(intent):
    if 'FifthAnswer' in intent['slots'].keys() and 'value' in intent['slots']['FifthAnswer'].keys():
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------------

def handle_error1_request(intent, session):
    
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return handle_help_session()
    else:    
        if 'FirstError' in intent['slots']:
            first_error_answer = intent['slots']['FirstError']['value']
            if session.get('attributes', {}).get('user_first'):
                return get_first_level_answer(intent,session)
            elif session.get('attributes', {}).get('user_first_answer'):
                return get_first_level_answer(intent,session)
            
            elif session.get('attributes', {}).get('user_second'):
                return get_second_level_answer(intent,session)
            elif session.get('attributes', {}).get('user_second_answer'):
                return get_second_level_answer(intent,session)
                
            elif session.get('attributes', {}).get('user_third'):
                return get_third_level_answer(intent,session)
            elif session.get('attributes', {}).get('user_third_answer'):
                return get_third_level_answer(intent,session)
                
            elif session.get('attributes', {}).get('user_fourth'):
                return get_fourth_level_answer(intent,session)
            elif session.get('attributes', {}).get('user_fourth_answer'):
                return get_fourth_level_answer(intent,session)
                
            elif session.get('attributes', {}).get('user_fifth'):
                return get_fifth_level_answer(intent,session)
            elif session.get('attributes', {}).get('user_fifth_answer'):
                return get_fifth_level_answer(intent,session)
            else:
                return handle_help_session()
            
            attributes = {}
            speech_output = speech_output
            reprompt_text = reprompt_text
            should_end_session = False
            card_title = ""
        return build_response( attributes,
            build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
# --------------- Events ------------------

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
    if intent_name == "MyQuizIntent":
        return get_first_level(intent, session)
    elif intent_name == "MySecondQuizIntent":
        return get_second_level(intent, session)
    elif intent_name == "MyThirdQuizIntent":
        return get_third_level(intent, session)
    elif intent_name == "MyFourthQuizIntent":
        return get_fourth_level(intent, session)
    elif intent_name == "MyFifthQuizIntent":
        return get_fifth_level(intent, session)

        
    elif intent_name == "FirstAnswerIntent":
        return get_first_level_answer(intent,session)
    elif intent_name == "SecondAnswerIntent":
        return get_second_level_answer(intent,session)
    elif intent_name == "ThirdAnswerIntent":
        return get_third_level_answer(intent,session)
    elif intent_name == "FourthAnswerIntent":
        return get_fourth_level_answer(intent,session)
    elif intent_name == "FifthAnswerIntent":
        return get_fifth_level_answer(intent,session)
    
    elif intent_name == "ErrorIntent":
        return handle_error1_request(intent, session)
    
    elif intent_name == "AMAZON.YesIntent":
        if session.get('attributes', {}).get('user_first'):
            return get_first_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_first_answer'):
            return get_first_level_answer(intent,session)
            
        elif session.get('attributes', {}).get('user_second'):
            return get_second_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_second_answer'):
            return get_second_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_prompted_to_continue'):
            return get_second_level(intent, session)
            
        elif session.get('attributes', {}).get('user_third'):
            return get_third_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_third_answer'):
            return get_third_level_answer(intent,session)    
        elif session.get('attributes', {}).get('user_prompted_continue'):
            return get_third_level(intent, session)
        
        elif session.get('attributes', {}).get('user_fourth'):
            return get_fourth_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_fourth_answer'):
            return get_fourth_level_answer(intent,session)    
        elif session.get('attributes', {}).get('user_prompted_fourth'):
            return get_fourth_level(intent, session)
        
        elif session.get('attributes', {}).get('user_fifth'):
            return get_fifth_level_answer(intent,session)
        elif session.get('attributes', {}).get('user_fifth_answer'):
            return get_fifth_level_answer(intent,session)    
        elif session.get('attributes', {}).get('user_prompted_fifth'):
            return get_fifth_level(intent, session)
            
        elif session.get('attributes', {}).get('user_prompted_re_enter'):
            return get_first_level(intent, session)
        return handle_error1_request(intent, session)
    
    
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
        
# ------- Skill specific  logic ------------------------------

LEVEL_LENGTH = 5
FIRST_LEVEL_QUESTIONS=[
    {"121 minus 30=?" : ["91"]},
    {"122 minus 30=?" : ["92"]},
    {"123 minus 30=?" : ["93"]},
    {"124 minus 30=?" : ["94"]},
    {"125 minus 30=?" : ["95"]},
    {"126 minus 30=?" : ["96"]},
    {"127 minus 30=?" : ["97"]},
    {"128 minus 30=?" : ["98"]},
    {"129 minus 30=?" : ["99"]},
    {"131 minus 40=?" : ["91"]},
    {"132 minus 40=?" : ["92"]},
    {"133 minus 40=?" : ["93"]},
    {"134 minus 40=?" : ["94"]},
    {"135 minus 40=?" : ["95"]},
    {"136 minus 40=?" : ["96"]},
    {"137 minus 40=?" : ["97"]},
    {"138 minus 40=?" : ["98"]},
    {"139 minus 40=?" : ["99"]},
    {"140 minus 39=?" : ["99"]},
    {"131 minus 33=?" : ["98"]},
    {"131 minus 34=?" : ["97"]},
    {"131 minus 35=?" : ["96"]},
    {"131 minus 36=?" : ["95"]},
    {"131 minus 37=?" : ["94"]},
    {"131 minus 38=?" : ["93"]},
    {"131 minus 39=?" : ["92"]},
    {"131 minus 40=?" : ["91"]},
    {"132 minus 33=?" : ["99"]}, 
    {"132 minus 34=?" : ["98"]},
    {"132 minus 36=?" : ["96"]}, 
    {"132 minus 37=?" : ["95"]}, 
    {"132 minus 38=?" : ["94"]}, 
    {"132 minus 39=?" : ["93"]},
    {"122 minus 31=?" : ["91"]},
    {"123 minus 31=?" : ["92"]},
    {"124 minus 31=?" : ["93"]},
    {"125 minus 31=?" : ["94"]},
    {"126 minus 31=?" : ["95"]},
    {"127 minus 31=?" : ["96"]},
    {"128 minus 31=?" : ["97"]},
    {"129 minus 31=?" : ["98"]},
    {"190 minus 31=?" : ["99"]},
    {"126 minus 35=?" : ["91"]},
    {"127 minus 35=?" : ["92"]},
    {"128 minus 35=?" : ["93"]},
    {"129 minus 35=?" : ["94"]},
    {"130 minus 35=?" : ["95"]},
    {"131 minus 35=?" : ["96"]},
    {"132 minus 35=?" : ["97"]},
    {"133 minus 35=?" : ["98"]},
    {"134 minus 35=?" : ["99"]},
    {"123 minus 32=?" : ["91"]},
    {"124 minus 32=?" : ["92"]},
    {"125 minus 32=?" : ["93"]},
    {"126 minus 32=?" : ["94"]},
    {"127 minus 32=?" : ["95"]},
    {"128 minus 32=?" : ["96"]},
    {"129 minus 32=?" : ["97"]},
    {"130 minus 32=?" : ["98"]},
    {"131 minus 32=?" : ["99"]},
    {"133 minus 42=?" : ["91"]},
    {"134 minus 42=?" : ["92"]},
    {"135 minus 42=?" : ["93"]},
    {"136 minus 42=?" : ["94"]},
    {"137 minus 42=?" : ["95"]},
    {"138 minus 42=?" : ["96"]},
    {"139 minus 42=?" : ["97"]},
    {"140 minus 42=?" : ["98"]},
    {"141 minus 42=?" : ["99"]}
   ]

SECOND_LEVEL_QUESTIONS=[
    {"151 minus 40=?" : ["111"]},
    {"152 minus 40=?" : ["112"]},
    {"153 minus 40=?" : ["113"]},
    {"154 minus 40=?" : ["114"]},
    {"155 minus 40=?" : ["115"]},
    {"156 minus 40=?" : ["116"]},
    {"157 minus 40=?" : ["117"]},
    {"158 minus 40=?" : ["118"]},
    {"159 minus 40=?" : ["119"]},
    {"153 minus 42=?" : ["111"]},
    {"154 minus 42=?" : ["112"]},
    {"155 minus 42=?" : ["113"]},
    {"156 minus 42=?" : ["114"]},
    {"157 minus 42=?" : ["115"]},
    {"158 minus 42=?" : ["116"]},
    {"159 minus 42=?" : ["117"]},
    {"160 minus 42=?" : ["118"]},
    {"161 minus 42=?" : ["119"]},
    {"156 minus 45=?" : ["111"]},
    {"157 minus 45=?" : ["112"]},
    {"158 minus 45=?" : ["113"]},
    {"159 minus 45=?" : ["114"]},
    {"160 minus 45=?" : ["115"]},
    {"161 minus 45=?" : ["116"]},
    {"162 minus 45=?" : ["117"]},
    {"163 minus 45=?" : ["118"]},
    {"164 minus 45=?" : ["119"]},
    {"157 minus 46=?" : ["111"]},
    {"158 minus 46=?" : ["112"]},
    {"159 minus 46=?" : ["113"]},
    {"160 minus 46=?" : ["114"]},
    {"161 minus 46=?" : ["115"]},
    {"162 minus 46=?" : ["116"]},
    {"163 minus 46=?" : ["117"]},
    {"164 minus 46=?" : ["118"]},
    {"165 minus 46=?" : ["119"]},
    {"158 minus 47=?" : ["111"]},
    {"159 minus 47=?" : ["112"]},
    {"160 minus 47=?" : ["113"]},
    {"161 minus 47=?" : ["114"]},
    {"162 minus 47=?" : ["115"]},
    {"163 minus 47=?" : ["116"]},
    {"164 minus 47=?" : ["117"]},
    {"165 minus 47=?" : ["118"]},
    {"166 minus 47=?" : ["119"]},
    {"159 minus 48=?" : ["111"]},
    {"160 minus 48=?" : ["112"]},
    {"161 minus 48=?" : ["113"]},
    {"162 minus 48=?" : ["114"]},
    {"163 minus 48=?" : ["115"]},
    {"164 minus 48=?" : ["116"]},
    {"165 minus 48=?" : ["117"]},
    {"166 minus 48=?" : ["118"]},
    {"167 minus 48=?" : ["119"]},
    {"161 minus 50=?" : ["111"]},
    {"162 minus 50=?" : ["112"]},
    {"163 minus 50=?" : ["113"]},
    {"164 minus 50=?" : ["114"]},
    {"165 minus 50=?" : ["115"]},
    {"166 minus 50=?" : ["116"]},
    {"167 minus 50=?" : ["117"]},
    {"168 minus 50=?" : ["118"]},
    {"169 minus 50=?" : ["119"]}
    ]
   
THIRD_LEVEL_QUESTIONS=[
    {"181 minus 50=?" : ["131"]},
    {"182 minus 50=?" : ["132"]},
    {"183 minus 50=?" : ["133"]},
    {"184 minus 50=?" : ["134"]},
    {"185 minus 50=?" : ["135"]},
    {"186 minus 50=?" : ["136"]},
    {"187 minus 50=?" : ["137"]},
    {"188 minus 50=?" : ["138"]},
    {"189 minus 50=?" : ["139"]},
    {"182 minus 51=?" : ["131"]},
    {"183 minus 51=?" : ["132"]},
    {"184 minus 51=?" : ["133"]},
    {"185 minus 51=?" : ["134"]},
    {"186 minus 51=?" : ["135"]},
    {"187 minus 51=?" : ["136"]},
    {"188 minus 51=?" : ["137"]},
    {"189 minus 51=?" : ["138"]},
    {"190 minus 51=?" : ["139"]},
    {"183 minus 52=?" : ["131"]},
    {"184 minus 52=?" : ["132"]},
    {"185 minus 52=?" : ["133"]},
    {"186 minus 52=?" : ["134"]},
    {"187 minus 52=?" : ["135"]},
    {"188 minus 52=?" : ["136"]},
    {"189 minus 52=?" : ["137"]},
    {"190 minus 52=?" : ["138"]},
    {"191 minus 52=?" : ["139"]},
    {"186 minus 55=?" : ["131"]},
    {"187 minus 55=?" : ["132"]},
    {"188 minus 55=?" : ["133"]},
    {"189 minus 55=?" : ["134"]},
    {"190 minus 55=?" : ["135"]},
    {"191 minus 55=?" : ["136"]},
    {"192 minus 55=?" : ["137"]},
    {"193 minus 55=?" : ["138"]},
    {"194 minus 55=?" : ["139"]},
    {"187 minus 56=?" : ["131"]},
    {"188 minus 56=?" : ["132"]},
    {"189 minus 56=?" : ["133"]},
    {"190 minus 56=?" : ["134"]},
    {"192 minus 57=?" : ["135"]},
    {"193 minus 57=?" : ["136"]},
    {"194 minus 57=?" : ["137"]},
    {"195 minus 57=?" : ["138"]},
    {"196 minus 57=?" : ["139"]},
    {"190 minus 59=?" : ["131"]},
    {"191 minus 59=?" : ["132"]},
    {"192 minus 59=?" : ["133"]},
    {"193 minus 59=?" : ["134"]},
    {"194 minus 59=?" : ["135"]},
    {"194 minus 58=?" : ["136"]},
    {"195 minus 58=?" : ["137"]},
    {"196 minus 58=?" : ["138"]},
    {"197 minus 58=?" : ["139"]},
    {"191 minus 60=?" : ["131"]},
    {"192 minus 60=?" : ["132"]},
    {"193 minus 60=?" : ["133"]},
    {"194 minus 60=?" : ["134"]},
    {"195 minus 60=?" : ["135"]},
    {"196 minus 60=?" : ["136"]},
    {"197 minus 60=?" : ["137"]},
    {"198 minus 60=?" : ["138"]},
    {"199 minus 60=?" : ["139"]},
    ]

FOURTH_LEVEL_QUESTIONS = [
    {"210 minus 59=?" : ["151"]},
    {"211 minus 59=?" : ["152"]},
    {"212 minus 59=?" : ["153"]},
    {"213 minus 59=?" : ["154"]},
    {"214 minus 59=?" : ["155"]},
    {"215 minus 59=?" : ["156"]},
    {"216 minus 59=?" : ["157"]},
    {"217 minus 59=?" : ["158"]},
    {"218 minus 59=?" : ["159"]},
    {"214 minus 63=?" : ["151"]},
    {"215 minus 63=?" : ["152"]},
    {"216 minus 63=?" : ["153"]},
    {"217 minus 63=?" : ["154"]},
    {"218 minus 63=?" : ["155"]},
    {"216 minus 60=?" : ["156"]},
    {"217 minus 60=?" : ["157"]},
    {"218 minus 60=?" : ["158"]},
    {"219 minus 60=?" : ["159"]},
    {"220 minus 61=?" : ["159"]},
    {"219 minus 61=?" : ["158"]},
    {"218 minus 61=?" : ["157"]},
    {"217 minus 61=?" : ["156"]},
    {"217 minus 62=?" : ["155"]},
    {"216 minus 62=?" : ["154"]},
    {"215 minus 62=?" : ["153"]},
    {"214 minus 62=?" : ["152"]},
    {"213 minus 62=?" : ["151"]},
    {"215 minus 64=?" : ["151"]},
    {"218 minus 66=?" : ["152"]},
    {"217 minus 64=?" : ["153"]},
    {"220 minus 66=?" : ["154"]},
    {"219 minus 64=?" : ["155"]},
    {"222 minus 66=?" : ["156"]},
    {"221 minus 64=?" : ["157"]},
    {"224 minus 66=?" : ["158"]},
    {"223 minus 64=?" : ["159"]},
    {"225 minus 66=?" : ["159"]},
    {"216 minus 65=?" : ["151"]},
    {"217 minus 65=?" : ["152"]},
    {"218 minus 65=?" : ["153"]},
    {"219 minus 65=?" : ["154"]},
    {"220 minus 65=?" : ["155"]},
    {"221 minus 65=?" : ["156"]},
    {"222 minus 65=?" : ["157"]},
    {"223 minus 65=?" : ["158"]},
    {"224 minus 65=?" : ["159"]},
    {"218 minus 67=?" : ["151"]},
    {"220 minus 68=?" : ["152"]},
    {"220 minus 67=?" : ["153"]},
    {"222 minus 68=?" : ["154"]},
    {"222 minus 67=?" : ["155"]},
    {"223 minus 67=?" : ["156"]},
    {"224 minus 67=?" : ["157"]},
    {"225 minus 67=?" : ["158"]},
    {"226 minus 67=?" : ["159"]},
    {"225 minus 68=?" : ["157"]},
    {"226 minus 68=?" : ["158"]},
    {"227 minus 65=?" : ["159"]},
    {"221 minus 70=?" : ["151"]},
    {"222 minus 70=?" : ["152"]},
    {"223 minus 70=?" : ["153"]},
    {"225 minus 70=?" : ["155"]},
    {"227 minus 70=?" : ["157"]},
    {"229 minus 70=?" : ["159"]},
    {"225 minus 72=?" : ["153"]},
    {"227 minus 72=?" : ["155"]},
    {"229 minus 72=?" : ["157"]},
    {"231 minus 72=?" : ["159"]},
    {"225 minus 73=?" : ["152"]},
    {"227 minus 73=?" : ["154"]},
    {"229 minus 73=?" : ["156"]},
    {"232 minus 73=?" : ["159"]},
    {"228 minus 75=?" : ["153"]},
    {"231 minus 75=?" : ["156"]},
    {"233 minus 75=?" : ["158"]},
    {"234 minus 75=?" : ["159"]}
    ]
    
FIFTH_LEVEL_QUESTIONS = [
    {"250 minus 79=?" : ["171"]},
    {"251 minus 80=?" : ["171"]},
    {"253 minus 81=?" : ["172"]},
    {"252 minus 79=?" : ["173"]},
    {"253 minus 79=?" : ["174"]},
    {"252 minus 81=?" : ["171"]},
    {"254 minus 81=?" : ["173"]},
    {"254 minus 79=?" : ["175"]},
    {"256 minus 80=?" : ["176"]},
    {"258 minus 81=?" : ["177"]},
    {"256 minus 79=?" : ["177"]},
    {"259 minus 81=?" : ["178"]},
    {"258 minus 80=?" : ["178"]},
    {"258 minus 79=?" : ["179"]},
    {"259 minus 80=?" : ["179"]},
    {"258 minus 79=?" : ["179"]},
    {"254 minus 83=?" : ["171"]},
    {"260 minus 83=?" : ["177"]},
    {"261 minus 83=?" : ["178"]},
    {"262 minus 83=?" : ["179"]},
    {"258 minus 83=?" : ["175"]},
    {"256 minus 85=?" : ["171"]},
    {"258 minus 85=?" : ["173"]},
    {"260 minus 85=?" : ["175"]},
    {"262 minus 85=?" : ["177"]},
    {"263 minus 85=?" : ["178"]},
    {"264 minus 85=?" : ["179"]},
    {"258 minus 87=?" : ["171"]},
    {"259 minus 87=?" : ["172"]},
    {"261 minus 87=?" : ["174"]},
    {"263 minus 87=?" : ["175"]},
    {"264 minus 87=?" : ["177"]},
    {"265 minus 87=?" : ["178"]},
    {"266 minus 87=?" : ["179"]},
    {"265 minus 86=?" : ["179"]},
    {"264 minus 86=?" : ["178"]},
    {"262 minus 86=?" : ["176"]},
    {"262 minus 90=?" : ["172"]},
    {"269 minus 90=?" : ["179"]},
    {"267 minus 95=?" : ["172"]},
    {"274 minus 95=?" : ["179"]},
    {"273 minus 95=?" : ["178"]},
    {"270 minus 97=?" : ["173"]},
    {"272 minus 97=?" : ["175"]},
    {"273 minus 97=?" : ["176"]},
    {"274 minus 97=?" : ["177"]},
    {"274 minus 99=?" : ["175"]},
    {"273 minus 99=?" : ["174"]},
    {"275 minus 100=?" : ["175"]},
    {"280 minus 105=?" : ["175"]},
    {"274 minus 103=?" : ["171"]},
    {"278 minus 105=?" : ["173"]},
    {"277 minus 102=?" : ["175"]},
    {"277 minus 103=?" : ["174"]},
    {"285 minus 110=?" : ["175"]},
    {"287 minus 112=?" : ["175"]},
    {"289 minus 118=?" : ["171"]},
    {"282 minus 115=?" : ["172"]},
    {"290 minus 111=?" : ["179"]},
    {"285 minus 110=?" : ["175"]},
    {"289 minus 113=?" : ["176"]},
    {"281 minus 106=?" : ["175"]}
    ]
