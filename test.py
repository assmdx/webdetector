import sys
import os
sys.path.append(os.path.abspath("./model"))
import Dataprocess
import model
data = Dataprocess.Dataprocess ("www.baidu.com")
print(model.predict(data))