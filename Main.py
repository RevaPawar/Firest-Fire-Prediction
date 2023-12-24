import pickle
import numpy

model = pickle.load(open('model.pkl','rb')) #rb = read binary

temp = int(input('Enter Temperature : '))#input from user
oxygen = int(input('Enter Oxygen : '))#input from user
humid = int(input('Enter Humidity : '))#input from user

features = [temp,oxygen,humid]
val = [numpy.array(features)]
prediction = model.predict_proba(val)
result = '{0:.{1}f}'.format(prediction[0][1],2)#formatting the result to 2 decimal places

if result > str(0.5):
    print('Your Forest is in Danger.\nProbability of fire occuring is {}' (result))
else:
    print('Your Forest is safe.\nProbability of fire occuring is {}' (result))

