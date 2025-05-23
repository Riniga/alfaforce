
# botcore
A Microsoft [Bot Framework](https://dev.botframework.com) bot that later should be available in Microsoft Teams
This bot is the interface to command other bots to do their best

## Prerequisites
Conda environmentt with python 3.13.3
packages: 
- pip install botbuilder
- pip install botbuilder-core

### Testing the bot using Bot Framework Emulator
[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.
- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Created bot from template
- cookiecutter https://github.com/microsoft/BotBuilder-Samples/releases/download/Templates/echo.zip

## Running the sample
- Run `python app.py`

### Connect to the bot using Bot Framework Emulator
- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`

## Deployement
az login --tenant <TenantID>
az login --tenant <TenantID> -u <email> -p <password>

## Further reading
- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)