# FDA  Submission

**Padma Chandramouli**

**Chest Xray Analyzer for detecting Pneumonia**

## Algorithm Description 

### 1. General Information

**Intended to assist Radiologist in identifying if xray imaging indicates Pneumonia condition.It is not intended for use in supporting life or sustaining life.** 

**Indications for Use: Assist Radiologist in screening Pneomonia between the ages 35-65 year old patients**

**Device Limitations: Difficult to detect Pneumonia when the patient has multiple conditions. Fails to detect Pneumonia in children under the age of 15 **

**Clinical Impact of Performance: Performance can be estimated by ROC curve and ROC AUC for binary classification algorithms. ROC curve summarizes binary classification performance on the positive class. ROCAUC (area under curve) is useful if one want to compare performance of multiple models. From my algorithm prespective, with limited data for training, the average precision is 0.5 which makes is a mediocre model for classification.With precision being 0.5 we can identify Penumonia in only 50% of the patients correctly.The value of False Positives and False negatives are pretty high and almost equal to True Positives. Hence this algorithm as is cannot be used to classify Pneumonia**

### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps:Exploratory Data Analysis was conducted to determine the age group we had xray images for which was between 35-65 years. Determined if Pneumonia occurs with other diseases or as a standalone condition. Determined how many cases of Penumonia existed vs cases no Pneumonia cases to understand Imbalance data.**

**Preprocessing Steps: Reshape the image (224,224) so it could be accepted as input to the model. Rotate the images by an angle of 5-10 deg. Horizontally flip, zoom in a bit and shear/crop the images. **

**CNN Architecture:Architecture uses transfer learning to use VGG16 model with last Maxpool layer replaced with 4 Fully connected layers. Each of these 4 layers have a Relu activation function and are followed by Dropout layer to reduce overfitting. The 5th layer has an activation Sigmoid to determine probability of Pneumonia. **


### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training
* Batch size
* Optimizer learning rate : 0.0001
* Layers of pre-existing architecture that were frozen: block1_conv1 to block5_conv3
* Layers of pre-existing architecture that were fine-tuned:block5_pool
* Layers added to pre-existing architecture: 5 fully connected layers. 

<< Insert algorithm training performance visualization >> Please refer to plot_history()from Build and Train Model notebook

<< Insert P-R curve >>plot_roc_curve() and plot_precision_recall_curve() from Build and Train Model notebook

**Final Threshold and Explanation:**

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:Split data to 20% validation set and 80% Training set. We also create balanced training set containing same number of Pneumonia and non Pneumonia cases.** 


**Description of Validation Dataset: Validation dataset should not be augmented. However they need to be resized to match the input dimensions and normalize them. There is no need to create Balanced data set. ** 


### 5. Ground Truth
"pneumonia_class" can be used as ground truth for the algorithm. However in reality we need to rely on existing device/aglorithm to compare performance with or use silver standard.



### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:** The training data had majority data from age group of 35-70. So the algorithm can be used for Pneumonia detection int the age group of 35-70.

**Ground Truth Acquisition Methodology: For now its keras, however in reality we need to collaborate with hospitals/clinics to get data and make sure that we have permission to use patient personal information or rather not use data that would identify patient and violiate HIPAA ** 

**Algorithm Performance Standard: It is difficult to get a gold standard We could compare our algorithm with the same xray images that was run through 2-3 radiologists. and then come up with ground truth based on observations of these 3 radiologists.**
