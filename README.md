


# Installation
The most reliable way of installing a template on anki is importing a deck with cards created using the template, in order to do that the we gonna run a Google Colab script that will generate the deck  for us, please click this [link](https://colab.research.google.com/github/viniciusdutra314/Anki-CardMaker/blob/main/AnkiCardMaker.ipynb#scrollTo=4PlW-rYmGAWG) and follow the instructions
<a href="https://colab.research.google.com/github/viniciusdutra314/Anki-CardMaker/blob/main/AnkiCardMaker.ipynb#scrollTo=4PlW-rYmGAWG">
<img src="images/colab.jpeg" alt="google_colab_logo" width=300>
</a>

# Main features

- **Cross-platform** : All the magic is done with anki templates which is a native feature for Anki on Windows/Mac/Linux and on the mobile versions of Android/iOS

- **Generate multiple cardtypes at once**:
Create one note and generate up to *3* different cards! Flash cards for passive/active vocabulary and writing skills with automatic correction


- **On the fly** audios: Audios are generated dynamically, without the need of storaging hundreads of megabytes of audios and support for different voices, accents and speeds

- **Dictionary Search**: Words/phrases can be study on more deepth inside the cards themselves with a quick search on a custom dictionary (examples: Reverso, Cambridge Dictionary)





(if you're a developer you can run the create_template.py by yourself)

# Voices and audio generation:
As explained on the [Main Features](#main-features) section, the audios are generated locally using the TTS (Text-To-Speech) of your device, you **need to have installed the TTS of the language that you will generate audios**. 

The next subsections will be a quick tutorial how to install TTS for an arbitray language on Android,Windows, and Linux, the some ideas are applicable to Mac/iOS,.
### Android:
The following tutorial was made on the version 12 of android, but should be applicable to other versions.



### Windows:

### Linux:
Unfortunately, Linux doesn't come with TTS by default like the other operational systems, one easy solution is to install the anki-addon [AwesomeTTS](https://ankiweb.net/shared/info/1436550454), it will generate audios using online services like Google Translate, you need to create a preset selecting a service/voice for your target language and this is it.

The audios will continue to be generated on the fly and other voices will be avaiable on your different devices