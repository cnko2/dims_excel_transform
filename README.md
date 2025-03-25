# DIMS Label 列印準備


## 方法

1. 顯示 ServerFarm
2. 顯示 Rack
3. 顯示 Hostname
4. 顯示 Label

```text
如果 ServerFarm 以及 Rack 與前一列的相同，則不再顯示，只要顯示HostName 及 Label
```

原始資料

```code
ServerFarm | Rack | HostName | Label
SF1        | A1   | Server1  | Server001
SF1        | A1   | Server2  | Server002
SF2        | A1   | Server3  | Server003
SF3        | A1   | Server3  | Server003
```

轉換後資料

```code
欄位
SF1
A1
Server1
Server001
Server2
Server002
SF2
A1
Server3
Server003
SF3
A1
Server3
Server003
```
