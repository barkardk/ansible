#Copyright: (c) 2019, kristin barkardottir
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# simple bool to verify base64 string
#!/usr/bin/python

from ansible.module_utils.basic import *
import base64
import binascii

def base_64_string_verify(data):
  b64 = data['base64string']
  try:
    base64.decodestring(b64)
  except binascii.Error:
    return  True, True, {"status": "FAILED"}
  return False, False, {"status": "SUCCESS" }


def main():
  fields = {
    "base64string" : {
     "required": True ,
     "type": "str"
    },
    "convert": {
       "required": False ,
       "type" : "bool"
     },
   }

  module = AnsibleModule(argument_spec=fields)
  is_error, has_changed, result = base_64_string_verify(module.params)

  if not is_error:
    module.exit_json(changed=has_changed, meta=result)
  else:
    module.fail_json(msg="Error string is not base64", meta=result)

if __name__ == '__main__':
    main()
