def html_replacing(cardtype: str,config:dict) -> list[str]:
    from os.path import join as path_join
    htmls=[]
    for side in ["Front.html","Back.html"]:
        with open(path_join("directory",cardtype,side),"r") as file:
            html = file.read()
        for key,value in config.items():
            html=html.replace(key,value)   
        htmls.append(html)
    return {"Front":htmls[0],"Back":htmls[1]}


def main(your_lang :str ,target_lang :str ,
        highlight_color :str,cardtypes:list[str],
        template_name:str, additional_voices:list[str]=[]):
    import langcodes
    import genanki
    import random
    FIELDS=("🔤 Phrase","🔄 Translated phrase or word",
                "❓ Unknown word","🗣️ Pronunciation")
    LINUX_SUPPORT="AwesomeTTS"
    CSS=""".card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
            }
        """

    #checking
    if not langcodes.get(your_lang).is_valid():
        print(f"You typed the code-lang of your language incorrectly")
        return 1
    if not langcodes.get(target_lang).is_valid():
        print(f"You typed the code-lang of your target language incorrectly")
        return 1
    your_lang_fullname=langcodes.get(your_lang).describe()["language"].lower()
    target_lang_fullname=langcodes.get(target_lang).describe()["language"].lower()


    if additional_voices: LINUX_SUPPORT=","+LINUX_SUPPORT
    your_voices=",".join(additional_voices)+LINUX_SUPPORT
    dictionary_link=f"https://context.reverso.net/translation/"
    dictionary_link+=f"{target_lang_fullname}-{your_lang_fullname}/"
    config={"your_voices":your_voices,"your_lang":your_lang,
            "target_lang":target_lang,"highlight_color":highlight_color,
            "dictionary_link":dictionary_link}
    cardtype_htmls={
            cardtype:html_replacing(cardtype,config) for cardtype in cardtypes}
    cardtypes_templates=[]
    for cardtype in cardtype_htmls:
        cardtypes_templates.append(
            {"name":cardtype,
            "qfmt":cardtype_htmls[cardtype]["Front"],
            "afmt":cardtype_htmls[cardtype]["Back"],
            })
    note_template=genanki.Model(
        random.randrange(1<<30,1<<31),
        template_name,
        fields=[
            {"name":FIELDS[0]},{"name":FIELDS[1]},
            {"name":FIELDS[2]},{"name":FIELDS[3]}
        ],
        templates=cardtypes_templates,
        css=CSS
    )
    dummy_deck=genanki.Deck(
        random.randrange(1<<30,1<<31),
        "Dummy Deck (just to import)"
    )
    dummy_note=genanki.Note(
        model=note_template,
        fields=["This is a dummy phrase",
        "an artificial substitute looking like the real thing",
        "dummy","/ˈdʌm·i/"]
    )
    dummy_deck.add_note(dummy_note)
    genanki.Package(dummy_deck).write_to_file("exemplo.apkg")
if __name__=="__main__":
    main("en_US","it_IT","green",["Passive","Active"],"awesome-features")