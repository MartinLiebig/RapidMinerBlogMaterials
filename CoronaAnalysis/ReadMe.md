# About this Project

These processes can be used to download and preprocess data abou the Corona (COVID-19) virus. The data is preprocessed by using a windowing. Afterwards a Neural Network is trained to predict the number of confirmed cases the day after.
We use this model to predict the cases for every country available. This is usually a prediction for the same day you are running it.


# How to Use these processes
To get the processes into RapidMiner you can download the processes as .zip. Afterwards you unpack and copy the files to a subfolder of your Repository Location.
Your Repository is usually available at:

C:\Users\USERNAME\.RapidMiner\repositories\Local Repository
on Windows or
/home/user/USERNAME/.RapidMiner/repositories/Local Repository/
on Mac/Linux.

The main process to run is ! Retrain. Please make sure that you change the value of basePath macro, to ensure that the result files are written to a correct location.



# Credits
Data is pulled from [https://github.com/CSSEGISandData/COVID-19] and is curated by John Hopkins university [https://systems.jhu.edu/]. There is no guarantee for the quality of this data, since sources may differ.
