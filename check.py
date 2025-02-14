import os
import json
import base64
import shlex

from os import path
from subprocess import Popen, PIPE
from threading import Timer


TITLE = '''
   ___       __                        __
  / _ |__ __/ /____  ___  _______ ____/ /__ ____
 / __ / // / __/ _ \\/ _ \\/ __/ _ \\/ _  / -_) __/
/_/ |_\\_,_/\\__/\\___/\\_, /_/  \\_,_/\\_,_/\\__/_/
                   /___/

             Machine Structures
     Great Ideas in Computer Architecture

lab: 01: C y CGDB
'''

class Result:
  stdout = ''
  stderr = ''
  returncode = 0
  timeout = False


def execute(cmd, timeout):
  result = Result()
  proc = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)

  def timeout_handler():
    proc.kill()
    result.timeout = True

  timer = Timer(timeout, timeout_handler)

  try:
    timer.start()
    stdout, stderr = proc.communicate()
    result.stdout = stdout.decode('utf-8').strip()
    result.stderr = stderr.decode('utf-8').strip()
    result.returncode = proc.returncode
  finally:
    timer.cancel()

  return result


def check_result(result):
  if result.timeout:
    return {
      'grade': 0,
      'stderr': 'Timeout',
      'stdout': result.stdout,
      'returncode': result.returncode
    }

  if result.returncode != 0:
    return {
      'grade': 0,
      'stderr': result.stderr,
      'stdout': result.stdout,
      'returncode': result.returncode
    }

ECCENTRIC = '''
V0 OK
V1 OK
V2 OK
V3 OK
'''

LL_EQUAL = '''
OK
OK
'''

LL_CYCLE = '''
OK
OK
OK
OK
OK
OK
'''


def test_eccentric():
  # compile
  result = execute('make clean', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('make test_eccentric', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('./test_eccentric', 5)
  error = check_result(result)
  if error is not None: return error

  expected = ECCENTRIC.strip().splitlines()
  output = result.stdout.splitlines()

  grade = 0
  points = 25 / 4

  for (exp, out) in zip(expected, output):
      exp = exp.strip()
      out = out.strip()

      if exp == out:
          grade += points

  return {
    'grade': round(grade),
    'stderr': result.stderr,
    'stdout': result.stdout,
    'returncode': result.returncode
  }

def test_cgdb():
  if not path.exists(path.join('.', 'ex2.txt')):
    return {
      'grade': 0,
      'stderr': 'ex2 does not exist',
      'stdout': '',
      'returncode': -1
    }

  output = {}
  with open('ex2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip()
      if line == '': continue

      parts = line.split(':')
      if len(parts) != 2: continue

      output[parts[0].lower()] = parts[1].lower()

  rp1 = 'eyIxIjogImIiLCAiMiI6ICJjIiwgIjMiOiAiZCIs'
  rp2 = 'ICI0IjogImIiLCAiNSI6ICJjIiwgIjYiOiAiYyIs'
  rp3 = 'ICI3IjogImEiLCAiOCI6ICJhIiwgIjkiOiAiYiJ9'

  grade = 0
  points = 25 / 9
  decoded_data = json.loads(base64.b64decode(''.join([rp1, rp2, rp3])).decode())

  for key in decoded_data.keys():
      out = output.get(key)
      exp = decoded_data.get(key)
      if exp == out:
          grade += points

  return {
    'grade': round(grade),
    'stderr': '',
    'stdout': str(output),
    'returncode': 0
  }


def test_ll_equal():
  # compile
  result = execute('make clean', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('make test_ll_equal', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('./test_ll_equal', 5)
  error = check_result(result)
  if error is not None: return error

  expected = LL_EQUAL.strip().splitlines()
  output = result.stdout.splitlines()

  grade = 0
  points = 25 / 2

  for (exp, out) in zip(expected, output):
      exp = exp.strip()
      out = out.strip()

      if exp == out:
          grade += points

  return {
    'grade': round(grade),
    'stderr': result.stderr,
    'stdout': result.stdout,
    'returncode': result.returncode
  }


def test_ll_cycle():
  # compile
  result = execute('make clean', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('make test_ll_cycle', 5)
  error = check_result(result)
  if error is not None: return error

  result = execute('./test_ll_cycle', 5)
  error = check_result(result)
  if error is not None: return error

  expected = LL_CYCLE.strip().splitlines()
  output = result.stdout.splitlines()

  grade = 0
  points = 25 / 6

  for (exp, out) in zip(expected, output):
      exp = exp.strip()
      out = out.strip()

      if exp == out:
          grade += points

  return {
    'grade': round(grade),
    'stderr': result.stderr,
    'stdout': result.stdout,
    'returncode': result.returncode
  }

if __name__ == '__main__':
  eccentric = test_eccentric()
  cgdb = test_cgdb()
  ll_equal = test_ll_equal()
  ll_cycle = test_ll_cycle()

  results = [eccentric, cgdb, ll_equal, ll_cycle]
  names = ['1. Eccentric', '2. CGDB', '3. LL Equal', '4. LL Cycle']
  grade = 0
  stdout = ''
  stderr = ''

  print(TITLE)


  for result, name in zip(results, names):
    grade += result['grade']
    prefix = f'{name}'.ljust(15)

    print(f'{prefix}: {result["grade"]}')

    if result['stdout'].strip() != '':
      stdout += f'{name}' + os.linesep * 2
      stdout += result['stdout'].strip() + os.linesep * 2

    if result['stderr'].strip() != '':
      stderr += f'{name}' + os.linesep * 2
      stderr += result['stderr'].strip() + os.linesep * 2

  print('')
  print(f'Total: {grade}')
  print('')
  print('---')
  print('')
  print('stdout:')
  print('')
  print(stdout.rstrip())
  print('')
  print('---')
  print('')
  print('stderr:')
  print(stderr)

