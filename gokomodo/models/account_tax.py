from odoo import models, fields, api, _

class AccountTax(models.Model):
    _inherit = 'account.tax'

    business_model_id = fields.Many2one('master.business.model', string='Business Model')
