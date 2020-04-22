from django.conf import settings
from rest_framework.views import APIView
import requests
from rest_framework.response import Response

class VerifyKhaltiPayment(APIView):

    def post(self,request,*args,**kwargs):
        token = request.POST.get('token')
        amount = request.POST.get('amount')
        payload = {
            "token":token,
            "amount":amount,
        }
        headers = {
            "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
        }
        try:
            response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers)
            if response.status_code == 200 :
                return Response({
                    'status':True,
                    'details':response.json(),
                })

            else:
                return Response({
                    'status':False,
                    'details':response.json(),
                })

        except requests.exceptions.HTTPError as e:
            return Response({
                'status':False,
                'details':response.json(),
            })