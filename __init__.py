from mycroft import MycroftSkill, intent_file_handler


class AirPollution(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pollution.air.intent')
    def handle_pollution_air(self, message):
        location = message.data.get('location')

        self.speak_dialog('pollution.air', data={
            'location': location
        })


def create_skill():
    return AirPollution()

