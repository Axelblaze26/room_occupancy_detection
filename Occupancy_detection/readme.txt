Problem Statement:
     As part of Data Science team operating in the Smart Housing solution I built ML model to detect occupancy on
floor area. As Proof-of-concept I have generated ML model pipeline
that accepts the input CSV file and store the prediction for the review as output_room_occupancy.csv.

Methodology:
1.Unzip the file
2.open terminal where you have extracted the folder
3.type command "pip install -r requirements.txt" and press enter
  which will download all the necessary packages for this project.
4.after that give command "python pipeline.py"
5.After program run successfully it will ask the path of input csv file.
6.after giving it path it will export the desired output file in current working directory.

Classification report:
                 precision    recall  f1-score   support

           0       0.96      0.90      0.93      4740
           1       0.91      0.96      0.93      4746

    accuracy                           0.93      9486
   macro avg       0.93      0.93      0.93      9486
weighted avg       0.93      0.93      0.93      9486

accuracy score on test dataset:89%
model is created using artificial neural network.

Confusion Matrix:

[[4271   469]
 [192    4554]]
TP= 4271
FP=469
TN=192
FN=4554


Model Comparison:

two models xgboost and ann are created.
but xgboost model was overfitted with precision 1.00,recall 0.99 and accuracy 0.99
so,ann model is used for final implementation which have relatively better metrics.


Conclusion:

room occupancy detection has the following benefits:
1.User experience:
  Occupancy detection systems can create a more comfortable environment for occupants
  by automatically adjusting lighting, temperature, and other factors based on their
  presence and preferences. This personalization enhances user experience and satisfaction.

2.Security:
  Occupancy detection can integrate with security systems to detect unauthorized access
  or suspicious activities.

3.Smart Building Systems: Occupancy detection can integrate with other smart building
  systems, such as access control, lighting control, or building automation systems.

Hence, room occupancy detection can be used in many ways for taking data driven decisions.


