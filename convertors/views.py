from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm, TypeFileForm
import csv, io, json


# Create your views here.
def index(request):
    return render(request, 'convertors/index.html')


def upload_file(request):
    # import ipdb; ipdb.set_trace()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        upload_file = request.FILES['file']
        file = io.StringIO(upload_file.read().decode())
        # print(file.read())
        reader = csv.DictReader(file)
        json_data = json.dumps(list(reader))
        print(json_data)

        return render(request, 'json.html', {'json_data': json_data})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})


def type_text(request):
    if request.method == "POST":
        x = request.POST
        text = x['text']
        print(text)
        file = io.StringIO(text)
        reader = csv.DictReader(file)
        json_data = json.dumps(list(reader))
        print(json_data)

        return render(request, 'json.html', {'json_data': json_data})
    else:
        form = TypeFileForm()
        return render(request, 'type.html', {'form': form})
