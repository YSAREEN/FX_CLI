import click
import requests
import json
from datetime import datetime


@click.group()
def cli():
   pass

@cli.command()
@click.option('-n', '--start', type=str, help='Start Date for historical rate in YYYY-MM-DD')
@click.option('-n', '--end', type=str, help='End Date for historical rate in YYYY-MM-DD')
@click.option('-n', '--base', type=str, help='Base currency to convert from', default='USD')
@click.option('-n', '--symbol', type=str, help='Currency to covert to - comma separated for multiple symbols',required=True)
@click.option('-n', '--output', type=str, help='Provide file name to output to file', default=None)
def history(start, end, base, symbol,output):
   base_url = "https://api.frankfurter.app/"
   now = datetime.now()

   '''
       DateValidation 1: if default is weekend, default it to last friday
       DateValidation 2: Validate if date is in format YYYY-MM-DD
       Add Output Param: to output to cli or to file - based on param call separate method for file output
       Format Output: Output formatting should also be in a separate method.
   '''
   if start is None or start == "":
       start = now.strftime("%Y-%m-%d")
       #click.echo(f'start_date:{start}')
   if end is None or end == "":
       end = now.strftime("%Y-%m-%d")
       #click.echo(f'end_date:{end}')

   if symbol is None or symbol == "" or symbol == 'USD':
       click.echo("Symbol is a required parameter. Please provide a valid currency symbol except USD")
       return

   date_params = start + ".." + end
   url = base_url + date_params
   parameters = {"from": base,
                 "to": symbol}
   try:
       response = requests.get(url, params=parameters)
   except requests.exceptions.RequestException as e:
       raise SystemExit(e)

   if response.status_code != 200:
       return

   text = json.dumps(response.json(), sort_keys=True, indent=4)

   json_dict = json.loads(text)
   display = traverse_json(json_dict)

   final_str = '\n'.join([i for i in display])

   if output is None:
       click.echo(final_str)
   else:
       with open(output, 'w') as f:
           f.write(final_str)


def traverse_json (d):
   display = []
   base = d['base']
   for to_date in d['rates']:
       for symbol in d['rates'][to_date]:
           rate = d['rates'][to_date][symbol]
           display.append("{" + "\"date\": \"" + to_date + "\"" +
                 ", \"base\": \"" + base + "\"" +
                 ", \"symbol\": \"" + symbol + "\"" +
                 ", \"rate\": " + str(rate) + "}")

   return display

@cli.command()
@click.option('-n', '--start', type=str, help='Start Date for historical rate in YYYY-MM-DD')
@click.option('-n', '--base', type=str, help='Base currency to convert from', default='USD')
@click.option('-n', '--symbol', type=str, help='Currency to covert to', required=True)
@click.option('-n', '--amount', type=int, help='the amount to convert', required=True)
def convert(start, base, symbol, amount):
   base_url = "https://api.frankfurter.app/"
   now = datetime.now()

   '''
       DateValidation 1: if default is weekend, default it to last friday
       DateValidation 2: Validate if date is in format YYYY-MM-DD
       Add Output Param: to output to cli or to file - based on param call separate method for file output
       Format Output: Output formatting should also be in a separate method.
   '''
   if start is None or start == "":
       start = now.strftime("%Y-%m-%d")
       #click.echo(f'start_date:{start}')

   end = start
   date_params = start + ".." + end
   url = base_url + date_params
   parameters = {"from": base,
                 "to": symbol,
                 "amount": amount}
   try:
       response = requests.get(url, params=parameters)
   except requests.exceptions.RequestException as e:
       raise SystemExit(e)

   if response.status_code != 200:
       return

   text = json.dumps(response.json(), sort_keys=True, indent=4)

   json_dict = json.loads(text)
   display = traverse_json(json_dict)

   final_str = '\n'.join([i for i in display])

   click.echo(final_str)
