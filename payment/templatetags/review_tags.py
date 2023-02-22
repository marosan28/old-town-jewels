from django import template

register = template.Library()

@register.filter(name='average_review')
def average_review(reviews):
    if reviews:
        reviews_count = reviews.count()
        reviews_sum = sum([review.rating for review in reviews])
        return round(reviews_sum / reviews_count, 1)
    else:
        return 0
