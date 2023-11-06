import requests
from xml.etree import ElementTree as ET
from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def send_request_and_create_rate(self):
        envelope = ET.Element("soap:Envelope")
        envelope.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        envelope.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
        envelope.set("xmlns:soap", "http://schemas.xmlsoap.org/soap/envelope/")
        body = ET.SubElement(envelope, "soap:Body")
        tipo_cambio_dia = ET.SubElement(body, "TipoCambioDia")
        tipo_cambio_dia.set("xmlns", "http://www.banguat.gob.gt/variables/ws/")
        xml_request = ET.tostring(envelope)
        url = "https://www.banguat.gob.gt/variables/ws/TipoCambio.asmx"
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://www.banguat.gob.gt/variables/ws/TipoCambioDia"
        }
        response = requests.post(url, data=xml_request, headers=headers)   
        venta = 1
        if response.status_code == 200:
            response_xml = ET.fromstring(response.content)
            for elem in response_xml.iter():
                if elem.tag.endswith("referencia"):
                    venta = float(elem.text)
                    break
            today = datetime.now().date()
            currency_id = self.env['res.currency'].search([('name', '=', 'GTQ')], limit=1)
            self.env['res.currency.rate'].create({
                'name': today,
                'currency_id': 2,
                'rate': 1 / venta,
            })
        else:
            raise UserError(f"Error de respuesta: {str(response)}")
    
        # visita nuestro canal de youtube promitgt para aprender mas !!!!


        return True
