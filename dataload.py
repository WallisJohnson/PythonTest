import numpy as np

data_path = '/home/g/junk/KFIR ABERMAN/deep-motion-editing-master/style_transfer/probe/../data/xia.npz'
dataset = np.load(data_path, allow_pickle=True)['train'].item()
motions, labels, metas = dataset["motion"], dataset["style"], dataset["meta"]
label_i = labels
len = len(label_i)
n = metas["style"][1]
new_metas0 = [{key: metas[key][i] for key in metas.keys()} for i in range(3)]
new_metas = [{key: metas[key][i] for key in metas.keys()} for i in range(len)]

print("yes")