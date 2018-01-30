#!/usr/bin/ruby -w

NAMESPACE = 'urn:ruby:calculation'
URL = 'http://localhost:11080/sofn-dgap-pre/ws/welcome1?wsdl'

begin
   driver = SOAP::RPC::Driver.new(URL, NAMESPACE)
   
   # Add remote sevice methods
   driver.add_method('getMessage')

   # Call remote service methods
   puts driver.getMessage()
rescue => err
   puts err.message
end
