from rest_framework.views import APIView
from rest_framework.response import Response
from access.decorators import require_permission


class OrdersView(APIView):

    @require_permission("orders", "read")
    def get(self, request):
        return Response(
            {"orders": ["order1", "order2", "order3"]}
        )

    @require_permission("orders", "create")
    def post(self, request):
        return Response({"status": "order created"})
