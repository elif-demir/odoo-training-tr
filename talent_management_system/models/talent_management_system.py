from odoo import api, models, fields
import datetime
from dateutil import relativedelta

class Talent(models.Model):
    _name = 'talent.management.system'
    _description = 'Talent_Management_System'

    employee_id = fields.Char(string='Employee ID')
    name = fields.Many2one('hr.employee', string='Employee Name')
    department_id = fields.Char(string= 'Department')
    email = fields.Char(string='E-mail')
    role_name = fields.Selection(
        [('technician', "Technician"),
         ('engineer', "Engineer"),
         ('Manager', "Manager"),
         ])

    start_date = fields.Date(string='Start Date')
    service_time = fields.Char(compute='_compute_service_time', string='Service Days')

    employee_skills = fields.Many2many("skills")


    @api.onchange('name')
    def onchange_name(self):
        self.email = self.name.work_email
        self.department_id = self.name.department_id.name

    @api.depends('start_date')
    def _compute_service_time(self):
        working_time = relativedelta.relativedelta(datetime.date.today(), self.start_date)
        self.service_time = str(working_time.years) + ' year(s) ' + str(working_time.months) + ' month(s) '+ str(working_time.days) + ' day(s)'


