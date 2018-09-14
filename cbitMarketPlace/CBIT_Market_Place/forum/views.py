from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from forum.forms import SellerForm,ItemForm,StatusForm
from forum.models import Post,Item,SellerStatus
from django.utils import timezone
from django.contrib.auth.decorators import login_required


class ForumView(TemplateView):
	template_name='forum/home.html'

	def get(self,request):
		form=SellerForm()
		posts=Post.objects.all().order_by('-created')
		#print(posts)
		args={'form':form,'posts':posts}
		return render(request,self.template_name,args)


	def post(self,request):
		form =  SellerForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']

			image=form.cleaned_data['post']
			form=SellerForm()
			return redirect('forum:forum')
		args={'form':form,'text':text,'image':image}
		return render(request,self.template_name,args)




def Status(request):
	item = Item.objects.all().order_by('-created_date')
	stat = SellerStatus.objects.all().order_by('-created_date')
	if request.method == 'POST':
		form =  ItemForm(request.POST)
		form1 =  StatusForm(request.POST)

		if form.is_valid() and form1.is_valid():
			post = form.save(commit=False)
			post1 = form1.save(commit=False)
			post.user = request.user
			post1.user = request.user
			post.created_date = timezone.now()
			post1.created_date = timezone.now()
			post.save()
			post1.save()
			form=ItemForm()
			form1=StatusForm()
			return redirect('forum:status')
	else:
		form = ItemForm()
		form1= StatusForm()

	return render(request,'forum/status.html',{'form':form,'form1':form1,'item':item,'stat':stat})
