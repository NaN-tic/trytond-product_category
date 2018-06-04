# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Category']


class Category:
    __metaclass__ = PoolMeta
    __name__ = "product.category"
    products = fields.Many2Many('product.template-product.category.all',
        'category', 'template', "Products", readonly=True)
