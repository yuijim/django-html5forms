from django import template
register = template.Library()

@register.inclusion_tag('html5forms/as_br.html')
def as_br(form,br_after_labels=False):
    u"""Tag that creates form with formatting based on <br />s."""
    
    return {
        'form': form,
        'br_after_labels': br_after_labels,
    } 

@register.inclusion_tag('html5forms/as_div_complex.html')
def as_div_complex(form):
    u"""Tag that creates form with formatting based on complex structure of <div>s, <fieldset>s and so."""
    
    return {
        'form': form
    }
    
@register.inclusion_tag('html5forms/as_inlines.html')
def as_inlines(formset):
    u"""Tag that creates inlines table from formset"""
    
    return {
        'formset': formset
    }