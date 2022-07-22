def fahr_to_celsius(far):
  cel = (far - 32) * 5/9
  return (cel)
def cel_to_kelvin(cel):
    kel = cel +273.15
    return (kel)
def fahr_to_kelvin():
    x = int(fahr_to_celsius(far))
    return (cel_to_kelvin(x))
far = int(input())
print(fahr_to_kelvin())
