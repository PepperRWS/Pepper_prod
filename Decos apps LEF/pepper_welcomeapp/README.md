# README Welcome app #

## Intro
The welcome app is designed to welcome visitors and ask them if they have an appointment, a session or if they want to go to CLC. Visitors can choose either one of these three options and after choosing for an appointment or a session it goes to a menu with further information about LEF, such as the Wifi code or where the wardrobe is. If they choose for CLC it will explain where it is and return back to the main menu. The main file for the flow can be found in rws\_welcomeApp.json.

Pepper uses webpages to show information on the screen. These webpages can be found in the html folder. The welcome app uses two modules to show all the information on the screen, namely:

1. Menu: to show the question with buttons displaying the answer
2. Display\_Data: to show a webpage with only images and text (no buttons)
3. First\_HR\_int: It is the first screen the users will see with a logo and a button to press.

## Service Dependecies
Before running this project, please make sure that you have the following service installed on Pepper!  

1.  DecosInteractionStates

## Suggested Services

1. DecosAppLauncher
