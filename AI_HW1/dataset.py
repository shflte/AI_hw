import os
import numpy as np
import cv2

def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1)
    # dataset = []
    # for folder in os.listdir(dataPath):
    #     if folder == 'face':
    #       for filename in os.listdir(os.path.join(dataPath, folder)):
    #         img = cv2.imread(os.path.join(os.path.join(dataPath, folder), filename))
    #         temp = (img, 1)
    #         dataset.append(temp)
    #     else:
    #       for filename in os.listdir(os.path.join(dataPath, folder)):
    #         img = cv2.imread(os.path.join(os.path.join(dataPath, folder), filename))
    #         temp = (img, 0)
    #         dataset.append(temp)

    dataset=[]
    rootDir = dataPath
    for lists in os.listdir(rootDir): 
      path = os.path.join(rootDir, lists) 
      for subpath in os.listdir(path):
        temp=[]
        ans = os.path.join(path, subpath) 
        img = cv2.imread(ans,0)
        np.array(img)
        if lists=='face':
          temp.append(img)
          temp.append(1)
        else:
          temp.append(img)
          temp.append(0)
        dataset.append(temp)

    # End your code (Part 1)
    return dataset
