from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    business_model_id = fields.Many2one('master.business.model', string='Business Model')
    tax_id = fields.Many2many('account.tax', string='Taxes')

    @api.model
    def create(self, vals):
        if 'business_model_id' in vals:
            business_model = self.env['master.business.model'].browse(vals['business_model_id'])
            if business_model:
                code_prefix = business_model.code
                vals['name'] = f"[{code_prefix}] - {self.env['ir.sequence'].next_by_code('sale.order') or _('New')}"
        return super(SaleOrder, self).create(vals)
    
    @api.onchange('business_model_id')
    def _onchange_business_model_id(self):
        vals = {}
        self.order_line = [(5, 0, 0)]
        if self.business_model_id:
            vals['business_model_id'] = self.business_model_id.id
            (self.order_line).update(vals)
            self.order_line._set_taxes_based_on_business_model()
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    business_model_id = fields.Many2one('master.business.model', string='Business Model')
   
    @api.onchange('product_id','business_model_id')
    def onchange_product(self):
        taxs_list = []
        if self.business_model_id:
            taxs = self.env['account.tax'].search([('business_model_id','=', self.business_model_id.id)])
            for tax in taxs:
                taxs_list.append(tax.id)
            res = {'domain': {'tax_id': [('id', 'in', taxs_list)]}}
            return res
    
    @api.depends('order_id.business_model_id')
    def _compute_tax_id(self):
        for line in self:
            line._set_taxes_based_on_business_model()
        
    def _set_taxes_based_on_business_model(self):
        taxs = self.env['account.tax'].sudo().search([('business_model_id','=', self.business_model_id.id)])
        if taxs:
            list_tax = []
            for tax in taxs:
                list_tax.append(tax.id)
            self.tax_id = [(6, 0, list_tax)]
        else:
             self.tax_id = [(5, 0, 0)]
    
    
    
    

    