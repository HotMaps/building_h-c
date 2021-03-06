"""
The schemas that will be taken as base by the api or the parameters, they are using marshmallow technology
"""

from flask_restplus_patched import Schema
from flask_marshmallow import base_fields
from ..common import schemas as commonSchema

class F107Schema(Schema):
    updated_demand_value = base_fields.Integer()
    output_dir = base_fields.String()
    outRasterPath = base_fields.String()
    response = base_fields.Dict()