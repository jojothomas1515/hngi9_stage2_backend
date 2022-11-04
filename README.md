# HNG STAGE 2 BACKEND TASK
> This backend app takes this json format 
> `{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }`
> process the value x and y with respect to the operation_type
> 
>`enum operation_type: addtion = 1, subtraction =2, multiplication = 3`
> 
> and return the following json form as output
> `{ “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }`
> ### api_view function handling the request
> [view.py](mathops/views.py)
> 
> function [for the operations](mathops/operation.py)