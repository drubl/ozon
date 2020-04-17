

class RegisterCustomer(APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            if check_email(User, serializer):
                return Response('Пользователь с таким email уже зарегистрирован',
                                status=status.HTTP_400_BAD_REQUEST)
            user_data = serializer.data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            print(f'USER CREATE {user}')
            if request.session.get('basket_id') and request.session.get('customer_id'):
                Customer.objects.filter(id=request.session['customer_id']).update(user=user)
                customer = Customer.objects.get(id=request.session['customer_id'])
                print(f'CUSTOMER UPDATE')
            else:
                customer, created = Customer.objects.update_or_create(user=user,
                                                                  phone=serializer.data.pop('phone'))
                Basket.objects.create(user_id=customer)
            return Response(f'Register {customer.user.username}', status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)