from odoo import models,fields

class Department(models.Model):
    _name = 'department.department'
    _description = 'Records the patient record according to the department'

    firstname = fields.Char(string="First Name")
    lastname = fields.Char(string="Last Name")

    consulted_doctor = fields.Char(string="Doctor Name")
    department = fields.Selection([('cardiology','Cardiology'),('internal medicine','Internal medicine'),('orthopedics','Orthopedics'),('neurology','Neurology'),('general surgery','General Surgery'),('urology','Urology'),('radiology','Radiology'),('nephrology','Nephrology'),('surgery','Surgery'),('pathology','Pathology'),('anesthesiology','Anesthesiology'),('gynaecology','Gynaecology')])
