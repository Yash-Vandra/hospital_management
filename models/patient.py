from odoo import models,fields

class HospitalManagement(models.Model):
    _name = "hospital.management"
    _description = "This is hospital management system"

    name = fields.Char(string="Name",required=True)
    age = fields.Integer(string='Age' ,required=True)
    patient_reports = fields.Text(string="Patient Reports")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')])

