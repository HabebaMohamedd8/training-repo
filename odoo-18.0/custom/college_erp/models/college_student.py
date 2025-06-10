from odoo import models, fields

class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    admission_no = fields.Char(string="Admission Number", required=True)
    admission_date = fields.Date(string="Admission Date", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    father_name = fields.Char(string="Father's Name", required=True)
    mother_name = fields.Char(string="Mother's Name", required=True)
    communication_address = fields.Text(string="Communication Address", required=True)
    street = fields.Char()
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
