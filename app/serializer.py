from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .database import *


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        load_instance = True
