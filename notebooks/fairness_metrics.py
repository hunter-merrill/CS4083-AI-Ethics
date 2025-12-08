from sklearn.metrics import confusion_matrix


def demographic_parity(data, majority, minority):
    try:
        probability_1 = len(
            data[(data["Ethnicity"] == majority) & (data["PredictedDiagnosis"])]
        ) / len(data[(data["Ethnicity"] == majority)])
        probability_2 = len(
            data[(data["Ethnicity"] == minority) & (data["PredictedDiagnosis"])]
        ) / len(data[(data["Ethnicity"] == minority)])
    except:
        return "Invalid"

    return abs(probability_1 - probability_2)


def equal_opportunity(data, majority, minority):
    try:
        conf_matrix_1 = (
            confusion_matrix(
                data[(data["Ethnicity"] == majority)]["TrueDiagnosis"],
                data[(data["Ethnicity"] == majority)]["PredictedDiagnosis"],
            )
            .ravel()
            .tolist()
        )
        conf_matrix_2 = (
            confusion_matrix(
                data[(data["Ethnicity"] == minority)]["TrueDiagnosis"],
                data[(data["Ethnicity"] == minority)]["PredictedDiagnosis"],
            )
            .ravel()
            .tolist()
        )

    except:
        return "Invalid"

    return abs(
        conf_matrix_1[3] / (conf_matrix_1[3] + conf_matrix_1[1])
        - conf_matrix_2[3] / (conf_matrix_2[3] + conf_matrix_2[1])
    )

def equalized_odds(data, majority, minority):
    try:
        tn_maj, fp_maj, fn_maj, tp_maj = (
            confusion_matrix(
                data[(data["Ethnicity"] == majority)]["TrueDiagnosis"],
                data[(data["Ethnicity"] == majority)]["PredictedDiagnosis"],
                labels=[0,1]
            )
            .ravel()
            .tolist()
        )
        tn_min, fp_min, fn_min, tp_min = (
            confusion_matrix(
                data[(data["Ethnicity"] == minority)]["TrueDiagnosis"],
                data[(data["Ethnicity"] == minority)]["PredictedDiagnosis"],
                labels=[0,1]
            )
            .ravel()
            .tolist()
        )

        tpr_maj = tp_maj/(tp_maj + fn_maj)
        tpr_min = tp_min/(tp_min + fn_min)
        fpr_maj = fp_maj/(fp_maj + tn_maj)
        fpr_min = fp_min/(fp_min + tn_min)

        tpr_diff = tpr_min - tpr_maj
        fpr_diff = fpr_min - fpr_maj

    except:
        return "Invalid"

    return [tpr_diff, fpr_diff]


def disparate_impact(data, majority, minority):
    try:
        probability_1 = len(
            data[(data["Ethnicity"] == majority) & (data["PredictedDiagnosis"])]
        ) / len(data[(data["Ethnicity"] == majority)])
        probability_2 = len(
            data[(data["Ethnicity"] == minority) & (data["PredictedDiagnosis"])]
        ) / len(data[(data["Ethnicity"] == minority)])

    except:
        return "Invalid"

    return probability_1 / probability_2