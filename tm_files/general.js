/*!
* FitVids 1.1
*
* Copyright 2013, Chris Coyier - http://css-tricks.com + Dave Rupert - http://daverupert.com
* Credit to Thierry Koblentz - http://www.alistapart.com/articles/creating-intrinsic-ratios-for-video/
* Released under the WTFPL license - http://sam.zoy.org/wtfpl/
*
*/;(function($){'use strict';$.fn.fitVids=function(options){var settings={customSelector:null,ignore:null};if(!document.getElementById('fit-vids-style')){var head=document.head||document.getElementsByTagName('head')[0];var css='.fluid-width-video-wrapper{width:100%;position:relative;padding:0;}.fluid-width-video-wrapper iframe,.fluid-width-video-wrapper object,.fluid-width-video-wrapper embed {position:absolute;top:0;left:0;width:100%;height:100%;}';var div=document.createElement('div');div.innerHTML='<p>x</p><style id="fit-vids-style">'+css+'</style>';head.appendChild(div.childNodes[1]);}
if(options){$.extend(settings,options);}
return this.each(function(){var selectors=['iframe[src*="player.vimeo.com"]','iframe[src*="youtube.com"]','iframe[src*="youtube-nocookie.com"]','iframe[src*="kickstarter.com"][src*="video.html"]','object','embed'];if(settings.customSelector){selectors.push(settings.customSelector);}
var ignoreList='.fitvidsignore';if(settings.ignore){ignoreList=ignoreList+', '+settings.ignore;}
var $allVideos=$(this).find(selectors.join(','));$allVideos=$allVideos.not('object object');$allVideos=$allVideos.not(ignoreList);$allVideos.each(function(count){var $this=$(this);if($this.parents(ignoreList).length>0){return;}
if(this.tagName.toLowerCase()==='embed'&&$this.parent('object').length||$this.parent('.fluid-width-video-wrapper').length){return;}
if((!$this.css('height')&&!$this.css('width'))&&(isNaN($this.attr('height'))||isNaN($this.attr('width')))){$this.attr('height',9);$this.attr('width',16);}
var height=(this.tagName.toLowerCase()==='object'||($this.attr('height')&&!isNaN(parseInt($this.attr('height'),10))))?parseInt($this.attr('height'),10):$this.height(),width=!isNaN(parseInt($this.attr('width'),10))?parseInt($this.attr('width'),10):$this.width(),aspectRatio=height/width;if(!$this.attr('id')){var videoID='fitvid'+count;$this.attr('id',videoID);}
$this.wrap('<div class="fluid-width-video-wrapper"></div>').parent('.fluid-width-video-wrapper').css('padding-top',(aspectRatio*100)+'%');$this.removeAttr('height').removeAttr('width');});});};})(window.jQuery||window.Zepto);/*! Gamajo Accessible Menu - v1.0.0 - 2014-09-08
* https://github.com/GaryJones/accessible-menu
* Copyright (c) 2014 Gary Jones; Licensed MIT */;(function($,window,document,undefined){'use strict';var pluginName='gamajoAccessibleMenu',hoverTimeout=[];function Plugin(element,options){this.element=element;this.opts=$.extend({},$.fn[pluginName].options,options);this.init();}
$.extend(Plugin.prototype,{init:function(){$(this.element).on('mouseenter.'+pluginName,this.opts.menuItemSelector,this.opts,this.menuItemEnter).on('mouseleave.'+pluginName,this.opts.menuItemSelector,this.opts,this.menuItemLeave).find('a').on('focus.'+pluginName+', blur.'+pluginName,this.opts,this.menuItemToggleClass);},menuItemEnter:function(event){$.each(hoverTimeout,function(index){$('#'+index).removeClass(event.data.hoverClass);clearTimeout(hoverTimeout[index]);});hoverTimeout=[];$(this).addClass(event.data.hoverClass);},menuItemLeave:function(event){var $self=$(this);hoverTimeout[this.id]=setTimeout(function(){$self.removeClass(event.data.hoverClass);},event.data.hoverDelay);},menuItemToggleClass:function(event){$(this).parents(event.data.menuItemSelector).toggleClass(event.data.hoverClass);}});$.fn[pluginName]=function(options){this.each(function(){if(!$.data(this,'plugin_'+pluginName)){$.data(this,'plugin_'+pluginName,new Plugin(this,options));}});return this;};$.fn[pluginName].options={hoverClass:'menu-item-hover',hoverDelay:250,menuItemSelector:'.menu-item'};})(jQuery,window,document);(function($,undefined){'use strict';var $document=$(document),$navs=$('nav');function debounce(func,wait){var timeout;return function(){var that=this;var args=arguments;clearTimeout(timeout);timeout=setTimeout(function(){timeout=null;func.apply(that,args);},wait);};}
function isHidden($object){var element=$object[0];if('undefined'===typeof element){return false;}
return(null===element.offsetParent);}
function addNavToggles(){$navs.before('<div class="menu-toggle"><span></span></div>');$navs.find('.sub-menu').before('<div class="sub-menu-toggle"></div>');}
function showHideNav(){$('.menu-toggle, .sub-menu-toggle').on('click',function(){var $that=$(this);$that.toggleClass('active');$that.next('nav, .sub-menu').slideToggle('slow');});}
function reflowNavs(){if(isHidden($navs)){$navs.removeAttr('style');$('.sub-menu-toggle, .menu-toggle').removeClass('active');}}
function navInit(){if(0!==$navs.length){addNavToggles();showHideNav();$(window).resize(debounce(reflowNavs,200));}}
$document.ready(function(){$('#genesis-content').fitVids();$document.gamajoAccessibleMenu();navInit();});}(jQuery));