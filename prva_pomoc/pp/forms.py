from django import forms

class NameForm(forms.Form):
    ime = forms.CharField(label='ime', max_length=100)

vodi = [("severni jeleni", "severni jeleni"), ("sokoli", "sokoli"), ("morske kozice", "morske kozice"), ("tigrasti črvi", "tigrasti črvi"), ("snežni leopardi", "snežni leopardi"), ("lenivci", "lenivci"), ("pume", "pume"), ("morske kače", "morske kače"), ("zmaji", "zmaji"), ("volkodlaki", "volkodlaki"), ("veverce", "veverce"), ("bogomolke", "bogomolke"), ("sove", "sove"), ("škorpijoni", "škorpijoni"), ("pujsi", "pujsi"), ("dinozavri", "dinozavri")]

class VodForm(forms.Form):
    vod = forms.ChoiceField(label="vod", choices = vodi)

class GesloForm(forms.Form):
    geslo = forms.CharField(label='geslo', max_length=100)
