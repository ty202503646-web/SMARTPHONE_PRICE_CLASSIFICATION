import numpy as np
from .ml_model import model

FEATURE_ORDER = [
    'battery_power','blue','clock_speed','dual_sim','fc','four_g',
    'int_memory','m_dep','mobile_wt','n_cores','pc','px_height',
    'px_width','ram','sc_h','sc_w','talk_time','three_g',
    'touch_screen','wifi'
]

def predict_price(data):
    features = np.array([data[f] for f in FEATURE_ORDER]).reshape(1, -1)
    return int(model.predict(features)[0])