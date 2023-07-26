import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def spaceRowHeatDifOut(t0, t1, folder_name):
    plt.figure(figsize=(10, 10))
    a = t0[1][:, :]
    b = t1[1][:, :]
    ab = abs(a - b)

    print("誤差")
    print(ab.sum())

    sns.heatmap(ab, vmin=0, vmax=1)
    
    # 保存先のフォルダが存在しない場合は作成
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 画像ファイルとしてヒートマップを保存
    plt.savefig(os.path.join(folder_name, f'heatmap_{len(os.listdir(folder_name))}.png'))
    plt.close()
    return ab

# 結果を保存するフォルダーの名前を指定
result_folder = 'result'

# b0からb2を読み込む
b0_list = [np.load(f'tensor_decomposition_b0_{i}.npy') for i in range(3)]
b1_list = [np.load(f'tensor_decomposition_b1_{i}.npy') for i in range(3)]
b2_list = [np.load(f'tensor_decomposition_b2_{i}.npy') for i in range(3)]
b3_list = [np.load(f'tensor_decomposition_b3_{i}.npy') for i in range(3)]

# Create an empty list to store the results
results = []

# Call spaceRowHeatDifOut function for each pair of tensors and store the results
results.append(spaceRowHeatDifOut(b0_list, b1_list, result_folder))
results.append(spaceRowHeatDifOut(b0_list, b2_list, result_folder))
results.append(spaceRowHeatDifOut(b0_list, b3_list, result_folder))
results.append(spaceRowHeatDifOut(b1_list, b2_list, result_folder))
results.append(spaceRowHeatDifOut(b1_list, b3_list, result_folder))
results.append(spaceRowHeatDifOut(b2_list, b3_list, result_folder))

# Save the results list as a numpy array
np.save(os.path.join(result_folder, 'results.npy'), np.array(results))

plt.show()
