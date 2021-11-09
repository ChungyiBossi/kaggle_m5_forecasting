# kaggle_m5_forecasting

## 探索性資料分析與分析結果說明
### Food / Hobbies / Household 三大類商品種類數
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Amount_of_items_by_category.jpg)
以種類數目來說, FOOD類較另外兩類為多, HOBBIE類型為最少

### 同大類總銷售數目
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Total_sales_by_item_type.jpg)
除了符合1.以外，銷售數量的成長也以FOOD的幅度為最大
--> 推測各分店的主要商品為FOOD類

### 個別商品的日銷售數
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/FOODS_3_090_SALE_AMOUNT.jpg)
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/HOBBIES_1_002_SALE_AMOUNT.jpg)
日銷量也以FOOD類為最多，每日也幾乎都有量，除了一開始有一段時間沒有銷出
--> 推測期間該商品可能不在架上
HOBBIES類則相對隨機，常在0 ~ 個位數間跳動
--> 推測可能跟節日有關

### Trend
觀察賣出量的分佈
#### FOODS_3_090_CA_3
1. 越接近假日前後，銷量越大，反之禮拜四為最低，可能為一種家庭下廚之常見食品
2. 2012後可能有相同定位之產品取而代之
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Trend_FOODS_3_090_CA_3_validation.jpg)
#### HOBBIES_1_234_CA_3
1. 1/6/12 為該商品之高峰期
2. 2014/2015年該產品銷量有大幅度成長
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Trend_HOBBIES_1_234_CA_3_validation.jpg)
#### HOUSEHOLD_1_118_CA_3
1. 7月的銷量低
2. 禮拜二銷量最多，但隨之而抵減
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Trend_HOUSEHOLD_1_118_CA_3_validation.jpg)
#### More "Trend"
觀察其他種商品
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/Trend_Random_Sample_Twenty.jpg)

### Data rolling for each store
觀察各分店的銷售情況
![](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/img/rolling_90_Day.jpg)

## 模型選用策略與模型架構
針對每一種商品（不同分店也視為不同種商品）做forecasting prediction
### 使用28日MA線做初步的分析, 取得初步的結果 [submission_ma](https://github.com/ChungyiBossi/kaggle_m5_forecasting/blob/main/submission_ma.csv)
### 使用 facebook prophet分析
1. 目前挑出三種商品: HOBBIES_1_001_CA_1_validation / HOUSEHOLD_1_001_CA_1_validation / FOODS_1_001_CA_1_validation
2. 整理snap day（補助日？）訊息，並加入feature內
3. 用multi-processing跑模型

## 預測效度與結果說明與可優化事項
1. 應該要減少訓練的模型數量，可以更好的知道全局的訊息，也能避免在新商品還未有足夠資訊的狀況下，喪失預測的能力
2. 嘗試用XGBoost，應該可以更有效率的訓練全局模型
3. snap day 可能只代表發放日，但是補助的使用期限可能數週或甚至數月，還未查詢相關知識 > <
4. 商品價格的資訊沒有使用到，可能可以藉此獲得3.的使用分佈
5. 沒有跑完Prophet....
6. 更多值得嘗試的演算法以及LeaderBoard遍地的idea

## 此模型可運用的其他場景(Optional)
1. 各大電商的銷售策略預測
2. 傳產股市分析
3. 金融產品的銷售情形

# Thank you for your time
