from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay
from matplotlib import pyplot as plt

def curve(classifier, X_test, y_test):

    # Get predicted probabilities for the positive class
    y_pred_proba = classifier.predict_proba(X_test)[:, 1]

    # Compute ROC curve values
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

    # Create the display object and plot the ROC curve
    roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr)

    roc_display.plot()
    plt.show()

    return roc_display