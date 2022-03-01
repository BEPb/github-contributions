![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/github-contributions) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/github-contributions)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/github-contributions)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/github-contributions) 
![GitHub](https://img.shields.io/github/license/BEPb/github-contributions) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/github-contributions)
![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)
<p align="left">
<img src="https://visitor-badge.laobi.icu/badge?page_id=BEPb.github-contributions" alt="visitors"/>
</p>

閱讀其他語言： [English](README.md), [हिन्दी](README.hindi.md), [中國人](README.chinese.md)
# GitHub 貢獻
如果你想美化你的 GitHub 活動歷史，那麼 Python 腳本 ``github_paint.py`` 的能力
將幫助您更換指定時期的供款。

## 重做 GitHub 上的活動，繪製個人資料
作為來源，您必須提前準備 52 x 7 像素的圖像：它將
代表您自動轉換為提交到您的單獨存儲庫。


該程序本身使用 README.md 文件初始化一個空存儲庫，並開始生成文件更新
添加貢獻： YYYY-MM-DD HH:MM 為您提交的每個提交。

使用 --date 開關創建
在過去提交。

＃＃＃ 如何使用
1. 創建一個新的空 GitHub 存儲庫。不要包含 README.md 文件，也不要初始化存儲庫。
2. 克隆此存儲庫或複制 github_paint.py 文件和您的提交繪圖。
3. 在存儲庫中，打開 html 頁面 Git.html 並繪製您的繪圖
4. 保存您的繪圖
5. 將其轉換為 52x7
6. 將 github_paint.py 中的行更改為您的繪圖文件名和您將在一年中的最後一天
   貼出你的畫
7. 使用密鑰（您的存儲庫的地址）運行 github_paint.py 程序，如下例所示：
```commandline
python github_paint.py --repository = https: //github.com/user/repo.git
```
 （HTTPS方式：賬號認證）
這個過程不需要太多時間（3-5分鐘）。
7.享受結果

> 注意：
如果您曾經在存儲庫中使用過這個腳本，那麼您將無法在同一個存儲庫中重複它。
您將不得不創建另一個存儲庫，否則您將在腳本日誌中收到錯誤。
強調使用尚未初始化的存儲庫。



### 工作示例：
1.初始繪圖`GENOM`：

![](./example/genom.png)

相同的繪圖，但分辨率為 52x7：
![](./example/genom_mini.png)

結果：
![](./example/genom_res.png)

2. 原圖 `I love Python`:

![](./example/i_l_p.png)

相同的繪圖，但分辨率為 52x7：
![](./example/i_l_p_mini.png)

結果：
![](./example/i_l_p_res.png)

2. 原圖 `I love Python`:

![](./example/heart.png)

相同的繪圖，但分辨率為 52x7：
![](./example/heart_mini.png)

結果：
![](./example/heart_res.png)

3. 原圖 `I love you`:

![](./example/I_love_you.png)

相同的繪圖，但分辨率為 52x7：
![](./example/I_love_you_mini.png)

結果：

![](./example/I_love_you_res.png)

4. 原圖`bugs, hex, sux`:

![](./example/bugs_hex_sux.png)

相同的繪圖，但分辨率為 52x7：
![](./example/bugs_hex_sux_mini.png)

結果：

![](./example/bugs_hex_sux_res.png)


5. 原圖 `do it`:

![](./example/do_it.png)

相同的繪圖，但分辨率為 52x7：
![](./example/do_it_mini.png)

結果：
![](./example/do_it_res.png)

6. 原圖 `pacman`:

![](./example/pacman.png)

相同的繪圖，但分辨率為 52x7：
![](./example/pacman_mini.png)

結果：
![](./example/pacman_res.png)

7. 原圖 `send nudes`:

![](./example/send_nudes.png)

8. 原圖 `sex_drugs_alco`:

![](./example/sex_drugs_alco.png)


所有工作示例都放置在“示例”文件夾中
ps 長期計劃創建一個 GUI 應用程序或 html 頁面，您可以在其中執行所有操作
在上傳到存儲庫之前繪製，但是還沒有時間......所以所有愛好者都開發這個項目
我邀請你參與，創建你自己的分支。

p.s.s. 如果你喜歡這個項目，別忘了給個星星，如果你有興趣，就註冊成為關注者。

