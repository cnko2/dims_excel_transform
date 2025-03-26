import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('../input/dims_label.xlsx')
output_excel_file = ('../output/KYEC_DIMS_20250326.xlsx')

# 初始化結果列表
result = []

# 記錄前一列的 ServerFarm 和 Rack
prev_farm, prev_rack = None, None

# 逐行處理資料
for _, row in df.iterrows():
    # 拆分 QRCode，避免變成 List 格式
    qrcode = str(row['QRCode']).strip("[]").replace("'", "").split(", ")[-1]  # 取最後的 UUID 部分

    # 如果 ServerFarm 或 Rack 變了，則加入一次
    if row['ServerFarm'] != prev_farm or row['Rack'] != prev_rack:
        result.append([row['ServerFarm'], qrcode])
        result.append([row['Rack'], qrcode])

    # 加入 HostName 和 Label
    result.append([row['HostName'], qrcode])
    result.append([row['Label'], qrcode])

    # 更新前一列記錄
    prev_farm, prev_rack = row['ServerFarm'], row['Rack']

# 轉換為 DataFrame 並存檔
df_out = pd.DataFrame(result, columns=["KYEC", "QRCode"])
df_out.to_excel(output_excel_file, index=False)

print("轉置完成，已儲存為 '", output_excel_file)