from replit import db
import os

def update_score(key_name:str, current_score:int, increment=1):
  new_score = current_score + 1
  db[key_name.lower()] = new_score
  return new_score

def set_score(key_name:str, new_score:int):
  key_name = key_name.lower()
  if key_name in db.keys():
    if new_score > db[key_name]:
      db[key_name] = new_score
  else:
    db[key_name] = new_score

def get_highscore(score_prefix:str='', give_as_int:bool=False):
  matches = db.prefix(score_prefix)
  high_score = 0
  high_score_holder = ''
  for key in matches:
    if db[key] > high_score:
      high_score = db[key]
      high_score_holder = key
      if give_as_int:
        return high_score
      else:
        return high_score_holder + ' has ' + str(high_score)
  
def delete_key():
  if input('What is the password?') == os.environ['delete_key_password']:
    to_be_deleted = db.prefix(input('Any specific keys?').lower())
    for key in to_be_deleted:
      del db[key.lower()]

def list_keys():
  if input('What is the password') == os.environ['list_key_password']:
    for key in db.keys():
      print(f'{key} has {db[key]} points.')