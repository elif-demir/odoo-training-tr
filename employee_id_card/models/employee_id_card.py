from odoo import models, fields

class Employee(models.Model):
    _name = 'employee.id.card'
    _description = 'Employee_Identification_number'

    name = fields.Many2one("hr.employee")
    card_type = fields.Selection(
        [('passport', "Passport"),
         ('id card', "ID Card"),
         ('driving license', "Driving License"),
         ],
        'Type')
    id_number = fields.Char('ID No')
