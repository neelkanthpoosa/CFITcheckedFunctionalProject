from django import forms
from forum.models import Post,Item,SellerStatus


class SellerForm(forms.ModelForm):
	 post=forms.CharField(max_length=255,widget=forms.TextInput(
	 attrs={
	 'class':'form-control',
	 'placeholder':'Want to sell or donate stuff? Wait no more.',
	 }
	 ))
	 class Meta:
		 model=Post
		 fields=('post',
				'image',
				)


class ItemForm(forms.ModelForm):
    CHOICES=(
	('Drafter','Drafter'),
	('Apron','Apron'),
    ('Calculator','Calculator'),
    ('Power Bank','Power Bank'),
    ('Book','Book'),
	)
    class Meta:
        model = Item
        fields = (
		'item',
		)


        widgets = {
    				'region': forms.Select(attrs={'class':'bootstrap-select'}),
					}




class StatusForm(forms.ModelForm):
	CHOICES=(
	('Available','Available'),
	('Nope','Not Available'),
	)



	class Meta:
		model = SellerStatus
		fields = (
		'status',
		)


		widgets = {
    				'region': forms.Select(attrs={'class':'bootstrap-select'}),
					}
