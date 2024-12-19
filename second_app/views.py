# from django.shortcuts import render,redirect
# from . import forms
# # Create your views here.
# from django.contrib import messages
# def registerForm(request):
#     if request.method=="POST":
#         reg_form=forms.Registratin_form(request.POST)
#         if reg_form.is_valid():
#             reg_form.save(commit=True)
#             messages.success(request,"Registered Successsfully!")
#             return redirect('homepage')
#     else:
#         reg_form=forms.Registratin_form()
#     return render(request,'register.html',{'form':reg_form})

from django.shortcuts import render
from . import forms
from . import models
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def search_products(request):
    query = request.GET.get('q', '')  # Retrieve the search query from the request
    results = models.Product.objects.filter(name__icontains=query) if query else models.Product.objects.none()
    return render(request, 'search_results.html', {'query': query, 'results': results})
    
def registerForm(request):
    if request.method=="POST":
        reg_form=forms.Registratin_form(request.POST)
        if reg_form.is_valid():
            reg_form.save(commit=True)
            messages.success(request,"Registered Successsfully!")
            return redirect('homepage')
    else:
        reg_form=forms.Registratin_form()
    return render(request,'register.html',{'form':reg_form})

class PostDetails(DetailView):
    model=models.Product
    pk_url_kwarg = 'id'
    template_name='blog_detail.html'
    context_object_name='car'

    def post(self,request,*args,**kwargs):
        comment_form=forms.ComentForm(data=request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product=post
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.ComentForm()

        context['comments']=comments
        context['comments_form']=comment_form
        return context
@login_required()
def buy_now(request, id):
    product = get_object_or_404(models.Product, id=id)

    if product.Quantity > 0:
        product.Quantity -= 1
        product.save()
        models.Purchase.objects.create(user=request.user, product=product)

        messages.success(request, "product purchased successfully!")
        return redirect('post_detail', id=id)
    else:
        messages.error(request, "Sorry, this product is out of stock.")
        return redirect('post_detail', id=id)


@login_required()  
def change_dat(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully")
                return redirect('profile')
        else:
            form = forms.change_data(instance=request.user)

        return render(request, './edit_profile.html', {'form': form})
    else:
        return redirect('signup')

@method_decorator(login_required,name="dispatch")
class ProfileVie(ListView):
    model=models.Purchase
    template_name="profiles.html"
    context_object_name='purchases'

    def get_queryset(self):
        return models.Purchase.objects.filter(user=self.request.user)
    


    