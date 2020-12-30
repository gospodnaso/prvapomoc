from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages

from .models import User
from .forms import NameForm, VodForm, GesloForm

def gesla(request):
    if request.method == 'POST':
        ime=request.POST.get('ime')
        vod=request.POST.get('vod')
        if(ime != None and vod != None):
            try:
                u = User(ime=ime, vod=vod, hashh=ime+vod)
                u.save()
            except:
                pass
        else:
            return HttpResponseRedirect('/pp/')
            
        form_geslo = GesloForm(request.POST)
        if form_geslo.is_valid():
            sporocilo = get_messages(request)
            for s in sporocilo:
                pass
            messages.add_message(request, messages.INFO, ime)
            messages.add_message(request, messages.INFO, vod)
            return HttpResponseRedirect('/pp/'+(request.POST.get('geslo')).lower())
        else:
            form_geslo = GesloForm()
            context = {"ime": request.POST.get('ime'), "vod": request.POST.get('vod'), "form_geslo":form_geslo, };
    else:
        context = {}
        return HttpResponseRedirect('/pp/')
    return render(request, 'pp/gesla.html', context)

def index(request):
    if request.method == 'POST':
        form_ime =  NameForm(request.POST)
        form_vod = VodForm(request.POST)
        if form_ime.is_valid() and form_vod.is_valid():
            return HttpResponseRedirect('gesla')
    else:
        form_ime = NameForm()
        form_vod = VodForm()

    return render(request, 'pp/index.html', {'form_ime': form_ime, 'form_vod': form_vod})

def rezultati(request):
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    vodi = ["severni jeleni", "sokoli", "morske kozice", "tigrasti črvi", "snežni leopardi", "lenivci", "pume", "morske kače", "zmaji", "volkodlaki", "veverce", "bogomolke", "sove", "škorpijoni", "pujsi"]

    tocke = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(vodi)):
        usrs = User.objects.filter(vod=vodi[i])
        for usr in usrs:
            usr.sum_tocke = usr.cal_sum()
            usr.save();
            tocke[i] += usr.sum_tocke

    context = {"ime": sporocila[0], "vod": sporocila[1], "t0": tocke[0], "t1": tocke[1], "t2": tocke[2], "t3": tocke[3], "t4": tocke[4], "t5": tocke[5], "t6": tocke[6], "t7": tocke[7], "t8": tocke[8], "t9": tocke[9], "t10": tocke[10], "t11": tocke[11], "t12": tocke[12], "t13": tocke[13], "t14": tocke[14]}
    return render(request, 'pp/rezultati.html', context)

def snezinka(request):
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    context = {"ime": sporocila[0], "vod": sporocila[1]}
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    return render(request, 'pp/snezinka.html', context)

def snezak(request):
    out = 0;
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context={"q1": '', "q2": '', "q3": '', "ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"q1":request.POST.get('q1'), "q2":request.POST.get('q2'), "q3":request.POST.get('q3'), "ime": sporocila[0], "vod": sporocila[1]}
        if(context["q1"] != '' or context["q2"] != '' or context["q3"] != ''):
            if(context["q1"] == "112"):
                context["c1"] = "#99ff99"
                out += 1
            else:
                context["c1"] = "#ff5050"
            if(context["q2"].lower() == "nikoli"):
                context["c2"] = "#99ff99"
                out += 1
            else:
                context["c2"] = "#ff5050"
            if(context["q3"].lower() == "zapustimo" or context["q3"].lower() == "zapuščamo"):
                context["c3"] = "#99ff99"
                out += 1
            else:
                context["c3"] = "#ff5050"
            usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
            if(usr.oddal_kt2 == False):
                usr.oddal_kt2 = True
                usr.tocke_kt2 = out
                usr.save()
    return render(request, 'pp/snezak.html', context)
def jelencek(request):
    out = 0
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
 
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context={"q1": '', "q2": '', "q3": '', "q4": '', "ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"q1":request.POST.get('q1'), "q2":request.POST.get('q2'), "q3":request.POST.get('q3'), "q4":request.POST.get('q4'), "ime": sporocila[0], "vod": sporocila[1]}
        if(context["q1"] != '' or context["q2"] != '' or context["q3"] != '' or context["q4"] != ''):
            if(context["q1"].lower() == "varnost"):
                context["c1"] = "#99ff99"
                out += 1
            else:
                context["c1"] = "#ff5050"
            if(context["q2"].lower() == "sprednje"):
                context["c2"] = "#99ff99"
                out += 1
            else:
                context["c2"] = "#ff5050"
            if(context["q3"].lower() == "ogovorimo"):
                context["c3"] = "#99ff99"
                out += 1
            else:
                context["c3"] = "#ff5050"
            if(context["q4"].lower() == "zavesti"):
                context["c4"] = "#99ff99"
                out += 1
            else:
                context["c4"] = "#ff5050"

            usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
            if(usr.oddal_kt3 == False):
                usr.oddal_kt3 = True
                usr.tocke_kt3 = out
                usr.save()


    return render(request, 'pp/jelencek.html', context)

def sani(request):
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context = {"ime": sporocila[0], "vod": sporocila[1]}
    return render(request, 'pp/sani.html', context)

def lucke(request):
    out = 0
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context={"q1": '', "q2": '', "q3": '', "q4": '', "ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"ime": sporocila[0], "vod": sporocila[1]}
        ting1 = request.POST.get('ting1')
        ting2 = request.POST.get('ting2')
        if(ting1 != '' or ting2 != ''):
            if(ting1 == "zvin"):
                context["c1"] = "#99ff99"
                context["c2"] = "#ffffff"
                context["q1"] = "checked=''"
                context["q2"] = ''
                out += 1
            else:
                context["c1"] = "#ff5050"
                context["c2"] = "#ffffff"
                if(ting1):
                    context["q2"] = "checked=''"
                context["q1"] = ''
            if(ting2 == "imobilizacija"):
                context["c3"] = "#ffffff"
                context["c4"] = "#99ff99"
                context["q3"] = ''
                context["q4"] = "checked=''"
                out += 1
            else:
                context["c3"] = "#ff5050"
                context["c4"] = "#ffffff"
                if(ting2):
                    context["q3"] = "checked=''"
                context["q4"] = ''
            usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
            if(usr.oddal_kt5 == False):
                usr.oddal_kt5 = True
                usr.tocke_kt5 = out
                usr.save()


    return render(request, 'pp/lucke.html', context)
def kraguljcki(request):
    out = 0
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context={"q1": '', "q2": '', "q3": '', "q4": '', "q5": '', "ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"q1":request.POST.get('q1'), "q2":request.POST.get('q2'), "q3":request.POST.get('q3'), "q4":request.POST.get('q4'), "q5":request.POST.get('q5'), "ime": sporocila[0], "vod": sporocila[1]}
        if(context["q1"] != '' or context["q2"] != '' or context["q3"] != '' or context["q4"] != '' or context["q5"]):
            if(context["q1"] == "1"):
                context["c1"] = "#99ff99"
                out += 1
            else:
                context["c1"] = "#ff5050"
            if(context["q2"] == "4"):
                context["c2"] = "#99ff99"
                out += 1
            else:
                context["c2"] = "#ff5050"
            if(context["q3"] == "5"):
                context["c3"] = "#99ff99"
                out += 1
            else:
                context["c3"] = "#ff5050"
            if(context["q4"] == "3"):
                context["c4"] = "#99ff99"
                out += 1
            else:
                context["c4"] = "#ff5050"
            if(context["q5"] == "2"):
                context["c5"] = "#99ff99"
                out += 1
            else:
                context["c5"] = "#ff5050"
            usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
            if(usr.oddal_kt6 == False):
                usr.oddal_kt6 = True
                usr.tocke_kt6 = out
                usr.save()

    return render(request, 'pp/kraguljcki.html', context)
def snezena_kepa(request):
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context = {"ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"ime": sporocila[0], "vod": sporocila[1]}
        context["frage"] = request.POST.get('frage')
        context['c1'] ="#cc66ff"
        usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
        if(usr.oddal_kt7 == False):
                usr.oddal_kt7 = True
                usr.beseda_kt7 = context["frage"]
                usr.save()

    return render(request, 'pp/snezena_kepa.html', context)
def mraz(request):
    out = 0
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context = {"ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"q1": request.POST.get('q1'), "q2": request.POST.get('q2'), "q3": request.POST.get('q3'), "q4": request.POST.get('q4'), "q5": request.POST.get('q5'), "q6": request.POST.get('q6'), "q7": request.POST.get('q7'), "q8": request.POST.get('q8'), "q9": request.POST.get('q9'), "q10": request.POST.get('q10'), "q11": request.POST.get('q11'), "q12": request.POST.get('q12'), "q13": request.POST.get('q13'), "q14": request.POST.get('q14'), "q15": request.POST.get('q15'), "q16": request.POST.get('q16'), "q17": request.POST.get('q17'), "q18": request.POST.get('q18'), "q19": request.POST.get('q19'), "q20": request.POST.get('q20'), "ime": sporocila[0], "vod": sporocila[1]}
        if not context['q1']:
            context['c1'] = "#99ff99"
            out += 1
        else:
            context['c1'] = "#ff5050"
        if not context['q2']:
            context['c2'] = "#99ff99"
            out += 1
        else:
            context['c2'] = "#ff5050"
        if context['q3'] == "on":
            context['c3'] = "#99ff99"
            out += 1
        else:
            context['c3'] = "#ff5050"
        if not context['q4']:
            context['c4'] = "#99ff99"
            out += 1
        else:
            context['c4'] = "#ff5050"
        if not context['q5']:
            context['c5'] = "#99ff99"
            out += 1
        else:
            context['c5'] = "#ff5050"
        if not context['q6']:
            context['c6'] = "#99ff99"
            out += 1
        else:
            context['c6'] = "#ff5050"
        if context['q7'] == "on":
            context['c7'] = "#99ff99"
            out += 1
        else:
            context['c7'] = "#ff5050"
        if not context['q8']:
            context['c8'] = "#99ff99"
            out += 1
        else:
            context['c8'] = "#ff5050"
        if context['q9'] == "on":
            context['c9'] = "#99ff99"
            out += 1
        else:
            context['c9'] = "#ff5050"
        if not context['q10']:
            context['c10'] = "#99ff99"
            out += 1
        else:
            context['c10'] = "#ff5050"
        if context['q11'] == "on":
            context['c11'] = "#99ff99"
            out += 1
        else:
            context['c11'] = "#ff5050"
        if context['q12'] == "on":
            context['c12'] = "#99ff99"
            out += 1
        else:
            context['c12'] = "#ff5050"
        if not context['q13']:
            context['c13'] = "#99ff99"
            out += 1
        else:
            context['c13'] = "#ff5050"
        if context['q14'] == "on":
            context['c14'] = "#99ff99"
            out += 1
        else:
            context['c14'] = "#ff5050"
        if context['q15'] == "on":
            context['c15'] = "#99ff99"
            out += 1
        else:
            context['c15'] = "#ff5050"
        if context['q16'] == "on":
            context['c16'] = "#99ff99"
            out += 1
        else:
            context['c16'] = "#ff5050"
        if not context['q17']:
            context['c17'] = "#99ff99"
            out += 1
        else:
            context['c17'] = "#ff5050"
        if context['q18'] == "on":
            context['c18'] = "#99ff99"
            out += 1
        else:
            context['c18'] = "#ff5050"
        if not context['q19']:
            context['c19'] = "#99ff99"
            out += 1
        else:
            context['c19'] = "#ff5050"
        if context['q20'] == "on":
            context['c20'] = "#99ff99"
            out += 1
        else:
            context['c20'] = "#ff5050"
        usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
        if(usr.oddal_kt8 == False):
            usr.oddal_kt8 = True
            usr.tocke_kt8 = out
            usr.save()

    for ch in context:
        if ('q' in ch): 
            if (context[ch] == "on"):
                context[ch] = "checked=''"
            else:

                context[ch] = ''
    return render(request, 'pp/mraz.html', context)

def sneg(request):
    out = 0
    sporocilo = get_messages(request)
    sporocila = []
    for s in sporocilo:
        sporocila.append(s.message)
    messages.add_message(request, messages.INFO, sporocila[0])
    messages.add_message(request, messages.INFO, sporocila[1])
    context = {"ime": sporocila[0], "vod": sporocila[1]}
    if request.method == 'POST':
        context = {"q1": request.POST.get('q1'), "q2": request.POST.get('q2'), "q3": request.POST.get('q3'), "q4": request.POST.get('q4'), "q5": request.POST.get('q5'), "q6": request.POST.get('q6'), "q7": request.POST.get('q7'), "q8": request.POST.get('q8'), "q9": request.POST.get('q9'), "q10": request.POST.get('q10'), "q11": request.POST.get('q11'), "q12": request.POST.get('q12'), "ime": sporocila[0], "vod": sporocila[1]}
        if context['q1'] == "on":
            context['c1'] = "#99ff99"
            out += 1
        else:
            context['c1'] = "#ff5050"
        if not context['q2']:
            context['c2'] = "#99ff99"
            out += 1
        else:
            context['c2'] = "#ff5050"
        if not context['q3']:
            context['c3'] = "#99ff99"
            out += 1
        else:
            context['c3'] = "#ff5050"
        if context['q4'] == "on":
            context['c4'] = "#99ff99"
            out += 1
        else:
            context['c4'] = "#ff5050"
        if not context['q5']:
            context['c5'] = "#99ff99"
            out += 1
        else:
            context['c5'] = "#ff5050"
        if context['q6'] == "on":
            context['c6'] = "#99ff99"
            out += 1
        else:
            context['c6'] = "#ff5050"
        if context['q7'] == "on":
            context['c7'] = "#99ff99"
            out += 1
        else:
            context['c7'] = "#ff5050"
        if not context['q8']:
            context['c8'] = "#99ff99"
            out += 1
        else:
            context['c8'] = "#ff5050"
        if context['q9'] == "on":
            context['c9'] = "#99ff99"
            out += 1
        else:
            context['c9'] = "#ff5050"
        if not context['q10']:
            context['c10'] = "#99ff99"
            out += 1
        else:
            context['c10'] = "#ff5050"
        if context['q11'] == "on":
            context['c11'] = "#99ff99"
            out += 1
        else:
            context['c11'] = "#ff5050"
        if(not context['q12']):
            context['c12'] = "#99ff99"
            out += 1
        else:
            context['c12'] = "#ff5050"
        usr = User.objects.filter(hashh=(str(sporocila[0]+sporocila[1]))).first()
        if(usr.oddal_kt9 == False):
            usr.oddal_kt9 = True
            usr.tocke_kt9 = out
            usr.save()

    for ch in context:
        if ('q' in ch): 
            if (context[ch] == "on"):
                context[ch] = "checked=''"
            else:
                context[ch] = ''

    return render(request, 'pp/sneg.html', context)
