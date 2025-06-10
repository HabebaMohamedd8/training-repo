from odoo import models,fields,api



class app(models.Model):
    _name = 'habeba.app'
    myname = fields.Char()
    myage = fields.Integer()
    mysalary = fields.Float()

    pass
