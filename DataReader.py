import pandas as pd
import numpy as np
from sklearn import preprocessing

class DataReader:
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def read_data(self):
        data_frames = []
        for file_path in self.file_paths:
            df = pd.read_csv(file_path)
            df['time'] = pd.to_datetime(df['time'])
            df = df.sort_values(['time', 'space'])
            data_frames.append(df)
        return data_frames

class DataProcessor:
    def __init__(self, file_paths, months, month1, month2, month3):
        self.file_paths = file_paths
        self.months = months
        self.month1 = month1
        self.month2 = month2
        self.month3 = month3

    def preprocess_data(self, data_frames):
        # データのスケーリング
        df_cluster0_sc = preprocessing.scale(data_frames[0][['AirIn', 'AirOut', 'CPU', 'Water']], axis=0)

        tensor_init = df_cluster0_sc.reshape(-1, 864, 4)
        min_months = min(self.months[self.month1], self.months[self.month2], self.months[self.month3])  # min_monthsを追加
        tensor_0 = tensor_init[self.total1:self.total1+self.months[self.month1], :, :]
        tensor_1 = tensor_init[self.total2:self.total2+self.months[self.month2], :, :]
        tensor_2 = tensor_init[self.total3:self.total3+self.months[self.month3], :, :]
        tensor_all = (tensor_0[:min_months, :, :] +
                      tensor_1[:min_months, :, :] +
                      tensor_2[:min_months, :, :]) / 3

        # テンソルをバイナリ形式で保存
        np.save('tensor_0.npy', tensor_0)
        np.save('tensor_1.npy', tensor_1)
        np.save('tensor_2.npy', tensor_2)
        np.save('tensor_all.npy', tensor_all)

    def process(self):
        self.total1 = sum(self.months[:self.month1])
        self.total2 = sum(self.months[:self.month2])
        self.total3 = sum(self.months[:self.month3])

        data_reader = DataReader(self.file_paths)
        data_frames = data_reader.read_data()
        self.preprocess_data(data_frames)

# 2014年度の5月、4月、3月の実行結果
if __name__ == "__main__":
    months = [30, 31, 30, 31, 31, 30, 25, 30, 31, 31, 28, 31]
    month1 = 2
    month2 = 1
    month3 = 0

    file_paths = ['./2014_drop.csv']

    data_processor = DataProcessor(file_paths, months, month1, month2, month3)
    data_processor.process()
