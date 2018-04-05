<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Funny-App" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Praatmetme" src="Praatmetme/Praatmetme.dlg" />
    </Dialogs>
    <Resources>
        <File name="elephant" src="behavior_1/elephant.ogg" />
        <File name="epicsax" src="behavior_1/epicsax.ogg" />
        <File name="hand-in-hand-kort" src="hand-in-hand-kort.ogg" />
    </Resources>
    <Topics>
        <Topic name="Praatmetme_dun" src="Praatmetme/Praatmetme_dun.top" topicName="Praatmetme" language="nl_NL" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_nl_NL" src="translations/translation_nl_NL.ts" language="nl_NL" />
    </Translations>
</Package>
