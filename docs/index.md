---
title: "原子核理論特講II<br>
「ハンズオンで学ぶ核力の基礎」"
layout: single
sidebar:
  nav: "main"
header:
  overlay_image: /assets/images/nuclfig.jpg
  overlay_height: 800px
  overlay_filter: 0.5
custom_js:
  - "/Lecture_Tsukuba2025/assets/js/chatbot.js"
---

# 概要
核力はフェムトスケールの量子系である原子核の存在形態やダイナミクスを微視的に理解する鍵である。本講義では、核力の基礎を数値計算を通じてハンズオン形式で学ぶ。数値計算にはPythonを使用するが、Pythonの予備知識を必要としない内容とするつもりである。また、核力が核子多体系の性質をどのように支配しているのかという点についても言及する(こちらはハンズオンではない)。

その他、参考書籍や範囲外の内容については[この資料](/assets/pdf/Tsukuba2025abstract.pdf){:target="_blank"}を確認してほしい。

<br>
<br>

# Dify icon

<svg width="100" height="100" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景の青い円 -->
  <circle cx="12" cy="12" r="11" fill="#1C64F2"/>
  
  <!-- 吹き出しの形 -->
  <path fill-rule="evenodd" clip-rule="evenodd" d="M7.7586 5L16.2412 5C17.0462 4.99999 17.7105 4.99998 18.2517 5.04419C18.8138 5.09012 19.3305 5.18868 19.8159 5.43598C20.5685 5.81947 21.1804 6.43139 21.5639 7.18404C21.8112 7.66937 21.9098 8.18608 21.9557 8.74818C21.9999 9.28937 21.9999 9.95373 21.9999 10.7587L22 13.1376C22.0004 13.933 22.0007 14.5236 21.8636 15.0353C21.4937 16.4156 20.4155 17.4938 19.0352 17.8637C18.7277 17.9461 18.3917 17.9789 17.9999 17.9918L17.9999 19.371C18 19.6062 18 19.846 17.9822 20.0425C17.9651 20.2305 17.9199 20.5852 17.6722 20.8955C17.3872 21.2525 16.9551 21.4602 16.4983 21.4597C16.1013 21.4593 15.7961 21.273 15.6386 21.1689C15.474 21.06 15.2868 20.9102 15.1031 20.7632L12.69 18.8327C12.1714 18.4178 12.0174 18.3007 11.8575 18.219C11.697 18.137 11.5262 18.0771 11.3496 18.0408C11.1737 18.0047 10.9803 18 10.3162 18H7.75858C6.95362 18 6.28927 18 5.74808 17.9558C5.18598 17.9099 4.66928 17.8113 4.18394 17.564C3.43129 17.1805 2.81937 16.5686 2.43588 15.816C2.18859 15.3306 2.09002 14.8139 2.0441 14.2518C1.99988 13.7106 1.99989 13.0463 1.9999 12.2413V9.75868C1.99989 8.95372 1.99988 8.28936 2.0441 7.74818C2.09002 7.18608 2.18859 6.66937 2.43588 6.18404C2.81937 5.43139 3.43129 4.81947 4.18394 4.43598C4.66928 4.18868 5.18598 4.09012 5.74808 4.04419C6.28927 3.99998 6.95364 3.99999 7.7586 5Z" fill="white"/>
  
  <!-- 目（左） -->
  <circle cx="9" cy="10" r="1.5" fill="#1C64F2"/>

  <!-- 目（右） -->
  <circle cx="15" cy="10" r="1.5" fill="#1C64F2"/>

  <!-- 口（スマイル） -->
  <path d="M9 14C9.5 15 10.5 16 12 16C13.5 16 14.5 15 15 14" stroke="#1C64F2" stroke-width="1.5" stroke-linecap="round"/>
</svg>

# スケジュール

| 2月26日 | 2月27日 | 2月28日 | 
| --- | --- | --- |
| [1. 核力の外観と原子核の基本的性質](#1-核力の外観と原子核の基本的性質) | [4. 中間子論 I](#4-中間子論-i-5-中間子論-ii) |  | 
| [2. Yukawaポテンシャルと重陽子](#2-yukawaポテンシャルと重陽子) | [5. 中間子論 II](#4-中間子論-i-5-中間子論-ii) | [7. セミナー](#7-セミナー) | 
| [3. テンソル力と重陽子](#3-テンソル力と重陽子) | [6. カイラル有効場理論と最近の話題](#6-カイラル有効場理論と最近の話題) |  | 

<br>
<br>


---
# 1. 核力の外観と原子核の基本的性質
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
- [Notebookをダウンロード](https://raw.githubusercontent.com/TokuroFukui/Lecture_Tsukuba2025/main/notebook.ipynb)
- [Google Colabで開く](https://colab.research.google.com/github/TokuroFukui/Lecture_Tsukuba2025/blob/main/notebook.ipynb){:target="_blank"}
<br>


---
# 2. Yukawaポテンシャルと重陽子
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
- [Notebookをダウンロード](https://raw.githubusercontent.com/TokuroFukui/Lecture_Tsukuba2025/main/notebook.ipynb)
- [Google Colabで開く](https://colab.research.google.com/github/TokuroFukui/Lecture_Tsukuba2025/blob/main/notebook.ipynb){:target="_blank"}
<br>


---
# 3. テンソル力と重陽子
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
- [Notebookをダウンロード](https://raw.githubusercontent.com/TokuroFukui/Lecture_Tsukuba2025/main/notebook.ipynb)
- [Google Colabで開く](https://colab.research.google.com/github/TokuroFukui/Lecture_Tsukuba2025/blob/main/notebook.ipynb){:target="_blank"}
<br>


---
# 3. テンソル力と重陽子
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
- [Notebookをダウンロード](https://raw.githubusercontent.com/TokuroFukui/Lecture_Tsukuba2025/main/notebook.ipynb)
- [Google Colabで開く](https://colab.research.google.com/github/TokuroFukui/Lecture_Tsukuba2025/blob/main/notebook.ipynb){:target="_blank"}
<br>


---
# 4. 中間子論 I, 5. 中間子論 II
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
- [Notebookをダウンロード](https://raw.githubusercontent.com/TokuroFukui/Lecture_Tsukuba2025/main/notebook.ipynb)
- [Google Colabで開く](https://colab.research.google.com/github/TokuroFukui/Lecture_Tsukuba2025/blob/main/notebook.ipynb){:target="_blank"}
<br>


---
# 6. カイラル有効場理論と最近の話題
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [講義資料](){:target="_blank"}
<br>


---
# 7. セミナー
「核力の到達距離」、「引力の強さ」、「斥力芯」などを学ぶ。ここでは精密な議論ではなく、実験事実や井戸型ポテンシャルを使った定性的な側面に焦点を合わせる。
- [セミナー資料](){:target="_blank"}
<br>


<!-- Dify chatbot -->
<script>
 window.difyChatbotConfig = {
  token: 'tAx3XVwPwJlsLzPu'
 }
</script>
<script
 src="https://udify.app/embed.min.js"
 id="tAx3XVwPwJlsLzPu"
 defer>
</script>
<style>
  #dify-chatbot-bubble-button {
    background-color: #1C64F2 !important;
  }
  #dify-chatbot-bubble-window {
    width: 24rem !important;
    height: 40rem !important;
  }
</style>
