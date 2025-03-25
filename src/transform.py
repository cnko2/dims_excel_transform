import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('../input/dims_label.xlsx')

# 初始化結果列表
result = ["欄位"]

# 記錄前一列的 ServerFarm 和 Rack
prev_farm, prev_rack = None, None

# 依序處理每一列資料
for _, row in df.iterrows():
    # 如果 ServerFarm 或 Rack 變了，則加入
    if row['ServerFarm'] != prev_farm or row['Rack'] != prev_rack:
        result.append(row['ServerFarm'])
        result.append(row['Rack'])
    
    # 一律加入 HostName 和 Label
    result.append(row['HostName'])
    result.append(row['Label'])

    # 更新前一列的 ServerFarm 和 Rack
    prev_farm, prev_rack = row['ServerFarm'], row['Rack']

# 儲存轉置結果
df_out = pd.DataFrame(result)
df_out.to_excel('../output/轉置結果.xlsx', index=False, header=False)

print("轉置完成，已儲存為 '轉置結果.xlsx'")
