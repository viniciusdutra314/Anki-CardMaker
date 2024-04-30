def html_replacing(cardtype: str,config:dict) -> list[str]:
    from os.path import join as path_join
    htmls=[]
    for side in ["Front.html","Back.html"]:
        with open(path_join(config["cardtypes_dir"],cardtype,side),"r") as file:
            html = file.read()
        for key,value in config.items():
            html=html.replace(key,value)   
        htmls.append(html)
    return {"Front":htmls[0],"Back":htmls[1]}

def sanitize_input(mother_tongue :str,target_lang:str,template_name:str) -> tuple[str,str,str]:
    import langcodes
    mother_tongue=mother_tongue.strip().replace(" ","_")
    target_lang=target_lang.strip().replace(" ","_")
    template_name=template_name.replace("_"," ")
    assert len(mother_tongue)==5 , "Your language is not on the 4 character format"
    assert langcodes.get(mother_tongue).is_valid() , "Your language langcode is not a valid code"
    assert len(target_lang)==5 , "Your translation language is not on the 4 character format"
    assert langcodes.get(target_lang).is_valid() , "Your translation language langcode is not a valid code"
    return mother_tongue,target_lang,template_name


def generate_dictionary_link(dictionary:str,target_lang_fullname:str,
                                your_lang_fullname:str)-> str:
    if dictionary=="reverso":
        dictionary_link=f"https://context.reverso.net/translation/"
    if dictionary=="cambridge":
        dictionary_link="https://dictionary.cambridge.org/dictionary/"

    dictionary_link+=f"{target_lang_fullname}-{your_lang_fullname}/"
    return dictionary_link
def create_dummy_deck(mother_tongue :str ,target_lang :str ,
        highlight_color :str,cardtypes_bools:list[bool], cardtypes_dir,
        template_name:str,dictionary, additional_voices:[str]=[]):
    import langcodes
    import genanki
    import random
    sanitize_input(mother_tongue,target_lang,template_name)

    LINUX_SUPPORT="AwesomeTTS"
    CSS=""".card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
            }
        """
    cardtypes=[]

    if cardtypes_bools[0]: cardtypes.append("Passive")
    if cardtypes_bools[1]: cardtypes.append("Active")
    if cardtypes_bools[2]: cardtypes.append("Writing")
    assert len(cardtypes)!=0 , "You have not selected any cardtype"

    your_lang_fullname=langcodes.get(mother_tongue).describe()["language"].lower()
    your_lang=langcodes.get(mother_tongue).to_tag().replace("-","_")
    target_lang_fullname=langcodes.get(target_lang).describe()["language"].lower()
    target_lang=langcodes.get(target_lang).to_tag().replace("-","_")
    
    FIELDS=(f"🔤 Phrase ({target_lang})",f"🔄 Translated phrase or word ({your_lang})",
                f"❓ Unknown word ({target_lang})",f"🗣️ Pronunciation")

    if additional_voices: LINUX_SUPPORT=","+LINUX_SUPPORT
    your_voices=additional_voices+LINUX_SUPPORT

    dictionary_link=generate_dictionary_link(dictionary,
                target_lang_fullname,your_lang_fullname)
    
    config={"your_voices":your_voices,"your_lang":your_lang,
            "target_lang":target_lang,"highlight_color":highlight_color,
            "dictionary_link":dictionary_link,"cardtypes_dir":cardtypes_dir}
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
        f"{template_name} (test the audio)"
    )

    dummy_note=genanki.Note(
        model=note_template,
        fields=["This is just an example to test the voices",
        "something that is typical of the group of things that you are talking about",
        "example"," /ɪɡˈzæm·pəl/"]
    )
    dummy_deck.add_note(dummy_note)
    genanki.Package(dummy_deck).write_to_file(f"{template_name}.apkg")


if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mother_tongue', type=str,required=True)
    parser.add_argument('--target_lang',type=str,required=True)
    parser.add_argument("--cardtypes_dir",type=str,required=True)
    parser.add_argument("--template_name",type=str,required=True)
    parser.add_argument("--highlight_color",type=str,default="red")
    parser.add_argument("--cardtypes_bools",type=str)
    parser.add_argument("--dictionary",type=str,default="reverso")
    parser.add_argument("--additional_voices",type=str,default="")
    args = parser.parse_args()
    cardtypes_bools=[x=="True" for x in args.cardtypes_bools.split()] 
    create_dummy_deck(args.mother_tongue,args.target_lang,args.highlight_color,
                    cardtypes_bools,args.cardtypes_dir,args.template_name,
                    args.dictionary,args.additional_voices)