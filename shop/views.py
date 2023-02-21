from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import CartAddProductForm
from .models import Category, Product, Review
from .forms import NewsletterForm, ReviewForm
from django.core.mail import EmailMessage
from django.contrib import messages
from users.models import SubscribedUsers
from django.views.decorators.http import require_POST


def home(request):
    category_slug = None
    products = product_list(request, category_slug)
    return render(request, 'shop/base.html', {'product_list': products})


def index(request):
    """The ladning page"""
    return render(request, 'shop/index.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    reviews = product.reviews.filter(active=True)
    review_form = ReviewForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'reviews': reviews,
                                                        'review_form': review_form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(
                subject, email_message, f"Online Jewels <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join(
        [active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='shop/newsletter.html', context={'form': form})


def category_carousel(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_carousel.html', context)


@require_POST
def review_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    review = None
    # A review was submitted
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # Create a Review object without saving it to the database
            review = form.save(commit=False)
            # Assign the product to the review
            review.product = product
            # Save the review to the database
            review.save()
            # Redirect to the product detail page
            return redirect('shop:product_detail', id=id, slug=slug)
    else:
        form = ReviewForm()
    return render(request, 'shop/review_form.html',
                           {'product': product,
                            'form': form,
                            'review': review})
