// Dify chatbot 
window.difyChatbotConfig = {
    token: 'tAx3XVwPwJlsLzPu'
};

(function() {
    var script = document.createElement('script');
    script.src = "https://udify.app/embed.min.js";
    script.id = "tAx3XVwPwJlsLzPu";
    script.defer = true;
    document.body.appendChild(script);
})();

var style = document.createElement('style');
style.innerHTML = `
  #dify-chatbot-bubble-button {
    background-color: #1C64F2 !important;
  }
  #dify-chatbot-bubble-window {
    width: 24rem !important;
    height: 40rem !important;
  }
`;
document.head.appendChild(style);
