# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResUsers(models.Model):

    _inherit = "res.users"

    sip_number = fields.Char('Sip Number', required=False)
    sip_password = fields.Char('Sip Password', required=False)
    
    sip_register_status = fields.Char('Sip Register Status', required=False)
    sip_phone_status = fields.Char('Sip Phone Status', required=False)
    sip_agent_status = fields.Char('Sip Agent Status', required=False)
