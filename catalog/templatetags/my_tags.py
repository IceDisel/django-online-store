from django import template

register = template.Library()


@register.filter()
def my_media(data):
    if data:
        return f'/media/{data}'
    return '#'


@register.filter()
def first_three_words(string):
    words = string.split()
    three_words = " ".join(words[:3])
    return three_words
