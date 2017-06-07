#lfa

from pprint import pprint 
import requests
import json


class Cep(object):

	def __init__(self):
		pass

	def headers(self):
		return {
			'Content-Type': 'application/json',
			'Accept': 'application/json',
			'Authorization': 'Token token=TOKEN AQUI' # cadastro no site cepaberto
		}

	def send(self, cep):
		try:
			cep = cep.replace( "-", "" )
			url = 'http://www.cepaberto.com/api/v2/ceps.json?cep=%s' %(cep)
			response = requests.get(url, headers=self.headers())
			return json.loads(response.content.decode('utf-8'))
		except Exception as error:
			raise
    

cep = Cep().send('25845-000')
pprint (cep)