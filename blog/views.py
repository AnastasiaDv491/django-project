from django.shortcuts import render

# Create a request for a template
def post_list(request):
    return render(request, 'blog/post_list.html', {})