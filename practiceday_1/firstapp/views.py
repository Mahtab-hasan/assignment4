from django.shortcuts import render,redirect
from .forms import ExamplateForm,MyModelForm,ExampleForm,ExampleForm2,Datetimes,ChangingColor

def contact (request):
    form = ExamplateForm()
    my_model_form = MyModelForm()
    example_form2 = ExampleForm2()
    examplate_form = ExamplateForm()
    datetimes_form = Datetimes()
    changing_color_form = ChangingColor()

    if request.method =='POST':
        if 'examplate_form' in request.POST:
            examplate_form= ExamplateForm(request.POST)
            if examplate_form.is_valid():
                print("examplate_form")
                print(f"came:{examplate_form.cleaned_data['name']}")
                print(f"comment:{examplate_form.cleaned_data['comment']}")
                print(f"agree:{examplate_form.cleaned_data['agree']}")


        elif 'my_model_form' in request.POST:
            my_model_form =MyModelForm(request.POST)
            if my_model_form.is_valid():
                print("my_model_form")
                print(f"name:{my_model_form.cleaned_data['name']}")
                print(f"comment:{my_model_form.cleaned_data['comment']}")
                print(f"agree:{my_model_form.cleaned_data['agree']}")
                print(f"birth_date:{my_model_form.cleaned_data['birth_date']}")

        elif 'example_form2' in request.POST:
            example_form2 =ExampleForm2(request.POST)
            if example_form2.is_valid():
                print("example_form2")
                print(f"agree:{example_form2.cleaned_data['agree']}")


        elif 'datetimes_form' in request.POST:
            datetimes_form= Datetimes(request.POST)
            if datetimes_form.is_valid():
                print("datetimes_form")
                print(f"birth_date:{datetimes_form.cleaned_data['birth_date']}")
            
    

    return render(request,"firstapp/contact.html",{"form": form,"changing_color_form" : changing_color_form})


    