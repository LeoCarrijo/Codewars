def duplicate_count(s):
  return [c for c in set(s.lower()) if s.lower().count(c)>1]
