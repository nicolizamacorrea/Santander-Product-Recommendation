def get_paramslist(N):
    parmslist = [{'objective': 'multi:softprob',
                  'eta': 0.051,
                  'max_depth': 6,
                  'silent': 1,
                  'num_class': N,
                  'eval_metric': "mlogloss",
                  'min_child_weight': 2.05,
                  'subsample': 0.92,
                  'gamma': 0.65,
                  'colsample_bytree': 0.9,
                  'seed': 125
                  },
                 {'objective': 'multi:softprob',
                  'eta': 0.05,
                  'max_depth': 4,
                  'silent': 1,
                  'num_class': N,
                  'eval_metric': "mlogloss",
                  'min_child_weight': 2,
                  'subsample': 0.9,
                  'colsample_bytree': 0.9,
                  'seed': 125,
                  },
                 {'objective': 'multi:softprob',
                  'num_class': N,
                  'colsample_bytree': 0.9181423087392605,
                  'gamma': 1.3122701510124506,
                  'max_depth': 5,
                  'min_child_weight': 4,
                  'subsample': 0.93981772820158194,
                  'seed': 123,
                  'eta': 0.05,
                  'silent': 1,
                  'eval_metric': "mlogloss",
                  },
                 {'objective': 'multi:softprob',
                  'num_class': N,
                  'colsample_bytree': 0.810195135669,
                  'gamma': 1.6446531418,
                  'max_depth': 4,
                  'min_child_weight': 2,
                  'subsample': 1.0,
                  'seed': 123,
                  'eta': 0.205950347095,
                  'silent': 1,
                  'eval_metric': "mlogloss",
                  },
                 {'objective': 'multi:softprob',
                  'num_class': N,
                  'colsample_bytree': 0.85,
                  'gamma': 0,
                  'max_depth': 6,
                  'min_child_weight': 10,
                  'subsample': 0.8,
                  'seed': 0,
                  'eta': 0.06,
                  'silent': 1,
                  'eval_metric': "mlogloss",
                  },
                 {'objective': 'multi:softprob',
                  'num_class': N,
                  'colsample_bytree': 0.7,
                  'gamma': 4.95,
                  'max_depth': 8,
                  'min_child_weight': 7,
                  'subsample': 0.73,
                  'seed': 123,
                  'eta': 0.05,
                  'silent': 1,
                  'eval_metric': "mlogloss",
                  },
                 {'objective': 'multi:softprob',
                  'num_class': N,
                  'colsample_bytree': 0.787,
                  'gamma': 3.9788,
                  'max_depth': 5,
                  'min_child_weight': 6,
                  'subsample': 0.9,
                  'seed': 123,
                  'eta': 0.0185,
                  'silent': 1,
                  'eval_metric': "mlogloss",
                  }
                 ]
    num_rounds_list = [115, 190, 200, 373, 50, 370, 379]
    return parmslist, num_rounds_list
