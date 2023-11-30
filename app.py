import pyttsx3, PyPDF2

#import the PDF you want to conver to speech

pdfreader = PyPDF2.PdfReader(open('Hello.pdf', 'rb'))

# Initialize the Text to speach reader

speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n',' ')
    print(clean_text)

speaker.save_to_file(clean_text, "Texttospeech.mp3") 
speaker.runAndWait()
speaker.say("The File is saved, Thank You")
speaker.stop()