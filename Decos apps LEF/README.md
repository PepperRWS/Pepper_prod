# Decos - RWS Pepper Project


1. Set the language on Pepper to Dutch.  
2. Install the services `pepper_navigation` and `pepper_interactionstates`
3. Install the `decos_applauncher` service. Take a look at the code. There is a config file that you can change to set the logos of every app and which app it should autostart. By default it starts the Foyer app.
3. Install the applications:  `pepper_foyerapp`, `pepper_goodbyeapp`, `pepper_welcomeApp` and `pepper_leanquiz`

Tip: sometimes the applications don't autostart after you install them. Quick fix is to restart pepper after step 3.

## Applications

Summary of all of the developed applications.   
You can find more detailed information inside each repository.   
Several services were also implemented, like: decos_navigation and decos_interactionstates. These need to be installed on pepper before you install the apps.    
decos_applauncher is also another service that was developed. Install this one if you wanna have an app menu showup after Pepper boots. If you do not install it no app will start by default.

### pepper_rws
This is the main foyer app. It uses navigation to navigate through the foyer.
It also has a simple chitchat implemented as well as a video and several slide presentations for some of the products at RWS

### pepper_goodbyeapp
This is the app the retrieves and stores user ratings. It is being used to ask for session feedback.
This app also comes with a website to retrieve the ratings. In order to access this you have to be connected to the same wifi network as pepper and then go to  http://pepper.local/apps/decos-goodbyeapp/ratings.html

## pepper_welcomeApp
App to put on pepper at the main reception. It asks some simple questions to the visitors.

## pepper_leanquiz
Lean quiz app. Simple questions regarding Kr8
