require 'savon'

client = Savon::Client.new(wsdl: "http://127.0.0.1:5000/soap/HelloWorldService?wsdl")

client.operations # => [:integer_to_string, :concat, :add_circle]

#result = client.call(:concat, message: { :a => "123", :b => "abc" })
result = client.call(:query_air_info)
print result
# actual wash_out
result.to_hash # => {:concat_reponse => {:value=>"123abc"}}

# wash_out below 0.3.0 (and this is malformed response so please update)
result.to_hash # => {:value=>"123abc"}