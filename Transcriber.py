from pytube import YouTube
import re

ytlink = input("Youtube Link:")
yt = YouTube(ytlink)
caption = yt.captions.get_by_language_code('en')
justTextCaption = re.sub("[<].*?[>]", " ", caption.generate_srt_captions())
#Because regex is easy to write and impossible to read sometimes:
#- Match a single character "<" ( [<] )
#- Match any character ( . ), 0-infinite times ( * ), lazily, AKA NOT GETTING EVERYTHING ( ? )
#- Match a single character ">" ( [>] )

#noTag Captions
print(justTextCaption) #youtube captions

#save text captions to file, for easier manipulation, since terminal isn't very user friendly
with open("Output.txt", "w") as text_file:
    text_file.write(justTextCaption)
