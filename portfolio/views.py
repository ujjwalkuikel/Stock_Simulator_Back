from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Portfolio
from .serializers import PortfolioSerializer

@api_view(['GET'])
def get_portfolio_by_user(request, uid):
    try:
        portfolio = Portfolio.objects.get(uid=uid)
    except Portfolio.DoesNotExist:
        return Response({"detail": "Portfolio not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PortfolioSerializer(portfolio)
    return Response(serializer.data, status=status.HTTP_200_OK)
