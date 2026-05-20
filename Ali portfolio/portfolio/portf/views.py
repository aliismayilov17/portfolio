


# views.py

from django.shortcuts import render, redirect
from .models import Comment, PortfolioFile


def home(request):

    if request.method == "POST":

        if request.user.is_authenticated:

            text = request.POST.get("comment")

            Comment.objects.create(
                user=request.user,
                text=text
            )

            return redirect("/")

    comments = Comment.objects.all().order_by("-created_at")
    files = PortfolioFile.objects.all().order_by("-uploaded_at")

    return render(request, "portfolio.html", {
        "comments": comments,
        "files": files
    })