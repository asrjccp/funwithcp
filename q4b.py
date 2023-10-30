def make_trace(name, records_tpl):
    lst = (name, records_tpl)
    return lst

def get_person(trace):
  return trace[0]

def get_records(trace):
    return trace[1]
