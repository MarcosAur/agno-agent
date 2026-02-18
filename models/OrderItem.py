from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    item: str = Field(description="Item que foi solicitado pelo cliente")
    quantity: int = Field(description="Quantidade de itens que foram solicitados no pedido")
    observations: str = Field(description="Informações adicionais que o cliente solicitou no pedido")