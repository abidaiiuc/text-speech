# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

from django.shortcuts import render, redirect
from googletrans import Translator
from gtts import gTTS
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
import pyttsx3
import playsound
import PyPDF2
import io
import os
# from . models import book
#
# def collection(request):
#     book= book.objects.all()
#     return render(request, 'collection.htm', {'book': book})

def home(request):
    return render(request, 'firstapp/one.html')
# def audio(request):
#     return render(request, 'audio/audio.html')
def about(request):
    return render(request, 'firstapp/about.html')
def contact(request):
    return render(request, 'firstapp/contact.html')
def collection(request):
    return render(request, 'firstapp/collection.html')
def audio(request):
    return render(request, 'firstapp/audio.html')
def bookpost(request):

    return render(request, 'firstapp/bookpost.html')
def mybook(request):

    return render(request, 'firstapp/mybook.html')
def fbook(request):

    return render(request, 'firstapp/fbook.html')
def four(request):

    return render(request, 'firstapp/four.html')
def five(request):

    return render(request, 'firstapp/five.html')
def six(request):

    return render(request, 'firstapp/six.html')
def some(request):
    book1 = request.GET['inp1']

    language = request.GET['lan']
    file1 = 'tem.mp3'
    tt = gTTS(text= book1, lang = language, slow = False)
    tt.save(file1)
    playsound.playsound(file1, True)
    os.remove(file1)
    return redirect('/')
def son(request):
    mytext1 = request.GET['inp2']
    language = 'en'
    filename = 'temp.mp3'
    tts = gTTS(text=mytext1, lang=language, slow=False)
    tts.save(filename)
    playsound.playsound(filename, True)
    os.remove(filename)
    return redirect('/')
def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text:', text, 'lang:', lang)
    #connect the translator
    translator=Translator()
    #detect Language
    dt=translator.detect(text)
    dt2=dt.lang
    #translate the text
    translated= translator.translate(text, lang)
    tr=translated.text
    file1 = 'temp.mp3'
    tt = gTTS(text=tr, lang=lang, slow=False)
    tt.save(file1)
    playsound.playsound(file1, True)
    os.remove(file1)
    return render(request, 'firstapp/translated.html', {'translated': tr, 'u_lang': dt2, 't_lang': lang})


def upl(request):
    # if request.method =='POST' and request.FILES['ab']:
        language='nh'
        file2 = 'temp.mp3'
        # pdf=request.FILES.get('ab', None)


        pdf = request.FILES.get('ab').read()
        if pdf:
            pdfReader=PyPDF2.PdfFileReader(io.BytesIO(pdf))
            content=""
            for pagenum in range(pdfReader.numPages):
                pageobj= pdfReader.getPage(pagenum)

                content +=pageobj.extractText()

            # text= content
            ttsy = gTTS(text=content, lang=language, slow=False)
            ttsy.save(file2)
            playsound.playsound(file2, True)
            os.remove(file2)
            return redirect('/')

    # fs = FileSystemStorage()
    # fs.save(uploaded_file.name, uploaded_file)
    # # print(uploaded_file.name)
    # # print(uploaded_file.size)
    # pdfreader=PyPDF2.PdfFileReader(uploaded_file)
    # pages = pdfreader.numPages
    #
    # for num in range(0,pages):
    #     page= pdfreader.getPage(num)
    #     text= page.extractText()
    #     player=pyttsx3.init()
    #     player.say(text)
    #     player.runAndWait()
    # return redirect('/')
    # return render(request, 'firstapp/upload.html')

# def some_view(request):
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# <!--<h2>upload</h2>-->
# <!--<from method ="post" enctype="multipart/form-data">-->
# <!--    {% csrf_token %}-->
# <!--    <input type="file" name="document">-->
# <!--    <button type="submit">submit</button>-->
#
# <!--</from>-->
#
# <!--{% enblock %}-->