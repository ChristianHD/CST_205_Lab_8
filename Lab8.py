#Christian Guerrero
#Jose Garcia Ledesma
#CST 205 - Lab 8
#Nov 19, 2017

#Decrease volume by half
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value / 2)
      
#Changes volume of sound by given percentage
#Increase volume if factor greater than 0%
#Decrease volume if factor less than 0%
def changeVolume(sound, factor):
  if factor > 0:
    pct = (factor/100.0) + 1
  if factor < 0:
    pct = (100 + factor)/100.0
    
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * pct)
          
#Finds the maximum sample value
def maxSample(sound):
  maxVal = getSampleValueAt(sound, 0)
  for i in range(0, getLength(sound)):
    maxVal = max(maxVal, getSampleValueAt(sound,i))
  return maxVal
  
def maxVolume(sound):
  maxVal = maxSample(sound)
  factor = 32767.0/maxVal
  for i in range(0, getLength(sound)):
    value = getSampleValueAt(sound,i)
    setSampleValueAt(sound,i, value * factor)
    
#Sets sample to 32767 if greater than 0 and set sample to -32767 is less than 0
def goToEleven(sound):
  for sample in getSamples(sound):
    if getSampleValue(sample) > 0:
      setSample(sample, 32767)
    if getSampleValue(sample) < 0:
      setSample(sample, -32767)
