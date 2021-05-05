chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  console.log(request, sender, sendResponse);
  sendResponse("我收到你的消息了：" + JSON.stringify("request"));
});
