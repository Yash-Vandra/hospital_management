from odoo import models,fields

class StaffManagement(models.Model):
    _name = 'staff.staff'
    _description = 'Records of the staff'

    fullname = fields.Char(string="Full Name")
    id_number = fields.Integer(string="Id Number")

    staff_department= fields.Selection([('doctors','Doctors'),('nurses','Nurses'),('dietitians','Dietitians'),('pharmacists','Pharmacists'),('physiotherapists','Physiotherapists'),('clinical assistants','Clinical Assistants')])

