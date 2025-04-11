import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView

from config import settings
from portfolio.forms import ContactForm
from portfolio.models import Post
from portfolio.signals import post_viewed


def home(request):
    return render(request, 'home/home.html')


def download_file(request):
    # Define the path to the file
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'myfile.txt')
    if os.path.exists(file_path):
        # Serve the file as a downloadable response
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='myfile.txt')
        return response
    else:
        # Handle case where the file doesn't exist
        return HttpResponse("File not found.", status=404)



def about(request):
    return render(request, 'home/home.html')


def skills(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact was sent successfully!")
            return redirect('home')  # Redirect to clear the form
        else:
            print(form.errors)  # Debug: Check errors in server console
            messages.error(request, "Something went wrong. Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'home/home.html', {"form": form})


class PostsView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/posts.html', {'page_obj': page_obj, "posts": posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        session_key = f'viewed_post_{self.object.slug}'
        if not request.session.get(session_key, False):
            post_viewed.send(sender='portfolio.Post', instance=self.object)
            request.session[session_key] = True
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
