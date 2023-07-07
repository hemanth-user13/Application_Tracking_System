from django.shortcuts import render, redirect
from .models import *
from .models import Candidate,Cse,Civil,Mechanical,Ece,Eee

# Create your views here.
def details(request):
    return render(request,'index.html')


def login_val(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username,"***********%%%%%%%%%%%%%%%%%")
        try:
            user = caditate_signup.objects.get(username=username)
        except caditate_signup.DoesNotExist:

            return render(request, 'index.html', {'error': 'Invalid username or password'})

        # Verify the password
        if user.password != password:
            return render(request, 'index.html', {'error': 'Invalid username or password'})

        # If the username and password match, redirect to another webpage
        return render(request,'dashboard.html')
    else:
        return render(request, 'dashboard.html')



#
# def excel(request):
#     if request.method == 'GET':
#         return render(request, 'excel.html')
#     else:
#         excel_files = request.FILES.getlist('excel_file')
#         combined_data = []
#         headers = None
#
#         for excel_file in excel_files:
#             df = pd.read_excel(excel_file)
#             df = df.applymap(str)  # Convert all values to strings
#
#             if headers is None:
#                 headers = df.columns.tolist()
#             else:
#                 if headers != df.columns.tolist():
#                     return HttpResponse("All Excel files must have the same columns.")
#
#             data = df.values.tolist()
#             combined_data.extend(data)
#
#         request.session['excel_data'] = combined_data
#         print(headers)
#         return render(request, 'excel.html', {"excel_data": combined_data, "headers": headers})

# def excel(request):
#     if request.method == 'GET':
#         query = request.GET.get('query', '')
#         excel_data = request.session.get('excel_data', [])
#         headers = request.session.get('headers', [])
#
#         if query:
#             filtered_data = []
#             for row in excel_data:
#                 for cell in row:
#                     if query.lower() in cell.lower():
#                         filtered_data.append(row)
#                         break
#             excel_data = filtered_data
#             print(headers)
#
#         return render(request, 'excel.html', {"excel_data": excel_data, "headers": headers})
#
#     else:
#         excel_files = request.FILES.getlist('excel_file')
#         combined_data = []
#         headers = None
#
#         for excel_file in excel_files:
#             df = pd.read_excel(excel_file)
#             df = df.applymap(str)  # Convert all values to strings
#
#             if headers is None:
#                 headers = df.columns.tolist()
#             else:
#                 if headers != df.columns.tolist():
#                     return HttpResponse("All Excel files must have the same columns.")
#
#             data = df.values.tolist()
#             combined_data.extend(data)
#
#         request.session['excel_data'] = combined_data
#         return render(request, 'excel.html', {"excel_data": combined_data, "headers": headers})
def excel(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        excel_data = request.session.get('excel_data', [])
        headers = request.session.get('headers', [])

        print("Headers:", headers)  # Print headers for debugging purposes

        if query:
            filtered_data = []
            for row in excel_data:
                for cell in row:
                    if query.lower() in cell.lower():
                        filtered_data.append(row)
                        break
            excel_data = filtered_data

        return render(request, 'excel.html', {"excel_data": excel_data, "headers": headers})

    else:
        excel_files = request.FILES.getlist('excel_file')
        combined_data = []
        headers = None

        for excel_file in excel_files:
            df = pd.read_excel(excel_file)
            df = df.applymap(str)  # Convert all values to strings

            if headers is None:
                headers = df.columns.tolist()
            else:
                if headers != df.columns.tolist():
                    return HttpResponse("All Excel files must have the same columns.")

            data = df.values.tolist()
            combined_data.extend(data)

        request.session['excel_data'] = combined_data
        request.session['headers'] = headers  # Store headers in the session
        return render(request, 'excel.html', {"excel_data": combined_data, "headers": headers})



def add_candidate(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        branch=request.POST.get('branch')
        skills = request.POST.get('skills')
        jr_number=request.POST.get('jr_number')
        phone_number=request.POST.get('phone_number')
        email_address=request.POST.get('email_address')
        current_company=request.POST.get('current_company')
        total_experience=request.POST.get('total_experience')
        ctc = request.POST.get('ctc')
        expected_ctc = request.POST.get('expected_ctc')
        offers_in_hand= request.POST.get('offers_in_hand')
        notice_period = request.POST.get('notice_period')
        current_location = request.POST.get('current_location')
        source = request.POST.get('source')
        screening_status = request.POST.get('screening_status')
        screened_by = request.POST.get('screened_by')
        Candidate.objects.create(first_name=first_name,last_name=last_name,branch=branch,skills=skills,jr_number=jr_number,phone_number=phone_number,email_address=email_address,ctc=ctc,expected_ctc=expected_ctc,total_experience=total_experience,offers_in_hand=offers_in_hand,notice_period=notice_period,screening_status=screening_status,screened_by=screened_by,source=source,current_company=current_company,current_location=current_location)
        if branch.lower() == 'cse':
            Cse.objects.create(first_name=first_name,last_name=last_name,branch=branch,skills=skills,jr_number=jr_number,phone_number=phone_number,email_address=email_address,ctc=ctc,expected_ctc=expected_ctc,total_experience=total_experience,offers_in_hand=offers_in_hand,notice_period=notice_period,screening_status=screening_status,screened_by=screened_by,source=source,current_company=current_company,current_location=current_location)

        elif branch.lower() == 'civil':
            Civil.objects.create(first_name=first_name,last_name=last_name,branch=branch,skills=skills,jr_number=jr_number,phone_number=phone_number,email_address=email_address,ctc=ctc,expected_ctc=expected_ctc,total_experience=total_experience,offers_in_hand=offers_in_hand,notice_period=notice_period,screening_status=screening_status,screened_by=screened_by,source=source,current_company=current_company,current_location=current_location)

        elif branch.lower() == 'mechanical':
            Mechanical.objects.create(first_name=first_name,last_name=last_name,branch=branch,skills=skills,jr_number=jr_number,phone_number=phone_number,email_address=email_address,ctc=ctc,expected_ctc=expected_ctc,total_experience=total_experience,offers_in_hand=offers_in_hand,notice_period=notice_period,screening_status=screening_status,screened_by=screened_by,source=source,current_company=current_company,current_location=current_location)
        elif branch.lower() == 'ece':
            Ece.objects.create(first_name=first_name, last_name=last_name, branch=branch, skills=skills,
                                 jr_number=jr_number, phone_number=phone_number, email_address=email_address, ctc=ctc,
                                 expected_ctc=expected_ctc, total_experience=total_experience,
                                 offers_in_hand=offers_in_hand, notice_period=notice_period,
                                 screening_status=screening_status, screened_by=screened_by, source=source,
                                 current_company=current_company, current_location=current_location)

        elif branch.lower() == 'eee':
            Eee.objects.create(first_name=first_name, last_name=last_name, branch=branch, skills=skills,
                                      jr_number=jr_number, phone_number=phone_number, email_address=email_address,
                                      ctc=ctc, expected_ctc=expected_ctc, total_experience=total_experience,
                                      offers_in_hand=offers_in_hand, notice_period=notice_period,
                                      screening_status=screening_status, screened_by=screened_by, source=source,
                                      current_company=current_company, current_location=current_location)

        return render(request, 'form.html')
    return render(request, 'form.html')






def option(request):
    if request.method == "POST":
        print("**********************")
        option = request.POST.get("visualization")
        if option == 'Registrationform':
            return render(request, 'form.html')  # Render tabular.html template
        elif option == 'Excel':
            return render(request, 'excel.html')
def signup(request):
    return render(request, 'signup.html')

def Stu_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # Check if the username already exists in the model
        if caditate_signup.objects.filter(username=username).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            password = request.POST.get('password')
            caditate_signup.objects.create(firstname=firstname,lastname=lastname,username=username,password=password)
            return render(request, 'index.html')



from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
import pandas as pd

from .models import Candidate

def candidate_list(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'candidate_list.html', context)

def candidate_list_excel(request):
    candidates = Candidate.objects.all()

    candidate_data = []
    for candidate in candidates:
        candidate_data.append([
            candidate.first_name,
            candidate.last_name,
            candidate.branch,
            candidate.skills,
            candidate.jr_number,
            candidate.phone_number,
            candidate.email_address,
            candidate.current_company,
            candidate.total_experience,
            candidate.ctc,
            candidate.expected_ctc,
            candidate.offers_in_hand,
            candidate.notice_period,
            candidate.current_location,
            candidate.source,
            candidate.screening_status,
            candidate.screened_by,
            candidate.source_date,
        ])

    df = pd.DataFrame(candidate_data, columns=['First Name', 'Last Name', 'Branch', 'Skills', 'JR Number',
                                               'Phone Number', 'Email Address', 'Current Company', 'Total Experience',
                                               'CTC', 'Expected CTC', 'Offers in Hand', 'Notice Period',
                                               'Current Location', 'Source', 'Screening Status', 'Screened By',
                                               'Source Date'])
    excel_file = 'candidate_data.xlsx'
    df.to_excel(excel_file, index=False)

    with open(excel_file, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=' + excel_file

    return response
