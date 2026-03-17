'''Docstring for dashboard ui logic'''
# Create your views here.
def dashboard_callback(request,context):
    '''Dashboard Callbacck PLugin Data'''
    context.update({
        "username": request.user.username,
    })

    return context
