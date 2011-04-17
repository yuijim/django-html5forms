from django import forms
from django.utils.encoding import force_unicode
from html5forms import widgets
import noconflict
from django.core import validators

wdg_rpl = {
    forms.widgets.DateInput : widgets.DateInputHTML5,
    forms.widgets.DateTimeInput : widgets.DateTimeInputHTML5,
    forms.widgets.TimeInput : widgets.TimeInputHTML5,
}
fld_rpl = {
    forms.fields.URLField : widgets.URLInputHTML5,
    forms.fields.EmailField : widgets.EmailInputHTML5,
    forms.fields.IntegerField : widgets.NumberInputHTML5,
}

class HTML5Form(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(HTML5Form, self).__init__(*args,**kwargs)
        
        for name,field in self.fields.items():
            if field.widget.__class__ in wdg_rpl.keys():
                field.widget = wdg_rpl[field.widget.__class__](field.widget.attrs)
            elif field.widget.__class__ == forms.widgets.TextInput and field.__class__ in fld_rpl.keys():
                field.widget = fld_rpl[field.__class__](field.widget.attrs)
            if field.widget.__class__ == widgets.NumberInputHTML5 or field.widget.__class__ == widgets.RangeInputHTML5:
                vs = [v.__class__ for v in field.validators]
                if validators.MinValueValidator in vs:
                    field.widget.attrs['min'] = str(field.validators[vs.index(validators.MinValueValidator)].limit_value)
                if validators.MaxValueValidator in vs:
                    field.widget.attrs['max'] = str(field.validators[vs.index(validators.MaxValueValidator)].limit_value)
            #add universal HTML5 attributes
            if field.help_text:
                field.widget.attrs['placeholder'] = force_unicode(field.help_text)
            if field.required:
                field.widget.attrs['required'] = 'required'
        
    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row = u'<div>%s',
            row_ender = u'</div>',
            help_text_html = u'<small>%s</small>',
            errors_on_separate_row = False)
        
class HTML5ModelForm(forms.ModelForm,HTML5Form):
    __metaclass__ = noconflict.classmaker()
