# -*- coding: utf-8 -*-
response.generic_patterns = ['*']

db.define_table('Portfolio',
                Field('Symbol', 'string' ,requires=IS_NOT_EMPTY()),
                Field('Quantity', requires = IS_NOT_EMPTY()),
                Field('Purchase_Price', requires = IS_NOT_EMPTY()),
                Field('Current_Price',readable=False,writable=False),
                Field('Previous_Total',readable=False,writable=False),
                Field('Current_Total',readable=False,writable=False),
                Field('Gain_Loss',readable=False,writable=False)
               )

db.define_table('WatchList',
                Field('Symbol', 'string' ,requires=IS_NOT_EMPTY()),
                Field('Current_Price',readable=False,writable=False)
                )

db.define_table('StockList',
                Field('Symbol', 'string' ,requires=IS_NOT_EMPTY()),
                Field('Current_Price',readable=False,writable=False)
                )
