# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Tipo de Cambio Guatemala USD",

    'summary': """Modulo que actualiza el tipo de cambio diario en base a BANGUAT, solo funciona para USD
    Configure la hora de actualización en Técnico>>Acciones Planificadas>>Enviar Solicitud de Tipo de Cambio
    """,
    "license": "OPL-1",

    'description': """
        Modulo que actualiza el tipo de cambio diario en base a BANGUAT"
    """,

    'author': "Promit",
    'website': "http://www.promitgt.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'images': ['static/description/logo.jpeg'],

    'depends': ['account'],

    'data': [
        'data/cron_tc.xml'
    ],
}
