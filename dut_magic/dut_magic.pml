<?xml version="1.0" encoding="UTF-8" ?>
<Package name="dun_magic" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="gedachte_lezen" src="gedachte_lezen/gedachte_lezen.dlg" />
    </Dialogs>
    <Resources>
        <File name="Dia1" src="html/Dia1.png" />
        <File name="Dia2" src="html/Dia2.png" />
        <File name="icon" src="icon.png" />
    </Resources>
    <Topics>
        <Topic name="gedachte_lezen_dun" src="gedachte_lezen/gedachte_lezen_dun.top" topicName="gedachte_lezen" language="nl_NL" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_nl_NL" src="translations/translation_nl_NL.ts" language="nl_NL" />
    </Translations>
</Package>
