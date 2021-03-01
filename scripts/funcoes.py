def infoclientesum(base,carac):
   return base.groupby(carac)['CLIENTNUM'].count()


def matriz_de_confusão(modelo,X_train, y_train, X_test, ytest):
   return (modelo.fit(X_train, y_train)
            ypred = m.predict(X_test)


    tn, fp, fn, tp = confusion_matrix(ytest, ypred).ravel()
    print("True Positive: " + str(tp))
    print("True Negative: " + str(tn))
    print("False Positive: " + str(fp))
    print("False Negative: " + str(fn))
       
   )