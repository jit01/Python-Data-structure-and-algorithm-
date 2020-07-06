from suds.client import Client
_client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
add = getattr(_client.service, 'Add')
print('addition = ', add(10, 12))
