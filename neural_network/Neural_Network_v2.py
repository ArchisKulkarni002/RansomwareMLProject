import numpy as np
import pickle

np.seterr(over='ignore')
learningRate = 0.1

#These are  data normalization functions

def minmax(input,derivative=False):
    return input/(np.amax(input)-np.amin(input)) if derivative else (input-np.amin(input))/(np.amax(input)-np.amin(input))

def zscore(input):
    return input - np.mean(input)/np.std(input)

#these are activation functions
def sigmoid(x,derivative=False):
    sigm=1. / (1. + np.exp(-x))
    return np.array([sigm * (1-sigm)]) if derivative else sigm  #Returns sigmoid if der is flase else returns der of sigmoid

def Lrelu(image,derivative=False):
    return np.array([image.clip(0.001,1)])if derivative else image.clip(0.001) #Returns relu if false

def relu(image,derivative=False):
    return np.array([image.clip(0,1)])if derivative else image.clip(0) #Returns relu if false

def softmax(input,derivative = False):
    exp = np.exp(input-np.max(input))
    softmax = exp / np.sum(exp)
    if derivative:
        return np.array([softmax*(1-softmax)])
    else:
        return softmax
def linear(input,derivative=False,a=0.3):
    return np.array([[a]]) if derivative else input*a

#Used to convert list object to  numpy array
# Arg:list object
#returns: numpy array
def convert_to_array(input):
    return np.concatenate(input).ravel()

#Used to calculate error
# Arg:layer object, target array,derivative
#returns: mean square error or its derivative
def getError(layer,target,derivative=False):
    return target-layer.out if derivative else np.square(target-layer.out)/(2*len(layer.out)) #returns the final error. To be used for final layer

def cross_entropy_error(predicted, target, derivative=False):
    if derivative:
        return predicted - target  # Derivative of cross-entropy
    else:
        epsilon = 1e-12  # Small value to prevent log(0)
        return -np.sum(target * np.log(predicted + epsilon))

#Used to create normalization layer
class NormalizeLayer:
    #Args: input, data type of input
    def __init__(self,input,input_type = 'array'):
        if input_type == 'array':
            self.images = input
        if input_type == 'list':
            self.images = convert_to_array(input)
    #Forward prop
    def train(self,function='minmax'):
        if function=='minmax':
            self.images = minmax(self.images)
    #Back prop
    def backprop(self):
        self.images = minmax(self.images,True)

#Used to create general nn layer
class Layer:
    #Args: number of inputs, number of perceptrons in layer,learning rate, activation function
    def __init__(self,numip,numpercep,learning_rate=0.1,activation='relu'):
        self.input = None #inputs to layer
        self.numpercep = numpercep                              #number of perceptrons in layer
        self.activation = activation                            #activation function to be used
        self.lr = learning_rate                                 #learning rate to be used
        # self.We = np.random.rand(numpercep, numip)/10           #weights array
        # self.We = np.zeros((numpercep, numip))                # weights array
        self.We = np.random.normal(0, 1/numpercep, (numpercep,numip))
        self.Bi = np.random.rand(numpercep)                     #bias array
        self.out = np.empty(numpercep)                          #output array
        self.z = np.empty(numpercep)                            #intermidiate calculation array

    #forward propogation
    def train(self,input,a=0.3):
        self.input = input  # inputs to layer
        self.z = np.array(list(self.calcZ(self.input,self.We[i],self.Bi[i]) for i in range(self.numpercep))) #get intermidiate calculations
        if self.activation == 'relu':
            self.out = relu(self.z) #get final output
        elif self.activation == 'softmax':
            self.out = softmax(self.z) #get final output
        elif  self.activation == 'sigmoid':
            self.out = sigmoid(self.z) #get final output
        elif  self.activation == 'linear':
            self.out = linear(self.z,a=a) #get final output
        elif  self.activation == 'Lrelu':
            self.out = Lrelu(self.z) #get final output


    #backward propogation
    def backprop(self,error,a=0.3):
        if self.activation == 'relu':
            self.deract =  relu(self.z,derivative=True)
        elif self.activation == 'softmax':
            self.deract =  softmax(self.z,derivative=True)
        elif self.activation == 'sigmoid':
            self.deract =  sigmoid(self.z,derivative=True)
        elif self.activation == 'linear':
            self.deract =  linear(self.z,a=a,derivative=True)
        elif self.activation == 'Lrelu':
            self.deract =  Lrelu(self.z,derivative=True)
        self.delbi = error * self.deract                #change in bias
        self.delwe = np.array([self.input]).T*self.delbi                #change in weights
        self.delip = np.dot(self.delbi,self.We)                 #error for previous layer
        self.We = np.add(self.We.T,learningRate*self.delwe)                 #change weights
        self.Bi = np.add(self.Bi, learningRate*self.delbi)              #change biases
        self.We = self.We.T
        self.Bi = self.Bi.T[:,0]

    def calcZ(self,input,weight,bias):
        return np.dot(weight,input)+bias                #intermidiate calculation

    #Used to save learnable parameters of the layer
    def save(self,name,filepath=''):
        if filepath:
            name = filepath+name
        savingDict = {'weight':self.We,'bias':self.Bi}
        with open(str(name),'wb') as outfile:
            pickle._dump(savingDict, outfile)

    # Used to load learnable parameters of the layer
    def load(self, filename,filepath=''):
        if filepath:
            filename = filepath+filename
        with open(filename,'rb') as infile:
            loadingDict = pickle._load(infile)
        self.We = loadingDict['weight']
        self.Bi = loadingDict['bias']

