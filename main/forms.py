from django import forms

# email form

class ContactUsForm(forms.Form):
	name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(
			attrs={
				'type' : 'text',
				'placeholder' : 'اسمك',
				'id' : 'name',
				'class' : 'form-control'
			}
		)
	)
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'type' : 'email',
				'placeholder' : 'الايميل الخاص بك',
				'id' : 'email',
				'class' : 'form-control'
			}
		)
	)


	subject = forms.CharField(
		max_length=100,
		widget=forms.TextInput(
			attrs={
				'type' : 'text',
				'placeholder' : 'العنوان',
				'id' : 'subject',
				'class' : 'form-control'
			}
		)
	)
	message = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
				'rows' : '6',
				'placeholder' : 'الرسالة أو السؤال',
				'id' : 'message',
				'class' : 'form-control'
			}
		)
	)

	def __str__(self):
		return self.email

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if not "@" in email:
			raise form.validationError("This is not a valid email!")
