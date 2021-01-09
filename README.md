# AIHealthCare
Projects pertaining to ComputerVision, Neural Net ,Deep Learning, Machine Learning applications in Healthcare.

## Pneumonia Detection using PyTorch
 Datasets used in this project. https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia#chest_xray.zip

## Description

The intention of this project is to create several architectures based on CNN that would detect  Pneumonia in given test images and classify them as "NORMAL" or "PNEUMONIA".

### Architecture One 
This architecture is designed from scratch wihout using any Transfer Learning.
Below is a snapshot of Architecture
XRayNet(
  (conv1): Conv2d(3, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv2): Conv2d(16, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv3): Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv4): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (conv5): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  (pool): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (fc1): Linear(in_features=12544, out_features=200, bias=True)
  (fc2): Linear(in_features=200, out_features=2, bias=True)
  (dropout): Dropout(p=0.2, inplace=False)
)

For this model, I used CrossEntropyLoss and Adam Optimizer. The training data from Kaggle had  1340 images for NORMAL and 3876 images for PNEUMONIA. 

Test Accuracy of     NORMAL: 62% (147/234)
Test Accuracy of     PNEUMONIA: 97% (381/390)

Test Accuracy (Overall): 84% (528/624)

The Same model was trained again with a more balanced data i.e. 1340 images each under NORMAL and PNEUMONIA with below results:
Test Accuracy of     NORMAL: 70% (165/234)
Test Accuracy of     PNEUMONIA: 89% (209/234)

Test Accuracy (Overall): 79% (374/468)
