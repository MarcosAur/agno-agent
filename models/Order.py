from pydantic import BaseModel, Field
from models.OrderItem import OrderItem


class Order(BaseModel):
    order_items: list[OrderItem] = Field(description="Lista de itens que foram solicitados no pedido")