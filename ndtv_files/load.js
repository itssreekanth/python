

if (typeof _tb_dis === 'undefined' || _tb_dis === null) {
    var _tb_dis = false;
}
if (!_tb_dis) {
    var pm_ppy = "ndtv";

    var _pmep = '//widget.perfectmarket.com/';
    var _pmep_geo = '//geo.perfectmarket.com/';
    if (document.URL.indexOf('https://') > -1) {
        _pmep = _pmep.replace(/88\//gi, '90/');
        _pmep_geo = _pmep_geo.replace(/88\//gi, '90/');
    }
    var _pmpmk = pm_ppy + '/pmk-201902003.14.js';
    var _pmasync = true;
    var _pmoptimization = true;
    var _pmoptimizationmanipulation = true;
    var _pmhp = false;
    var _pmsb = false;

    function _pmloadfile(fileName) {

        if (_pmasync) {
            var js, elements = document.getElementsByTagName("head")[0];
            js = document.createElement("script");
            js.setAttribute("type", "text/javascript");
            js.setAttribute("src", fileName);
            js.setAttribute('async','');
            elements.appendChild(js);
        } else {
            document.writeln('<script src=' + fileName + '></script>');
        }
    }

    var pmk, pmglb, pmfa, pmad, pmdebug_c;
    pmglb = pmglb || null;
    pmfa = pmfa || null;
    pmad = pmad || null;
    pmdebug_c = pmdebug_c || null;
    pmk = pmk || null;
    var _pmenv = _tb_getUrlParameter('pmenv');
    //pm async
    var _pma = _tb_getUrlParameter('_pma');
    if (_pma == true) {
        _pmasync = true;
    }

    if (_pmenv && _pmenv == 'sandbox' && !_pmsb) {

        _pmep = '//widget.sandbox.perfectmarket.com/';
        _pmep_geo = '//geo.sandbox.perfectmarket.com/';
        var _tb_d = new Date();
        var _tb_rand = _tb_d.getTime();
        _pmpmk = pm_ppy + "/load.js?" + _tb_rand;
    }

    (function () {
        var sc = 'script', doc = document;
        _pmloadfile(_pmep + _pmpmk);
    })();
    function pmws_request_done() {
        var sc = "script", doc = document;
        if (doc.all && !window.opera) {
            doc.write('<' + sc + ' type="text/javascript" id="pm_contentloadtag" defer="defer" src="javascript:void(0)"><\/' + sc + '>');
            var pm_contentloadtag = doc.getElementById("pm_contentloadtag");
            if (pm_contentloadtag)pm_contentloadtag.onreadystatechange = function () {
                if (this.readyState == "complete") return;
            }
        }
        _pmloadfile(_pmep + _pmpmk);
    }


    function _tb_getUrlParameter(name) {
        var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
        return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
    }


     /** Generated CJS **/ if (window.location.href.indexOf('www.ndtv.com') > -1) {
    var _pm_ecd = {
        'sp': 1,
        'ax': "(//span[@itemprop='author']//span[@itemprop='name']|//div[@itemprop='author']//span[@itemprop='name']|//div[@class='dateline']/a/span[@itemprop='author']/span[@class='reviewer']|//div[@class='storyarticle']//div[@class='dateline']/a[1]|//div[contains(@class,'ndmv-datetime')]//a[1]|//div[contains(@class,'reviews')]//span[@class='art__author']/span[@itemprop='author']/a[1])"
    };
} else {
    var _pm_ecd = {
        'sr': "\\/\\/(.*)\\.ndtv.com",
        'ax': "(//span[@itemprop='author']//span[@itemprop='name']|//div[@itemprop='author']//span[@itemprop='name']|//div[@class='dateline']/a/span[@itemprop='author']/span[@class='reviewer']|//div[@class='storyarticle']//div[@class='dateline']/a[1]|//div[contains(@class,'ndmv-datetime')]//a[1]|//div[contains(@class,'reviews')]//span[@class='art__author']/span[@itemprop='author']/a[1] | //div[@class='article__meta']/a)"
    };
}

var _tb_vpx = [{
    xpath: ".//div[contains(@class, 'twitter-video')]//iframe",
    attr: "iframe"
}, {
    xpath: ".//img[contains(@src, 'playbutton_red')]/..",
    attr: "div",
    clickToPlayXPath: [{
        xpath: ".//iframe[contains(@src, 'video/embed-player')]",
        attr: "iframe"
    }]
}, {
    xpath: ".//object[contains(@id, 'js-mediaplayer')]//iframe",
    attr: "div"
},
{
    xpath: "//div[@id='html5Container']//div[@id='vidContainer']//div[@id='vidHolder']",
    attr: "div"
}

];



var _tb_noBC = true;
var _tb_noKP = true;
var _tb_noOP = true;
var _tb_noJP = true;/** Generated CJS end **/ 
}