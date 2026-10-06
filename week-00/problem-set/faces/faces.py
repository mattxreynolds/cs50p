def main():
  print(convert(input()))

def convert(text):
  return text.replace(':(', '🙁').replace(':)', '🙂')

main()
