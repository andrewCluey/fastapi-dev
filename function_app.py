
import azure.functions as func

from api.fastapi_app import create_app

fastapi_app = create_app()

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.FUNCTION)



#import azure.functions as func

#from WrapperFunction import app as fastapi_app

#app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
