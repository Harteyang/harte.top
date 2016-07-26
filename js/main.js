/*jslint browser: true*/
/*global $, jQuery, alert, console*/
$(document).ready(function () {
  "use strict";
  $(".highlight > pre:has(code[data-lang])").each(function() {
    $(this).addClass("lang");
    var lang = $(this).children("code:first").attr("data-lang");
    $(this).addClass(lang);  // add language named class
  });
});

