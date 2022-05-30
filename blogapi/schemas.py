from dotenv import load_dotenv
import motor.motor_asyncio
import os
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client.blogapi


class PyObjectid(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectID")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: PyObjectid = Field(default_factory=PyObjectid, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_type_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "test test",
                "email": "test@example.com",
                "password": "password",
            }
        }


class UserResponse(BaseModel):
    id: PyObjectid = Field(default_factory=PyObjectid, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_type_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "test test",
                "email": "test@example.com",
            }
        }
