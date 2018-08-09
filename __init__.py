from mycroft import MycroftSkill, intent_file_handler


class TicketStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.ticket.intent')
    def handle_status_ticket(self, message):
        self.speak_dialog('status.ticket')


def create_skill():
    return TicketStatus()

