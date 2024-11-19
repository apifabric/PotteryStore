from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger(__name__)

app_logger.debug("\napi/expose_api_models.py - endpoint for each table")


def expose_models(api, method_decorators = []): 
    """
        Declare API - on existing SAFRSAPI to expose each model - API automation 
        - Including get (filtering, pagination, related data access) 
        - And post/patch/update (including logic enforcement) 

        Invoked at server startup (api_logic_server_run) 

        You typically do not customize this file 
        - See https://apilogicserver.github.io/Docs/Tutorial/#customize-and-debug 
    """
    api.expose_object(database.models.Activity, method_decorators= method_decorators)
    api.expose_object(database.models.Artist, method_decorators= method_decorators)
    api.expose_object(database.models.Class, method_decorators= method_decorators)
    api.expose_object(database.models.ClassReport, method_decorators= method_decorators)
    api.expose_object(database.models.Customer, method_decorators= method_decorators)
    api.expose_object(database.models.Enrollment, method_decorators= method_decorators)
    api.expose_object(database.models.Student, method_decorators= method_decorators)
    api.expose_object(database.models.Item, method_decorators= method_decorators)
    api.expose_object(database.models.Order, method_decorators= method_decorators)
    api.expose_object(database.models.OrderDetail, method_decorators= method_decorators)
    api.expose_object(database.models.OrderReport, method_decorators= method_decorators)
    api.expose_object(database.models.StudentActivity, method_decorators= method_decorators)
    return api
