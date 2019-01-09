from django.shortcuts import render
from .scrape import get_words_from_website, normalise_results
from .models import Word
from django import forms
from django.core.validators import URLValidator

TOP_WORDS = 100

class SubmitForm(forms.Form):
    target_url = forms.URLField(
        max_length=200, 
            label='Enter a url', 
            initial='http://',
        validators=[URLValidator(schemes=['http', 'https'])]
    )

def process_results(url):
    results = {}
    total_words = get_words_from_website(url, ['p', 'div'])
    results.update(top_100 = total_words.most_common(TOP_WORDS))
    results.update(normalised_top_100 =
    normalise_results(total_words.most_common(TOP_WORDS)))
    return results

def wordcloud(request):
    template = "word_cloud/word_cloud.html"
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'wordcloud_url': form['target_url'].value()
            }
            results = process_results(form['target_url'].value())
            Word.save_word_histogram(results['top_100'])
            context.update(results)
            return render(request, template, context)
        else:
            messages.add_message(request, messages.ERROR, 'Enter a valid url (http or https)')
            return redirect(reverse('wordcloud'))
    else:
        return render(request, template, context={'form': SubmitForm()})

def admin(request):
    template  = "word_cloud/admin.html"
    all_words = Word.fetch_word_histogram()
    content   = dict(histogram = all_words)
    return render(request, template, context=content)
    
