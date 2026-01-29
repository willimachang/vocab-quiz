# 網站佈署指南

因為這是一個「靜態網站」(Static Website)，由 HTML、JS 和 CSV 組成，所以非常容易發布到網路上，而且完全免費！

這裡推薦兩種最簡單的方法：

## 方法一：Netlify Drop (最推薦，超簡單) 👍

**適合：不想用 Git 指令，只想把檔案拉進去就好的情況。**

1. 準備好你的資料夾：確認 `cryo-supernova` 資料夾裡面有 `index.html` 和 `vocabulary.csv`。
2. 打開瀏覽器，前往 [Netlify Drop](https://app.netlify.com/drop)。
3. **登入** (可以用 GitHub 或 Email 註冊/登入)。
4. 登入後，你會看到一個 "Drag and drop your site output folder here" 的區域。
5. 直接把整個 `cryo-supernova` **資料夾拖曳進去**。
6. 等待幾秒鐘，網址就產生了！你可以把那個網址傳給朋友或學生使用。

---

## 方法二：GitHub Pages (適合長期維護)

**適合：如果你已經有在使用 GitHub，或者想要有穩定的版本控制。**

1. 在 GitHub 上建立一個新的 Repository (例如命名為 `vocab-quiz`)。
2. 將 `cryo-supernova` 資料夾內的檔案上傳到這個 Repository。
    - 你可以使用 Git 指令，或者直接在 GitHub 網頁上點 "Upload files"。
3. 上傳完成後，進入 Repository 的 **Settings (設定)**。
4. 在左側選單找到 **Pages**。
5. 在 **Build and deployment** 下方：
    - **Source** 選擇 `Deploy from a branch`。
    - **Branch** 選擇 `main` (或 `master`)，資料夾選擇 `/ (root)`。
6. 按下 **Save**。
7. 等待約 1-2 分鐘，重新整理頁面，你會在上方看到你的網站網址 (例如 `https://yourname.github.io/vocab-quiz/`)。

---

## 注意事項 ⚠️

1. **CSV 路徑**：在網路上，檔案名稱的大小寫很敏感。請確保程式碼裡的 `fetch('vocabulary.csv')` 和實際檔名 `vocabulary.csv` 大小寫完全一致。
2. **CORS 問題**：佈署上線後，瀏覽器會正常允許讀取同一網站下的 CSV，所以不需要 `start_quiz.bat`，那個只有在本機電腦上測試才需要。
