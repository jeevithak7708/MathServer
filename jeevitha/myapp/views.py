from django.shortcuts import render
def calculate_BMI(request):
    bmi=None
    weight=None
    height=None
    if request.method=="POST":
        weight=float(request.POST.get("weight"))
        height=float(request.POST.get("height"))/100
        bmi=weight/(height**2)
        bmi=round(bmi,2)
        print(f"1weight in kg:{weight}, Height in m:{height},bmi: {bmi}")
    return render(request, 'myapp/math.html',{'bmi':bmi})

