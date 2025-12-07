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
