#
# import json
# a = {
#   "test1" : {
#     "aliases" : {
#       "test3" : { }
#     },
#     "mappings" : {
#       "jdbc" : {
#         "dynamic_templates" : [
#           {
#             "strings" : {
#               "match" : "*",
#               "mapping" : {
#                 "fields" : {
#                   "keyword" : [{
#                     "normalizer" : "custom_normalizer1",
#                     "type" : "keyword1"
#                   },
#                   {
#                     "normalizer" : "custom_normalizer2",
#                     "type" : "keyword2"
#                   },
#                 ]},
#                 "type" : "text"
#               }
#             }
#           }
#         ]
#       }
#     }
#   }
# }
# #
# # Output :
# #
# # custom_normalizer1 keyword1
# # custom_normalizer2 keyword2
# #
# #
# # INPUT:
#
# # best case O(1)
# # worst case O(n)
# validate = json.dumps(a)
# data = a['test1']['mappings']['jdbc']['dynamic_templates'][0]['strings']['mapping']['fields']['keyword']
# # for i in data:
# #     print(i['normalizer'] + i['type'])
#


input = ['abcab','abba','bcaacb']
result = []
for ele in input:
    if ele[:] == ele[::-1]:     # abcab   ['a', 'b', 'c' , 'a', 'b'] == ['b', 'a', 'c', 'b', 'a']
        result.append('Yes')
    else:
        result.append('No')

print(input)
print(result)
