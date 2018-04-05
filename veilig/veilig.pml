<?xml version="1.0" encoding="UTF-8" ?>
<Package name="datagovernance" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Voetbalclub" src="Voetbalclub/Voetbalclub.dlg" />
    </Dialogs>
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="startup" src="html/startup.mp4" />
        <File name="roffel" src="roffel.mp3" />
        <File name="hand-in-hand-kort" src="hand-in-hand-kort.ogg" />
        <File name="elephant" src="behavior_1/elephant.ogg" />
        <File name="epicsax" src="behavior_1/epicsax.ogg" />
        <File name="logof" src="html/logof.png" />
        <File name="dia1" src="html/dia1.png" />
        <File name="dia2" src="html/dia2.png" />
        <File name="dia3" src="html/dia3.png" />
        <File name="dia4" src="html/dia4.png" />
    </Resources>
    <Topics>
        <Topic name="Voetbalclub_dun" src="Voetbalclub/Voetbalclub_dun.top" topicName="Voetbalclub" language="nl_NL" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_nl_NL" src="translations/translation_nl_NL.ts" language="nl_NL" />
    </Translations>
</Package>
