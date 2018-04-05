import States

def getState(state_name):
    states = { 'DEFAULT': States.Default, 'STATICWAITINGINTERACTION': States.StaticWaitingInteraction, 'DEFAULTINTERACTION': States.DefaultInteraction, 'TABLETINTERACTION': States.TabletInteraction, 'TABLETTYPEINTERACTION': States.TabletTypeInteraction, 'WAITINGINTERACTION': States.WaitingInteraction, 'APPROACHWAITINGINTERACTION': States.ApproachWaitingInteraction }

    return states[ state_name ]

class StateManager:
    def __init__(self,session):
        self.session = session
        self.current_state = None

    def change_state(self, state_name):
        if self.current_state:
            self.current_state.stop()

        self.current_state = getState(state_name)(self.session)
        self.current_state.start()
