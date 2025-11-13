"""
Database Schemas for Vape E-commerce + Services

Each Pydantic model represents a MongoDB collection (collection name is the lowercase class name).
"""
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    password_hash: Optional[str] = Field(None, description="Hashed password")
    is_active: bool = Field(True)


class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None)
    price: float = Field(..., ge=0)
    category: str = Field(..., description="Category name")
    in_stock: bool = Field(True)
    stock_qty: int = Field(0, ge=0)
    images: List[str] = Field(default_factory=list)
    specs: Dict[str, str] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)


class OrderItem(BaseModel):
    product_id: str
    title: str
    price: float
    quantity: int = Field(..., ge=1)
    image: Optional[str] = None


class Address(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    line1: str
    line2: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str


class Order(BaseModel):
    user_email: EmailStr
    items: List[OrderItem]
    total: float = Field(..., ge=0)
    shipping: Address
    payment_method: str = Field("card", description="card | cod | wallet | placeholder")
    status: str = Field("pending", description="pending | paid | shipped | completed | cancelled")


class Booking(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    device_type: str
    issue_description: str
    image_base64: Optional[str] = Field(None, description="Optional base64 image string")
    preferred_datetime: Optional[str] = None
    payment_option: str = Field("pay_on_service")


class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str
