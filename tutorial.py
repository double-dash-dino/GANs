# run the installs

pip install keras
pip install tensorflow

# Run the imports
from keras.datasets.cifar10 import load_data
from matplotlib import pyplot

(trainX, trainy), (textX, testy) = load_data