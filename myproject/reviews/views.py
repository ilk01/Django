from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from .models import Product, Review

def product_list(request):
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products_list, 9)  # Показывать по 9 продуктов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "reviews/product_list.html", {"page_obj": page_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by("-created_at")
    return render(request, "reviews/product_detail.html", {"product": product, "reviews": reviews})

@login_required
def add_review(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        text = request.POST.get("text")
        rating = request.POST.get("rating")
        Review.objects.create(
            product=product,
            user=request.user,
            text=text,
            rating=rating
        )
    return redirect("product_detail", product_id=product_id)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if review.user != request.user:
        return HttpResponseForbidden("You can only edit your own reviews.")
    
    if request.method == "POST":
        review.text = request.POST.get("text")
        review.rating = request.POST.get("rating")
        review.save()
    
    return redirect("product_detail", product_id=review.product.id)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product_id = review.product.id
    if review.user != request.user:
        return HttpResponseForbidden("You can only delete your own reviews.")
    
    if request.method == "POST":
        review.delete()
    
    return redirect("product_detail", product_id=product_id)
