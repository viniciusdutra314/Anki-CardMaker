def html_replacing(cardtype: str,config:dict) -> list[str]:
    from os.path import join as path_join
    htmls=[]
    for side in ["front.html","back.html"]:
        with open(path_join("directory",cardtype,side),"r") as file:
            html = file.read()
        for key,value in config.items():
            html=html.replace(key,value)   
        htmls.append(html)
    return {"front":htmls[0],"back":htmls[1]}


def main(your_lang :str ,target_lang :str ,
        highlight_color :str,cardtypes:list[str],
        additional_voices:list[str]=[]):
    import langcodes
    FIELDS=("🔤 Phrase","🔄 Translated phrase or word",
                "❓ Unknown word","🗣️ Pronunciation")
    LINUX_SUPPORT="AwesomeTTS"
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
    cardtype_templates={
            cardtype:html_replacing(cardtype,config) for cardtype in cardtypes}
if __name__=="__main__":
    main("en_US","it_IT","green",["Passive","Active"])