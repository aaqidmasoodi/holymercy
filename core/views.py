from django.shortcuts import render


def home_view(request):
    return render(request, "core/index.html")


def gallery_view(request):
    return render(request, "core/gallery.html")


def premium_features_view(request):
    return render(request, "core/premium_features.html")


def books_view(request):
    return render(request, "core/books.html")
