from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .database import *


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        load_instance = True


class IdeasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'is_public', 'category_id', 'category', 'user_id', 'user')
        include_relationships = True
        load_instance = True


