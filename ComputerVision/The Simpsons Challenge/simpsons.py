import argparse, os
import numpy as np

#IMPORTANT: Your solution should not take more than 5 minutes to provide outputs

###########################################################
#Class names and numbers 
classes = {'bart': 0,'homer':1,'lisa': 2,
           'marge': 3,'maggie' : 4}

#Write output
def write_output(x,y,output_name):
    fd = open(output_name,'w')

    for fname,label in zip(x,y):        
        fd.write(f'{fname} {label}\n')

    fd.close()

###########################################################
parser = argparse.ArgumentParser(description='Simpsons classification.')

parser.add_argument('--train', required=True)
parser.add_argument('--test', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

#Data Loader
x_train=[]
y_train=[]
with open(args.train) as fd_train:
    for line in fd_train:
        line = line.strip()
        x_train.append(line)
        label = line.split('/')[-1][:-7] #remove 000.bmp
        label = classes[label]
        y_train.append(label)


x_test=[]
y_test=[]
with open(args.test) as fd_test:
    for line in fd_test:
        line = line.strip()
        x_test.append(line)	

        label = line.split('/')[-1][:-7] #remove 000.bmp
        label = classes[label]
        y_test.append(label)


x_train = np.array(x_train)
x_test = np.array(x_test)

y_train = np.array(y_train)
y_test = np.array(y_test)

##########################################
#your code goes here
#read image data based on train path samples
#process and feature extraction
#training
#evaluation
    
#A dummy prediction (random)
#To better illustrate, lets say that random function could predict test samples
#So, the 'y' is an array of the same size as x_test. Both arrays are direct related
y = np.random.randint(0,6,size=x_test.shape[0])	
#####################

#Writes the result to the output
#x_test == test filenames
#y == predicted labels
write_output(x_test,y,args.output)



#%%
