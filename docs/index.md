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
  <path fill-rule="evenodd" clip-rule="evenodd" d="M7.7586 2L16.2412 2C17.0462 1.99999 17.7105 1.99998 18.2517 2.04419C18.8138 2.09012 19.3305 2.18868 19.8159 2.43598C20.5685 2.81947 21.1804 3.43139 21.5639 4.18404C21.8112 4.66937 21.9098 5.18608 21.9557 5.74818C21.9999 6.28937 21.9999 6.95373 21.9999 7.7587L22 14.1376C22.0004 14.933 22.0007 15.5236 21.8636 16.0353C21.4937 17.4156 20.4155 18.4938 19.0352 18.8637C18.7277 18.9461 18.3917 18.9789 17.9999 18.9918L17.9999 20.371C18 20.6062 18 20.846 17.9822 21.0425C17.9651 21.2305 17.9199 21.5852 17.6722 21.8955C17.3872 22.2525 16.9551 22.4602 16.4983 22.4597C16.1013 22.4593 15.7961 22.273 15.6386 22.1689C15.474 22.06 15.2868 21.9102 15.1031 21.7632L12.69 19.8327C12.1714 19.4178 12.0174 19.3007 11.8575 19.219C11.697 19.137 11.5262 19.0771 11.3496 19.0408C11.1737 19.0047 10.9803 19 10.3162 19H7.75858C6.95362 19 6.28927 19 5.74808 18.9558C5.18598 18.9099 4.66928 18.8113 4.18394 18.564C3.43129 18.1805 2.81937 17.5686 2.43588 16.816C2.18859 16.3306 2.09002 15.8139 2.0441 15.2518C1.99988 14.7106 1.99989 14.0463 1.9999 13.2413V7.75868C1.99989 6.95372 1.99988 6.28936 2.0441 5.74818C2.09002 5.18608 2.18859 4.66937 2.43588 4.18404C2.81937 3.43139 3.43129 2.81947 4.18394 2.43598C4.66928 2.18868 5.18598 2.09012 5.74808 2.04419C6.28927 1.99998 6.95364 1.99999 7.7586 2Z" fill="white"></path>
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
