var Botkit = require('botkit');

var controller = Botkit.slackbot({clientId: "49104941602.867346169906",
	clientSigningSecret: "9a68afacd24767dad24b9af835e83f1f"});

var bot = controller.spawn({

  token: "2566cb5bbcd84379b270b2c3deaf5b58"

})



controller.hears(["Hello","Hi"],["direct_message","direct_mention","mention","ambient"],function(bot,message) {

  bot.reply(message,'Hello, how are you today?');

});

controller.hears(['weather in (.*)', '(.*) weather'], 'direct_message,direct_mention,mention', function(bot,message) {
    var city = message.match[1];
});