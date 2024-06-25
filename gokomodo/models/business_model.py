from odoo import models, fields, api

class BusinessModel(models.Model):
    _name = 'master.business.model'

    code = fields.Char('Business Model Code')
    name = fields.Char('Business Model Name')

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s [%s]' % (rec.name, rec.code)))
        return result