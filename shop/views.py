from django.shortcuts import render, get_object_or_404, redirect, reverse
from cart.forms import CartAddProductForm
from .models import Category, Product, Review
from .forms import NewsletterForm, ReviewForm
from django.core.mail import EmailMessage
from django.contrib import messages
from users.models import SubscribedUsers
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile


def error_404(request, exception):
    return render(request, 'shop/404.html', status=404)


def home(request):
    category_slug = None
    products = product_list(request, category_slug)
    return render(request, 'shop/base.html', {'product_list': products})


def index(request):
    products = Product.objects.all()
    product_list = products[:3]  
    context = {
        'product_list': product_list,
    }
    return render(request, 'shop/index.html', context)


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

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    reviews = product.reviews.filter(active=True)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review was submitted successfully!')
            return redirect('shop:product_detail', id=id, slug=slug)
    else:
        if request.user.is_authenticated:
            review_form = ReviewForm()
        else:
            review_form = ReviewForm()

    rating_stars_list = []
    for review in reviews:
        rating_stars = review_form.fields['rating'].widget.render('rating', review.rating)
        rating_stars_list.append(rating_stars)

    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'reviews': reviews,
                                                        'review_form': review_form,
                                                        'rating_stars_list': rating_stars_list})


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


@login_required
@require_POST
def review_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.rating = int(request.POST['rating'])
            review.save()
            messages.success(request, 'Your review was submitted successfully!')
            return redirect('shop:product_detail', id=id, slug=slug)
    else:
        form = ReviewForm()
    reviews = product.reviews.filter(active=True)
    rating_stars_list = []
    for review in reviews:
        rating_stars = form.fields['rating'].widget.render('rating', review.rating)
        rating_stars_list.append(rating_stars)

    context = {'product': product, 'form': form, 'reviews': reviews, 'rating_stars_list': rating_stars_list}
    return render(request, 'shop/product/detail.html', context)

@login_required
def edit_review(request, product_id, product_slug, review_id):
    product = get_object_or_404(Product, id=product_id)
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review was updated successfully!')
            return redirect('shop:product_detail', id=product_id, slug=product_slug)
    else:
        form = ReviewForm(instance=review, initial={'body': request.POST.get('body', '')})

    context = {'form': form, 'product': product, 'review': review}
    return render(request, 'shop/edit_review.html', context)

@login_required
def delete_review(request, product_id, product_slug, review_id):
    product = get_object_or_404(Product, id=product_id)
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, 'Your review was deleted successfully!')
    return redirect('shop:product_detail', id=product_id, slug=product_slug)
















