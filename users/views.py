from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from credit_request.models import CreditRequestModel
from django.contrib.auth import get_user_model


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if email is None or password is None:
        return Response({'success': False, 'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'success': False, 'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user_info = {'email': user.email, 'credit': user.credit, 'count': user.count, 'is_active': user.is_active,
                 'is_admin': user.is_admin,
                 'first_name': user.first_name, 'last_name': user.last_name}
    return Response({'success': True, 'token': token.key, 'user': user_info},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def me(request):
    User = get_user_model()
    user = User.objects.get(email=request.user)

    user_info = {'email': user.email, 'credit': user.credit, 'count': user.count, 'is_active': user.is_active,
                 'is_admin': user.is_admin,
                 'first_name': user.first_name, 'last_name': user.last_name}

    return Response({'success': True, 'user': user_info},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def credit_request(request):
    req_instance = CreditRequestModel.objects.create(user=request.user)
    req_instance.save()
    # If already have a credit request then IntegrityError will raise else
    return Response({'success': True, 'msg': 'Request Successfully!'}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def screenshot(request):
    User = get_user_model()
    user = User.objects.get(email=request.user)

    if user.credit == 0:
        return Response({'success': False, 'msg': "Sorry! You don't have enough Credit!"}, status=HTTP_200_OK)
    else:
        user.credit = user.credit - 1
        user.count = user.count + 1
        user.save()
        return Response({'success': True, 'msg': 'Screenshot Request Successfully!'}, status=HTTP_200_OK)
