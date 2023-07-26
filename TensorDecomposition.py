import numpy as np
from NTD import non_negative_tucker_core

# tensor_0とtensor_allをnpyファイルから読み込む
tensor_0 = np.load('tensor_0.npy')
tensor_1 = np.load('tensor_1.npy')
tensor_2 = np.load('tensor_2.npy')
tensor_all = np.load('tensor_all.npy')

# 以下は先ほどのコードと同じです
import numpy as np
from tensorly.decomposition import non_negative_tucker
import time

# tensor_0, tensor_1, tensor_2, tensor_allの定義や読み込み

def ntd(tensor, rank_list):
    # Non-negative Tucker decompositionを実行する関数
    return non_negative_tucker(tensor, rank_list, tol=1.0e-10, n_iter_max=100)

# rank_listは各モードのランクを指定するリスト [R1, R2, R3]
rl1 = 4
rl2 = 4
rl3 = 4
rank_list = [rl1, rl2, rl3]

cp = 0

# CP分解をするかどうかのフラグ cp (0: CP分解をしない, 1: CP分解をする)
if cp == 0:
    # Non-negative Tucker decompositionをtensor_0, tensor_1, tensor_2, tensor_allに対して実行
    tt0, u0 = ntd(tensor_0, rank_list)
    tt1, u1 = ntd(tensor_1, rank_list)
    tt2, u2 = ntd(tensor_2, rank_list)
    tt3, u3 = ntd(tensor_all, rank_list)

    # tt0, tt1, tt2を結合して平均をとる
    tt0 = (tt0 + tt1 + tt2) / 3

if cp == 1:
    # tt0を指定した形状で生成 (ここでは対角行列の場合)
    tt0 = np.zeros((rl1, rl2, rl3))
    tt0[0, 0, 0] = 1
    tt0[1, 1, 1] = 1
    tt0[2, 2, 2] = 1
    tt0[3, 3, 3] = 1

# 開始
start_time = time.perf_counter()

# 1回目のNon-negative Tucker decomposition
# a0はtt0に対するTuckerコアテンソル、b0はu0に対するTuckerファクター
a0, b0 = non_negative_tucker_core(tensor_0, rank_list, tt0, u0, tensor_all)

# 2回目のNon-negative Tucker decomposition
a1, b1 = non_negative_tucker_core(tensor_1, rank_list, tt0, b0, tensor_all)

# 3回目のNon-negative Tucker decomposition
a2, b2 = non_negative_tucker_core(tensor_2, rank_list, tt0, b0, tensor_all)

# 修了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time0 = end_time - start_time

# 開始
start_time = time.perf_counter()

# tensor_allに対してNon-negative Tucker decompositionを実行
a3, b3 = non_negative_tucker_core(tensor_all, rank_list, tt0, b0, tensor_all)

# 修了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time1 = end_time - start_time

print("Elapsed time for a0, a1, a2:", elapsed_time0)
print("Elapsed time for a3:", elapsed_time1)

# 結果をファイルに保存
np.save('tensor_decomposition_a0.npy', a0)
np.save('tensor_decomposition_a1.npy', a1)
np.save('tensor_decomposition_a2.npy', a2)
np.save('tensor_decomposition_a3.npy', a3)

# リスト内の各要素を個別に保存
for i, item in enumerate(b0):
    np.save(f'tensor_decomposition_b0_{i}.npy', np.array(item))

for i, item in enumerate(b1):
    np.save(f'tensor_decomposition_b1_{i}.npy', np.array(item))

for i, item in enumerate(b2):
    np.save(f'tensor_decomposition_b2_{i}.npy', np.array(item))

for i, item in enumerate(b3):
    np.save(f'tensor_decomposition_b3_{i}.npy', np.array(item))


c1 = np.zeros((rl1*rl2*rl3))
c2 = np.zeros((rl1*rl2*rl3))
c3 = np.zeros((rl1*rl2*rl3))
c4 = np.zeros((rl1*rl2*rl3))
count = 0
mem = []

for i in range(0, rl1):
    for j in range(0, rl2):
        for k in range(0, rl3):
            mem.append(str(i) + str(j) + str(k))
            c1[count] = a0[i, j, k]
            c2[count] = a1[i, j, k]
            c3[count] = a2[i, j, k]
            c4[count] = a3[i, j, k]
            count += 1

# Save the arrays as .npy files
np.save('c1.npy', c1)
np.save('c2.npy', c2)
np.save('c3.npy', c3)
np.save('c4.npy', c4)
np.save('mem.npy',mem)
