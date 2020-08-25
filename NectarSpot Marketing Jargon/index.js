'use strict';

var AlexaSkill = require('./AlexaSkill'),
    data = require('./data');

var APP_ID = undefined; //OPTIONAL: replace with 'amzn1.echo-sdk-ams.app.[your-unique-value-here]';


var HowTo = function () {
    AlexaSkill.call(this, APP_ID);
};

// Extend AlexaSkill
HowTo.prototype = Object.create(AlexaSkill.prototype);
HowTo.prototype.constructor = HowTo;

HowTo.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    var speechText = 'Welcome to NectarSpot Marketing Jargon. '+
                        '  Tell me a word to abbreviate, '+
                        '  For Example, you can say , API';
    var repromptText = 'Tell me a word to abbreviate, '+
                        '  For Example, you can say , API';
    //var cardTitle = 'Welcome';
    
    response.ask(speechText, repromptText);
};

HowTo.prototype.intentHandlers = {
    "wordIntent": function (intent, session, response) {
        var itemSlot = intent.slots.Item,
            itemName;
        if (itemSlot && itemSlot.value){
            itemName = itemSlot.value.toUpperCase();
            
        }

        var cardTitle = "Abbreviation for " + itemName,
            word = data[itemName],
            speechOutput,
            repromptOutput;
        if (word) {
            speechOutput = {
                speech: word +' .  What else can I help with?',
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
            repromptOutput = {
                speech: "What else can I help with?  you can say a word for abbreviation." +
                        "  or say word list for words.  " +
                        " or say stop.",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
            response.tellWithCard(speechOutput, repromptOutput, cardTitle, word);
        } else {
            var speech;
            if (itemName) {
                speech = "I'm sorry, I currently do not know the abbreviation for  " + itemName + ".  What else can I help with?";
            } else {
                speech = "I'm sorry, I currently do not know that abbreviation. What else can I help with?"+
                            " Don't worry "+
                            " You can refer our word list."+
                            " By saying."+
                            ' Word list.'+
                            'or say stop';
            }
            speechOutput = {
                speech: speech,
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
            repromptOutput = {
                speech: "What else can I help with?",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
            response.ask(speechOutput, repromptOutput);
        }
    },
    
    
  
    "WordListIntent": function (intent, session, response) {
        var cardTitle = "Word List ",
            speechOutput,
            repromptOutput;
        var wordlist = 'AAA.   ABC. AIDA.   AJAX.   AOV.    API.    AR. ASO.'+
                '   ASP.   ATD.  B2B. etc';
                
        speechOutput = {
                speech: wordlist +
                        '   What else can I help with?',
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
        repromptOutput = {
                speech: "What else can I help with?  you can say a word for abbreviation." +
                        "  or say word list for words.  " +
                        " or say stop.",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
            };
            response.tellWithCard(speechOutput, repromptOutput, cardTitle, wordlist);
        },

    
    

    "AMAZON.StopIntent": function (intent, session, response) {
        var speechOutput = 'Thank you for using NectarSpot Marketing Jargon.';
        response.tell(speechOutput);
    },

    "AMAZON.CancelIntent": function (intent, session, response) {
        var speechOutput = 'Thank you for using NectarSpot Marketing Jargon.';
        response.tell(speechOutput);
    },

    "AMAZON.HelpIntent": function (intent, session, response) {
        var speechText = 'Tell me a word to abbreviate. '+
                        ' For Example, you can say , API';
        var repromptText = "Sorry I didn't get any word for abbriviate."+ 
                            " Don't worry "+
                            " You can refer our word list."+
                            " By saying."+
                            ' Word list.'+
                            'or say stop';
        var speechOutput = {
            speech: speechText,
            type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        var repromptOutput = {
            speech: repromptText,
            type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        response.ask(speechOutput, repromptOutput);
    }
};

exports.handler = function (event, context) {
    var howTo = new HowTo();
    howTo.execute(event, context);
};
