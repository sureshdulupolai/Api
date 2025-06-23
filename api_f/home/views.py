from rest_framework import generics
from .models import ProfileModel
from .serializers import ProfileSerializer
from django.shortcuts import render, HttpResponse

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class ProfileListAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

class ProfileDeleteAPIView(generics.DestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


# ---------------------------------------------------------------------------------------------------------------------------
# view base data save in api model
def profile_form_page(request):
    if request.method == 'POST':

        # data getting
        varUserModelNo = request.POST.get('userModelNo'); varUserGmail = request.POST.get('userGmail'); varProfileName = request.POST.get('profileName')

        # data printing
        print("Form Data:", varUserModelNo, varUserGmail, varProfileName)

        # creating s object to save in model
        # API ke tarike se save karte hai using serializer
        data = { 'userModelNo': varUserModelNo, 'userGmail': varUserGmail, 'profileName': varProfileName }

        # send to serializer.py -> serializer
        # to check proper model data save
        serializer = ProfileSerializer(data=data)

        # if no error
        if serializer.is_valid():
            
            # save in api model
            serializer.save()
            return HttpResponse('SuccessFully Save!')
        
        else:
            return HttpResponse('Error Here!!!')

    return render(request, 'profile.html')