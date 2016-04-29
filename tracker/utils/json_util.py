import json
import datetime

import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)

# a = {'Alice': '2341', 'Beth': '9102', 'Cecil': datetime.date(2002, 3, 11)}

# print json.dumps(a, cls=DateTimeEncoder)
