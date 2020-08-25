const Alexa = require('ask-sdk-core');
const i18n = require('i18next');
const sprintf = require('i18next-sprintf-postprocessor');

const LaunchHandler = {
    canHandle(handlerInput) {
        const request = handlerInput.requestEnvelope.request;

        return request.type === 'LaunchRequest';
    },
    handle(handlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const requestAttributes = attributesManager.getRequestAttributes();
        const speechOutput = `${requestAttributes.t('WELCOME')}`;
        const repromptOutput=`${requestAttributes.t('WELCOME_Reprompt')}`;
    
        const cardTitle= "Welcome!";
        const cardBody= "King soopers, Target, Safeway, Sam's Club, Aldi, Trader Joe's, Walmart, Walgreens, Whole Foods Market, Costco Wholesale, Dollar General, Bog Lots, Albertsons, Balducci's, BJ's Whole Sale Club, Fareway Meat and Grocery, Fresh Market, Fresco y Mas, Giant Food, Mother's Market, Harveys SuperMarket, Publix, Schnucks, Sedabo's SuperMarket, Smith's Food and Drug Store, Vallarat SuperMarket, Winn Dixie.     ";
    
        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(repromptOutput)
            .withStandardCard(cardTitle,cardBody)
            .getResponse();
        
    },
};
const MallListIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'mallListIntent';
    },
    handle(handlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const requestAttributes = attributesManager.getRequestAttributes();
        
        const speechOutput =`${requestAttributes.t('ListSession')}`; 

        const cardTitle= "Shopping Mall Lists";
        const cardBody= "King soopers, Target, Safeway, Sam's Club, Aldi, Trader Joe's, Walmart, Walgreens, Whole Foods Market, Costco Wholesale, Dollar General, Bog Lots, Albertsons, Balducci's, BJ's Whole Sale Club, Fareway Meat and Grocery, Fresh Market, Fresco y Mas, Giant Food, Mother's Market, Harveys Supermarket, Publix, Schnucks, Sedabo's Supermarket, Smith's Food and Drug Store, Vallarta Supermarket, Winn Dixie.";
    
        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(speechOutput)
            //.withStandardCard(cardTitle,cardBody, smallImageUrl, largeImageUrl)
            .withStandardCard(cardTitle,cardBody)
            .getResponse();
    }
};
 
const HelpIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const requestAttributes = attributesManager.getRequestAttributes();
        
        const speechOutput =`${requestAttributes.t('HelpSession')}`; 

        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(speechOutput)
            .getResponse();
    }
};
const YesValueHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.YesIntent';
    },
    handle(handlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const requestAttributes = attributesManager.getRequestAttributes();
        
        const speechOutput =`${requestAttributes.t('YesSession')}`; 

        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(speechOutput)
            .getResponse();
    }
};
const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && (Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.CancelIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.StopIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.NoIntent');
    },
    handle(handlerInput) {
        const speechOutput = 'See you soon! Have a nice shopping!';
        return handlerInput.responseBuilder
            .speak(speechOutput)
            .getResponse();
    }
};
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};


const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speechOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speechOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.log(`~~~~ Error handled: ${error.stack}`);
        const speechOutput = `Sorry, I had trouble doing what you asked. Please try again.`;

        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(speechOutput)
            .getResponse();
    }
};

const ChooseMallHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
        && handlerInput.requestEnvelope.request.intent.name === 'choosenMallIntent';
  },
  handle(handlerInput) {
    let itemName;
      const itemSlot = handlerInput.requestEnvelope.request.intent.slots.mallSlot;
      if (itemSlot && itemSlot.value) {
        itemName = itemSlot.value.toLowerCase();
      }
    return generateMallOutput(handlerInput, itemName);
  },
};




// 1. Constants ==================================================================================
const malls={
        MALL_EN_US: {
            "king soopers"  : "Monday, Wednesday, Friday from 7am to 8am",
            "target"  : "Wednesday from 8am to 9am",
            "safeway"  : "Tuesday and Thursday from 7am to 9am",
            "sam's club" : "Tuesday and Thursday from 8am to 9am",
            "aldi": "Tuesday and Thursday from 8.30am to 9.30am",
            "trader joe's": "Each day from 9am to 10am",
            "walmart": "Tuesday from 6am to 7am",
            "walgreens": "Tuesday from 8am to 9am",
            "whole foods market": "Each day from 7am to 8am",
            "costco wholesale": " Tuesday and Thursday from 8am to 9am",
            "dollar general": "First hour of eachday that is from 8am to 9am",
            "bog lots": " Each day from 9am to 10am",
            "albertsons": "Tuesday and Thursday from 7am to 9am",
            "balducci's": " Each day from 8am to 9am",
            "bj's whole sale club": " Eachday from 8am to 9am",
            "fareway meat and grocery": " Monday to Saturday from 8am to 9am",
            "fresh market": "Monday to Friday from 8am to 9am",
            "Fresco y mas": " Monday to Friday from 8am to 9am",
            "giant food": " Everyday from 6am to 7am",
            "mother's market": " Every Wednesday from 6am to 7am",
            "harveys supermarket": " Monday to Friday from 8am to 9am",
            "publix": " Every Wednesday from 7am to 8am ",
            "schnucks": " Everyday from 6am to 7am",
            "sedabo's SuperMarket": " Every Thursday from 7am to 8am",
            "smith's food and drug store": "Every Monday, Wednesday,Friday from 7am to 8am",
            "vallarta supermarket": "Everyday from 7am to 8am",
            "winn dixie": " Monday to Friday from 8am to 9am",
            
    },
};

const languageStrings = {
    en: {
        translation: {
            MALLS: malls.MALL_EN_US,
            SKILL_NAME: '',
            WELCOME: " Welcome to Senior Shopping Hours."
                          + "<break time = \"0.1s\"/> "
                          +" I am glad that I can be of help."
                          + "<break time = \"0.05s\"/> "
                          +" You can start by saying the retailer name you want to know senior only hours, "
                          + "<break time = \"0.1s\"/> "
                          +" for e.g. Target" ,
            WELCOME_Reprompt:" I am glad that I can be of help."
                          + "<break time = \"0.05s\"/> "
                          +" You can start by saying the retailer name you want to know senior only hours, "
                          + "<break time = \"0.1s\"/> "
                          +" for e.g. Target" ,
           
            HelpSession: " You can start by saying the retailer name you want to know senior only hours,"
                          + "<break time = \"0.1s\"/> " 
                          +" for e.g. King soopers."
                            + "<break time = \"0.1s\"/> "
                            +" Target, Safeway, Sam's Club, Aldi, Trader Joe's, Walmart, Walgreens, Whole Foods Market, Costco Wholesale, Dollar General, Bog Lots, Albertsons, Balducci's, BJ's Whole Sale Club, Fareway Meat and Grocery, Fresh Market, Fresco y Mas, Giant Food, Mother's Market, Harveys Supermarket, Publix, Schnucks, Sedabo's Supermarket, Smith's Food and Drug Store, Vallarta Supermarket, Winn Dixie.     ",
    
            ListSession: "Here is the shopping mall list for seniors: "
                            + "<break time = \"0.1s\"/> "
                            +" King soopers."
                            + "<break time = \"0.1s\"/> "
                            +" Target, Safeway, Sam's Club, Aldi, Trader Joe's, Walmart, Walgreens, Whole Foods Market, Costco Wholesale, Dollar General, Bog Lots, Albertsons, Balducci's, BJ's Whole Sale Club, Fareway Meat and Grocery, Fresh Market, Fresco y Mas, Giant Food, Mother's Market, Harveys Supermarket, Publix, Schnucks, Sedabo's Supermarket, Smith's Food and Drug Store, Vallarta Supermarket, Winn Dixie.     "                          
                            + " For which retailer name you want to know senior only hours?",
            YesSession: " You can start by saying the retailer name you want to know senior only hours,"
                          + "<break time = \"0.1s\"/> "
                          +" for e.g. Aldi or you can say mall list.",
            STOP: 'Okay, see you next time!',
            RECIPE_REPEAT_MESSAGE: 'Try saying repeat.',
      RECIPE_NOT_FOUND_WITH_ITEM_NAME: 'I\'m sorry, I currently do not know the menu for %s. ',
      RECIPE_NOT_FOUND_WITHOUT_ITEM_NAME: 'I\'m sorry, I currently do not know that menu. ',
      RECIPE_NOT_FOUND_REPROMPT: 'What else can I help with?',
        },
    },
   
    'en-US': {
    translation: {
      MALLS: malls.MALL_EN_US,
      SKILL_NAME: '',
    },
  },
};

///////////////-------------------
const LocalizationInterceptor = {
  process(handlerInput) {
    const localizationClient = i18n.use(sprintf).init({
      lng: handlerInput.requestEnvelope.request.locale,
      resources: languageStrings,
    });
    localizationClient.localize = function localize() {
      const args = arguments; // eslint-disable-line prefer-rest-params
      const values = [];
      for (let i = 1; i < args.length; i += 1) {
        values.push(args[i]);
      }
      const value = i18n.t(args[0], {
        returnObjects: true,
        postProcess: 'sprintf',
        sprintf: values,
      });
      if (Array.isArray(value)) {
        return value[Math.floor(Math.random() * value.length)];
      }
      return value;
    };
    const attributes = handlerInput.attributesManager.getRequestAttributes();
    attributes.t = function translate(...args) {
      return localizationClient.localize(...args);
    };
  },
};

const RequestHistoryInterceptor = {
  process(handlerInput) {
    const maxHistorySize = 10; // number of intent/request events to store
    const thisRequest = handlerInput.requestEnvelope.request;
    const sessionAttributes = handlerInput.attributesManager.getSessionAttributes();
    let requestHistory = sessionAttributes.requestHistory;
    const currentRequest = {
      requestType: thisRequest.type,
      intentName: '',
      slots: {},
    };
    if (thisRequest.type === 'IntentRequest') {
      currentRequest.intentName = thisRequest.intent.name;
      if (thisRequest.intent.slots) {
        for (let slot in thisRequest.intent.slots) {
          currentRequest.slots[slot] = thisRequest.intent.slots[slot].value;
        }
      }
    }

    if (!requestHistory) {
      requestHistory = [];
    }

    if (requestHistory.length >= maxHistorySize) {
      requestHistory.shift();
    }
    requestHistory.push(currentRequest);

    sessionAttributes.requestHistory = requestHistory;
  },
};

const RequestLog = {
  process(handlerInput) {
    console.log(`REQUEST ENVELOPE = ${JSON.stringify(handlerInput.requestEnvelope)}`);
  },
};

const ResponseLog = {
  process(handlerInput) {
    console.log(`RESPONSE BUILDER = ${JSON.stringify(handlerInput)}`);
    console.log(`RESPONSE = ${JSON.stringify(handlerInput.responseBuilder.getResponse())}`);
  },
};


function generateMallOutput(handlerInput, itemName) {
  const requestAttributes = handlerInput.attributesManager.getRequestAttributes();
  const sessionAttributes = handlerInput.attributesManager.getSessionAttributes();

  const myMalls = requestAttributes.t('MALLS');
  const mall = myMalls[itemName];
  let speechOutput = '';
  let repromptOutput = '';
  if (mall) {
    sessionAttributes.speechOutput = "Senior only hour at " + itemName + " is " + mall +". Do you want to know any other retailer 'senior shopping hours'?";
    
    handlerInput.attributesManager.setSessionAttributes(sessionAttributes);

    const responseBuilder = handlerInput.responseBuilder;
     // saved for repeat
   sessionAttributes.repromptSpeech = "Senior only hour at " + itemName + " is " + mall+". Do you want to know any other retailer 'senior shopping hours'?";

    Object.assign(sessionAttributes, {
      mallYes:mall
     });

    return responseBuilder
      .speak(sessionAttributes.speechOutput)
      .reprompt(sessionAttributes.repromptOutput)
      .getResponse();
  } 
  else{
      sessionAttributes.speechOutput = "Currently we don't have information regarding this shopping center. Please try again later.";
      const responseBuilder = handlerInput.responseBuilder;
      return responseBuilder
      .speak(sessionAttributes.speechOutput)
      .getResponse();
  }
  
}

const skillBuilder = Alexa.SkillBuilders.custom();
exports.handler = skillBuilder
    .addRequestHandlers(
        LaunchHandler,
        ChooseMallHandler,
        MallListIntentHandler,
        HelpIntentHandler,
        YesValueHandler,
        CancelAndStopIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler,
        
        )
        
    
    .addRequestInterceptors(
      LocalizationInterceptor,
      RequestLog,
      RequestHistoryInterceptor,
    )
    
    .addResponseInterceptors(ResponseLog)
    
    .addErrorHandlers(
        ErrorHandler
    )
    .lambda();
    