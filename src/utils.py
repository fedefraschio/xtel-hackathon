import numpy as np

def mape_per_product(y_true, y_pred, product_ids, eps=1e-6):
    mape_list = []
    for pid in np.unique(product_ids):
        mask = product_ids == pid
        y_t = y_true[mask]
        y_p = y_pred[mask]

        # evita divisioni per zero
        y_t = np.where(y_t == 0, eps, y_t)

        mape = np.mean(np.abs((y_t - y_p) / y_t))
        mape_list.append(mape)

    return np.mean(mape_list)
