"""Módulo responsável por definir os contratos de dados da aplicação."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator


class CategoriaEnum(str, Enum):
    """Enum para as categorias dos produtos.

    Args:
        categoria1 (str): Categoria 1
        categoria2 (str): Categoria 2
        categoria3 (str): Categoria 3
    """

    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


class Sales(BaseModel):
    """
    Modelo de dados para as vendas.

    Atributos:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        quantidade (PositiveInt): quantidade de produtos
        produto (str): nome do produto
        categoria (str): categoria do produto Enum(categoria1, categoria2, categoria3)
    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: str
    categoria: CategoriaEnum

    @field_validator("categoria")
    def categoria_deve_estar_no_enum(cls: type, error: str) -> str:
        """Valida se a categoria está no Enum.

        Args:
            error (str): Mensagem de erro.

        Returns:
            str: Mensagem de erro.
        """
        return error
