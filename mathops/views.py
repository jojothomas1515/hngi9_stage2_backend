import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .operation import operate
# functions for api endpoint defination starts hear

@api_view(['POST'])
def index(request):
    if request.method == "POST":
        try:
            operator = request.data['operation_type']
            x = request.data['x']
            y = request.data['y']
            result = operate(operator, x, y)
        except Exception as e:
            print(e)

        json_form = {"slackUsername": "Jojothomas",
                     "operation_type": int(operator),
                     "result": result,
                     }

        return Response(json.dumps(json_form, indent=4))
