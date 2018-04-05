# Running in dev mode

Before running in development mode, please make sure that no instance of this service is running on Pepper. If there is one, please remove it.

## Start the service

```
python decos_interactionstates.py --qi-url <ip-of-pepper>
```
## Include the service

```python
self.int_states = self.session.service('DecosInteractionStates')
```

## Available functions

```
DecosInteractionStates::change_state(string state_name)
```

Where `state_name` is:   

1. **DEFAULT**: Default autonomous life state.   
2. **DEFAULTINTERACTION**: Default interaction state. The head will look forwards without any tracking activities   
3. **WAITINGINTERACTION**: This state should be used when Pepper is waiting for human contact.   
4. **TABLETINTERACTION**: when the user is asked to interact with the tablet. The hands can move freely because the user is not typing on the tablet.   
5. **TABLETTYPEINTERACTION**: when the user is asked to type or interact with the tablet. The hand movement is restricted   
6. **APPROACHWAITINGINTERACTION**: When Pepper is waiting and detects a person he will approach him. after the interaction has finished (and this states start again) Pepper return backward.

| State Name | Head Movement | Body Movement | Volume | Speech Sensitivity | Stimulus |
|------------|---------------|---------------|--------|--------------------|----------|
| DEFAULT    | On and tracking| On and tracking | - | - |People, Sound and Movement on|
| DEFAULTINTERACTION| Forwards Up | Only arms | -     | -                  | All off  |
| WAITINGINTERACTION | On and tracking | On and tracking | - | -           | All on   |
| STATICWAITINGINTERACTION | On and tracking | Stopped   | - | -           | All on   |
| TABLETINTERACTION | Forwards Up | Only arms | -     | -                  | All off  |
| TABLETTYPEINTERACTION | Forwards Up | Stopped   | - | -                  | All off  |
| APPROACHWAITINGINTERACTION | On and tracking | Stopped   | - | -                  | All on  |

# Running in production

Make sure that the service is in autorun and install it to the robot.
