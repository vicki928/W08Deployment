#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle
import random


# In[2]:


app = Flask(__name__)
api = Api(app)


# In[3]:


def log_transform(x):
    return np.log(x.astype(float) + 1)


# In[4]:


class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        with open('/Users/vickichen/Desktop/mini-project-IV/bestmodel.pickle', 'rb') as f:
            best_model=pickle.load(f)
        res = best_model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist()


# In[5]:


api.add_resource(Scoring, '/scoring')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


# In[ ]:





# In[ ]:




