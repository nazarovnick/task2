from django.http import HttpResponse
from openpyxl.workbook import Workbook
from tempfile import NamedTemporaryFile
from rest_framework import mixins
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_csv.renderers import CSVRenderer

from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
def index_page(request):

    comments = Comment.objects.all()

    context = {
                'comments' : comments,
               }

    return render(request = request, template_name = 'index.html', context = context)


class APIMixin(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericViewSet):
    pass

class CountryViewSet(APIMixin):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DeveloperViewSet(APIMixin):

    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class CarViewSet(APIMixin):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(APIMixin):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

import csv
from django.http import HttpResponse
from rest_framework.views import APIView


class CSVviewSet(APIView):
    def get(self, request, format=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.DictWriter(response, fieldnames=['emp_name', 'dept', 'birth_month'])
        writer.writeheader()
        writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
        return response




class GenerateExcelView(APIView):

    def get(self, request):

        filetype = request.GET.get('type')

        if filetype == 'csv':
            pass

        elif filetype == 'xlsx':
            filename = 'all_data.xlsx'
            wb = Workbook()
            ws = wb.active
            ws.title = "Workbook"

            ws[f'A1'] = 'Текст комментария'
            ws[f'B1'] = 'Дата добавления'
            ws[f'C1'] = 'E-mail автора'
            ws[f'D1'] = 'Автомобиль'
            ws[f'E1'] = 'Производитель'
            ws[f'F1'] = 'Страна'
            ws[f'G1'] = 'Дата начала производства'
            ws[f'H1'] = 'Дата окончания производства'

            data = Comment.objects.all()
            row_counter = 2
            for line in data:

                ws[f'A{row_counter}'] = line.comment_text
                ws[f'B{row_counter}'] = line.date_created.strftime('%d.%m.%Y')
                ws[f'C{row_counter}'] = line.author_email
                ws[f'D{row_counter}'] = line.car_key.name
                ws[f'E{row_counter}'] = line.car_key.developer_key.name
                ws[f'F{row_counter}'] = line.car_key.developer_key.country_key.name
                ws[f'G{row_counter}'] = line.car_key.date_production_start.strftime('%d.%m.%Y')
                ws[f'H{row_counter}'] = line.car_key.date_production_stop.strftime('%d.%m.%Y')

                row_counter += 1

            with NamedTemporaryFile() as tmp:
                wb.save(tmp.name)
                tmp.seek(0)
                stream = tmp.read()

            response = HttpResponse(content = stream, content_type = 'application/ms-excel')
            response["Content-Disposition"] = 'attachment; filename="' + filename + '"'
            return response
