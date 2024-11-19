from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse,HttpResponseRedirect
import csv
from io import TextIOWrapper
from Location.models import CityModel
from Location.models import StatesModel
# Create your views here.
def home(request):
    return render(request,"home.html")


def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

# def qr(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input_text')

        
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(input_text)
#         qr.make(fit=True)

#         img = qr.make_image(fill_color="black", back_color="white")

        
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         buffer.seek(0)
#         return HttpResponse(buffer, content_type="image/png")

#     return render(request, "QR.html")




def upload_csv(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('csv_file')  # Get the uploaded file
        if not uploaded_file:
            return HttpResponse("No file uploaded.", status=400)

        try:
            # Read the file data using TextIOWrapper for text-based CSV files
            file_data = TextIOWrapper(uploaded_file.file, encoding='utf-8')
            csv_reader = csv.reader(file_data)

            # Skip the header row
            next(csv_reader, None)

            for row in csv_reader:
                try:
                    cityname = row[0].strip() 
                    state_id = int(row[1].strip())

                    stateobj = StatesModel.objects.get(state_id = state_id)

                    if not CityModel.objects.filter(cityname=cityname, state_id=stateobj).exists():
                        obj = CityModel()
                        obj.cityname = cityname
                        obj.state_id = stateobj
                        obj.save()
                    else:
                        print(f"Duplicate entry found: {cityname} in state {state_id}. Skipping this row.")

                except Exception as e:
                    print(f"Error processing row {row}: {e}")
                    continue  # Skip the row on error

            return HttpResponse("CSV data has been saved to the database.")
        except Exception as e:
            print(f"Error reading the CSV file: {e}")
            return HttpResponse("Failed to process the uploaded file.", status=500)

    return render(request, "QR.html")


def cookiesexample(request):
    if request.method == "GET":
        return render(request,"Cookies.html")
    else:

        #name = request.POST.get("textInput")
        #name = request.COOKIES.get("firstname","x")
        #return HttpResponse(name)
        response = HttpResponseRedirect("/cookiesexample")
        response.delete_cookie("firstname")
        return response
        # response.set_cookie("firstname",name,max_age = 3600)
        #return response
