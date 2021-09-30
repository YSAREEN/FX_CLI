from click.testing import CliRunner
from FX_Rate_tool import history, convert

def test_history():
   runner = CliRunner()
   result = runner.invoke(history, ['--start', '2021-09-28', '--end', '2021-09-28', '--symbol', 'EUR'])
   print("\nResult: " + result.output)
   assert result.exit_code == 0
   assert result.output.find("0.85631") != -1

def test_convert():
   runner = CliRunner()
   result = runner.invoke(convert, ['--start', '2021-09-28', '--base', 'USD', '--symbol', 'EUR', '--amount', '100'])
   print("\nResult: " + result.output)
   assert result.exit_code == 0
   assert result.output.find("85.63") != -1
