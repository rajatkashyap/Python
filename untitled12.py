# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:03:07 2018

@author: U40MV02
"""

yelp_html='''
<!DOCTYPE html>
<!-- saved from url=(0079)https://www.yelp.com/search?find_desc=fried+chicken&find_loc=Atlanta%2C+GA&ns=1 -->
<html xmlns:fb="http://www.facebook.com/2008/fbml" class="js gr__yelp_com" lang="en"><!--<![endif]--><head data-component-bound="true"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link type="text/css" rel="stylesheet" href="./Best Fried chicken in Atlanta, GA - Yelp_files/css"><style type="text/css">.gm-style .gm-style-cc span,.gm-style .gm-style-cc a,.gm-style .gm-style-mtc div{font-size:10px}
</style><style type="text/css">@media print {  .gm-style .gmnoprint, .gmnoprint {    display:none  }}@media screen {  .gm-style .gmnoscreen, .gmnoscreen {    display:none  }}</style><style type="text/css">.gm-style-pbc{transition:opacity ease-in-out;background-color:rgba(0,0,0,0.45);text-align:center}.gm-style-pbt{font-size:22px;color:white;font-family:Roboto,Arial,sans-serif;position:relative;margin:0;top:50%;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%)}
</style><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/rules-p-M4yfUTCPeS3vn.js" style=""></script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/segments.json" async="" type="text/javascript"></script>


    <script src="./Best Fried chicken in Atlanta, GA - Yelp_files/102029836881428" async=""></script><script async="" src="./Best Fried chicken in Atlanta, GA - Yelp_files/fbevents.js"></script><script async="" src="./Best Fried chicken in Atlanta, GA - Yelp_files/async-ads.js"></script><script async="" src="./Best Fried chicken in Atlanta, GA - Yelp_files/analytics.js"></script><script>            window.yPageStart = new Date().getTime();
</script>

    <script>            var initialVisibilityState = document.webkitVisibilityState;

                yPerfTimings = [];

                ySitRepParams = {"b3Sampled": null, "edgeStartTime": 1505255565245572, "site": "main", "uniqueRequestID": "f2da9c903fcf056d", "isLoggedIn": false, "clientIP": "76.20.254.8", "servlet": "search", "zipkinTraceID": "f2da9c903fcf056d", "datacenter": "us-east-1", "cfRayID": null, "serverStartTime": 1505255565272, "action": "search_html", "yuv_record": "WZD9cdROxjIbbAxurlTGZAvM4H4Tb3yahub1Mx34vjgM5OvLvcHrctoizFPNkLM3nOyCpaGokHa5xijxqgBR0L6aE_fwB1EN"};
                window.ySitRepParams['initialVisibilityState'] = initialVisibilityState;
                window.ySitRepParams['seoCohorts'] = null;


            (function(H){H.className=H.className.replace(/\bno-js\b/,'js');})(document.documentElement);
</script>

            <script>            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
</script>


            <script>
            (function() {
                var main = null;

                var d=this;function h(a,b){var c=a.split("."),e=d;c[0]in e||!e.execScript||e.execScript("var "+c[0]);for(var f;c.length&&(f=c.shift());)c.length||void 0===b?e[f]?e=e[f]:e=e[f]={}:e[f]=b};function k(a,b){for(var c=0;c<a.length;c++)if(a[c]===b)return c;return-1};function l(a){var b=$(window);function c(a,b){return 0<=a&&a<=b}function e(a,b){return 0>=a.left&&a.right>=b.width()||0>=a.top&&a.bottom>=b.height()}function f(a,b){return c(a.left,b.width())&&!(a.top>=b.height()||0>=a.bottom)}function g(a,b){return c(a.right,b.width())&&!(a.top>=b.height()||0>=a.bottom)}function n(a,b){return c(a.bottom,b.height())&&!(a.left>=b.width()||0>=a.right)}a=a.getBoundingClientRect();return function(a,b){return c(a.top,b.height())&&!(a.left>=b.width()||0>=a.right)}(a,b)||
f(a,b)||g(a,b)||n(a,b)||e(a,b)};function m(){this.a=[];this.hasOwnProperty("value_")&&delete this.value_}m.prototype.J=function(a){var b=this;this.hasOwnProperty("value_")?setTimeout(function(){a.call(this,b.value_)},0):this.a.push(a)};m.prototype.getInstance=m.prototype.J;function q(a){window.ga||(window.ga=function(){});this.U=(new Date).getTime();this.reload(a)}var r;h("yelp_google_analytics.google_analytics",q);var u=new m,v=["global","m","www","biz","webview"];function w(a,b,c){if(c)for(var e in c[b])c[b].hasOwnProperty(e)&&(a.g[b][e]=c[b][e][0])}q.prototype.F=function(a,b){window.ga(x("set",b),"page",a)};q.prototype.setPage=q.prototype.F;q.prototype.K=function(){return window.ga.getAll()};q.prototype.getTrackers=q.prototype.K;
q.prototype.s=function(a){for(var b in this.a)this.a.hasOwnProperty(b)&&y(this,String(b),a)};q.prototype.firePageviews=q.prototype.s;q.prototype.H=function(a){for(var b in this.a)this.a.hasOwnProperty(b)&&("global"!==b||this.l)&&y(this,String(b),a)};q.prototype.firePageviewsWithGlobalTrackerSampled=q.prototype.H;function y(a,b,c){c&&a.F(c,b);window.ga(x("send",b),"pageview")}
function x(a,b){if(0<=k(v,b))return[b,a].join(".");throw Error("google analytics attempted to set "+a+" to an unrecognized tracker alias: "+b);}q.prototype.N=function(a,b,c){a=this.g[c][a];"undefined"!=typeof a&&null!==b&&(this.b[c]["dimension"+a]=b.toString())};q.prototype.setDimensionOneEvent=q.prototype.N;q.prototype.j=function(a,b,c){a=this.g[c][a];"undefined"!=typeof a&&null!==b&&window.ga(x("set",c),"dimension"+a,b.toString())};q.prototype.setDimension=q.prototype.j;
q.prototype.O=function(a,b){for(var c in a)a.hasOwnProperty(c)&&this.j(c,a[c],b)};q.prototype.setDimensions=q.prototype.O;q.prototype.D=function(a,b,c){window.ga(x("set",c),"metric"+a,b)};q.prototype.setMetric=q.prototype.D;q.prototype.P=function(a,b,c){this.c[c][a]=b};q.prototype.setMetricOneEvent=q.prototype.P;
q.prototype.i=function(a,b,c,e,f){for(var g in this.a)if(this.a.hasOwnProperty(g)){var n={hitType:"event",eventCategory:a,eventAction:b,eventLabel:c,eventValue:e,hitCallback:f,nonInteraction:!0},p;for(p in this.b[g])this.b[g].hasOwnProperty(p)&&(n[p]=this.b[g][p]);for(var t in this.c[g])this.c[g].hasOwnProperty(t)&&(n["metric"+t]=this.c[g][t]);this.b[g]={};this.c[g]={};"global"!==g&&window.ga(x("send",String(g)),n)}};q.prototype.trackEvent=q.prototype.i;
q.prototype.T=function(a,b,c,e){a={hitType:"timing",timingCategory:a,timingVar:b,timingValue:c,timingLabel:e};for(var f in this.a)this.a.hasOwnProperty(f)&&(b=a,window.ga(x("send",String(f)),b))};q.prototype.trackTiming=q.prototype.T;q.prototype.G=function(a,b,c,e,f){this.l&&this.i(a+" / 10",b,c,e,f)};q.prototype.trackEventHighVolume=q.prototype.G;q.prototype.M=function(a,b){return b in this.g[a]};q.prototype.isExperimentSet=q.prototype.M;
q.prototype.v=function(){var a=this;$(window).on("beforeunload",function(){a.j("viewport_tracking",a.m.join(","),"www");var b=Math.round(((new Date).getTime()-a.U)/1E3),c="240+";0>=b?c="5":30>=b?c=(5*Math.ceil(b/5)).toString():120>=b?c=(15*Math.ceil(b/15)).toString():240>=b&&(c=(30*Math.ceil(b/30)).toString());a.G("time on page","unload",c,b)})};q.prototype.initTimeOnPageEvent=q.prototype.v;q.prototype.u=function(){var a=this;setTimeout(function(){a.i("dwell time","dwell","30 seconds")},3E4)};
q.prototype.initDwellTimeEvent=q.prototype.u;q.prototype.o=function(){for(var a=document.getElementsByClassName("js-ga-widget"),b=0;b<a.length;b++){var c=a[b],e=c.getAttribute("data-ga-widget-name")||"Unnamed Widget";0>k(this.m,e)&&l(c)&&this.m.push(e)}};q.prototype.addNewlyVisibleWidgets_=q.prototype.o;q.prototype.L=function(){if(Function.prototype.bind&&document.getElementsByClassName&&window.addEventListener){var a=this.o.bind(this);a();window.addEventListener("scroll",a)}};
q.prototype.initViewportEvent=q.prototype.L;q.init=function(a){z(new q(a))};function z(a){r=a;u.value_=a;for(a=0;a<u.a.length;a++)u.a[a].call(u,u.value_)}q.setInstance=z;function A(){var a=r;if(void 0===a)throw Error("yelp_google_analytics.google_analytics not initialized. Call a site specific GA init!");return a}q.getInstance=A;
q.prototype.reload=function(a){this.a=a.trackers;this.domain=a.domain;this.w=a.clientID;this.C=a.user_id;this.f=a.dimensions;this.h=a.metrics;this.A=a.js_dimensions;this.l=a.enable_high_volume_events;this.B=a.site_speed_sample_rate;this.m=[];this.g={};this.b={};this.c={};for(var b in this.a)if(this.a.hasOwnProperty(b)){a=String(b);var c=String(this.a[b]),e={cookieDomain:this.domain,name:a,clientId:this.w,siteSpeedSampleRate:this.B||1};this.C&&(e.userId=this.C);window.ga("create",c,e);this.g[a]={};
this.b[a]={};this.c[a]={};w(this,a,this.f);w(this,a,this.A);c=void 0;for(c in this.f[a])this.f[a].hasOwnProperty(c)&&this.j(String(c),this.f[a][c][1],a);c=void 0;for(c in this.h[a])this.h[a].hasOwnProperty(c)&&this.D(this.h[a][c][0],this.h[a][c][1],a)}};q.prototype.reload=q.prototype.reload;q.prototype.I=function(){return{trackers:this.a,domain:this.domain,clientID:this.w,user_id:this.W,dimensions:this.f,metrics:this.h,js_dimensions:this.A,enable_high_volume_events:this.l,site_speed_sample_rate:this.B}};
q.prototype.getGaConfig=q.prototype.I;function B(a,b,c,e){a(b,function(){0<e?B(a,b,c,e-1):c()})};function C(a){q.call(this,a)}(function(){function a(){}a.prototype=q.prototype;C.b=q.prototype;C.prototype=new a;C.prototype.constructor=C;C.a=function(a,c,e){for(var f=Array(arguments.length-2),g=2;g<arguments.length;g++)f[g-2]=arguments[g];return q.prototype[c].apply(a,f)}})();h("yelp_google_analytics.www.google_analytics",C);
C.prototype.R=function(){for(var a=this,b=[".js-main-header",".js-header-nav"],c=0;c<b.length;c++)$(b[c]).on("click",".js-analytics-click",function(b){b.stopPropagation();b=$(b.currentTarget).data("analyticsLabel");a.i("header","click",b)})};C.prototype.trackHeaderNavClicks=C.prototype.R;
C.prototype.S=function(){var a=!1;return function(){if(!a){var b=this;$.each({logo:"logo","home-link":"home","about-me":"about_me","write-review":"write_a_review","find-friends":"find_friends",messaging:"messaging",talk:"talk",events:"events",delivery:"delivery","member-search":"member_search","biz-owner-link":"biz owner","notifications-icon":"notifications_icon","messages-icon":"messages_icon","header-sign-up":"signup","header-log-in":"login",Zprofile:"account_settings","header-log-out":"logout",
"dropdown_user-name":"about_me","dropdown_find-friends":"find_friends","dropdown_about-me":"about_me","dropdown_user-photo":"about_me"},function(a,e){$("#"+a).click(function(){b.i("header","click",e)})})}a=!0}}();C.prototype.trackNavClicks=C.prototype.S;
function D(a){B(function(a,c){var e=new XMLHttpRequest;e.onreadystatechange=function(){this.readyState===XMLHttpRequest.DONE&&(200===this.status?a(JSON.parse(this.responseText)):c())};e.open("GET","/yuv",!0);try{e.send()}catch(f){c()}},function(b){a(b.X)},function(){throw Error("Failed to fetch YUV from /yuv, Google Analytics is not going to be initialized.");},3)}C.fetchClientId=D;C.getInstance=function(){return A()};h("yelp_google_analytics.www.google_analytics.deferredInstance",u);
h("yelp_google_analytics.www.google_analytics.SITE","www");function E(a,b,c){function e(){z(new C(a));var c=A();c.s(b);c.u()}c?D(function(b){a.V=b;e()}):e()}h("yelp_google_analytics.www.init.initGoogleAnalytics",E);h("yelp_google_analytics.www.init.initTimeOnPageAnalytics",function(){A().v()});null===main&&(main=E); //# sourceMappingURL=


                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main({"metrics": {"www": {"mtb-reply-rate-shown": [4, null], "mtb-response-time-shown": [1, null]}, "global": {}}, "site_speed_sample_rate": null, "domain": "yelp.com", "user_id": null, "dimensions": {"www": {"ynra_suggestion_algo_changes": [108, "status_quo"], "promote_ads_to_non_advertiser_on_search_impression_shown": [147, "False"], "eat24_free_delivery_banner": [45, "disabled"], "query_words_number": [52, "2"], "search_page_title_case": [43, "desc_city"], "biz_page_actions": [188, "status_quo"], "payment.cde.www.rewards": [171, "enabled"], "yr_diner.www.direct_checkout_for_exact_match": [163, "disabled"], "ytp_eat24_yelp_style_to_iframe": [136, "enabled"], "www_education_banner": [190, "disabled"], "distil": [53, 1], "internal_ip": [27, "False"], "www_search_snippets_in_sync_with_ads": [112, "status_quo_8"], "yr_diner.www.reservations_notify_me": [149, "enabled"], "traffic_search_internal_linking_experiment_v2": [19, "giver"], "pinterest_share_on_biz_photo": [80, "status_quo"], "ytp_delivery_landing": [125, "platform_pages"], "password_meter": [99, "meter_2"], "growth.www.phone_number_signup": [198, "second_page"], "payment.ux.card_formatting.www.rewards": [56, "enabled"], "account_level": [1, "anon"], "traffic_search_title_varying_rpp_experiment": [118, "no_cohort"], "www_current_location_suggestion": [185, "enabled"], "service": [107, "yelp-main"], "page_depth": [41, "0"], "pagelet_mode_www_home": [23, "allow_async"], "content_country": [15, "US"], "integration": [14, ""], "payment.cde.www.checkout": [195, "enabled"], "www_fixed_header_v2": [13, "status_quo"], "hierarchy_breadcrumbs": [82, "False"], "traffic_search_url_normalization_experiment_page_family_role": [40, "giver"], "ytp_order_confirmation_page": [143, "enabled"], "txn_growth.www.reservation_button_color_experiment": [104, "green_button"], "has_canonical": [36, "True"], "full_url": [34, "/search?find_desc=fried+chicken\u0026find_loc=Atlanta%2C+GA\u0026ns=1"], "nav_show_message_count": [59, "show_message_count"], "distil_js_enabled": [138, true], "payment.ux.exp_date_input_type.www.rewards": [32, "textbox_field"], "review_actions_dropdown": [2, "disabled"], "www_signup_redesign": [92, "status_quo"], "yr_diner.www.reservation_sticky_bar": [126, "status_quo_embedded"], "www_biz_details_raq_sticky": [84, "enabled"], "business_id": [141, ""], "ynra_ui_homepage_designs_round_two": [16, "composer_expand_inline"], "traffic_search_within_x_miles_experiment": [146, "no_cohort"], "is_indexable": [42, "True"], "list_details_service": [116, "enabled"], "www_asymetrica": [119, "status_quo"], "traffic_search_year_title_experiment": [130, "no_cohort"], "traffic_descriptive_search_urls": [187, "no_cohort"], "lower_promoted_delivery_threshold": [58, "reduced_to_fifteen"], "traffic_index_new_pages_cross_validation": [177, "test_group"], "viewport_tracking": [29, null], "pagelet_mode_www_biz_details": [24, "allow_async"], "traffic_varied_rpp_search_content_experiment": [150, "inactive_status_quo_02"], "traffic_search_photos_experiment": [121, "inactive_first_result_2"], "exact_name_match": [50, "False"], "embeddable_reviews": [98, "enabled"], "decrypted_yuv_id": [3, "9BF44709B38A0F50"], "search_city": [49, "Atlanta"], "traffic_search_internal_linking_related_categories": [26, "no_cohort"], "referrer": [64, "yelp"], "results_on_page": [51, "10"], "mtb_weekly_growth_1": [85, "txn_growth.request_an_appointment_separated_search-enabled"], "top_level_categories": [11, ""], "is_biz_user": [129, "False"], "business_features_raq": [160, "services_only"], "ytp_start_orders_cta_btn_color_exp": [65, "green_button"], "platform_pickup_filter": [20, "enabled"], "payment.braintree_tokenization_key.paypal": [199, "enabled"], "traffic_rev_last_update_search_title_experiment": [30, "inactive_removed_last_updated_01"], "txn_hydra_cash_back_injection": [153, "status_quo"], "contributions.www.master_holdback": [31, "enabled"], "remote_ip": [4, "76.20.254.8"], "yr_diner.www.autosearch_on_load": [54, "enabled"], "search_accuracy": [48, "4"]}, "global": {"distil_js_enabled": [13, true], "search_page_title_case": [32, "desc_city"], "exact_name_match": [14, "False"], "results_on_page": [29, "10"], "search_city": [31, "Atlanta"], "is_indexable": [19, "True"], "referrer": [28, "yelp"], "has_canonical": [16, "True"], "content_country": [11, "US"], "query_words_number": [25, "2"], "integration": [17, ""], "top_level_categories": [7, ""], "distil": [12, 1], "internal_ip": [18, "False"], "search_accuracy": [30, "4"], "full_url": [15, "/search?find_desc=fried+chicken\u0026find_loc=Atlanta%2C+GA\u0026ns=1"], "account_level": [1, "anon"]}}, "enable_high_volume_events": false, "trackers": {"www": "UA-30501-24", "global": "UA-30501-1"}, "js_dimensions": {"www": {"platform_order_type": [127, null], "js_vertical_search_type": [39, null]}, "global": {}}, "ga_enabled": true, "clientID": "9BF44709B38A0F50"},null,false);
            })();
    </script>

        


            <script>        (function (d, w) {
            if (('ontouchstart' in w) || w.DocumentTouch && d instanceof w.DocumentTouch){
                var html = d.getElementsByTagName("html")[0];
                html.classList.add("touch");
            }
        }(document, window));
</script>


                
    <meta http-equiv="Content-Language" content="en">


                    <meta name="description" content="Reviews on Fried chicken in Atlanta, GA - Gus&#39;s World Famous Fried Chicken, South City Kitchen - Midtown, Mary Mac&#39;s Tea Room, Busy Bee Cafe, Richards&#39; Southern Fried, Greens &amp; Gravy, Colonnade Restaurant, South City Kitchen Buckhead, Poor…">


                <meta name="keywords" content="Yelp,recommendation,San Francisco, bay area, local,business,review,friend,restaurant,dentist,doctor,salon,spa,shopping,store,share,community,massage,sushi,pizza,nails,New York,Los Angeles">


                    <meta name="viewport" content="width=1020">

            
    <meta name="application-name" content="Yelp">

    <meta name="msapplication-TileImage" content="https://s3-media3.fl.yelpcdn.com/assets/2/www/img/7f906850f02b/ico/win8-tile.png">
    <meta name="msapplication-TileColor" content="#c41200">

    <meta name="msapplication-starturl" content="https://www.yelp.com/">
    <meta name="msapplication-navbutton-color" content="#c41200">
    <meta name="msapplication-window" content="width=1024;height=768">
    <meta name="msapplication-tooltip" content="Go to Yelp.com">

    <meta name="msapplication-task" content="name=Find Reviews; action-uri=/; icon-uri=https://s3-media1.fl.yelpcdn.com/assets/2/www/img/a6bbc59c7458/ico/favicon-16x16.ico">

    <meta name="msapplication-task" content="name=Hot New Businesses; action-uri=/openings; icon-uri=https://s3-media1.fl.yelpcdn.com/assets/2/www/img/a6bbc59c7458/ico/favicon-16x16.ico">

    <meta name="msapplication-task" content="name=Yelp Deals; action-uri=/search?find_desc=deals; icon-uri=https://s3-media1.fl.yelpcdn.com/assets/2/www/img/a6bbc59c7458/ico/favicon-16x16.ico">


                                <meta name="apple-itunes-app" content="app-id=284910350, app-argument=yelp:///search?location=Atlanta%2C%20GA&amp;terms=fried%20chicken&amp;utm_campaign=default&amp;utm_source=www">


                            <link href="android-app://com.yelp.android/yelp-app-indexing/search?find_desc=fried%20chicken&amp;find_loc=Atlanta%2C%20GA&amp;utm_campaign=search&amp;utm_medium=organic&amp;utm_source=google" rel="alternate">
        <link href="ios-app://284910350/yelp//search?location=Atlanta%2C%20GA&amp;terms=fried%20chicken&amp;utm_campaign=search&amp;utm_medium=organic&amp;utm_source=google" rel="alternate">


                            <meta property="al:ios:app_name" content="Yelp">
        <meta property="al:ios:app_store_id" content="284910350">
        <meta property="al:ios:url" content="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;utm_campaign=search&amp;utm_medium=organic&amp;utm_source=apple">


                <link rel="mask-icon" sizes="any" href="https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_styleguide/4374c8fd03d1/assets/img/logos/yelp_burst.svg" content="#c41200">
    <link rel="shortcut icon" href="https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/118ff475a341/assets/img/logos/favicon.ico">


                <link rel="search" type="application/opensearchdescription+xml" href="https://www.yelp.com/opensearch" title="Yelp">



            
        <link rel="canonical" href="https://www.yelp.com/search?find_desc=best+fried+chicken&amp;find_loc=Atlanta%2C+GA">
            <link href="https://en.yelp.be/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-be" rel="alternate">
            <link href="https://www.yelp.fr/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fr-fr" rel="alternate">
            <link href="https://en.yelp.com.ph/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-ph" rel="alternate">
            <link href="https://fi.yelp.fi/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fi-fi" rel="alternate">
            <link href="https://www.yelp.pt/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="pt-pt" rel="alternate">
            <link href="https://en.yelp.my/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-my" rel="alternate">
            <link href="https://www.yelp.it/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="it-it" rel="alternate">
            <link href="https://nl.yelp.be/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="nl-be" rel="alternate">
            <link href="https://nz.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-nz" rel="alternate">
            <link href="https://www.yelp.nl/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="nl-nl" rel="alternate">
            <link href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-us" rel="alternate">
            <link href="https://www.yelp.com.sg/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-sg" rel="alternate">
            <link href="https://fr.yelp.be/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fr-be" rel="alternate">
            <link href="https://www.yelp.ie/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-ie" rel="alternate">
            <link href="https://www.yelp.com.au/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-au" rel="alternate">
            <link href="https://en.yelp.com.hk/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-hk" rel="alternate">
            <link href="https://de.yelp.ch/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="de-ch" rel="alternate">
            <link href="https://www.yelp.cl/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="es-cl" rel="alternate">
            <link href="https://www.yelp.co.jp/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="ja-jp" rel="alternate">
            <link href="https://fil.yelp.com.ph/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fil-ph" rel="alternate">
            <link href="https://www.yelp.com.ar/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="es-ar" rel="alternate">
            <link href="https://www.yelp.es/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="es-es" rel="alternate">
            <link href="https://www.yelp.co.uk/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-gb" rel="alternate">
            <link href="https://www.yelp.ca/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-ca" rel="alternate">
            <link href="https://zh.yelp.com.hk/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="zh-hk" rel="alternate">
            <link href="https://www.yelp.at/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="de-at" rel="alternate">
            <link href="https://www.yelp.com.br/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="pt-br" rel="alternate">
            <link href="https://en.yelp.ch/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="en-ch" rel="alternate">
            <link href="https://www.yelp.dk/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="da-dk" rel="alternate">
            <link href="https://www.yelp.com.tw/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="zh-tw" rel="alternate">
            <link href="https://www.yelp.cz/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="cs-cz" rel="alternate">
            <link href="https://ms.yelp.my/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="ms-my" rel="alternate">
            <link href="https://www.yelp.com.tr/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="tr-tr" rel="alternate">
            <link href="https://fr.yelp.ch/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fr-ch" rel="alternate">
            <link href="https://www.yelp.de/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="de-de" rel="alternate">
            <link href="https://www.yelp.com.mx/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="es-mx" rel="alternate">
            <link href="https://sv.yelp.fi/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="sv-fi" rel="alternate">
            <link href="https://fr.yelp.ca/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="fr-ca" rel="alternate">
            <link href="https://www.yelp.se/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="sv-se" rel="alternate">
            <link href="https://it.yelp.ch/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="it-ch" rel="alternate">
            <link href="https://www.yelp.pl/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="pl-pl" rel="alternate">
            <link href="https://www.yelp.no/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA" hreflang="nb-no" rel="alternate">



                    <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">




                <meta name="critical_css_middleware">

                        <meta property="fb:app_id" content="97534753161">
        <meta property="og:site_name" content="Yelp">
        <meta property="og:type" content="website">
        <meta property="og:image" content="https://s3-media3.fl.yelpcdn.com/assets/srv0/seo_metadata/f9149736ad8d/assets/img/logos/yelp_og_image.png">
        <meta property="og:image:height" content="1080">
        <meta property="og:image:width" content="1920">



        
            <title>Best Fried chicken in Atlanta, GA - Yelp</title>


            <!--[if (IE 9)|(lt IE 9) ]> <link rel="stylesheet" type="text/css" media="all" href="https://s3-media2.fl.yelpcdn.com/assets/2/www/css/69fab8d61e90/www-pkg-main.css">
            <link rel="stylesheet" type="text/css" media="all" href="https://s3-media4.fl.yelpcdn.com/assets/2/www/css/86ebae39a475/www-pkg-more.css"> <![endif]-->
            <!--[if (gt IE 9)|!(IE)]><!--> <!--<![endif]-->
    


    <script></script>


                    <link href="https://www.facebook.com/yelp" itemprop="sameAs" id="sitelink-profile-facebook">
        <link href="https://twitter.com/yelp" itemprop="sameAs" id="sitelink-profile-twitter">
        <link href="https://www.linkedin.com/company/31517" itemprop="sameAs" id="sitelink-profile-linkedin">
        <link href="https://instagram.com/yelp" itemprop="sameAs" id="sitelink-profile-instagram">

    <meta itemscope="" itemtype="http://schema.org/WebSite" itemref="sitename sitelink  sitelink-profile-facebook sitelink-profile-twitter sitelink-profile-linkedin sitelink-profile-instagram">
    <meta itemprop="name" content="Yelp" id="sitename">
    <link href="https://www.yelp.com/" itemprop="url" id="sitelink">


            <style id="middleware_injected">html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:baseline;}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block;}body{line-height:1;}ol,ul{list-style:none;}blockquote,q{quotes:none;}blockquote:before,blockquote:after{content:"";content:none;}q:before,q:after{content:"";content:none;}table{border-collapse:collapse;border-spacing:0;}body:before{z-index:10000;}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0;font-weight:normal;}th,td{vertical-align:middle;}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0;}button{overflow:visible;}img{vertical-align:middle;}.hidden{display:none;}.inline-block{display:-moz-inline-stack;display:inline-block;}.align-middle{vertical-align:middle !important;}.no-js .no-js-hidden,.js .js-hidden{display:none !important;}.offscreen{clip:rect(0 0 0 0);position:absolute;left:-9999px;top:auto;overflow:hidden;width:1px;height:1px;}.clearfix{}.clearfix:before,.clearfix:after{content:" ";display:table;}.clearfix:after{clear:both;}.media-block{position:relative;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;}.media-title a{font-weight:bold;}.media-story{-webkit-box-flex:1;-moz-box-flex:1;-webkit-flex:1;-ms-flex:1;flex:1;min-width:0;min-height:0;}.media-block>.media-avatar{border-right:6px solid transparent;border-left:none;}.media-block--12>.media-avatar{border-right:12px solid transparent;border-left:none;}.ie .media-block{display:table;width:100%;}.ie .media-avatar,.ie .media-story{display:table-cell;vertical-align:top;}.ie .media-story{width:100%;}.nowrap{white-space:nowrap;}.u-pseudo-link{margin:0;padding:0;background:none;border:0;outline:0;color:#0073bb;cursor:pointer;}.u-pseudo-link:hover,.u-pseudo-link:focus{text-decoration:underline;}h1,.h1,h2,.h2,h3,.h3,h4,.h4{font-weight:bold;color:#d32323;margin:0 0 6px;}h1,.h1{font-size:18px;}h2,.h2{font-size:16px;}h3,.h3{font-size:14px;}h4,.h4{font-size:12px;margin:0 0 3px;}.events .content ul{margin-bottom:10px;overflow:hidden;width:100%;}.events .content ul li{zoom:1;float:left;line-height:14px;margin:0 0 10px;width:155px;}.events .content ul li *{position:relative;}.events .content ul li strong,.events .content ul li span.date{float:right;font-weight:normal;margin:0;width:100%;}@media print{.rating{background:transparent;text-indent:0em !important;}}@media only screen and (max-width: 989px){.responsive .section-header_block{margin:0 auto;}}@media only screen and (max-width: 989px){.responsive .section-header_block-main{float:none;width:auto;clear:both;margin:15px 0 0;padding:0;border:0;-webkit-box-shadow:none;box-shadow:none;}}@media only screen and (max-width: 989px){.responsive .section-header_block-side{float:none;width:auto;clear:both;margin:15px 0 0;padding:0;border:0;-webkit-box-shadow:none;box-shadow:none;}}@media only screen and (max-width: 989px){.responsive .section-header--complex .section-header_block-main,.responsive .section-header--complex .section-header_block-side{width:auto;}}body{font-size:14px;line-height:1.28571em;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;color:#333;}h1,.h1,h2,.h2,h3,.h3,h4,.h4{margin-bottom:6px;word-wrap:break-word !important;word-break:break-word !important;overflow-wrap:break-word !important;}h1 b,.h1 b,h2 b,.h2 b,h3 b,.h3 b,h4 b,.h4 b{font-weight:normal;color:#333;}h2,.h2,h3,.h3{color:#d32323;}h1,.h1{padding-top:6px;font-size:30px;line-height:1.2em;color:#333;}@media only screen and (max-width: 989px){.responsive h1,.responsive .h1{font-size:21px;line-height:1.28571em;}}@media only screen and (max-width: 479px){.responsive h1,.responsive .h1{font-size:24px;line-height:1.25em;}}h2,.h2{font-size:21px;line-height:1.28571em;}h3,.h3{font-size:16px;line-height:1.3125em;}@media only screen and (max-width: 479px){.responsive h3,.responsive .h3{font-size:18px;line-height:1.33333em;}}h4,.h4{font-size:14px;line-height:1.28571em;color:#333;}@media only screen and (max-width: 479px){.responsive{font-size:16px;line-height:1.5em;}}p{margin-bottom:12px;}a{color:#0073bb;text-decoration:none;}a:hover{text-decoration:underline;}b,strong,h1,h2,h3,h4,h5{font-weight:bold;}small{font-size:12px;line-height:1.5em;}@media only screen and (max-width: 479px){.responsive small{font-size:14px;line-height:1.28571em;}}address{display:block;font-style:normal;}pre{font-family:Monaco, Consolas, 'Courier New', monospace;}@media only screen and (max-width: 479px){.responsive .time-stamp{font-size:14px;line-height:1.28571em;}}@media only screen and (max-width: 479px){.responsive .legal-copy{font-size:14px;line-height:1.28571em;}}.bullet-before:before,.bullet-after:after{content:"•";position:relative;top:-1px;margin:0 3px;color:#999;font-size:10px;line-height:18px;}blockquote,.pull-quote{padding-left:18px;margin-bottom:12px;}blockquote{border-left:6px solid;border-color:#e6e6e6;border-color:rgba(0,0,0,0.1);}input::-webkit-input-placeholder,textarea::-webkit-input-placeholder{color:#999;}input:-moz-placeholder,textarea:-moz-placeholder{color:#999;}.layout-block{margin:0 -15px;}.layout-block:before,.layout-block:after{content:" ";display:table;}.layout-block:after{clear:both;}.layout-full .column-alpha{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;}.layout-a .column-alpha{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:66.66667%;}.layout-a .column-beta{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:33.33333%;}.hidden-non-responsive-inline,.hidden-non-responsive-inline-block,.hidden-non-responsive-block,.hidden-non-responsive-table-cell{display:none !important;}@media only screen and (max-width: 479px){.responsive .responsive-small-display-inline-block{display:inline-block !important;}.responsive .responsive-small-display-block{display:block !important;}.responsive .responsive-small-display-inline{display:inline !important;}}@media only screen and (max-width: 989px){.responsive .responsive-medium-display-inline-block{display:inline-block !important;}.responsive .responsive-medium-display-block{display:block !important;}.responsive .responsive-medium-display-inline{display:inline !important;}}@media only screen and (min-width: 990px){.responsive .responsive-large-display-inline-block{display:inline-block !important;}.responsive .responsive-large-display-block{display:block !important;}.responsive .responsive-large-display-inline{display:inline !important;}}@media only screen and (max-width: 479px){.responsive .responsive-visible-small-inline{display:inline !important;}.responsive .responsive-visible-small-inline-block{display:inline-block !important;}.responsive .responsive-visible-small-block{display:block !important;}.responsive .responsive-visible-small-table-cell{display:table-cell !important;}}@media only screen and (min-width: 480px) and (max-width: 989px){.responsive .responsive-visible-medium-only-inline{display:inline !important;}.responsive .responsive-visible-medium-only-inline-block{display:inline-block !important;}.responsive .responsive-visible-medium-only-block{display:block !important;}.responsive .responsive-visible-medium-only-table-cell{display:table-cell !important;}}@media only screen and (max-width: 989px){.responsive .responsive-visible-medium-inline{display:inline !important;}.responsive .responsive-visible-medium-inline-block{display:inline-block !important;}.responsive .responsive-visible-medium-block{display:block !important;}.responsive .responsive-visible-medium-table-cell{display:table-cell !important;}}@media only screen and (min-width: 990px){.responsive .responsive-visible-large-inline{display:inline !important;}.responsive .responsive-visible-large-inline-block{display:inline-block !important;}.responsive .responsive-visible-large-block{display:block !important;}.responsive .responsive-visible-large-cell{display:table-cell !important;}}@media only screen and (max-width: 479px){.responsive .responsive-hidden-small{display:none !important;}}@media only screen and (min-width: 480px) and (max-width: 989px){.responsive .responsive-hidden-medium-only{display:none !important;}}@media only screen and (max-width: 989px){.responsive .responsive-hidden-medium{display:none !important;}}@media only screen and (min-width: 990px){.responsive .responsive-hidden-large{display:none !important;}}@media only screen and (max-width: 989px){.responsive .row--responsive{margin:0 auto;}}@media only screen and (max-width: 989px){.responsive .column--responsive{float:none;width:auto;clear:both;margin:15px 0 0;padding:0;border:0;-webkit-box-shadow:none;box-shadow:none;}.responsive .column--responsive:first-child{margin-top:0;}}@media only screen and (max-width: 479px){.responsive .alert{padding:12px;border:1px solid #f15c00;font-size:14px;line-height:1.28571em;background:white;}.responsive .alert b{color:#f15c00;}}@media only screen and (max-width: 479px){.responsive .alert-message .read-more{font-size:14px;line-height:1.28571em;}}@media only screen and (max-width: 479px){.responsive .alert-content-wrapper>.arrange_unit{vertical-align:middle;}}@media only screen and (max-width: 479px){.responsive .alert-success{border-color:#41a700;}.responsive .alert-success b{color:#41a700;}}@media only screen and (max-width: 479px){.responsive .alert-error{border-color:#d32323;}.responsive .alert-error b{color:#d32323;}}@media only screen and (max-width: 479px){.responsive .alert-info{border-color:#0073bb;}.responsive .alert-info b{color:#333;}}@media only screen and (max-width: 989px){.responsive .alert--site{min-width:0;}}.arrange{display:table;min-width:100%;table-layout:auto;}.arrange.hidden{display:none;}.arrange_unit{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:table-cell;vertical-align:top;}.arrange_unit--fill{width:100%;}.arrange--middle>.arrange_unit{vertical-align:middle;}.arrange--baseline>.arrange_unit{vertical-align:baseline;}.arrange--6{margin-left:-6px;margin-right:-6px;border-collapse:separate;border-spacing:6px 0;}.arrange--6.arrange--equal,.arrange--6.arrange--wrap{margin-left:-3px;margin-right:-3px;}.arrange--6>.arrange_unit{margin-left:3px;margin-right:3px;border-collapse:collapse;border-spacing:0 0;}.ie .arrange--6.arrange--equal{border-collapse:collapse;border-spacing:0 0;}.ie .arrange--6.arrange--equal>.arrange_unit,.arrange--6.arrange--wrap>.arrange_unit{margin-left:auto;margin-right:auto;padding-left:3px;padding-right:3px;}@media only screen and (max-width: 989px){.responsive .arrange--6.arrange--stack>.arrange_unit+.arrange_unit{margin-top:6px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-6{margin-top:6px !important;}}.arrange--12{margin-left:-12px;margin-right:-12px;border-collapse:separate;border-spacing:12px 0;}.arrange--12.arrange--equal,.arrange--12.arrange--wrap{margin-left:-6px;margin-right:-6px;}.arrange--12>.arrange_unit{margin-left:6px;margin-right:6px;border-collapse:collapse;border-spacing:0 0;}.ie .arrange--12.arrange--equal{border-collapse:collapse;border-spacing:0 0;}.ie .arrange--12.arrange--equal>.arrange_unit,.arrange--12.arrange--wrap>.arrange_unit{margin-left:auto;margin-right:auto;padding-left:6px;padding-right:6px;}@media only screen and (max-width: 989px){.responsive .arrange--12.arrange--stack>.arrange_unit+.arrange_unit{margin-top:12px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-12{margin-top:12px !important;}}.arrange--18{margin-left:-18px;margin-right:-18px;border-collapse:separate;border-spacing:18px 0;}.arrange--18.arrange--equal,.arrange--18.arrange--wrap{margin-left:-9px;margin-right:-9px;}.arrange--18>.arrange_unit{margin-left:9px;margin-right:9px;border-collapse:collapse;border-spacing:0 0;}.ie .arrange--18.arrange--equal{border-collapse:collapse;border-spacing:0 0;}.ie .arrange--18.arrange--equal>.arrange_unit,.arrange--18.arrange--wrap>.arrange_unit{margin-left:auto;margin-right:auto;padding-left:9px;padding-right:9px;}@media only screen and (max-width: 989px){.responsive .arrange--18.arrange--stack>.arrange_unit+.arrange_unit{margin-top:18px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-18{margin-top:18px !important;}}@media only screen and (max-width: 989px){.responsive .arrange--24.arrange--stack>.arrange_unit+.arrange_unit{margin-top:24px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-24{margin-top:24px !important;}}.arrange--30{margin-left:-30px;margin-right:-30px;border-collapse:separate;border-spacing:30px 0;}.arrange--30.arrange--equal,.arrange--30.arrange--wrap{margin-left:-15px;margin-right:-15px;}.arrange--30>.arrange_unit{margin-left:15px;margin-right:15px;border-collapse:collapse;border-spacing:0 0;}.ie .arrange--30.arrange--equal{border-collapse:collapse;border-spacing:0 0;}.ie .arrange--30.arrange--equal>.arrange_unit,.arrange--30.arrange--wrap>.arrange_unit{margin-left:auto;margin-right:auto;padding-left:15px;padding-right:15px;}@media only screen and (max-width: 989px){.responsive .arrange--30.arrange--stack>.arrange_unit+.arrange_unit{margin-top:30px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-30{margin-top:30px !important;}}@media only screen and (max-width: 989px){.responsive .arrange--36.arrange--stack>.arrange_unit+.arrange_unit{margin-top:36px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-36{margin-top:36px !important;}}@media only screen and (max-width: 989px){.responsive .arrange--42.arrange--stack>.arrange_unit+.arrange_unit{margin-top:42px;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--stack-42{margin-top:42px !important;}}.arrange--wrap{display:block;font-size:0;line-height:1;text-align:left;}.arrange--wrap>.arrange_unit{display:inline-block;zoom:1;width:auto;font-size:14px;line-height:1.28571em;}@media only screen and (max-width: 479px){.responsive .arrange--wrap>.arrange_unit{font-size:16px;line-height:1.3125em;}}.arrange--wrap.arrange--6{margin-top:-6px;}.arrange--wrap.arrange--6>.arrange_unit{margin-top:6px;}.arrange--wrap.arrange--12{margin-top:-12px;}.arrange--wrap.arrange--12>.arrange_unit{margin-top:12px;}.arrange--wrap.arrange--18{margin-top:-18px;}.arrange--wrap.arrange--18>.arrange_unit{margin-top:18px;}.arrange--wrap.arrange--30{margin-top:-30px;}.arrange--wrap.arrange--30>.arrange_unit{margin-top:30px;}@media only screen and (max-width: 989px){.responsive .arrange--wrap.arrange--stack{margin-top:0;}.responsive .arrange--wrap.arrange--stack>.arrange_unit:first-child{margin-top:0;}}@media only screen and (max-width: 479px){.responsive .arrange--wrap.arrange--stack-small{margin-top:0;}.responsive .arrange--wrap.arrange--stack-small>.arrange_unit:first-child{margin-top:0;}}.arrange--2-units>.arrange_unit{width:50%;}@media only screen and (max-width: 989px){.responsive .arrange--stack{display:block;margin-right:auto;margin-left:auto;}.responsive .arrange--stack>.arrange_unit{display:block;margin-right:auto;margin-left:auto;padding-right:0;padding-left:0;}.responsive .arrange--stack>.arrange_unit+.arrange_unit{margin-top:15px;}.responsive .arrange--stack>.nowrap{white-space:normal;}.responsive .arrange--stack.arrange--wrap>.arrange_unit{display:block;width:auto;}.responsive .arrange--stack.arrange--wrap.arrange--6.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:6px;padding-top:6px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--6.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--12.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:12px;padding-top:12px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--12.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--18.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:18px;padding-top:18px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--18.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--24.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:24px;padding-top:24px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--24.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--30.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:30px;padding-top:30px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--30.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--36.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:36px;padding-top:36px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--36.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack.arrange--wrap.arrange--42.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:42px;padding-top:42px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack.arrange--wrap.arrange--42.arrange--wrap-bordered>.arrange_unit::before{display:none;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small{display:block;margin-right:auto;margin-left:auto;}.responsive .arrange--stack-small>.arrange_unit{display:block;margin-right:auto;margin-left:auto;padding-right:0;padding-left:0;}.responsive .arrange--stack-small>.arrange_unit+.arrange_unit{margin-top:15px;}.responsive .arrange--stack-small>.nowrap{white-space:normal;}.responsive .arrange--stack-small.arrange--wrap>.arrange_unit{display:block;width:auto;}.responsive .arrange--stack-small.arrange--wrap.arrange--6.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:6px;padding-top:6px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--6.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--12.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:12px;padding-top:12px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--12.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--18.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:18px;padding-top:18px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--18.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--24.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:24px;padding-top:24px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--24.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--30.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:30px;padding-top:30px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--30.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--36.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:36px;padding-top:36px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--36.arrange--wrap-bordered>.arrange_unit::before{display:none;}.responsive .arrange--stack-small.arrange--wrap.arrange--42.arrange--wrap-bordered>.arrange_unit+.arrange_unit{margin-top:42px;padding-top:42px;border-top:1px solid #e6e6e6;}.responsive .arrange--stack-small.arrange--wrap.arrange--42.arrange--wrap-bordered>.arrange_unit::before{display:none;}}.arrange--equal{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;}.arrange--equal>.arrange_unit{-webkit-box-flex:1;-moz-box-flex:1;-webkit-flex:1;-ms-flex:1;flex:1;min-width:0;min-height:0;display:block;}.arrange--equal.arrange--middle{-webkit-box-align:center;-moz-box-align:center;-ms-flex-align:center;box-align:center;-webkit-align-items:center;align-items:center;}.arrange--equal.arrange--baseline{-webkit-box-align:baseline;-moz-box-align:baseline;-ms-flex-align:baseline;box-align:baseline;-webkit-align-items:baseline;align-items:baseline;}.ie .arrange--equal{width:100%;table-layout:fixed;}.ie .arrange--equal>.arrange_unit{width:1%;display:table-cell;}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-1-2{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-1-2{width:auto;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-1-3{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-1-3{width:auto;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-2-3{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-2-3{width:auto;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-1-4{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-1-4{width:auto;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-2-4{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-2-4{width:auto;}}@media only screen and (max-width: 989px){.responsive .arrange--stack>.arrange_unit--grid-3-4{width:auto;}}@media only screen and (max-width: 479px){.responsive .arrange--stack-small>.arrange_unit--grid-3-4{width:auto;}}@media only screen and (max-width: 989px){.responsive .card-num-field-holder{height:20px;padding-top:1px;}}.indexed-biz-name{display:block;}.indexed-biz-name .biz-name{display:inline;}.price-range{letter-spacing:1px;white-space:nowrap;}.price-range::after{content:attr(data-remainder);color:#999;}.price-category{clear:both;}.biz-listing-large .biz-name{font-size:16px;line-height:1.3125em;}.biz-listing-large .neighborhood-str-list,.biz-listing-large .service-area{display:block;margin-bottom:6px;}.indexed-biz-archive{position:relative;}.indexed-biz-archive .biz-listing-large{margin:0 -15px;}.indexed-biz-archive .biz-listing-large:before,.indexed-biz-archive .biz-listing-large:after{content:" ";display:table;}.indexed-biz-archive .biz-listing-large:after{clear:both;}.indexed-biz-archive .main-attributes{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:62.5%;}.indexed-biz-archive .secondary-attributes{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:37.5%;margin-top:3px;}.indexed-biz-archive .secondary-attributes .neighborhood-str-list{margin-bottom:8px;}.indexed-biz-archive .snippet-block{margin-top:12px;}@media only screen and (max-width: 479px){.event-browse-quicklink::after{content:none;}}.rating-qualifier{display:block;float:left;color:#666;font-weight:normal;}.biz-rating-large{margin:6px 0;}@media only screen and (max-width: 479px){.responsive .biz-rating-large{font-size:14px;line-height:1.28571em;}}.biz-rating-large .rating-large{float:left;margin:-1px 6px 0 0;}@media (max-width: 960px){.lightbox--media-details{padding-right:0;padding-left:0;}.lightbox-close{right:0;}}@media only screen and (max-width: 479px){.responsive .throbber{background-position:center;width:100%;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.throbber{background-image:url(//s3-media4.fl.yelpcdn.com/assets/2/www/img/434a0c97b379/loaders/small-throbber@2x.gif);background-size:21px 21px;}}.circle-spinner{width:18px;height:18px;position:relative;}.circle-spinner .container2{-webkit-transform:rotateZ(45deg);-moz-transform:rotateZ(45deg);-ms-transform:rotateZ(45deg);transform:rotateZ(45deg);}.circle-spinner .container3{-webkit-transform:rotateZ(90deg);-moz-transform:rotateZ(90deg);-ms-transform:rotateZ(90deg);transform:rotateZ(90deg);}.circle-spinner_segment{position:absolute;width:80%;height:80%;margin-top:2px;margin-left:2px;}.circle-spinner_segment .circle1{top:0;left:0;}.circle-spinner_segment .circle2{top:0;right:0;}.circle-spinner_segment .circle3{right:0;bottom:0;}.circle-spinner_segment .circle4{left:0;bottom:0;}.circle-spinner_segment>div{width:4px;height:4px;background-color:#fff;border-radius:100%;position:absolute;-webkit-animation:bouncedelay 1.2s infinite ease-in-out;animation:bouncedelay 1.2s infinite ease-in-out;-webkit-animation-fill-mode:both;animation-fill-mode:both;}.container2 .circle1{-webkit-animation-delay:-1.1s;animation-delay:-1.1s;}.container3 .circle1{-webkit-animation-delay:-1s;animation-delay:-1s;}.container1 .circle2{-webkit-animation-delay:-.9s;animation-delay:-.9s;}.container2 .circle2{-webkit-animation-delay:-.8s;animation-delay:-.8s;}.container3 .circle2{-webkit-animation-delay:-.7s;animation-delay:-.7s;}.container1 .circle3{-webkit-animation-delay:-.6s;animation-delay:-.6s;}.container2 .circle3{-webkit-animation-delay:-.5s;animation-delay:-.5s;}.container3 .circle3{-webkit-animation-delay:-.4s;animation-delay:-.4s;}.container1 .circle4{-webkit-animation-delay:-.3s;animation-delay:-.3s;}.container2 .circle4{-webkit-animation-delay:-.2s;animation-delay:-.2s;}.container3 .circle4{-webkit-animation-delay:-.1s;animation-delay:-.1s;}.i-stars{background:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/9b34e39ccbeb/assets/img/stars/stars.png) no-repeat;background-size:132px 560px;display:inline-block;vertical-align:middle;}@media print{.i-stars{background-image:none !important;}.i-stars img{position:relative;width:auto;height:auto;}}@media print{.i-stars--large-0 img{left:0;top:0;}}@media print{.i-stars--large-1 img{left:0;top:-24px;}}@media print{.i-stars--large-1-half img{left:0;top:-48px;}}@media print{.i-stars--large-2 img{left:0;top:-72px;}}@media print{.i-stars--large-2-half img{left:0;top:-96px;}}@media print{.i-stars--large-3 img{left:0;top:-120px;}}@media print{.i-stars--large-3-half img{left:0;top:-144px;}}@media print{.i-stars--large-4 img{left:0;top:-168px;}}@media print{.i-stars--large-4-half img{left:0;top:-192px;}}@media print{.i-stars--large-5 img{left:0;top:-216px;}}@media print{.i-stars--regular-0 img{left:0;top:-240px;}}@media print{.i-stars--regular-1 img{left:0;top:-258px;}}@media print{.i-stars--regular-1-half img{left:0;top:-276px;}}@media print{.i-stars--regular-2 img{left:0;top:-294px;}}@media print{.i-stars--regular-2-half img{left:0;top:-312px;}}@media print{.i-stars--regular-3 img{left:0;top:-330px;}}.i-stars--regular-3-half{width:102px;height:18px;background-position:0 -348px;}@media print{.i-stars--regular-3-half img{left:0;top:-348px;}}.i-stars--regular-4{width:102px;height:18px;background-position:0 -366px;}@media print{.i-stars--regular-4 img{left:0;top:-366px;}}.i-stars--regular-4-half{width:102px;height:18px;background-position:0 -384px;}@media print{.i-stars--regular-4-half img{left:0;top:-384px;}}@media print{.i-stars--regular-5 img{left:0;top:-402px;}}@media print{.i-stars--small-0 img{left:0;top:-420px;}}@media print{.i-stars--small-1 img{left:0;top:-434px;}}@media print{.i-stars--small-1-half img{left:0;top:-448px;}}@media print{.i-stars--small-2 img{left:0;top:-462px;}}@media print{.i-stars--small-2-half img{left:0;top:-476px;}}@media print{.i-stars--small-3 img{left:0;top:-490px;}}@media print{.i-stars--small-3-half img{left:0;top:-504px;}}@media print{.i-stars--small-4 img{left:0;top:-518px;}}@media print{.i-stars--small-4-half img{left:0;top:-532px;}}@media print{.i-stars--small-5 img{left:0;top:-546px;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.i-stars{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/de2252bea656/assets/img/stars/stars@2x.png);}}@media print{.i-gray-stars{background-image:none !important;}.i-gray-stars img{position:relative;width:auto;height:auto;}}@media print{.i-gray-stars--large-0 img{left:0;top:0;}}@media print{.i-gray-stars--large-1 img{left:0;top:-24px;}}@media print{.i-gray-stars--large-1-half img{left:0;top:-48px;}}@media print{.i-gray-stars--large-2 img{left:0;top:-72px;}}@media print{.i-gray-stars--large-2-half img{left:0;top:-96px;}}@media print{.i-gray-stars--large-3 img{left:0;top:-120px;}}@media print{.i-gray-stars--large-3-half img{left:0;top:-144px;}}@media print{.i-gray-stars--large-4 img{left:0;top:-168px;}}@media print{.i-gray-stars--large-4-half img{left:0;top:-192px;}}@media print{.i-gray-stars--large-5 img{left:0;top:-216px;}}@media print{.i-gray-stars--regular-0 img{left:0;top:-240px;}}@media print{.i-gray-stars--regular-1 img{left:0;top:-258px;}}@media print{.i-gray-stars--regular-1-half img{left:0;top:-276px;}}@media print{.i-gray-stars--regular-2 img{left:0;top:-294px;}}@media print{.i-gray-stars--regular-2-half img{left:0;top:-312px;}}@media print{.i-gray-stars--regular-3 img{left:0;top:-330px;}}@media print{.i-gray-stars--regular-3-half img{left:0;top:-348px;}}@media print{.i-gray-stars--regular-4 img{left:0;top:-366px;}}@media print{.i-gray-stars--regular-4-half img{left:0;top:-384px;}}@media print{.i-gray-stars--regular-5 img{left:0;top:-402px;}}@media print{.i-gray-stars--small-0 img{left:0;top:-420px;}}@media print{.i-gray-stars--small-1 img{left:0;top:-434px;}}@media print{.i-gray-stars--small-1-half img{left:0;top:-448px;}}@media print{.i-gray-stars--small-2 img{left:0;top:-462px;}}@media print{.i-gray-stars--small-2-half img{left:0;top:-476px;}}@media print{.i-gray-stars--small-3 img{left:0;top:-490px;}}@media print{.i-gray-stars--small-3-half img{left:0;top:-504px;}}@media print{.i-gray-stars--small-4 img{left:0;top:-518px;}}@media print{.i-gray-stars--small-4-half img{left:0;top:-532px;}}@media print{.i-gray-stars--small-5 img{left:0;top:-546px;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.i-gray-stars{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/8307695437ff/assets/img/stars/gray_stars@2x.png);}}.rating,.rating-large,.rating-very-large{position:relative;overflow:hidden;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.filtered-reviews-content .i-stars{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/8307695437ff/assets/img/stars/gray_stars@2x.png);}}.island{padding:11px;background:#f5f5f5;border:1px solid #e6e6e6;border-radius:4px;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.island-city-scape,.island--city-scape{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/yelp_styleguide/248de198b86e/assets/img/structural/cityscape@2x.png);}}@media only screen and (max-width: 479px){.responsive .card_content-text{display:-webkit-box;height:3em;-webkit-line-clamp:2;-webkit-box-orient:vertical;text-overflow:-o-ellipsis-lastline;overflow:hidden;position:relative;}}@media only screen and (max-width: 479px){.responsive .card--horizontal .card_photo{float:none;width:100%;}.responsive .card--horizontal .card_body{width:100%;margin-left:0;}.responsive .card--horizontal .card_content{padding:12px 12px 0;height:auto;}}.dropdown{position:relative;display:inline-block;}.dropdown_menu{display:none;padding:.5em 0;position:absolute;top:auto;z-index:5;border-radius:3px;border:1px solid #e6e6e6;background-color:white;-webkit-box-shadow:0 2px 8px rgba(0,0,0,0.2);box-shadow:0 2px 8px rgba(0,0,0,0.2);}.dropdown_menu.is-visible,.no-js .dropdown:hover .dropdown_menu{display:block;}.dropdown_menu-container{z-index:5;}.dropdown_toggle:focus{outline:0;}.dropdown_arrow{left:-3px;}.dropdown_toggle-action:hover{text-decoration:none;}.dropdown_toggle-action[data-dropdown-prefix]::before{content:attr(data-dropdown-prefix);}.dropdown_toggle-action[data-dropdown-prefix] .dropdown_toggle-text{font-weight:bold;}.dropdown_item{width:100%;min-width:200px;}.dropdown_link{display:block;text-overflow:ellipsis;overflow:hidden;white-space:nowrap;padding:.25em 1em;}.dropdown--hover .dropdown_link[href]:hover,.dropdown--hover .dropdown_link[href]:focus,.dropdown--hover .dropdown_link.is-selected{background-color:#0073bb;color:white;text-decoration:none;}html:not(.ie9) .dropdown--fade .dropdown_menu{display:block !important;}html:not(.ie9) .dropdown--fade .dropdown_menu-container{position:absolute;}html:not(.ie9) .dropdown--fade.dropdown--arrow .dropdown_toggle::before,html:not(.ie9) .dropdown--fade.dropdown--arrow .dropdown_toggle::after{display:block;}html:not(.ie9) .dropdown--fade .dropdown_toggle:not(.is-active) ~ .dropdown_menu-container,html:not(.ie9) .dropdown--fade.dropdown--arrow .dropdown_toggle:not(.is-active)::before,html:not(.ie9) .dropdown--fade.dropdown--arrow .dropdown_toggle:not(.is-active)::after{-webkit-animation:fadeOutToNone .15s ease-out;animation:fadeOutToNone .15s ease-out;-webkit-animation-fill-mode:forwards;animation-fill-mode:forwards;pointer-events:none;}html:not(.ie9) .dropdown--fade.fade-initial-load .dropdown_toggle ~ .dropdown_menu-container,html:not(.ie9) .dropdown--fade.fade-initial-load.dropdown--arrow .dropdown_toggle::before,html:not(.ie9) .dropdown--fade.fade-initial-load.dropdown--arrow .dropdown_toggle::after{display:none !important;}@media only screen and (max-width: 479px){.responsive .dropdown--boxed-on-mobile .dropdown_arrow{position:absolute;top:0;left:initial;bottom:0;margin:auto;right:12px;color:#333;}}@media only screen and (max-width: 479px){.responsive .dropdown--boxed-on-mobile .dropdown_menu{width:100%;}}@media only screen and (max-width: 479px){.responsive .dropdown--boxed-on-mobile .dropdown_toggle-action{display:block;color:#333;}}@media only screen and (max-width: 479px){.responsive .dropdown--boxed-on-mobile .dropdown_toggle{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;font-size:14px;line-height:1.28571em;width:100%;background:#fafafa;background:rgba(250,250,249,0.9);padding:9px;border:1px solid #ccc;border-radius:3px;cursor:pointer;}}@media only screen and (max-width: 479px){.responsive .dropdown--boxed-on-mobile{width:100%;}}.dropdown--separate-groups .dropdown_menu{padding:0;}.dropdown--separate-groups .dropdown_menu-group{margin:0;padding:.5em 0;border-top:1px solid #e6e6e6;}.dropdown--separate-groups .dropdown_menu-group:first-child{border-top:0;}.dropdown--arrow .dropdown_toggle{position:relative;}.dropdown--arrow .dropdown_toggle::before,.dropdown--arrow .dropdown_toggle::after{content:"";position:absolute;z-index:5;left:50%;bottom:-11px;width:0;height:0;border:solid transparent;pointer-events:none;display:none;}.dropdown--arrow .dropdown_toggle::after{border-bottom-color:white;border-width:10px;margin-left:-10px;}.dropdown--arrow .dropdown_toggle::before{border-bottom-color:#e6e6e6;border-width:11px;margin-left:-11px;}.dropdown--arrow .dropdown_toggle ~ .dropdown_menu-container{position:absolute;padding-top:10px;top:auto;z-index:5;display:inline;}.dropdown--arrow .dropdown_menu{position:static;}.dropdown--restricted .dropdown_menu{max-height:350px;overflow-y:auto;}@media only screen and (max-width: 479px){.responsive .read-more{font-size:14px;line-height:1.28571em;}}.link-more{font-size:12px;}@media only screen and (max-width: 479px){.responsive .link-more{font-size:14px;line-height:1.28571em;}}@media only screen and (max-width: 479px){.responsive .action-link{font-size:14px;line-height:1.28571em;}}@media only screen and (max-width: 479px){.responsive .chiclet-link{font-size:14px;line-height:1.28571em;}}.show-tooltip{position:relative;}.tooltip-wrapper{position:absolute;left:-9999px;bottom:100%;width:250px;margin-left:-125px;margin-bottom:5px;text-align:center;text-decoration:none;}.show-tooltip:hover .tooltip-wrapper{left:50%;}.tooltip{display:inline-block;position:relative;padding:6px 9px;z-index:4;vertical-align:middle;white-space:normal;font-size:12px;pointer-events:none;font-weight:bold;line-height:18px;background:#333;background:rgba(0,0,0,0.8);color:white;border-radius:5px;text-shadow:none;text-align:left;cursor:default;-webkit-box-shadow:0 1px rgba(255,255,255,0.1);box-shadow:0 1px rgba(255,255,255,0.1);}@media only screen and (max-width: 479px){.responsive .tooltip{font-size:14px;line-height:1.28571em;}}.tooltip::after{display:block;position:absolute;content:" ";width:0;height:0;border:7px solid transparent;margin:auto;z-index:5;left:50%;top:100%;right:auto;bottom:auto;margin-left:-7px;border-top-color:#333;border-top-color:rgba(0,0,0,0.8);}.tooltip::before{display:block;position:absolute;content:" ";width:0;height:0;border:8px solid transparent;margin:auto;z-index:5;left:50%;top:100%;right:auto;bottom:auto;margin-left:-8px;border-top-color:"";border-top-color:rgba(255,255,255,0.1);}@media screen and (min-width: 0\0){.tooltip-wrapper--left-edge .tooltip::before,.tooltip-wrapper--left-edge .tooltip::after{margin-left:-1px;}}.ylist>li{margin-bottom:12px;}.ylist-bordered>li{margin:0;padding:18px 0;border-bottom:1px solid #e6e6e6;padding-bottom:17px;}.inline-layout{margin:-3px;display:block;font-size:0;line-height:1;text-align:left;}.inline-layout>li{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline-block;zoom:1;vertical-align:top;font-size:14px;line-height:1.28571em;width:50%;padding:0 3px;margin:3px 0;}@media only screen and (max-width: 989px){.responsive .inline-layout--stack>li{float:none;width:100%;margin:6px 0;}}@media only screen and (max-width: 989px){.responsive .titled-nav{margin:0 -15px;}.responsive .titled-nav.titled-nav--show-first-mobile-title .titled-nav_menu:first-child .titled-nav-header_content{display:block;}.responsive .titled-nav_menus{display:none;}.responsive .titled-nav-header{background-color:#f5f5f5;padding:12px;}.responsive .titled-nav_menu{border:0;border-radius:0;margin:0;}.responsive .titled-nav_menu:first-child .titled-nav-header_content{display:none;}.responsive .titled-nav_item:last-child .titled-nav_link-content{border-bottom:0;}.responsive .titled-nav_link{padding-left:18px;background-color:white;}.responsive .titled-nav_link.is-active{font-weight:normal;color:#333;}.responsive .titled-nav_link.is-active::before{width:6px;}.responsive .titled-nav_link.is-active .titled-nav_link-subtext{color:#999;opacity:1;}.responsive .titled-nav_link:hover,.responsive .titled-nav_link:focus{background:white;}.responsive .titled-nav_new-window{padding-right:5px;}.responsive .titled-nav_subnav .titled-nav_link{padding-left:36px;}}@media only screen and (max-width: 989px){.responsive .table--responsive td,.responsive .table--responsive th{font-size:12px;line-height:1.5em;padding:6px 3px;vertical-align:middle;}}@media only screen and (max-width: 989px){.responsive .table.table--stack tr,.responsive .table.table--stack td,.responsive .table.table--stack th{display:block;width:auto;}.responsive .table.table--stack td,.responsive .table.table--stack th{border-top:0;padding:12px;}.responsive .table.table--stack td+td,.responsive .table.table--stack td+th,.responsive .table.table--stack th+td,.responsive .table.table--stack th+th{padding-top:0;}.responsive .table.table--stack thead{border-bottom:1px solid #e6e6e6;}.responsive .table.table--stack tfoot,.responsive .table.table--stack tr+tr{border-top:1px solid #e6e6e6;}.responsive .table.table--stack [data-td-label]:before{content:attr(data-td-label);display:block;font-weight:bold;margin-bottom:12px;}.responsive .table.table--stack.table-analytics [data-td-label]:before{font-weight:normal;font-size:12px;line-height:1em;}}.toggle-list-content{padding-left:15px;display:none;}.toggle-list-item--active>.toggle-list-content{display:block;}.toggle-link-arrow-wrap{width:8px;margin-right:7px;}.toggle-link-arrow{width:0;height:0;content:'';display:inline-block;border-style:solid;border-color:transparent transparent transparent #999;border-left-style:solid;border-width:4px 0 4px 6.9282px;}.toggle-list-item--active>.toggle-list-link .toggle-link-arrow{width:0;height:0;content:'';display:inline-block;border-style:solid;border-color:#999 transparent transparent;border-top-style:solid;border-width:6.9282px 4px 0;}@media only screen and (max-width: 989px){.responsive .biz-feed-row{margin:0 auto;}}@media only screen and (max-width: 989px){.responsive .biz-feed-column-a{float:none;width:auto;clear:both;margin:15px 0 0;padding:0;border:0;-webkit-box-shadow:none;box-shadow:none;}}@media only screen and (max-width: 989px){.responsive .biz-feed-column-b{float:none;width:auto;clear:both;margin:15px 0 0;padding:0;border:0;-webkit-box-shadow:none;box-shadow:none;}}.yloca-tip{float:left;margin:1px 6px 0 0;padding:0 4px 0 3px;background:#ebac2c;color:#fff;font-size:12px;line-height:normal;font-weight:bold;-webkit-font-smoothing:antialiased;border-radius:3px;}.yloca-info{float:right;margin-left:3px;color:#ebac2c;}@media only screen and (max-width: 479px){.responsive .yform .business_finder .submit_container{padding-top:0;}}@media only screen and (max-width: 479px){.responsive #contact-form .business_finder .search-biz-name,.responsive #contact-form .business_finder .search-location{width:100%;}}.date-picker .date-input{width:65px;}.date-picker .icon{margin-top:1px;}.drop-menu-origin{position:relative;}.drop-menu-origin+.drop-menu-origin{margin-left:12px;}.drop-menu-link{display:inline-block;font-size:12px;line-height:1.5em;cursor:pointer;}.drop-menu-link:active,.drop-menu-link:hover{text-decoration:none;}.drop-menu{display:none;position:absolute;z-index:11;right:0;padding:12px;min-width:217px;background:white;border:1px solid #ccc;border-color:rgba(0,0,0,0.2);border-radius:3px;-webkit-box-shadow:0 2px 8px rgba(0,0,0,0.2);box-shadow:0 2px 8px rgba(0,0,0,0.2);-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}.drop-menu-active .drop-menu,.no-js .drop-menu-origin:hover .drop-menu{display:block;}.drop-menu-has-arrow{margin-top:10px;}.drop-menu-arrow{position:relative;top:-12px;}.drop-menu-arrow:after,.drop-menu-arrow:before{bottom:100%;right:8px;border:solid transparent;content:"";height:0;width:0;position:absolute;pointer-events:none;}.drop-menu-arrow:before{border-bottom-color:rgba(0,0,0,0.2);border-width:11px;margin-left:-11px;}.drop-menu-arrow:after{border-bottom-color:white;border-width:10px;margin-left:-10px;}.drop-down-menu-link+.drop-down-menu-link{margin-top:6px;}.drop-down-menu-link a{display:block;word-wrap:break-word;}.drop-menu-group+.drop-menu-group{margin-top:12px;border-top:1px solid #e6e6e6;padding-top:11px;}.pagination-block{border-bottom:1px solid #e6e6e6;}@media only screen and (max-width: 989px){.responsive .pagination-block{text-align:center;}}.pagination-block .page-of-pages{padding:11px 0;}.pagination-block .page-of-pages,.pagination-block .pagination-links{white-space:nowrap;}@media only screen and (max-width: 479px){.responsive .pagination-block .page-of-pages,.responsive .pagination-block .pagination-links{white-space:normal;}}@media only screen and (max-width: 989px){.responsive .pagination-block .page-of-pages.arrange_unit+.pagination-links.arrange_unit{margin-top:-11px;}}.pagination-links .page-option{display:inline-block;min-width:15px;margin:0;margin-bottom:-1px;text-align:center;}@media only screen and (max-width: 989px){.responsive .pagination-links .page-option{padding-top:0;}}.pagination-links .page-option:hover{text-decoration:none;}.pagination-links .page-option.available-number:hover{text-decoration:underline;}.pagination-links .page-option.current .pagination-links_anchor{color:#333;border-bottom-color:#d32323;cursor:auto;}.pagination-links .page-option .pagination-links_anchor{display:inline-block;padding:12px 6px 9px;border-bottom:3px solid transparent;}.pagination-links .next{margin-left:12px !important;padding-right:0;}.pagination-links .pagination-label:hover{text-decoration:underline;}.photo-box .photo-box-img{border-radius:4px;}.photo-box a:visited img{outline:none;}.pb-30s .photo-box-img{margin-top:3px;}@media only screen and (max-width: 479px){.responsive .photo-box-shelf .photo-box{height:100px;}}@media screen and (max-width: 1800px){.photo-box-shelf_fill-item+.photo-box-shelf_fill-item{display:none !important;}}@media screen and (max-width: 1500px){.photo-box-shelf_fill-item{display:none !important;}}@media only screen and (max-width: 479px){.responsive .responsive-photo-box .pb-60s .photo-box-img{height:30px;width:30px;}}.ybtn{display:inline-block;vertical-align:middle;margin:0;cursor:pointer;border:1px solid;font-weight:bold;text-align:center;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;font-size:14px;line-height:1.28571em;border-color:#ccc;color:#666;background-color:#f7f7f7;background:-webkit-linear-gradient(#fff, #f7f7f7);background:linear-gradient(#fff, #f7f7f7);-webkit-box-shadow:0 1px 1px rgba(0,0,0,0.1);box-shadow:0 1px 1px rgba(0,0,0,0.1);padding:8px 19px 9px;border-radius:3px;}.ybtn:focus{outline:thin dotted;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px;}@media only screen and (max-width: 989px){.responsive .yform .ybtn{padding:9px 18px;}}@media only screen and (max-width: 479px){.responsive .ybtn{padding:12px 14px;-webkit-box-shadow:none;box-shadow:none;font-weight:normal;}}.ybtn:hover{background-color:#fff;background:-webkit-linear-gradient(#fff, #fff);background:linear-gradient(#fff, #fff);}.ybtn:active{background-color:#ededed;background:-webkit-linear-gradient(#f5f5f5, #ededed);background:linear-gradient(#f5f5f5, #ededed);}.ybtn.ybtn-disabled,.ybtn.ybtn--disabled,.ybtn[disabled]{background-color:#e3e3e3;background:-webkit-linear-gradient(#ebebeb, #e3e3e3);background:linear-gradient(#ebebeb, #e3e3e3);-webkit-box-shadow:none;box-shadow:none;}a.ybtn{text-decoration:none !important;}a.ybtn:hover,a.ybtn:visited{color:#666;}.ybtn-disabled,.ybtn--disabled,.ybtn[disabled]{opacity:0.4;outline:none;cursor:default;}.ybtn+a,.ybtn+.ybtn-sibling{display:inline-block;vertical-align:middle;margin-left:12px;}.ybtn+a:not(.ybtn),.ybtn+.ybtn-sibling:not(.ybtn){margin-top:9px;margin-bottom:7px;font-size:14px;line-height:1.28571em;}@media only screen and (max-width: 479px){.responsive .ybtn+a:not(.ybtn),.responsive .ybtn+.ybtn-sibling:not(.ybtn){font-size:16px;line-height:1.3125em;}}.ybtn-small:not(.ybtn--social),.ybtn--small:not(.ybtn--social){padding:5px 8px;font-size:12px;line-height:1.5em;}@media only screen and (max-width: 479px){.responsive .ybtn-small:not(.ybtn--social),.responsive .ybtn--small:not(.ybtn--social){font-size:14px;line-height:1.28571em;}}.ybtn-small:not(.ybtn--social)+a:not(.ybtn),.ybtn-small:not(.ybtn--social)+.ybtn-sibling:not(.ybtn),.ybtn--small:not(.ybtn--social)+a:not(.ybtn),.ybtn--small:not(.ybtn--social)+.ybtn-sibling:not(.ybtn){margin-top:5px;margin-bottom:5px;font-size:12px;line-height:1.5em;}@media only screen and (max-width: 479px){.responsive .ybtn-small:not(.ybtn--social)+a:not(.ybtn),.responsive .ybtn-small:not(.ybtn--social)+.ybtn-sibling:not(.ybtn),.responsive .ybtn--small:not(.ybtn--social)+a:not(.ybtn),.responsive .ybtn--small:not(.ybtn--social)+.ybtn-sibling:not(.ybtn){font-size:14px;line-height:1.28571em;}}@media only screen and (max-width: 989px){.responsive .yform .ybtn-small:not(.ybtn--social),.responsive .yform .ybtn--small:not(.ybtn--social){padding:7px 10px;}}.ybtn-full,.ybtn--full{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}@media only screen and (max-width: 989px){.responsive .ybtn-full-responsive-medium{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}}@media only screen and (max-width: 479px){.responsive .ybtn-full-responsive-small{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}}@media only screen and (max-width: 479px){.responsive .ybtn-full-responsive-small+a,.responsive .ybtn-full-responsive-small+.ybtn-sibling{display:block;text-align:center;margin-left:auto;}}@media only screen and (max-width: 989px){.responsive .ybtn-full-responsive-medium+a,.responsive .ybtn-full-responsive-medium+.ybtn-sibling{display:block;text-align:center;margin-left:auto;}}.ie button.ybtn>span,.ie input[type=submit].ybtn>span{position:relative;display:block;}.ybtn .icon.icon--size-24{margin:-12px 0;}.ybtn .icon.icon--size-18{margin:-9px 0;}.ybtn .icon.icon--size-14{margin:-7px 0;}.ybtn-primary,.ybtn--primary{color:white;border-color:#8d0005;-webkit-box-shadow:0 1px 1px rgba(0,0,0,0.3);box-shadow:0 1px 1px rgba(0,0,0,0.3);background-color:#d90007;background:-webkit-linear-gradient(#d90007, #c91400);background:linear-gradient(#d90007, #c91400);}.ybtn-primary:hover,.ybtn--primary:hover{background-color:#ed0008;background:-webkit-linear-gradient(#ed0008, #dd1600);background:linear-gradient(#ed0008, #dd1600);}.ybtn-primary:active,.ybtn--primary:active{background-color:#c50006;background:-webkit-linear-gradient(#c50006, #b51200);background:linear-gradient(#c50006, #b51200);}.ybtn-primary.ybtn-disabled,.ybtn-primary.ybtn--disabled,.ybtn-primary[disabled],.ybtn--primary.ybtn-disabled,.ybtn--primary.ybtn--disabled,.ybtn--primary[disabled]{background-color:#b00006;background:-webkit-linear-gradient(#b00006, #a01000);background:linear-gradient(#b00006, #a01000);-webkit-box-shadow:none;box-shadow:none;}a.ybtn--twitter:hover,a.ybtn--twitter:visited,a.ybtn--facebook:hover,a.ybtn--facebook:visited,a.ybtn--google-plus:hover,a.ybtn--google-plus:visited,a.ybtn--line:hover,a.ybtn--line:visited,a.ybtn--github:hover,a.ybtn--github:visited,a.ybtn--rss:hover,a.ybtn--rss:visited,a.ybtn-primary:hover,a.ybtn-primary:visited,a.ybtn--primary:hover,a.ybtn--primary:visited,a.ybtn-deal:hover,a.ybtn-deal:visited,a.ybtn-platform:hover,a.ybtn-platform:visited,a.ybtn-cta:hover,a.ybtn-cta:visited,a.ybtn--cta:hover,a.ybtn--cta:visited,a.ybtn--green:hover,a.ybtn--green:visited{color:white;}@media only screen and (max-width: 479px){.responsive .ybtn--social{padding-bottom:9px;}.responsive .ybtn--social .icon.icon--size-24{margin:0 12px 0 0;}.responsive .ybtn--social.ybtn--social.is-empty{padding-left:12px;padding-top:12px;padding-bottom:8px;}}@media only screen and (max-width: 479px){.responsive .ybtn-giant .info-text{font-size:14px;line-height:1.28571em;}}.yform{margin-bottom:18px;}.yform [type="text"],.yform [type="password"],.yform [type="email"],.yform [type="url"],.yform [type="tel"],.yform [type="date"],.yform textarea,.yform select,.yform .pseudo-input{display:block;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:100%;margin:0 0 18px;padding:5px 9px;background:#fff;border:1px solid #999;border-radius:3px;font-size:14px;line-height:1.28571em;line-height:1.29em;}.yform [type="text"]:disabled,.yform [type="text"].is-disabled,.yform [type="password"]:disabled,.yform [type="password"].is-disabled,.yform [type="email"]:disabled,.yform [type="email"].is-disabled,.yform [type="url"]:disabled,.yform [type="url"].is-disabled,.yform [type="tel"]:disabled,.yform [type="tel"].is-disabled,.yform [type="date"]:disabled,.yform [type="date"].is-disabled,.yform textarea:disabled,.yform textarea.is-disabled,.yform select:disabled,.yform select.is-disabled,.yform .pseudo-input:disabled,.yform .pseudo-input.is-disabled{background:#f5f5f5;border-color:#ccc;-webkit-text-fill-color:#999;}.yform [type="text"]:disabled::-webkit-input-placeholder,.yform [type="text"]:disabled::-moz-placeholder,.yform [type="text"]:disabled:-moz-placeholder,.yform [type="text"]:disabled:-ms-input-placeholder,.yform [type="text"].is-disabled::-webkit-input-placeholder,.yform [type="text"].is-disabled::-moz-placeholder,.yform [type="text"].is-disabled:-moz-placeholder,.yform [type="text"].is-disabled:-ms-input-placeholder,.yform [type="password"]:disabled::-webkit-input-placeholder,.yform [type="password"]:disabled::-moz-placeholder,.yform [type="password"]:disabled:-moz-placeholder,.yform [type="password"]:disabled:-ms-input-placeholder,.yform [type="password"].is-disabled::-webkit-input-placeholder,.yform [type="password"].is-disabled::-moz-placeholder,.yform [type="password"].is-disabled:-moz-placeholder,.yform [type="password"].is-disabled:-ms-input-placeholder,.yform [type="email"]:disabled::-webkit-input-placeholder,.yform [type="email"]:disabled::-moz-placeholder,.yform [type="email"]:disabled:-moz-placeholder,.yform [type="email"]:disabled:-ms-input-placeholder,.yform [type="email"].is-disabled::-webkit-input-placeholder,.yform [type="email"].is-disabled::-moz-placeholder,.yform [type="email"].is-disabled:-moz-placeholder,.yform [type="email"].is-disabled:-ms-input-placeholder,.yform [type="url"]:disabled::-webkit-input-placeholder,.yform [type="url"]:disabled::-moz-placeholder,.yform [type="url"]:disabled:-moz-placeholder,.yform [type="url"]:disabled:-ms-input-placeholder,.yform [type="url"].is-disabled::-webkit-input-placeholder,.yform [type="url"].is-disabled::-moz-placeholder,.yform [type="url"].is-disabled:-moz-placeholder,.yform [type="url"].is-disabled:-ms-input-placeholder,.yform [type="tel"]:disabled::-webkit-input-placeholder,.yform [type="tel"]:disabled::-moz-placeholder,.yform [type="tel"]:disabled:-moz-placeholder,.yform [type="tel"]:disabled:-ms-input-placeholder,.yform [type="tel"].is-disabled::-webkit-input-placeholder,.yform [type="tel"].is-disabled::-moz-placeholder,.yform [type="tel"].is-disabled:-moz-placeholder,.yform [type="tel"].is-disabled:-ms-input-placeholder,.yform [type="date"]:disabled::-webkit-input-placeholder,.yform [type="date"]:disabled::-moz-placeholder,.yform [type="date"]:disabled:-moz-placeholder,.yform [type="date"]:disabled:-ms-input-placeholder,.yform [type="date"].is-disabled::-webkit-input-placeholder,.yform [type="date"].is-disabled::-moz-placeholder,.yform [type="date"].is-disabled:-moz-placeholder,.yform [type="date"].is-disabled:-ms-input-placeholder,.yform textarea:disabled::-webkit-input-placeholder,.yform textarea:disabled::-moz-placeholder,.yform textarea:disabled:-moz-placeholder,.yform textarea:disabled:-ms-input-placeholder,.yform textarea.is-disabled::-webkit-input-placeholder,.yform textarea.is-disabled::-moz-placeholder,.yform textarea.is-disabled:-moz-placeholder,.yform textarea.is-disabled:-ms-input-placeholder,.yform select:disabled::-webkit-input-placeholder,.yform select:disabled::-moz-placeholder,.yform select:disabled:-moz-placeholder,.yform select:disabled:-ms-input-placeholder,.yform select.is-disabled::-webkit-input-placeholder,.yform select.is-disabled::-moz-placeholder,.yform select.is-disabled:-moz-placeholder,.yform select.is-disabled:-ms-input-placeholder,.yform .pseudo-input:disabled::-webkit-input-placeholder,.yform .pseudo-input:disabled::-moz-placeholder,.yform .pseudo-input:disabled:-moz-placeholder,.yform .pseudo-input:disabled:-ms-input-placeholder,.yform .pseudo-input.is-disabled::-webkit-input-placeholder,.yform .pseudo-input.is-disabled::-moz-placeholder,.yform .pseudo-input.is-disabled:-moz-placeholder,.yform .pseudo-input.is-disabled:-ms-input-placeholder{color:#999;}.yform [type="text"].hidden,.yform [type="password"].hidden,.yform [type="email"].hidden,.yform [type="url"].hidden,.yform [type="tel"].hidden,.yform [type="date"].hidden,.yform textarea.hidden,.yform select.hidden,.yform .pseudo-input.hidden{display:none;}.yform [type="text"].inline-block,.yform [type="password"].inline-block,.yform [type="email"].inline-block,.yform [type="url"].inline-block,.yform [type="tel"].inline-block,.yform [type="date"].inline-block,.yform textarea.inline-block,.yform select.inline-block,.yform .pseudo-input.inline-block{display:inline-block;}@media only screen and (max-width: 989px){.responsive .yform [type="text"],.responsive .yform [type="password"],.responsive .yform [type="email"],.responsive .yform [type="url"],.responsive .yform [type="tel"],.responsive .yform [type="date"],.responsive .yform textarea,.responsive .yform select,.responsive .yform .pseudo-input{font-size:16px;line-height:1.3125em;}}.yform .pseudo-input{cursor:text;position:relative;overflow:hidden;}.yform .pseudo-input .yselect{position:static;}.yform textarea{height:78px;resize:vertical;}.yform select{height:30px;line-height:30px;}@media only screen and (max-width: 989px){.responsive .yform select{height:auto;}}.yform [type="text"]:focus,.yform [type="password"]:focus,.yform [type="email"]:focus,.yform [type="url"]:focus,.yform [type="tel"]:focus,.yform [type="date"]:focus,.yform textarea:focus,.yform select:focus,.yform .pseudo-input.focused,.yform .pseudo-input.is-focused{border-color:#0073bb;-webkit-box-shadow:0 0 4px rgba(0,115,187,0.3);box-shadow:0 0 4px rgba(0,115,187,0.3);outline:none;color:#333;}.yform .pseudo-input textarea,.yform .pseudo-input textarea:focus,.yform .pseudo-input.focused textarea,.yform .pseudo-input input,.yform .pseudo-input input:focus,.yform .pseudo-input.focused input{margin:0;border:0;outline:0;-webkit-box-shadow:none;box-shadow:none;background:none;padding:2px;display:inline-block;vertical-align:middle;}.yform .pseudo-input select{cursor:pointer;position:absolute;top:0;left:0;width:120%;height:100%;background:transparent;-webkit-appearance:none;-moz-appearance:none;appearance:none;margin:0;padding:5px 5px 5px 30px;line-height:1;border:none;outline:none;-webkit-box-shadow:none;box-shadow:none;}.yform .pseudo-input_text{float:left;margin-right:5px;font-weight:bold;color:#333;cursor:default;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}.yform .pseudo-input_field-holder{display:block;overflow:hidden;}.yform .pseudo-input_field{width:100%;vertical-align:baseline !important;padding:0 !important;}.yform label,.yform legend{display:inline-block;font-weight:bold;margin:0 0 6px;}@media only screen and (max-width: 479px){.responsive .yform label{font-size:14px;line-height:1.28571em;}}.yform [type="checkbox"]{margin:0.2em 1px 0;}.yform [type="radio"]{margin:0.15em 1px 0;}.yform fieldset{margin-bottom:18px;}.yform fieldset label{display:block;}.yform fieldset label span{font-weight:normal;}.yform fieldset .radio-check{padding-left:1.3em;position:relative;}.yform fieldset .radio-check input{position:absolute;left:0;}.ie .yform fieldset .radio-check input{margin:0 1px;left:-3px;}.yform fieldset .radio-check _:-ms-input-placeholder,:root .yform fieldset .radio-check input{margin:0 1px;left:-3px;}.yform fieldset .radio-check _:-ms-fullscreen [type="checkbox"],.yform fieldset .radio-check _:-ms-fullscreen [type="radio"],:root .yform fieldset .radio-check [type="checkbox"],:root .yform fieldset .radio-check [type="radio"]{left:0;}.yform fieldset .radio-check _:-ms-fullscreen [type="checkbox"],:root .yform fieldset .radio-check [type="checkbox"]{margin:0.2em 1px 0;}.yform fieldset .radio-check _:-ms-fullscreen [type="radio"],:root .yform fieldset .radio-check [type="radio"]{margin:0.15em 1px 0;}.yform [type="file"]{display:block;margin:6px 0 18px;}.yform .text-error{color:#d32323;}.yform .pseudo-input>.icon{position:absolute;}.yform .pseudo-input>.icon.hidden{display:none;}@media only screen and (max-width: 989px){.responsive .yform .pseudo-input.input-success>.icon,.responsive .yform .pseudo-input.input-warning>.icon,.responsive .yform .pseudo-input.input-error>.icon{top:6px;}}.yselect{position:relative;box-shadow:none;margin:0 0 18px;}.yselect select{-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;line-height:inherit;padding-right:28px;margin:0;box-shadow:none;}.yselect select:focus{background-color:white;color:inherit;}.ie .yselect select{padding-right:5px;}.yselect select:disabled+.yselect_arrow{fill:#999;}.yselect x:-o-prefocus,.yselect .yselect_arrow{display:none;}@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none){.yselect select::-ms-expand{display:none;}.yselect select:focus::-ms-value{background:white;color:inherit;}}.yselect select:-moz-focusring{color:transparent;text-shadow:0 0 0 #000;}.yselect .yselect_arrow{position:absolute;right:6px;top:0;bottom:0;margin:auto;pointer-events:none;}.ie .yselect .yselect_arrow{display:none;}.yform-input-field-wrap{display:table-cell;width:100%;padding-right:5px;}.yform-inline{display:table;width:100%;}.yform-inline [type="text"]{display:inline;margin:0;}.yform-inline .ybtn{display:table-cell;position:relative;top:-1px;white-space:nowrap;}.yform--continuous [type="text"],.yform--continuous .pseudo-input{margin:0;}.yform--continuous .ybtn{position:relative;left:-4px;width:calc(100% + 4px);border-radius:0 3px 3px 0;-webkit-box-shadow:none;box-shadow:none;}.ysection{margin-bottom:18px;}@media only screen and (max-width: 479px){.responsive .ysection{margin-bottom:36px;}.responsive .ysection:last-child{margin-bottom:0;}}.ysection:last-child{margin-bottom:0;}.curloc-error-modal ol{list-style:decimal inside;}.curloc-error-modal ol>li::before{content:counter(step-counter) ".";display:table-cell;text-align:right;padding-right:.3em;}.curloc-error-modal ol>li{counter-increment:step-counter;display:table-row;}.curloc-error-modal p:last-child{margin-bottom:0;}.suggestions-list-container{border-top:1px solid #ccc;}.autocomplete_choices,.suggestions-list-container{position:absolute;z-index:2 !important;margin:0;padding:0;}.autocomplete_choices>ul,.suggestions-list-container>ul{font-size:14px;line-height:1.28571em;margin:0 1px;padding:0;background-color:white;border-top:none;list-style:none;margin-top:0 !important;-webkit-box-shadow:0 21px 38px rgba(0,0,0,0.2);box-shadow:0 21px 38px rgba(0,0,0,0.2);border-radius:0 0 4px 4px;max-height:430px;overflow-y:auto;}@media only screen and (max-width: 479px){.responsive .autocomplete_choices>ul,.responsive .suggestions-list-container>ul{font-size:16px;}}.autocomplete_choices>ul>li,.suggestions-list-container>ul>li{margin:0;padding:8px 15px;color:black;cursor:pointer;font-size:14px;}.autocomplete_choices>ul>li .media-avatar,.suggestions-list-container>ul>li .media-avatar{margin-right:5px;}.modal_head{border-bottom:1px solid #ccc;padding:12px;padding-right:48px;}.modal_body{padding:18px 12px;}.modal_body:first-child{padding:0;}.modal_section{margin:18px -24px;padding:18px 24px;border:1px solid #e6e6e6;border-left:0;border-right:0;}.modal_section:last-child{margin-bottom:-30px;border-bottom:0;border-bottom-right-radius:5px;border-bottom-left-radius:5px;}.yelp-map-container{border:solid 1px #ccc;width:298px;height:300px;position:relative;}.engine-container{position:relative;height:100%;width:100%;}.yelp-map-container{border:solid 1px #ccc;width:300px;height:300px;}#print-masthead{display:none;}@media print{#print-masthead{display:block;height:50px;position:relative;text-align:left;margin-bottom:10px;}.business-owner-header,#mastHead,#header-account,#alert-container,.lightbox,#overlay,.fb_connect_bar_container,#floater,#footer,.promo-box,.miniOrange,.yloca,.ypop,.rateReview,.ybtn{display:none !important;}.ie #wrap{width:auto;}.ie .column{position:relative;border:none !important;float:none !important;}.ie .container{border:none !important;}}svg:not(:root){overflow:hidden;}.icon{display:inline-block;vertical-align:middle;position:relative;overflow:hidden;top:-.1em;fill:#666;}.icon:before{position:absolute;display:block;left:0;}.icon_svg,.icon_amp-svg{fill:inherit;display:block;left:0;top:0;right:0;bottom:0;}.icon_svg{position:absolute;width:100%;height:100%;}.icon::after{content:'';display:block;position:absolute;left:0;right:0;top:0;bottom:0;}.icon:before{content:'';background-color:transparent;background-position:0 0;background-repeat:no-repeat;background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/svg_icons/fa8847e6123e/assets/sprite.png);background-image:-webkit-linear-gradient(transparent, transparent),none;background-image:linear-gradient(transparent, transparent),none;}@media all and (min-width: 0){.icon:before{background:none;}}.no-js .icon:before,.icon-svg-unavailable .icon:before{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/svg_icons/fa8847e6123e/assets/sprite.png);}[class*="icon--active-"].is-active .icon,[class*="icon--hover-"]:hover .icon,[class*="icon--hover-"]:focus .icon{fill:inherit;}.icon--currentColor,.icon--hover-currentColor:hover,.icon--hover-currentColor:focus{fill:currentColor;}.icon--white,.icon--hover-white:hover,.icon--hover-white:focus{fill:#fff;}.icon--black,.icon--hover-black:hover,.icon--hover-black:focus{fill:#333;}.icon--inverse,.icon--hover-inverse:hover,.icon--hover-inverse:focus{fill:#fff;}.icon--neutral-gray,.icon--hover-neutral-gray:hover,.icon--hover-neutral-gray:focus{fill:#999;}.icon--success,.icon--hover-success:hover,.icon--hover-success:focus{fill:#41a700;}@media print{.i-selector-stars{background-image:none !important;}.i-selector-stars img{position:relative;width:auto;height:auto;}}@media print{.i-selector-stars--extra-large-0 img{left:0;top:0;}}@media print{.i-selector-stars--extra-large-1 img{left:0;top:-30px;}}@media print{.i-selector-stars--extra-large-2 img{left:0;top:-60px;}}@media print{.i-selector-stars--extra-large-3 img{left:0;top:-90px;}}@media print{.i-selector-stars--extra-large-4 img{left:0;top:-120px;}}@media print{.i-selector-stars--extra-large-5 img{left:0;top:-150px;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.i-selector-stars{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/yelp_design_web/b25de66c1adb/assets/img/stars/selector_stars@2x.png);}}@media only screen and (max-width: 479px){.responsive .star-selector_description{font-size:14px;line-height:1.28571em;}}.disambiguation-links{margin-top:6px;}@media only screen and (max-width: 479px){.responsive .signup-wrapper{padding-left:0;padding-right:0;}}.top-shelf{width:100%;min-width:1020px;position:relative;padding-top:15px;}.top-shelf h1{padding-top:0;}@media only screen and (max-width: 989px){.responsive .top-shelf{min-width:0;}}.top-shelf-grey{background:#f5f5f5;border-bottom:1px solid #e6e6e6;}.main-header_wrapper{padding:12px 0;position:relative;background:#d32323 url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_styleguide/c146b0884f6a/assets/img/structural/header_stars.png) no-repeat center;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_wrapper{background:#d32323 url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/15ee41b0c3b2/assets/img/structural/header_stars@2x.png) no-repeat center;background-size:1135px auto, 100%;}}@media only screen and (max-width: 989px){.responsive .main-header_wrapper{background:#d32323;}}@media only screen and (max-width: 479px){.responsive .main-header_wrapper{padding:0;}}.main-header_logo{width:80px;height:40px;background-repeat:no-repeat;}@media only screen and (max-width: 479px){.responsive .main-header_logo{width:52px;height:42px;background-size:52px 26px;background-position:0 8px;}}.main-header_logo a{display:block;width:100%;height:100%;text-indent:-1000em;}.main-header_logo{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/48792dd29811/assets/img/logos_desktop/default.png);background-size:80px 40px;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/yelp_design_web/b085a608c15f/assets/img/logos_desktop/default@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--april-fools{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/06233a5eff3e/assets/img/logos_desktop/april_fools@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--autumn{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/d6fef4228d0d/assets/img/logos_desktop/autumn@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--election{background-image:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/99318ece2df0/assets/img/logos_desktop/election@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--fawkes{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/478614d48eee/assets/img/logos_desktop/fawkes@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--german{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_design_web/75c49eff3a65/assets/img/logos_desktop/german@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--halloween{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_design_web/71412255d8f6/assets/img/logos_desktop/halloween@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--neutrality{background-image:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/12f91bb75262/assets/img/logos_desktop/neutrality@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--olympics{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_design_web/ca2c2613119e/assets/img/logos_desktop/olympics@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--pride{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/811008e21691/assets/img/logos_desktop/pride@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--soccer{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/86d12a59817b/assets/img/logos_desktop/soccer@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--st-patricks{background-image:url(https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_design_web/0e66a894c38d/assets/img/logos_desktop/st_patricks@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--thanksgiving{background-image:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/5faa2375d44d/assets/img/logos_desktop/thanksgiving@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--valentines{background-image:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/5f66465428b9/assets/img/logos_desktop/valentines@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-header_logo--winter{background-image:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/948fbfff37bd/assets/img/logos_desktop/winter@2x.png);}}@media only screen and (max-width: 989px){.responsive .main-header_title{font-size:16px;line-height:1.3125em;}}@media only screen and (max-width: 479px){.responsive .main-header_title{max-width:120px;height:49px;line-height:46px;margin:0;}.responsive .main-header_title span{line-height:18px;vertical-align:middle;display:inline-block;}}@media only screen and (max-width: 479px){.responsive .main-header_search{padding:9px 0;}}.main-header{z-index:6;}.main-header .main-header_button,.main-header .main-header_account .user-account_button,.main-header .main-header_nav-dropdown .user-account_button{-webkit-box-shadow:none;box-shadow:none;vertical-align:middle;margin:0;outline:0;border:none;border-radius:4px;background:#bd1f1f;line-height:24px;padding:6px 18px;}.main-header .main-header_button:focus,.main-header .main-header_button:hover,.main-header .main-header_button:active,.main-header .main-header_account .user-account_button:focus,.main-header .main-header_account .user-account_button:hover,.main-header .main-header_account .user-account_button:active,.main-header .main-header_nav-dropdown .user-account_button:focus,.main-header .main-header_nav-dropdown .user-account_button:hover,.main-header .main-header_nav-dropdown .user-account_button:active{background:#a71c1c;}.main-header .main-header_account .user-account_button,.main-header .main-header_nav-dropdown .user-account_button{padding:0;}.main-header_account,.main-header_nav-dropdown{float:right;}.main-header_account .user-account_button,.main-header_nav-dropdown .user-account_button{width:58px;}@media only screen and (max-width: 989px){.responsive .main-header_account .user-account_button,.responsive .main-header_nav-dropdown .user-account_button{width:auto;padding:6px;}}@media only screen and (max-width: 479px){.responsive .main-header_account .user-account_button,.responsive .main-header_nav-dropdown .user-account_button{background:none;}}.main-header_account .drop-menu-link_open,.main-header_account .drop-menu-link_close,.main-header_nav-dropdown .drop-menu-link_open,.main-header_nav-dropdown .drop-menu-link_close{display:none;}@media only screen and (max-width: 989px){.responsive .main-header_account .header-nav,.responsive .main-header_nav-dropdown .header-nav{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-direction:reverse;-webkit-box-orient:horizontal;-webkit-flex-direction:row-reverse;-moz-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse;-webkit-box-align:center;-moz-box-align:center;-ms-flex-align:center;box-align:center;-webkit-align-items:center;align-items:center;}.ie .responsive .main-header_account .header-nav,.ie .responsive .main-header_nav-dropdown .header-nav{width:147px;}.ie .responsive .main-header_account .header-nav .header-nav_item,.ie .responsive .main-header_nav-dropdown .header-nav .header-nav_item{float:right;}.ie .responsive .main-header_account .header-nav .header-nav_item+.header-nav_item,.ie .responsive .main-header_nav-dropdown .header-nav .header-nav_item+.header-nav_item{float:left;margin-right:0;}}@media only screen and (max-width: 989px) and (max-width: 479px){.ie .responsive .main-header_account .header-nav .header-nav_item+.header-nav_item,.ie .responsive .main-header_nav-dropdown .header-nav .header-nav_item+.header-nav_item{float:right;}}@media only screen and (max-width: 989px){.responsive .main-header_account .header-nav_item+.header-nav_item,.responsive .main-header_nav-dropdown .header-nav_item+.header-nav_item{margin-right:12px;}.responsive .main-header_account .drop-menu,.responsive .main-header_nav-dropdown .drop-menu{padding:3px 12px;}.responsive .main-header_account .drop-menu-link_open,.responsive .main-header_nav-dropdown .drop-menu-link_open{display:inline-block;}.responsive .main-header_account .drop-menu-highlighted .drop-menu-link_open,.responsive .main-header_nav-dropdown .drop-menu-highlighted .drop-menu-link_open{display:none;}.responsive .main-header_account .drop-menu-highlighted .drop-menu-link_close,.responsive .main-header_nav-dropdown .drop-menu-highlighted .drop-menu-link_close{display:inline-block;}.responsive .main-header_account .drop-menu_auth-buttons,.responsive .main-header_nav-dropdown .drop-menu_auth-buttons{margin-top:9px;}.responsive .main-header_account .drop-menu-arrow,.responsive .main-header_nav-dropdown .drop-menu-arrow{top:-3px;}.responsive .main-header_account .drop-menu-arrow::after,.responsive .main-header_account .drop-menu-arrow::before,.responsive .main-header_nav-dropdown .drop-menu-arrow::after,.responsive .main-header_nav-dropdown .drop-menu-arrow::before{right:-2px;}.responsive .main-header_account .drop-menu-group,.responsive .main-header_nav-dropdown .drop-menu-group{margin:0;padding:0;border:0;}.responsive .main-header_account .drop-down-menu-link,.responsive .main-header_nav-dropdown .drop-down-menu-link{margin:0;padding:9px 0;border-top:1px solid #e6e6e6;}.responsive .main-header_account .drop-down-menu-link strong,.responsive .main-header_nav-dropdown .drop-down-menu-link strong{font-weight:normal;}.responsive .main-header_account .drop-menu-group--nav a,.responsive .main-header_nav-dropdown .drop-menu-group--nav a{color:#333;}.responsive .main-header_account .drop-menu-group--nav a:focus,.responsive .main-header_account .drop-menu-group--nav a:hover,.responsive .main-header_nav-dropdown .drop-menu-group--nav a:focus,.responsive .main-header_nav-dropdown .drop-menu-group--nav a:hover{color:#1a1a1a;}.responsive .main-header_account .drop-menu-group--nav a:active,.responsive .main-header_nav-dropdown .drop-menu-group--nav a:active{color:#000;}.responsive .main-header_account .drop-menu-group:first-child>.drop-down-menu-link:first-child,.responsive .main-header_account .drop-menu-group--nav>.drop-down-menu-link:first-child,.responsive .main-header_nav-dropdown .drop-menu-group:first-child>.drop-down-menu-link:first-child,.responsive .main-header_nav-dropdown .drop-menu-group--nav>.drop-down-menu-link:first-child{border-top:0;}}@media only screen and (max-width: 479px){.responsive .main-header_account,.responsive .main-header_nav-dropdown{margin-top:1px;}.responsive .main-header_account .drop-menu-origin,.responsive .main-header_nav-dropdown .drop-menu-origin{position:static;}.responsive .main-header_account .drop-menu,.responsive .main-header_nav-dropdown .drop-menu{top:100%;left:0;margin:0;border-radius:0;}}@media only screen and (max-width: 989px){.drop-down-menu-link--logout{line-height:24px;}}@media only screen and (max-width: 989px){.drop-down-menu-link.responsive-visible-large-block:first-child+.drop-down-menu-link{border-top:0 !important;}}@media only screen and (max-width: 479px){.responsive .drop-down-menu-link_new-label{display:block;}}@media only screen and (max-width: 479px){.ie .main-header--slim .main-header_account .header-nav .header-nav_item+.header-nav_item,.ie .main-header--slim .main_header_nav-dropdown .header-nav .header-nav_item+.header-nav_item{float:right;}}@media only screen and (max-width: 479px){.responsive .main-header--slim .main-header_account .header-nav_item+.header-nav_item,.responsive .main-header--slim .main_header_nav-dropdown .header-nav_item+.header-nav_item{margin-right:0;}}@media only screen and (min-width: 480px) and (max-width: 989px){.responsive .main-header--slim .main-header_account .header-nav_item+.header-nav_item,.responsive .main-header--slim .main_header_nav-dropdown .header-nav_item+.header-nav_item{margin-right:5px;}}.main-search_search-field-arrange{width:50%;}@media only screen and (max-width: 479px){.responsive .main-search_search-field-arrange{width:100%;}}.main-search_suggestions-field{position:relative;}.main-search_suggestions{position:absolute;width:100%;top:100%;left:0;}.suggestions-list-container>.suggestions-list{margin:-3px 0 0;}.main-search_field:focus{outline:0;}@media only screen and (max-width: 479px){.responsive .main-search_submit,.responsive .main-search_close{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;}}@media only screen and (max-width: 479px){.main-search_action-icon-wrap{vertical-align:middle;}}@media only screen and (max-width: 479px){.responsive .main-search_action{width:50%;}}@media only screen and (max-width: 479px){.responsive .main-search_action-text{font-size:14px;vertical-align:middle;display:inline-block;}}.main-search_pseudo-input,.yform .main-search_pseudo-input{-webkit-box-shadow:none;box-shadow:none;padding:8px 12px;border:none;border-radius:0;background:#fff;margin:0;height:36px;line-height:20px;}@media only screen and (max-width: 479px){.responsive .main-search_pseudo-input,.responsive .yform .main-search_pseudo-input{height:auto;padding:6px 9px;}}.main-search_pseudo-input--find,.yform .main-search_pseudo-input--find{border-radius:4px 0 0 4px;position:relative;}@media only screen and (max-width: 479px){.responsive .main-search_pseudo-input--find,.responsive .yform .main-search_pseudo-input--find{border-radius:4px;}}.main-search_pseudo-input--find::after,.yform .main-search_pseudo-input--find::after{content:"";position:absolute;top:8px;right:0;bottom:8px;width:1px;background-color:#ccc;}@media only screen and (max-width: 479px){.responsive .main-search_pseudo-input--find::after,.responsive .yform .main-search_pseudo-input--find::after{display:none;}}@media only screen and (max-width: 479px){.responsive .main-search_pseudo-input--near,.responsive .yform .main-search_pseudo-input--near{border-radius:4px 0 0 4px;}}.main-search_submit,.yform .main-search_submit{-webkit-box-shadow:none;box-shadow:none;border:0;border-radius:0 4px 4px 0;background:#bd1f1f;line-height:36px;padding:0 15px;width:54px;}.main-search_submit:hover,.main-search_submit:focus,.main-search_submit:active,.yform .main-search_submit:hover,.yform .main-search_submit:focus,.yform .main-search_submit:active{background:#a71c1c;}.main-search_submit .circle-spinner,.yform .main-search_submit .circle-spinner{width:20px;height:20px;top:5px;}.main-header_nav-wrapper{background:#bd1f1f;}.main-header_nav-wrapper .header-nav_link{border-radius:0;}.main-header_nav-wrapper .header-nav+.header-nav::before{content:'\b7';color:white;margin:0 6px;}.main-header_wrapper .header-nav_button--sign-up,.main-header_nav-wrapper .header-nav_link--log-in{padding-left:12px;padding-right:12px;min-width:80px;text-align:center;}@media only screen and (max-width: 989px){.responsive .main-header_wrapper .header-nav_button--sign-up,.responsive .main-header_nav-wrapper .header-nav_link--log-in{min-width:auto;padding-left:18px;padding-right:18px;}}.main-header_nav{margin-left:-12px;}.main-header_nav .header-nav_item{display:-moz-inline-stack;display:inline-block;}@media only screen and (min-width: 480px) and (max-width: 989px){.responsive .main-header_nav .header-nav_link,.responsive .main-header_nav .header-nav_text,.responsive .main-header_account .header-nav_link,.responsive .main-header_account .header-nav_text{padding:6px 12px;line-height:24px;}}@media only screen and (max-width: 479px){.responsive .main-header_nav .header-nav_link,.responsive .main-header_nav .header-nav_text,.responsive .main-header_account .header-nav_link,.responsive .main-header_account .header-nav_text{padding:15px 12px 14px;}}.header-nav{display:inline-block;}.header-nav_link,.header-nav_text{color:#fff;display:block;padding:3px 15px;font-size:13px;line-height:1.38462em;font-weight:bold;line-height:21px;}.header-nav_link{border-radius:3px;}.header-nav_link:hover,.header-nav_link:focus,.header-nav_link.tabon,.header-nav_link.hover{color:white;text-decoration:none;background:#a71c1c;background:rgba(51,51,51,0.3);}.main-header_account .header-nav_link--log-in{display:none;}@media only screen and (min-width: 480px) and (max-width: 989px){.responsive .main-header_account .header-nav_link--log-in{display:block;}}.icon.user-account_button-arrow{top:6px;}@media only screen and (max-width: 479px){.responsive .main-header .main-search_near-field-arrange,.responsive .main-header .main-search_actions{display:none;}.responsive .main-header .content-container{padding:0 12px;}.responsive .main-header.is-searching .main-header_wrapper{padding:4px 0;}.responsive .main-header.is-searching .content-container{padding:0 6px;}.responsive .main-header.is-searching .main-header_arrange{margin:0 !important;}.responsive .main-header.is-searching .main-header--full_arrange_unit{padding:0 !important;}.responsive .main-header.is-searching .main-header--full_arrange_unit:nth-child(1),.responsive .main-header.is-searching .main-header--full_arrange_unit:nth-child(3),.responsive .main-header.is-searching .main-header--full_arrange_unit:nth-child(4){display:none;}.responsive .main-header.is-searching .main-search_actions,.responsive .main-header.is-searching .main-search_near-field-arrange{display:block;}.responsive .main-header.is-searching .main-search_pseudo-input--near{border-radius:4px;}.responsive .main-header.is-searching .main-search_submit{width:100%;border-radius:4px;padding:0;}.responsive .main-header .main-search_suggestions-field{position:static;}.responsive .main-header .suggestions-list{margin:0;}.responsive .main-header .main-header_button{line-height:20px;padding:8px 16px;font-weight:normal;font-size:16px;height:36px;}.responsive .main-header .main-header_button .icon{top:-3px;}.responsive .main-header .main-header_button .circle-spinner{top:2px;}}@media only screen and (max-width: 989px){.responsive .main-header .main-header_arrange{margin-right:-6px;margin-left:-6px;border-spacing:6px 0;}.responsive .main-header .main-header_logo{margin-right:6px;}.responsive .main-header.main-header--simple .main-header_logo{margin:0 auto;}}body{background:#f5f5f5;}.content-container{width:960px;margin:0 auto;padding:0 15px;}@media only screen and (max-width: 989px){.responsive .content-container{width:auto;}}.main-content-wrap{min-width:1020px;}@media only screen and (max-width: 989px){.responsive .main-content-wrap{min-width:0;}}.main-content-wrap--full{background:white;}.main-content-wrap--full>.content-container{padding-top:15px;padding-bottom:36px;}@media screen and (min-width: 1040px){.main-content-wrap--box>.content-container{padding:15px 30px 30px;}}.main-content-wrap--separated{border-top:1px solid #ccc;}.main-footer{padding:36px 0 18px;font-size:14px;line-height:1.28571em;color:#666;}@media only screen and (max-width: 479px){.responsive .main-footer{padding:24px 0;}}.main-footer .xref,.main-footer .data-provider-attribution{color:#999;text-align:center;}.main-footer_menu{margin-bottom:36px;}.main-footer_item{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:25%;}.main-footer_item.arrange_unit{float:none;}@media only screen and (max-width: 479px){.responsive .main-footer_item{width:100%;float:none;}}.main-footer_copyright{display:block;margin-top:18px;text-align:center;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.ltie9{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_styleguide/ce4d102c522c/assets/img/structural/footer_cityscape@2x.png);}}@media only screen and (min-width: 990px){.main-footer_city-landscape-img{background:url(https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/573fa19c8435/assets/img/structural/footer_cityscape.png) no-repeat center bottom;background-size:660px 140px;margin:42px auto 18px;height:140px;}}@media only screen and (min-width: 990px) and (-webkit-min-device-pixel-ratio: 2), only screen and (min-width: 990px) and (min-resolution: 192dpi){.main-footer_city-landscape-img{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_styleguide/ce4d102c522c/assets/img/structural/footer_cityscape@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-footer_city-landscape-img--fixed{background-image:url(https://s3-media4.fl.yelpcdn.com/assets/srv0/yelp_styleguide/ce4d102c522c/assets/img/structural/footer_cityscape@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.main-footer_city-landscape-img--winter{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/yelp_styleguide/f36eb1f4e838/assets/img/structural/660x140_footer_winter_skyline@2x.png);}}.main-footer_logo-copyright,.main-footer_logo-burst{vertical-align:bottom;}.footer-menu_header{margin-bottom:12px;}.footer-menu_item{margin-bottom:6px;}.footer-menu_section{margin-bottom:24px;}.footer-menu--inline{font-size:13px;line-height:1.38462em;text-align:center;word-break:break-all;}.footer-menu--inline .footer-menu_header{font-size:13px;line-height:1.38462em;margin-left:3px;}@media only screen and (max-width: 989px){.responsive .footer-menu--inline .footer-menu_header{display:block;margin-bottom:6px;}}@media only screen and (max-width: 479px){.responsive .footer-menu--inline .footer-menu_header{margin-bottom:12px;}}.footer-menu--inline .footer-menu_list{display:inline;}.footer-menu--inline .footer-menu_item{display:inline;padding:0 3px;}.footer-menu--inline .footer-menu_header,.footer-menu--inline .footer-menu_list,.footer-menu--inline .footer-menu_item{margin-bottom:0;}.footer-menu--inline.footer-menu--bordered .footer-menu_list{font-size:0;}.footer-menu--inline.footer-menu--bordered .footer-menu_item{font-size:13px;line-height:1.38462em;}.footer-menu--inline.footer-menu--bordered .footer-menu_item,.footer-menu--inline .footer-menu_item--bordered{padding:0;}.footer-menu--inline.footer-menu--bordered .footer-menu_item a,.footer-menu--inline .footer-menu_item--bordered a{border-left:1px solid #999;white-space:nowrap;padding:0 6px;}.footer-menu--inline.footer-menu--bordered .footer-menu_item:first-child a,.footer-menu--inline .footer-menu_item--bordered:first-child a{border-left:0 !important;}@media only screen and (max-width: 989px){.responsive .footer-menu--inline.footer-menu--bordered .footer-menu_item a,.responsive .footer-menu--inline .footer-menu_item--bordered a{border-left:0;}}@media only screen and (max-width: 989px){.responsive .footer-menu--inline .footer-menu_item--bordered a{margin-left:auto;}}@media only screen and (max-width: 479px){.responsive .main-footer_mobile-links .footer-menu_item a{font-size:16px;line-height:1.3125em;}}.main-footer_mobile-links .footer-menu_item{padding:0 6px;}.footer-menu--separated{padding:6px 0;border-top:1px solid #e6e6e6;}@media only screen and (max-width: 989px){.responsive .footer-menu--separated{padding:12px 0;}.responsive .footer-menu--separated .footer-menu_header{display:block;margin-bottom:6px;}}.drop-menu{z-index:1012;}.dropdown_menu{z-index:1012;}.dropdown--arrow .dropdown_toggle ~ .dropdown_menu-container{z-index:1012;}.app-header,.main-header_wrapper{z-index:1011;}.tooltip{z-index:1012;}.tooltip-wrapper::after{z-index:1013;}.u-offscreen{clip:rect(0 0 0 0) !important;position:absolute !important;left:-9999px !important;top:auto !important;overflow:hidden !important;width:1px !important;height:1px !important;}.u-inline-block{display:inline-block !important;}.u-hidden{display:none !important;}.u-pseudo-link{margin:0 !important;padding:0 !important;background:none !important;border:0 !important;outline:0 !important;color:#0073bb !important;cursor:pointer !important;font-family:inherit !important;font-size:inherit !important;-webkit-box-shadow:none;box-shadow:none;}.u-pseudo-link:hover,.u-pseudo-link:focus{text-decoration:underline !important;}.u-cursor-pointer{cursor:pointer !important;}.u-decoration-none,.u-decoration-none:hover{text-decoration:none !important;}.u-absolute{position:absolute !important;}.u-nowrap{white-space:nowrap !important;}.u-text-centered{text-align:center !important;}.u-text-right{text-align:right !important;}.u-bg-color{background-color:#f5f5f5 !important;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.u-bg-city-scape{background-image:url(https://s3-media3.fl.yelpcdn.com/assets/srv0/yelp_styleguide/248de198b86e/assets/img/structural/cityscape@2x.png);}}.u-triangle-direction-down{-webkit-transform:rotate(0deg);-moz-transform:rotate(0deg);-ms-transform:rotate(0deg);transform:rotate(0deg);}.u-space-l0{margin-left:0px !important;}.u-space-r-half{margin-right:3px !important;}.u-space-r1{margin-right:6px !important;}.u-space-t1{margin-top:6px !important;}.u-space-t2{margin-top:12px !important;}.u-space-b0{margin-bottom:0px !important;}.u-space-b1{margin-bottom:6px !important;}@media only screen and (max-width: 989px){.responsive .u-md-space-0{margin:0px !important;}.responsive .u-md-space-half{margin:3px !important;}.responsive .u-md-space-1{margin:6px !important;}.responsive .u-md-space-2{margin:12px !important;}.responsive .u-md-space-3{margin:18px !important;}.responsive .u-md-space-4{margin:24px !important;}.responsive .u-md-space-5{margin:30px !important;}.responsive .u-md-space-6{margin:36px !important;}.responsive .u-md-space-l0{margin-left:0px !important;}.responsive .u-md-space-l-half{margin-left:3px !important;}.responsive .u-md-space-l1{margin-left:6px !important;}.responsive .u-md-space-l2{margin-left:12px !important;}.responsive .u-md-space-l3{margin-left:18px !important;}.responsive .u-md-space-l4{margin-left:24px !important;}.responsive .u-md-space-l5{margin-left:30px !important;}.responsive .u-md-space-l6{margin-left:36px !important;}.responsive .u-md-space-r0{margin-right:0px !important;}.responsive .u-md-space-r-half{margin-right:3px !important;}.responsive .u-md-space-r1{margin-right:6px !important;}.responsive .u-md-space-r2{margin-right:12px !important;}.responsive .u-md-space-r3{margin-right:18px !important;}.responsive .u-md-space-r4{margin-right:24px !important;}.responsive .u-md-space-r5{margin-right:30px !important;}.responsive .u-md-space-r6{margin-right:36px !important;}.responsive .u-md-space-t0{margin-top:0px !important;}.responsive .u-md-space-t-half{margin-top:3px !important;}.responsive .u-md-space-t1{margin-top:6px !important;}.responsive .u-md-space-t2{margin-top:12px !important;}.responsive .u-md-space-t3{margin-top:18px !important;}.responsive .u-md-space-t4{margin-top:24px !important;}.responsive .u-md-space-t5{margin-top:30px !important;}.responsive .u-md-space-t6{margin-top:36px !important;}.responsive .u-md-space-b0{margin-bottom:0px !important;}.responsive .u-md-space-b-half{margin-bottom:3px !important;}.responsive .u-md-space-b1{margin-bottom:6px !important;}.responsive .u-md-space-b2{margin-bottom:12px !important;}.responsive .u-md-space-b3{margin-bottom:18px !important;}.responsive .u-md-space-b4{margin-bottom:24px !important;}.responsive .u-md-space-b5{margin-bottom:30px !important;}.responsive .u-md-space-b6{margin-bottom:36px !important;}}@media only screen and (max-width: 479px){.responsive .u-sm-space-0{margin:0px !important;}.responsive .u-sm-space-half{margin:3px !important;}.responsive .u-sm-space-1{margin:6px !important;}.responsive .u-sm-space-2{margin:12px !important;}.responsive .u-sm-space-3{margin:18px !important;}.responsive .u-sm-space-4{margin:24px !important;}.responsive .u-sm-space-5{margin:30px !important;}.responsive .u-sm-space-6{margin:36px !important;}.responsive .u-sm-space-l0{margin-left:0px !important;}.responsive .u-sm-space-l-half{margin-left:3px !important;}.responsive .u-sm-space-l1{margin-left:6px !important;}.responsive .u-sm-space-l2{margin-left:12px !important;}.responsive .u-sm-space-l3{margin-left:18px !important;}.responsive .u-sm-space-l4{margin-left:24px !important;}.responsive .u-sm-space-l5{margin-left:30px !important;}.responsive .u-sm-space-l6{margin-left:36px !important;}.responsive .u-sm-space-r0{margin-right:0px !important;}.responsive .u-sm-space-r-half{margin-right:3px !important;}.responsive .u-sm-space-r1{margin-right:6px !important;}.responsive .u-sm-space-r2{margin-right:12px !important;}.responsive .u-sm-space-r3{margin-right:18px !important;}.responsive .u-sm-space-r4{margin-right:24px !important;}.responsive .u-sm-space-r5{margin-right:30px !important;}.responsive .u-sm-space-r6{margin-right:36px !important;}.responsive .u-sm-space-t0{margin-top:0px !important;}.responsive .u-sm-space-t-half{margin-top:3px !important;}.responsive .u-sm-space-t1{margin-top:6px !important;}.responsive .u-sm-space-t2{margin-top:12px !important;}.responsive .u-sm-space-t3{margin-top:18px !important;}.responsive .u-sm-space-t4{margin-top:24px !important;}.responsive .u-sm-space-t5{margin-top:30px !important;}.responsive .u-sm-space-t6{margin-top:36px !important;}.responsive .u-sm-space-b0{margin-bottom:0px !important;}.responsive .u-sm-space-b-half{margin-bottom:3px !important;}.responsive .u-sm-space-b1{margin-bottom:6px !important;}.responsive .u-sm-space-b2{margin-bottom:12px !important;}.responsive .u-sm-space-b3{margin-bottom:18px !important;}.responsive .u-sm-space-b4{margin-bottom:24px !important;}.responsive .u-sm-space-b5{margin-bottom:30px !important;}.responsive .u-sm-space-b6{margin-bottom:36px !important;}}.radio-list label{-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}.radio-list input[type=radio]{display:none;}.radio-list-links .radio-link{color:#0073bb;cursor:pointer;}.radio-list-links .radio-link:hover{text-decoration:underline;}.radio-list-links .radio:checked+span{font-weight:bold;color:#333;text-decoration:none;cursor:default;}.reservations .reservation-fields{margin-bottom:3px;}.reservations .date-picker{width:100%;}.reservations .date-input{padding-left:30px;margin-bottom:0;-webkit-box-shadow:none;box-shadow:none;cursor:pointer;}.reservations .date-input:focus{-webkit-box-shadow:none;box-shadow:none;color:transparent;text-shadow:0px 0px 0px black;}.reservations .date-picker,.reservations .time-picker,.reservations .people-picker{cursor:pointer;}.reservations .date-picker .yselect,.reservations .time-picker .yselect,.reservations .people-picker .yselect{margin:0;}.reservations .reservation-input{border:1px solid #ccc;}.reservations .date-picker .yselect{border-right:none;}.reservations .reservation-time-select,.reservations .reservation-party-size-select{padding-left:30px;cursor:pointer;}.reservations .reservation-search-input-icon{position:absolute;top:6px;left:6px;}.reservations .text-error{margin-top:12px;margin-bottom:6px;font-weight:bold;}.reservation--inline .reservation-fields{display:inline-block;width:67%;vertical-align:middle;margin-bottom:0;margin-top:0;}.reservation--inline .date-picker{width:36%;position:relative;}.reservation--inline .time-picker{width:31%;}.reservation--inline .people-picker{width:33%;}.reservation--inline .reservation-filter-label,.reservation--inline .reservation-fields>li{margin:0;}.reservation--inline .vertical-search-text-section{width:33%;display:inline-block;vertical-align:middle;}.reservation-popup-date-picker{position:relative;width:100%;max-width:275px;margin:0 auto;}.reservation-popup-date-picker .drop-menu-arrow{top:7px;z-index:1055;text-align:center;}.reservation-popup-date-picker .drop-menu-arrow::before,.reservation-popup-date-picker .drop-menu-arrow::after{right:auto;}.platform-vsearch-popup{position:relative;}.platform-vsearch-popup fieldset{margin-bottom:6px;}.platform-vsearch-popup .yform-inline{margin-bottom:12px;}.platform-search{margin-bottom:18px;}.platform-search .yform{margin-bottom:0;}.platform-search .arrange_unit>.dropdown_menu{width:305px;}.platform-search .vertical-search-address-section .text-error{margin-top:6px;margin-bottom:0;}.platform-search .yform--continuous select{display:inline;margin:0;width:auto;padding-right:18px;}.platform-search .arrange_unit.search-button-wrap{vertical-align:middle;}.platform-search .delivery-address-suggestions-wrap .suggestions-list{margin-top:1px;}.platform-search .platform-search-button{display:none;padding-left:4px;padding-right:4px;}.search-results>li:first-child{border-top:1px solid #e6e6e6;padding-top:17px;}.search-results>li.yloca-search-result{border-color:#ebc074;}.regular-search-result+.yloca-search-result{margin-top:-1px;border-top:1px solid #ebc074;padding-top:17px;}.snippet-block{margin-bottom:0;font-size:13px;line-height:1.38462em;}.snippet-block .snippet{margin-bottom:0;}.snippet-block .highlighted{font-weight:bold;}.search-avatar-offset{margin-left:102px;}.search-result-title{font-weight:normal;margin-bottom:6px;}.search-result-title .highlighted{font-weight:bold;}.search-result-title a{padding:3px 0;}.search-result_tags{margin-top:6px;}.search-result_tags .highlighted{line-height:1;}.search-result_tags li{display:block;}.search-result .indexed-biz-name{color:#333;}[class*="tag-18x18_deal"],[class*="tag-18x18_cash_back"]{color:#41a700;}[class*="tag-18x18_order"]{color:#d38855;}[class*="tag-18x18_flame"]{color:#f15c00;}.vertical-search-text-section .title-text{display:inline-block;vertical-align:middle;font-weight:bold;}.vertical-search-text-section .title-text--no-st-picker{padding-right:6px;}.vertical-search-text-section .search-checkbox{vertical-align:middle;margin-right:5px;margin-bottom:5px;}.island--slim{padding:6px;}.search-result-cta{border:None;background-color:#f5f5f5;margin-bottom:6px;}.search-result-cta .cta-text{font-size:13px;color:#333;}.search-result-cta .low-intent-search-action-button{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;min-width:84px;}.search-result-cta .coachmark-tooltip-content{white-space:normal;z-index:1001;}.search-result-cta-error-row{margin-top:3px;}.search-result-cta-error-row .text-error{color:#d32323;}.search-result .main-attributes .yloca-info{display:none;}.search-result .yloca-tip,.biz-yloca-hovercard .yloca-tip{margin-top:3px;}.scroll-map-container{position:relative;}.search-feedback-box{margin-top:24px;}.search-feedback-box .feedback-biz-suggest{border-bottom:1px solid #ccc;padding-bottom:11px;margin-bottom:12px;}.coachmark-close{cursor:pointer;position:absolute;top:6px;}.coachmark-tooltip-content{background:#0097ec;color:#fff;position:absolute;margin-right:8px;z-index:5;border-radius:5px;width:200px;display:none;font-weight:normal;padding:9px;}.coachmark-tooltip{display:inline-block;position:relative;}.coachmark-tooltip--bottom .coachmark-tooltip-content{padding-right:24px;}.coachmark-tooltip--bottom .coachmark-tooltip-content .coachmark-close{right:6px;}.coachmark-tooltip--bottom .coachmark-tooltip-content::before{position:absolute;top:0;bottom:0;margin:auto;width:0;height:0;content:'';display:inline-block;border-style:solid;border-color:transparent transparent #0097ec;border-bottom-style:solid;border-width:0 6px 6px;top:-6px;left:50%;margin:0 0 -6px;}.filter-bar .radio-check{display:inline;float:none;padding:0;}.filter-bar .radio-check input[type=checkbox]{display:none;}.filter-bar .radio-check .anchor-link{color:#333;}.filter-bar .radio-check .anchor-link:hover{text-decoration:none;}.filter-bar .radio-check .filter-label{display:inline-block;border:1px solid #ccc;padding:8px 11px;border-radius:4px;background-color:#fff;font-size:14px;cursor:pointer;min-height:12px;min-width:13px;text-align:center;}.filter-bar .radio-check .filter-label:hover{-webkit-box-shadow:0 2px 2px 0 rgba(0,0,0,0.1);box-shadow:0 2px 2px 0 rgba(0,0,0,0.1);}.filter-bar .radio-check input[type=checkbox]:checked ~ .filter-label{border-color:#348c42;background-color:#c4f3a4;color:#348c42;}.filter-bar .radio-check .current-time{display:none;}.filter-panel{font-size:12px;line-height:1.5em;position:relative;}.filter-panel .query-refinement_filters{overflow:hidden;margin:0 -15px;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;margin:0 -21px;padding-bottom:11px;}.filter-panel .query-refinement_filters:before,.filter-panel .query-refinement_filters:after{content:" ";display:table;}.filter-panel .query-refinement_filters:after{clear:both;}.filter-panel .query-refinement_filters:before{content:"";z-index:1;display:block;margin:0 15px;border-top:1px solid #ccc;padding-bottom:11px;}.filter-panel .query-refinement_filters::before{margin:0;}.filter-panel .query-refinement_filters.is-collapsed{display:none;}.filter-panel .query-refinement_filters .container{position:relative;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-direction:normal;-webkit-box-orient:horizontal;-webkit-flex-direction:row;-moz-flex-direction:row;-ms-flex-direction:row;flex-direction:row;padding:6px 18px;}.filter-panel .query-refinement_filters .refinements-container{-webkit-box-flex:1;-webkit-flex-grow:1;-moz-flex-grow:1;-ms-flex-positive:1;flex-grow:1;align-self:center;overflow:hidden;position:relative;white-space:nowrap;}.filter-panel .query-refinement_filters .scroll-container{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-direction:normal;-webkit-box-orient:horizontal;-webkit-flex-direction:row;-moz-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-transition:transform 400ms;transition:transform 400ms;z-index:1000;}.filter-panel .query-refinement_filters:not(.on-last-page):not(.has-single-page) .refinements-container::after{content:"";width:70px;height:100%;position:absolute;top:0;right:0;z-index:1001;background:-webkit-linear-gradient(left, rgba(255,255,255,0), #f5f5f5);background:linear-gradient(to right, rgba(255,255,255,0), #f5f5f5);}.filter-panel .query-refinement_filters .refinement-arrow-left,.filter-panel .query-refinement_filters .refinement-arrow-right{cursor:pointer;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;align-items:center;}.filter-panel .query-refinement_filters.inactive-left-arrow .refinement-arrow-left-inner,.filter-panel .query-refinement_filters.inactive-right-arrow .refinement-arrow-right-inner{fill:#e6e6e6;}.filter-panel h4{margin:0 0 6px;}.filter-panel .filter-set{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:16.66667%;padding-bottom:12px;}.filter-panel input[type=radio]{display:inline;position:absolute;left:-9999em;}.filter-panel .more-link{display:inline-block;}.filter-panel .more{display:none;}.filter-panel .filter-panel_filters{overflow:hidden;margin:0 -15px;margin:0 -21px;}.filter-panel .filter-panel_filters:before,.filter-panel .filter-panel_filters:after{content:" ";display:table;}.filter-panel .filter-panel_filters:after{clear:both;}.filter-panel .filter-panel_filters:before{content:"";z-index:1;display:block;margin:0 15px;border-top:1px solid #ccc;padding-bottom:11px;}.filter-panel .filter-panel_filters::before{margin:0;}.filter-panel .filter-panel_filters>.container{display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-direction:normal;-webkit-box-orient:horizontal;-webkit-flex-direction:row;-moz-flex-direction:row;-ms-flex-direction:row;flex-direction:row;padding:0 6px;}.filter-panel .filter-panel_filters .filter-set{-webkit-box-flex:1 1 auto;-moz-box-flex:1 1 auto;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;min-width:0;min-height:0;width:inherit;}.filter-panel .filter-panel_filters h4,.filter-panel .filter-panel_filters .sort-filters,.filter-panel .filter-panel_filters .distance-filters{white-space:nowrap;}.filter-panel .filter-panel_filters a{white-space:nowrap;}.filter-panel .filter-panel_filters.is-collapsed{display:none;}.filter-panel .filter-panel_filters[data-component-bound="true"]{position:static;}.filter-panel .filter-panel_filters[data-component-bound="true"] ~ .filter-panel_overlay{display:none;}.filter-panel_overlay{position:absolute;top:0;right:0;bottom:0;left:0;z-index:1;opacity:0;}.no-js .filter-panel_overlay{display:none;}.filter-panel_filters .radio-check,.filter-group .radio-check{display:block;margin:0 0 3px;padding-left:19px;text-indent:-19px;float:left;width:100%;}.filter-panel_filters .radio-check span,.filter-group .radio-check span{text-indent:0;}.filter-panel_filters input[type=checkbox],.filter-group input[type=checkbox]{width:13px;height:13px;padding:0;margin:2px 2px 0 0;vertical-align:top;position:relative;overflow:hidden;}.feature .current-time{color:#999;}.feature input.open-at[type=text]{width:60px;margin:0;font-size:11px;line-height:1;}.feature select{margin:0;font-size:11px;}.filter-group .content{margin:0 -15px;padding:6px 15px;}.filter-group .content:before,.filter-group .content:after{content:" ";display:table;}.filter-group .content:after{clear:both;}.filter-group .column{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:50%;}.filter-group .radio-check{font-size:12px;}.suggested-filters .suggested-filters_filter-list{padding-bottom:18px;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;}.suggested-filters .suggested-filters_filter-list .suggested-filters_filter{padding-right:6px;margin-bottom:12px;-webkit-box-flex:0;-webkit-flex-grow:0;-moz-flex-grow:0;-ms-flex-positive:0;flex-grow:0;-webkit-flex-shrink:0;-moz-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}.suggested-filters .suggested-filters_filter-list .suggested-filters_filter:last-child{padding-right:0;}.suggested-filters .suggested-filters_filter.platform-in-panel-filter{padding-right:0;}.suggested-filters .yform input[type=text],.suggested-filters .yform .pseudo-input input[type=text]{-webkit-box-shadow:none;box-shadow:none;}.suggested-filters .suggested-filters_price-filters>li{display:inline-block;}.suggested-filters .suggested-filters_price-filters{font-size:0;}.suggested-filters .suggested-filters_price-filters .radio-check .filter-label{position:relative;border-right-width:0;border-radius:0;padding-bottom:9px;}.suggested-filters .suggested-filters_price-filters .radio-check input[type=checkbox]:checked ~ .filter-label{border:1px solid #41a700;margin-right:-1px;z-index:10;}.suggested-filters .suggested-filters_price-filters li:first-child .radio-check .filter-label{border-top-left-radius:4px;border-bottom-left-radius:4px;}.suggested-filters .suggested-filters_price-filters li:last-child .radio-check .filter-label{border-right-width:1px;padding-right:11px;border-top-right-radius:4px;border-bottom-right-radius:4px;}.suggested-filters .suggested-filters_price-filters li:last-child .radio-check input[type=checkbox]:checked ~ .filter-label{margin-right:0;}.suggested-filters .coachmark-tooltip-content{z-index:1002;width:150px;}#category-filters .column{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:50%;}#place-filters .column{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:25%;}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.free-delivery-banner_img{background:url(//s3-media3.fl.yelpcdn.com/assets/2/www/img/a6b69dda150a/search/food_banner@2x.png) no-repeat center;background-size:cover;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.free-delivery-banner_card{background-image:url(//s3-media3.fl.yelpcdn.com/assets/2/www/img/9f952c936024/search/white_card@2x.png);}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.mo-map .free-delivery-banner_img{background:url(//s3-media3.fl.yelpcdn.com/assets/2/www/img/1b654bfcc806/search/food_banner_half@2x.png) no-repeat center;}}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){.mo-map .free-delivery-banner_card{background-image:url(//s3-media3.fl.yelpcdn.com/assets/2/www/img/a99e97751d44/search/white_card_half@2x.png);background-size:222px 102px;}}.search-header{padding-top:12px;padding-bottom:7px;}.search-header .search-header-title-container{width:100%;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-direction:normal;-webkit-box-orient:horizontal;-webkit-flex-direction:row;-moz-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:baseline;-moz-box-align:baseline;-ms-flex-align:baseline;box-align:baseline;-webkit-align-items:baseline;align-items:baseline;-webkit-box-pack:justify;-ms-flex-pack:justify;-webkit-justify-content:space-between;-moz-justify-content:space-between;justify-content:space-between;}.search-header h1,.search-header h3,.search-header .pagination-results-window{-webkit-box-flex:1 1 auto;-moz-box-flex:1 1 auto;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;min-width:0;min-height:0;}.search-header h1,.search-header h3{float:left;-webkit-box-flex:1 1 auto;-moz-box-flex:1 1 auto;-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;min-width:0;min-height:0;padding-top:6px;}.search-header h1 .non-em,.search-header h1 .query-location,.search-header h3 .non-em,.search-header h3 .query-location{font-weight:normal;}.search-header h1{font-size:21px;line-height:1.28571em;}.search-header .pagination-results-window{float:right;font-size:14px;line-height:2.14286em;-webkit-box-flex:0 0 auto;-moz-box-flex:0 0 auto;-webkit-flex:0 0 auto;-ms-flex:0 0 auto;flex:0 0 auto;min-width:0;min-height:0;}.search-map{position:relative;border:1px solid #ccc;overflow:hidden;z-index:1000;}.search-map .yelp-map-container{border:none;-webkit-backface-visibility:hidden;-webkit-transform:translateZ(0);}.map-header{font-size:12px;line-height:1.5em;border-bottom:1px solid #ccc;background-color:#f5f5f5;padding:6px 0;}.map-header .mo-map-trigger{margin-top:4px;float:left;font-weight:bold;}.map-header .cube-wrapper{height:30px;position:relative;float:right;}.map-header .cube{height:100%;-webkit-transition:-webkit-transform 0.5s ease;-moz-transition:-moz-transform 0.5s ease;-ms-transition:-ms-transform 0.5s ease;transition:transform 0.5s ease;}.map-header .cube .face{height:30px;background-color:#f5f5f5;}.map-header .cube .face1 label{float:right;cursor:pointer;margin:6px 9px 0 0;}.map-header .cube .face2{display:none;}.map-header .cube .face2 a{float:right;margin-right:5px;}.map-wrapper{width:298px;}.talk-list-container,.list-feedback-container{margin:0 -15px;margin-top:24px;}.talk-list-container:before,.talk-list-container:after,.list-feedback-container:before,.list-feedback-container:after{content:" ";display:table;}.talk-list-container:after,.list-feedback-container:after{clear:both;}.talk-list-container .column,.list-feedback-container .column{float:left;padding:0 15px;min-height:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;width:50%;}.talk-list-container .column-borders .column:first-child,.list-feedback-container .column-borders .column:first-child{-webkit-box-shadow:1px 0 0 #e6e6e6;box-shadow:1px 0 0 #e6e6e6;}.talk-list-container .column-borders .column+.talk-list-container .column-borders .column,.list-feedback-container .column-borders .column+.talk-list-container .column-borders .column,.talk-list-container .column-borders .column+.list-feedback-container .column-borders .column,.list-feedback-container .column-borders .column+.list-feedback-container .column-borders .column{border-left:1px solid #e6e6e6;}.mtb-response-time-fast-responder{color:#41a700;text-decoration:inherit;}.search-exception{display:none;}</style>
    <script type="text/javascript" src="./Best Fried chicken in Atlanta, GA - Yelp_files/yly-dwbvvayubdqatw.js" defer=""></script><style type="text/css">#d__fFH{position:absolute;top:-5000px;left:-5000px}#d__fF{font-family:serif;font-size:200px;visibility:hidden}#yqxtayqwcaqsbfwdxeeayq{display:none!important}</style><script async="" src="./Best Fried chicken in Atlanta, GA - Yelp_files/svg_sprite.js"></script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/quant.js" type="text/javascript" async=""></script><style id="style-1-cropbar-clipper">/* Copyright 2014 Evernote Corporation. All rights reserved. */
.en-markup-crop-options {
    top: 18px !important;
    left: 50% !important;
    margin-left: -100px !important;
    width: 200px !important;
    border: 2px rgba(255,255,255,.38) solid !important;
    border-radius: 4px !important;
}

.en-markup-crop-options div div:first-of-type {
    margin-left: 0px !important;
}
</style><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/common.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/map.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/util.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/marker.js"></script><style type="text/css">/**
 * Style sheet used by new LibX tooltip code
 */

/* We insert a <div> with libx-tooltip style under the body.
 * This will inherit body's style - we can't afford to inherit undesirable 
 * styles and we must redefine what we need.  OTOH, some things, e.g.
 * font-size, might be ok to be inherited to stay within the page's tone.
 */
.libx-tooltip {
    display: none;
    overflow: visible;
    padding: 5px;
    z-index: 100;
    background-color: #eee;
    color: #000;
    font-weight: normal;
    font-style: normal;
    text-align: left;
    border: 2px solid #666;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
}

.libx-tooltip p {
    /* override default 1em margin to keep paragraphs inside a tooltip closer together. */
    margin: .2em;
}
</style><style type="text/css">/**
 * Style sheet used by LibX autolinking code
 */
.libx-autolink {
}

</style><style type="text/css">.gm-style {
        font: 400 11px Roboto, Arial, sans-serif;
        text-decoration: none;
      }
      .gm-style img { max-width: none; }</style><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/onion.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/controls.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/usage.js"></script><style type="text/css">.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:"lucida grande", tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset>div{overflow:hidden}.fb_link img{border:none}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_dialog{background:rgba(82, 82, 82, .7);position:absolute;top:-10000px;z-index:10001}.fb_reset .fb_dialog_legacy{overflow:visible}.fb_dialog_advanced{padding:10px;-moz-border-radius:8px;-webkit-border-radius:8px;border-radius:8px}.fb_dialog_content{background:#fff;color:#333}.fb_dialog_close_icon{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 0 transparent;cursor:pointer;display:block;height:15px;position:absolute;right:18px;top:17px;width:15px}.fb_dialog_mobile .fb_dialog_close_icon{top:5px;left:5px;right:auto}.fb_dialog_padding{background-color:transparent;position:absolute;width:1px;z-index:-1}.fb_dialog_close_icon:hover{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -15px transparent}.fb_dialog_close_icon:active{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -30px transparent}.fb_dialog_loader{background-color:#f6f7f9;border:1px solid #606060;font-size:24px;padding:20px}.fb_dialog_top_left,.fb_dialog_top_right,.fb_dialog_bottom_left,.fb_dialog_bottom_right{height:10px;width:10px;overflow:hidden;position:absolute}.fb_dialog_top_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 0;left:-10px;top:-10px}.fb_dialog_top_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -10px;right:-10px;top:-10px}.fb_dialog_bottom_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -20px;bottom:-10px;left:-10px}.fb_dialog_bottom_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -30px;right:-10px;bottom:-10px}.fb_dialog_vert_left,.fb_dialog_vert_right,.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{position:absolute;background:#525252;filter:alpha(opacity=70);opacity:.7}.fb_dialog_vert_left,.fb_dialog_vert_right{width:10px;height:100%}.fb_dialog_vert_left{margin-left:-10px}.fb_dialog_vert_right{right:0;margin-right:-10px}.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{width:100%;height:10px}.fb_dialog_horiz_top{margin-top:-10px}.fb_dialog_horiz_bottom{bottom:0;margin-bottom:-10px}.fb_dialog_iframe{line-height:0}.fb_dialog_content .dialog_title{background:#6d84b4;border:1px solid #365899;color:#fff;font-size:14px;font-weight:bold;margin:0}.fb_dialog_content .dialog_title>span{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/Cou7n-nqK52.gif) no-repeat 5px 50%;float:left;padding:5px 0 7px 26px}body.fb_hidden{-webkit-transform:none;height:100%;margin:0;overflow:visible;position:absolute;top:-10000px;left:0;width:100%}.fb_dialog.fb_dialog_mobile.loading{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/3rhSv5V8j3o.gif) white no-repeat 50% 50%;min-height:100%;min-width:100%;overflow:hidden;position:absolute;top:0;z-index:10001}.fb_dialog.fb_dialog_mobile.loading.centered{width:auto;height:auto;min-height:initial;min-width:initial;background:none}.fb_dialog.fb_dialog_mobile.loading.centered #fb_dialog_loader_spinner{width:100%}.fb_dialog.fb_dialog_mobile.loading.centered .fb_dialog_content{background:none}.loading.centered #fb_dialog_loader_close{color:#fff;display:block;padding-top:20px;clear:both;font-size:18px}#fb-root #fb_dialog_ipad_overlay{background:rgba(0, 0, 0, .45);position:absolute;bottom:0;left:0;right:0;top:0;width:100%;min-height:100%;z-index:10000}#fb-root #fb_dialog_ipad_overlay.hidden{display:none}.fb_dialog.fb_dialog_mobile.loading iframe{visibility:hidden}.fb_dialog_content .dialog_header{-webkit-box-shadow:white 0 1px 1px -1px inset;background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#738ABA), to(#2C4987));border-bottom:1px solid;border-color:#1d4088;color:#fff;font:14px Helvetica, sans-serif;font-weight:bold;text-overflow:ellipsis;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0;vertical-align:middle;white-space:nowrap}.fb_dialog_content .dialog_header table{-webkit-font-smoothing:subpixel-antialiased;height:43px;width:100%}.fb_dialog_content .dialog_header td.header_left{font-size:12px;padding-left:5px;vertical-align:middle;width:60px}.fb_dialog_content .dialog_header td.header_right{font-size:12px;padding-right:5px;vertical-align:middle;width:60px}.fb_dialog_content .touchable_button{background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#4966A6), color-stop(.5, #355492), to(#2A4887));border:1px solid #29487d;-webkit-background-clip:padding-box;-webkit-border-radius:3px;-webkit-box-shadow:rgba(0, 0, 0, .117188) 0 1px 1px inset, rgba(255, 255, 255, .167969) 0 1px 0;display:inline-block;margin-top:3px;max-width:85px;line-height:18px;padding:4px 12px;position:relative}.fb_dialog_content .dialog_header .touchable_button input{border:none;background:none;color:#fff;font:12px Helvetica, sans-serif;font-weight:bold;margin:2px -12px;padding:2px 6px 3px 6px;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog_content .dialog_header .header_center{color:#fff;font-size:16px;font-weight:bold;line-height:18px;text-align:center;vertical-align:middle}.fb_dialog_content .dialog_content{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat 50% 50%;border:1px solid #555;border-bottom:0;border-top:0;height:150px}.fb_dialog_content .dialog_footer{background:#f6f7f9;border:1px solid #555;border-top-color:#ccc;height:40px}#fb_dialog_loader_close{float:left}.fb_dialog.fb_dialog_mobile .fb_dialog_close_button{text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog.fb_dialog_mobile .fb_dialog_close_icon{visibility:hidden}#fb_dialog_loader_spinner{animation:rotateSpinner 1.2s linear infinite;background-color:transparent;background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/t-wz8gw1xG1.png);background-repeat:no-repeat;background-position:50% 50%;height:24px;width:24px}@keyframes rotateSpinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.fb_iframe_widget{display:inline-block;position:relative}.fb_iframe_widget span{display:inline-block;position:relative;text-align:justify}.fb_iframe_widget iframe{position:absolute}.fb_iframe_widget_fluid_desktop,.fb_iframe_widget_fluid_desktop span,.fb_iframe_widget_fluid_desktop iframe{max-width:100%}.fb_iframe_widget_fluid_desktop iframe{min-width:220px;position:relative}.fb_iframe_widget_lift{z-index:1}.fb_hide_iframes iframe{position:relative;left:-10000px}.fb_iframe_widget_loader{position:relative;display:inline-block}.fb_iframe_widget_fluid{display:inline}.fb_iframe_widget_fluid span{width:100%}.fb_iframe_widget_loader iframe{min-height:32px;z-index:2;zoom:1}.fb_iframe_widget_loader .FB_Loader{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat;height:32px;width:32px;margin-left:-16px;position:absolute;left:50%;z-index:4}</style><script async="true" type="text/javascript" src="https://s.adroll.com/j/roundtrip.js"></script><script type="text/javascript" charset="UTF-8" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stats.js"></script></head>













    <body id="yelp_main_body" class="jquery country-us logged-out" data-gr-c-s-loaded="true" style="zoom: 1;"><svg class="js-svg-spritesheet" height="0" style="display: block;" width="0"><symbol id="14x14_add" height="14" viewBox="0 0 14 14" width="14"><path d="M11 8H8v3a1 1 0 0 1-2 0V8H3a1 1 0 0 1 0-2h3V3a1 1 0 0 1 2 0v3h3a1 1 0 0 1 0 2z"></path></symbol><symbol id="14x14_apple" height="14" viewBox="0 0 14 14" width="14"><path d="M10.13 6.563c.014 1.87 1.518 2.49 1.537 2.497a6.5 6.5 0 0 1-.8 1.754c-.47.76-.965 1.5-1.75 1.515-.76.016-1.017-.486-1.89-.486-.883 0-1.156.47-1.887.502-.747.03-1.317-.81-1.806-1.563-.976-1.536-1.736-4.328-.717-6.228.494-.932 1.394-1.532 2.356-1.548.748-.017 1.442.543 1.902.543.45 0 1.308-.67 2.193-.57.37.01 1.423.158 2.102 1.225-.054.036-1.254.795-1.24 2.356zM6.984 2.84c-.084-.702.24-1.45.602-1.906.41-.518 1.12-.915 1.69-.942.075.73-.194 1.45-.587 1.98-.41.522-1.068.92-1.707.87z"></path></symbol><symbol id="14x14_arrow_down" height="14" viewBox="0 0 14 14" width="14"><path d="M12 6l-4.996 6L2 6h3V3h4v3h3z"></path></symbol><symbol id="14x14_arrow_up" height="14" viewBox="0 0 14 14" width="14"><path d="M9 9v3H5V9H2l4.996-6L12 9H9z"></path></symbol><symbol id="14x14_baron" height="14" viewBox="0 0 14 14" width="14"><path d="M12.06 9.5h-.43c.2-.75 1.87-2.46 1.22-3.81-.34-.71-.9-.99-1.48-.99-1.26 0-1.63.49-4.37.49s-3.11-.48-4.37-.48c-.58 0-1.14.26-1.48.98C.5 7.04 2.17 8.75 2.37 9.5h-.43c-.37 0-.66.39-.66.75s.29.75.66.75h10.12c.37 0 .66-.39.66-.75s-.29-.75-.66-.75zM4 8.75c-.41 0-.75-.34-.75-.75s.34-.75.75-.75.75.34.75.75-.34.75-.75.75zm3 0c-.41 0-.75-.34-.75-.75s.34-.75.75-.75.75.34.75.75-.34.75-.75.75zm3 0c-.41 0-.75-.34-.75-.75s.34-.75.75-.75.75.34.75.75-.34.75-.75.75zm-3-7a1.25 1.25 0 1 0 0 2.5 1.25 1.25 0 0 0 0-2.5z"></path></symbol><symbol id="14x14_bookmark" height="14" viewBox="0 0 14 14" width="14"><path d="M9 1H5a2 2 0 0 0-2 2v10l4-3 4 3V3a2 2 0 0 0-2-2zm-.44 6.964l-1.58-.97L5.455 8l.295-1.73L4.5 5.05l1.728-.252L6.98 3l.79 1.796 1.73.252L8.25 6.27l.31 1.694z"></path></symbol><symbol id="14x14_bullet" height="14" viewBox="0 0 14 14" width="14"><path d="M10 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"></path></symbol><symbol id="14x14_camera" height="14" viewBox="0 0 14 14" width="14"><path d="M11 12H3a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h1a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2zM7 4.5a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm0 4.75a1.75 1.75 0 1 1 0-3.5 1.75 1.75 0 0 1 0 3.5z"></path></symbol><symbol id="14x14_car" height="14" viewBox="0 0 14 14" width="14"><path d="M11 6l-.527-3.164A1 1 0 0 0 9.486 2H4.514a1 1 0 0 0-.987.836L3 6a1 1 0 0 0-1 1v3h1v1a1 1 0 0 0 2 0v-1h4v1a1 1 0 0 0 2 0v-1h1V7a1 1 0 0 0-1-1zM3.747 8.278a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5zM3.833 6l.5-3h5.334l.5 3H3.833zm6.42 2.278a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5z"></path></symbol><symbol id="14x14_cash_back" height="14" viewBox="0 0 14 14" width="14"><path d="M7.878 6.44c1.01.194 1.872.696 1.872 1.895 0 1.16-.878 1.915-2.304 2.052l.006.613h-.848v-.61C4.88 10.275 4.264 9.3 4.25 8.404h1.43c.02.425.34.79.955.873v-1.72l-.447-.093c-.974-.2-1.806-.78-1.806-1.896 0-1.18.98-1.832 2.232-1.943V3h.853v.628c1.32.14 2.136.93 2.15 1.94h-1.39c-.01-.366-.283-.747-.786-.833v1.612l.44.092zM7.44 9.27c.494-.038.85-.34.85-.79 0-.384-.25-.637-.757-.774-.03-.004-.06-.014-.092-.02V9.27zm-.805-4.54c-.447.048-.777.317-.777.726 0 .34.23.585.665.716a.7.7 0 0 0 .112.033V4.73zm5.773 1.72l-.51-.45A5.01 5.01 0 0 0 7 2C4.243 2 2 4.243 2 7s2.243 5 5 5a5.002 5.002 0 0 0 4.576-3h1.075A5.996 5.996 0 0 1 1 7a5.996 5.996 0 0 1 11.91-1l-.502.45z"></path></symbol><symbol id="14x14_check_in" height="14" viewBox="0 0 14 14" width="14"><path d="M13.5 7l-1.543-1.33.673-1.92-2.002-.38-.378-2-1.922.672L6.998.5 5.674 2.042 3.75 1.37l-.38 2-2 .38.674 1.92L.5 7l1.544 1.33-.674 1.92 2 .38.38 2 1.923-.673L7 13.5l1.328-1.543 1.922.673.378-2 2.002-.38-.673-1.922L13.5 7zM6.31 9.624l-.92-.92-1.378-1.378.92-.92 1.38 1.38 2.756-2.758.92.92L6.31 9.622z"></path></symbol><symbol id="14x14_checkmark" height="14" viewBox="0 0 14 14" width="14"><path d="M5.857 10.985L2.293 7.42a1 1 0 0 1 1.414-1.413l2.15 2.15 4.436-4.435a1 1 0 1 1 1.414 1.414l-5.85 5.85z"></path></symbol><symbol id="14x14_chevron_down" height="14" viewBox="0 0 14 14" width="14"><path d="M2 4.793a1 1 0 0 1 1.707-.707L7 7.38l3.293-3.294A1 1 0 1 1 11.707 5.5L7 10.207 2.293 5.5A.997.997 0 0 1 2 4.793z"></path></symbol><symbol id="14x14_chevron_left" height="14" viewBox="0 0 14 14" width="14"><path d="M9.207 2a1 1 0 0 1 .707 1.707L6.62 7l3.294 3.293A1 1 0 0 1 8.5 11.707L3.793 7 8.5 2.293A.997.997 0 0 1 9.207 2z"></path></symbol><symbol id="14x14_chevron_left_outline" height="14" viewBox="0 0 14 14" width="14"><path d="M9.25 11.5a.502.502 0 0 1-.354-.146L4.543 7l4.353-4.354a.5.5 0 0 1 .707.708L5.957 7l3.646 3.646a.5.5 0 0 1-.353.854z"></path></symbol><symbol id="14x14_chevron_right" height="14" viewBox="0 0 14 14" width="14"><path d="M4.793 12a1 1 0 0 1-.707-1.707L7.38 7 4.085 3.707A1 1 0 1 1 5.5 2.293L10.207 7 5.5 11.707a.997.997 0 0 1-.707.293z"></path></symbol><symbol id="14x14_chevron_right_outline" height="14" viewBox="0 0 14 14" width="14"><path d="M5.043 11.5c.128 0 .256-.05.353-.146L9.75 7 5.396 2.646a.5.5 0 0 0-.707.708L8.334 7 4.69 10.646a.502.502 0 0 0 .353.854z"></path></symbol><symbol id="14x14_chevron_up" height="14" viewBox="0 0 14 14" width="14"><path d="M12 9.207a1 1 0 0 1-1.707.707L7 6.62 3.707 9.915A1 1 0 1 1 2.293 8.5L7 3.793 11.707 8.5c.195.195.293.45.293.707z"></path></symbol><symbol id="14x14_clock" height="14" viewBox="0 0 14 14" width="14"><path d="M7 13A6 6 0 1 1 7 1a6 6 0 0 1 0 12zM7 2C4.243 2 2 4.243 2 7s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5zm2.165 6.75a.494.494 0 0 1-.25-.067L6.5 7.29V4a.5.5 0 0 1 1 0v2.71l1.915 1.107a.5.5 0 0 1-.25.933z"></path></symbol><symbol id="14x14_close" height="14" viewBox="0 0 14 14" width="14"><path d="M7.025 8.4l-2.122 2.12A1 1 0 0 1 3.49 9.106l2.12-2.122-2.12-2.12A1 1 0 1 1 4.903 3.45l2.122 2.12 2.12-2.12a1 1 0 1 1 1.415 1.41L8.44 6.98l2.12 2.123a1 1 0 0 1-1.414 1.414L7.026 8.4z"></path></symbol><symbol id="14x14_comment" height="14" viewBox="0 0 14 14" width="14"><path d="M12 6c0-2.21-2.24-4-5-4S2 3.79 2 6c0 1.304.792 2.452 2 3.182V12l3.385-2.03C9.963 9.81 12 8.103 12 6z"></path></symbol><symbol id="14x14_deal" height="14" viewBox="0 0 14 14" width="14"><path d="M12.982 2.013a.998.998 0 0 0-.995-.995L7.817 1a1 1 0 0 0-.713.293L1.38 7.016a1.315 1.315 0 0 0 .01 1.86l3.734 3.735c.516.52 1.348.52 1.86.01l5.723-5.72A1 1 0 0 0 13 6.184l-.018-4.17zm-2.444 3.53A1.495 1.495 0 0 1 8.425 3.43a1.495 1.495 0 0 1 2.113 2.115z"></path></symbol><symbol id="14x14_directions" height="14" viewBox="0 0 14 14" width="14"><path d="M12.32 5.36L8.64 1.68a2.32 2.32 0 0 0-3.28 0L1.68 5.36a2.32 2.32 0 0 0 0 3.28l3.68 3.68a2.32 2.32 0 0 0 3.28 0l3.68-3.68a2.32 2.32 0 0 0 0-3.28zM8 9V7H6v2H5V6h3V4l2.5 2.5L8 9z"></path></symbol><symbol id="14x14_drafts" height="14" viewBox="0 0 14 14" width="14"><path d="M12.796 1.204C10.112.86 7.37 1.682 5.37 3.68a8.647 8.647 0 0 0-2.328 4.27l5.762-3.666-5.957 6.152v.01l-2.07 2.07a.502.502 0 0 0 .352.855.51.51 0 0 0 .35-.142l2.073-2.074c2.468.14 4.932-.69 6.766-2.522 2-2 2.82-4.74 2.476-7.425z"></path></symbol><symbol id="14x14_duke" height="14" viewBox="0 0 14 14" width="14"><path d="M13 7.062a.75.75 0 1 0-1.28.53c-.448.68-.807 1.103-1.236.96-.395-.135-.37-1.032-.227-2.104.39-.114.68-.46.68-.886a.938.938 0 0 0-1.874 0c0 .33.18.605.435.772-.198.866-.43 1.93-1.012 1.93-.483 0-.813-1.38-.98-2.24a1.313 1.313 0 1 0-1.82-1.212c0 .534.32.99.778 1.196-.165.86-.495 2.255-.982 2.255-.576 0-.81-1.048-1.007-1.91a.924.924 0 0 0 .462-.79.937.937 0 0 0-1.875 0 .93.93 0 0 0 .65.88c.144 1.074.17 1.974-.228 2.108-.425.147-.782-.27-1.224-.94a.744.744 0 0 0 .24-.545.75.75 0 0 0-1.5 0c0 .376.28.675.643.73L2.335 9.5h-.21c-.363 0-.656.387-.656.75s.29.75.652.75h9.75c.362 0 .656-.387.656-.75s-.294-.75-.656-.75h-.24l.69-1.703A.742.742 0 0 0 13 7.062z"></path></symbol><symbol id="14x14_event" height="14" viewBox="0 0 14 14" width="14"><path d="M10 12H4c-1.103 0-2-.897-2-2V4c0-1.103.897-2 2-2a1 1 0 0 1 2 0h2a1 1 0 0 1 2 0c1.103 0 2 .897 2 2v6c0 1.103-.897 2-2 2zm1-7H3v5a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V5zM7.747 8.902L7 10.5l-.747-1.598A1.747 1.747 0 0 1 7 5.575a1.747 1.747 0 0 1 .747 3.327zM7 6.825a.5.5 0 1 0 0 1 .5.5 0 0 0 0-1z"></path></symbol><symbol id="14x14_file" height="14" viewBox="0 0 14 14" width="14"><path d="M3 13V1h3v5h5v7H3zM7 1l4 4H7V1z"></path></symbol><symbol id="14x14_first" height="14" viewBox="0 0 14 14" width="14"><path d="M13.5 7l-1.543-1.33.673-1.92-2.002-.38-.378-2-1.922.672L6.998.5 5.674 2.042 3.75 1.37l-.38 2-2 .38.673 1.92L.5 7l1.543 1.33-.673 1.92 2 .38.38 2 1.923-.674L7 13.5l1.328-1.544 1.922.674.378-2 2.002-.38-.673-1.922L13.5 7zM9 10H5V9h1V6H5V5l3-1v5h1v1z"></path></symbol><symbol id="14x14_flag" height="14" viewBox="0 0 14 14" width="14"><path d="M5 7.69V1.31c2 1.076 4-1.075 6 0v6.38c-2-1.076-4 1.075-6 0zM3.5 13a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 1 0v11a.5.5 0 0 1-.5.5z"></path></symbol><symbol id="14x14_flame" height="14" viewBox="0 0 14 14" width="14"><path d="M8.252 9.145c.68.982 1.046 2.226-.178 3.48 5.934-2.83 4.272-7.31.72-9.568.84 1.822-.332 1.702-.497 2.91-.522-3.647-3.477-4.59-3.477-4.59 1.462 2.02-1.36 3.587-2.593 6.247-1.052 2.262 1.81 4.08 3.336 5.002-1.537-2.245-.4-3.765 1.153-5.095-.577 1.84.36 2.2.75 2.96.507-.234.734-.98.786-1.342z"></path></symbol><symbol id="14x14_friends" height="14" viewBox="0 0 14 14" width="14"><g><path d="M6.592 7.53l-1.846 3.832c-.41.856-1.082.85-1.492-.007l-1.846-3.82c-.41-.856.005-1.53.923-1.53h3.34c.918 0 1.333.67.923 1.526zM4 5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path><path d="M12.592 7.53l-1.846 3.832c-.41.856-1.082.85-1.492-.007l-1.846-3.82c-.41-.856.005-1.53.923-1.53h3.34c.918 0 1.333.67.923 1.526zM10 5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z" opacity=".502"></path></g></symbol><symbol id="14x14_gift" height="14" viewBox="0 0 14 14" width="14"><path d="M13 7H8V5H6v2H1V5h4a2 2 0 1 1 2-2 2 2 0 1 1 2 2h4v2zM6 3c0-.55-.45-1-1-1s-1 .45-1 1 .45 1 1 1h1V3zm4 0c0-.55-.45-1-1-1s-1 .45-1 1v1h1c.55 0 1-.45 1-1zM6 13H3.857C2.753 13 2 12.105 2 11V8h4v5zm6-2c0 1.105-.753 2-1.857 2H8V8h4v3z"></path></symbol><symbol id="14x14_heart" height="14" viewBox="0 0 14 14" width="14"><path d="M9.14 3.11A2.52 2.52 0 0 0 7 4.3a2.522 2.522 0 0 0-2.14-1.19 2.53 2.53 0 0 0-2.527 2.535c0 2.44 3.254 3.44 4.667 5.244 1.413-1.807 4.667-2.808 4.667-5.247A2.53 2.53 0 0 0 9.14 3.11z"></path></symbol><symbol id="14x14_histogram" height="14" viewBox="0 0 14 14" width="14"><path d="M9 11V5h2v6H9zM6 3h2v8H6V3zM3 7h2v4H3V7z"></path></symbol><symbol id="14x14_info" height="14" viewBox="0 0 14 14" width="14"><path d="M7 13A6 6 0 1 1 7 1a6 6 0 0 1 0 12zM7 2C4.243 2 2 4.243 2 7s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5zM6 6h2v4H6V6zm0-2h2v1H6V4z"></path></symbol><symbol id="14x14_king" height="14" viewBox="0 0 14 14" width="14"><path d="M11.683 9.5h.38c.362 0 .655.387.655.75s-.293.75-.656.75H1.938c-.363 0-.656-.387-.656-.75s.293-.75.656-.75h.38C1.988 8.305.445 6.14 1.21 4.965c.267-.412.582-.903 1.57-.903 1.697 0 2.627.687 4.22.687s2.523-.69 4.22-.69c.988 0 1.303.49 1.57.903.764 1.176-.78 3.34-1.107 4.535zM4 7L3 8l1 1 1-1-1-1zm3-.375L5.625 8 7 9.375 8.375 8 7 6.625zM10 7L9 8l1 1 1-1-1-1zM7 4.25a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5z"></path></symbol><symbol id="14x14_light_bulb" height="14" viewBox="0 0 14 14" width="14"><path d="M9 8.445V10H5V8.445C3.81 7.752 3 6.477 3 5a4 4 0 0 1 8 0c0 1.477-.81 2.752-2 3.445zM6 3.41a.95.95 0 1 0 0 1.9.95.95 0 0 0 0-1.9zM7 13c-1.105 0-2-1-2-2h4c0 1-.895 2-2 2z"></path></symbol><symbol id="14x14_light_bulb_outline" height="14" viewBox="0 0 14 14" width="14"><path d="M9 8.445V10H5V8.445C3.81 7.752 3 6.477 3 5a4 4 0 0 1 8 0c0 1.477-.81 2.752-2 3.445zM7 2C5.346 2 4 3.346 4 5c0 1.068.562 2.033 1.503 2.58L6 7.87V9h2V7.87l.497-.29A2.964 2.964 0 0 0 10 5c0-1.654-1.346-3-3-3zM6 5.36a1 1 0 1 1 0-1.998 1 1 0 0 1 0 2zM7 13c-1.105 0-2-1-2-2h4c0 1-.895 2-2 2z"></path></symbol><symbol id="14x14_lightning_bolt" height="14" viewBox="0 0 14 14" width="14"><path d="M10.61 6H7.245a.2.2 0 0 1-.196-.24l.77-3.846c.04-.212-.236-.33-.36-.156L3.224 7.684A.2.2 0 0 0 3.39 8h3.108a.2.2 0 0 1 .198.23l-.577 3.953c-.03.208.236.316.36.145l4.292-6.012A.2.2 0 0 0 10.61 6z"></path></symbol><symbol id="14x14_list" height="14" viewBox="0 0 14 14" width="14"><path d="M5 11v-1h7v1H5zm0-7h7v1H5V4zm-3 6h2v1H2v-1zm0-3h2v1H2V7zm0-3h2v1H2V4zm8 4H5V7h5v1z"></path></symbol><symbol id="14x14_location" height="14" viewBox="0 0 14 14" width="14"><path d="M1.5 7.15l11-5.65-5.65 11-.45-4.9-4.9-.45z"></path></symbol><symbol id="14x14_marker" height="14" viewBox="0 0 14 14" width="14"><path d="M10.89 5.444a3.89 3.89 0 0 0-7.78 0c0 1.533.895 2.845 2.183 3.48L7 12.444l1.707-3.52a3.877 3.877 0 0 0 2.182-3.48zM7 3.89A1.556 1.556 0 1 1 7 7a1.556 1.556 0 0 1 0-3.11z"></path></symbol><symbol id="14x14_marker_grouped" height="14" viewBox="0 0 14 14" width="14"><g><path d="M10.89 5.444a3.89 3.89 0 0 0-7.78 0c0 1.458.813 2.714 2 3.38L7 12.444l1.89-3.62c1.187-.667 2-1.923 2-3.38zM7 3.89A1.556 1.556 0 1 1 7 7a1.556 1.556 0 0 1 0-3.11z"></path><path d="M12.316 9.728L11 12.444 9.683 9.728a3.063 3.063 0 0 1-.54-.35 4.496 4.496 0 0 0 1.426-1.22c.132.05.276.086.43.086a1.2 1.2 0 0 0 .45-2.31c.02-.162.05-.32.05-.49 0-.482-.097-.937-.237-1.373A2.99 2.99 0 0 1 14 7.046a2.99 2.99 0 0 1-1.684 2.684zM3 12.444L1.683 9.728A2.99 2.99 0 0 1 0 7.044 2.99 2.99 0 0 1 2.736 4.07c-.14.437-.236.892-.236 1.374 0 .17.032.328.05.49A1.198 1.198 0 0 0 3 8.244c.153 0 .297-.033.43-.086.384.503.87.916 1.427 1.22a3.063 3.063 0 0 1-.54.35L3 12.445z" opacity=".502"></path></g></symbol><symbol id="14x14_menu" height="14" viewBox="0 0 14 14" width="14"><path d="M2 13V2h10v11H2zm9-10H3v9h8V3zM8 6H4V5h4v1zm0 2H4V7h4v1zm0 2H4V9h4v1zm2-4H9V5h1v1zm0 2H9V7h1v1zm0 2H9V9h1v1z"></path></symbol><symbol id="14x14_message" height="14" viewBox="0 0 14 14" width="14"><path d="M10.5 2h-7A1.5 1.5 0 0 0 2 3.5v4A1.5 1.5 0 0 0 3.5 9H4v3l3-3h3.5A1.5 1.5 0 0 0 12 7.5v-4A1.5 1.5 0 0 0 10.5 2z"></path></symbol><symbol id="14x14_more" height="14" viewBox="0 0 14 14" width="14"><path d="M11 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2zM7 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2zM3 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"></path></symbol><symbol id="14x14_new" height="14" viewBox="0 0 14 14" width="14"><path d="M13 5.556l-3.66-.62.476-3.747-2.76 2.524L4.476 1l.22 3.77L1 5.13l3.034 2.177-2.027 3.164L5.57 9.416 6.738 13l1.41-3.494 3.482 1.307-1.805-3.3L13 5.555z"></path></symbol><symbol id="14x14_nope" height="14" viewBox="0 0 14 14" width="14"><path d="M7 1a6 6 0 1 0 0 12A6 6 0 0 0 7 1zm5 6c0 1.198-.44 2.284-1.146 3.146l-7-7C4.716 2.44 5.802 2 7 2c2.757 0 5 2.243 5 5zM2 7c0-1.198.44-2.284 1.146-3.147l7 7A4.935 4.935 0 0 1 7 12c-2.757 0-5-2.243-5-5z"></path></symbol><symbol id="14x14_order" height="14" viewBox="0 0 14 14" width="14"><g><path d="M4 4V3h1v1H4m1-2H4a1 1 0 0 0-1 1v1H2a1 1 0 0 0-1 1v3h7V5a1 1 0 0 0-1-1H6V3a1 1 0 0 0-1-1" opacity=".502"></path><path d="M11 6V2H8v6H1v2h1a2 2 0 0 0 4 0h2a2 2 0 0 0 4 0h1V7l-2-1zm-7 5c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm5-8h1v2H9V3zm1 8c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"></path></g></symbol><symbol id="14x14_paper_plane" height="14" viewBox="0 0 14 14" width="14"><path d="M14 2.5L0 6.036l3.856 1.61 6.962-3.217L4.95 8.2l-1.13 2.98 2.387-1.897L8.91 11.5l5.09-9z"></path></symbol><symbol id="14x14_pencil" height="14" viewBox="0 0 14 14" width="14"><path d="M12.95 3.05c0-.512-.195-1.023-.586-1.414a1.996 1.996 0 0 0-2.83 0L8.122 3.05 2.465 8.707 1.05 12.95l4.243-1.414L10.95 5.88l1.414-1.416c.39-.39.586-.902.586-1.414zm-8.197 7.61l-2.122.71.71-2.123 5.49-5.49 1.415 1.415-5.49 5.49z"></path></symbol><symbol id="14x14_phone" height="14" viewBox="0 0 14 14" width="14"><path d="M12.885 10.013l-2.496-1.44a.383.383 0 0 0-.42.075l-1.36 1.446c-.1.105-.3.194-.445.198 0 0-.93.026-2.685-1.7-1.755-1.728-1.76-2.674-1.76-2.674 0-.147.08-.353.18-.458l1.25-1.334a.42.42 0 0 0 .07-.432l-1.4-2.578c-.063-.133-.196-.155-.296-.05L1.22 3.5a.926.926 0 0 0-.214.456s-.29 2.506 3.218 5.956c3.51 3.45 5.97 3.076 5.97 3.076a.907.907 0 0 0 .442-.23l2.302-2.437c.1-.1.076-.24-.053-.302z"></path></symbol><symbol id="14x14_pin" height="14" viewBox="0 0 14 14" width="14"><path d="M1.106 5.036l3.932-3.9c.22-.22.61-.105.7.204.166.568.19 1.16.084 1.724l2.452 2.434a4.37 4.37 0 0 1 2.357.023c.36.105.506.563.25.815L9.135 8.07l3.804 4.55c.157.193.03.502-.167.346L8.095 9.1l-1.75 1.735c-.252.252-.714.108-.818-.248a4.29 4.29 0 0 1-.023-2.34L3.05 5.814a3.794 3.794 0 0 1-1.737-.083c-.31-.09-.427-.475-.207-.693z"></path></symbol><symbol id="14x14_regular" height="14" viewBox="0 0 14 14" width="14"><path d="M2 2.878c.124 3.945-.522 6.86 5.082 9.122 5.284-1.868 4.88-5.326 4.918-8.997-3.726-1.38-6.275-1.252-10-.125zm4.345 6.026L5.47 8.03 4.16 6.72l.875-.873 1.31 1.31 2.62-2.62.874.873-3.496 3.494z"></path></symbol><symbol id="14x14_reply" height="14" viewBox="0 0 14 14" width="14"><path d="M5.16 5.704H5V2.92l-4 4 4 4.002V7.82l.16-.002A8.787 8.787 0 0 1 12 11.08a7.042 7.042 0 0 0-6.84-5.376z"></path></symbol><symbol id="14x14_reservation" height="14" viewBox="0 0 14 14" width="14"><path d="M10 12H4c-1.103 0-2-.897-2-2V4c0-1.103.897-2 2-2a1 1 0 0 1 2 0h2a1 1 0 0 1 2 0c1.103 0 2 .897 2 2v6c0 1.103-.897 2-2 2zm1-7H3v5a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V5zM8 8h2v2H8V8z"></path></symbol><symbol id="14x14_review" height="14" viewBox="0 0 14 14" width="14"><path d="M10 2H4c-1.1 0-2 .9-2 2v6c0 1.1.9 2 2 2h6c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM8.687 7.74l.418 2.287-2.13-1.31-2.06 1.358.398-2.334-1.688-1.65 2.333-.34 1.016-2.424L8.04 5.75l2.335.34-1.688 1.65z"></path></symbol><symbol id="14x14_search" height="14" viewBox="0 0 14 14" width="14"><path d="M11.937 10.73a.926.926 0 0 0-.214-.33h.007L9.318 7.986c.36-.596.573-1.293.573-2.04a3.945 3.945 0 1 0-3.94 3.942c.747 0 1.444-.212 2.04-.573l2.406 2.406.003.005a.95.95 0 0 0 .335.212.932.932 0 0 0 1.205-1.207zm-5.99-2.344a2.444 2.444 0 0 1-2.442-2.44 2.445 2.445 0 0 1 2.44-2.44 2.446 2.446 0 0 1 2.442 2.44 2.445 2.445 0 0 1-2.44 2.44z"></path></symbol><symbol id="14x14_settings" height="14" viewBox="0 0 14 14" width="14"><path d="M12.923 6.088c.046.298.077.6.077.912 0 .31-.03.613-.076.91l-1.9.286a4.253 4.253 0 0 1-.33.806l1.14 1.542a5.98 5.98 0 0 1-.586.693l-.01.01a5.946 5.946 0 0 1-.693.586l-1.543-1.14a4.19 4.19 0 0 1-.806.332l-.285 1.9a5.94 5.94 0 0 1-.9.075h-.02a5.94 5.94 0 0 1-.9-.076l-.284-1.9a4.19 4.19 0 0 1-.806-.33l-1.544 1.14a5.946 5.946 0 0 1-.692-.586l-.01-.01a6.065 6.065 0 0 1-.587-.694l1.14-1.542a4.253 4.253 0 0 1-.33-.806l-1.9-.285A6.074 6.074 0 0 1 1 7c0-.31.03-.614.077-.912l1.898-.285c.084-.28.194-.55.332-.805l-1.14-1.543a6.037 6.037 0 0 1 1.29-1.29l1.54 1.14c.255-.136.525-.246.807-.33l.285-1.9C6.383 1.032 6.69 1 7 1c.31 0 .614.03.91.076l.286 1.9c.282.083.552.193.806.33l1.542-1.14c.493.362.927.797 1.29 1.29l-1.14 1.542c.137.254.247.524.33.805l1.9.285zM7 5a2 2 0 1 0 0 4 2 2 0 0 0 0-4z"></path></symbol><symbol id="14x14_speech" height="14" viewBox="0 0 14 14" width="14"><path d="M10.5 2h-7A1.5 1.5 0 0 0 2 3.5v4A1.5 1.5 0 0 0 3.5 9H4v3l3-3h3.5A1.5 1.5 0 0 0 12 7.5v-4A1.5 1.5 0 0 0 10.5 2z"></path></symbol><symbol id="14x14_speech_round" height="14" viewBox="0 0 14 14" width="14"><path d="M12 6c0-2.21-2.24-4-5-4S2 3.79 2 6c0 1.304.792 2.452 2 3.182V12l3.385-2.03C9.963 9.81 12 8.103 12 6z"></path></symbol><symbol id="14x14_star" height="14" viewBox="0 0 14 14" width="14"><path d="M6.957 1.5l1.74 3.95 3.803.556-2.75 2.69.68 3.725-3.473-2.13L3.6 12.5l.65-3.803-2.75-2.69 3.803-.557L6.957 1.5z"></path></symbol><symbol id="14x14_stopwatch" height="14" viewBox="0 0 14 14" width="14"><path d="M12.296 3.795a.5.5 0 0 1-.707 0l-.887-.883a.5.5 0 1 1 .707-.707l.886.883a.5.5 0 0 1 0 .707zM8.5 2h-1v1.05C10.023 3.305 12 5.41 12 8A5 5 0 0 1 2 8c0-2.59 1.977-4.695 4.5-4.95V2h-1a.5.5 0 0 1 0-1h3a.5.5 0 0 1 0 1zM3 8c0 2.206 1.794 4 4 4s4-1.794 4-4-1.794-4-4-4-4 1.794-4 4zm4 1a.5.5 0 0 1-.5-.5v-3a.5.5 0 0 1 1 0v3A.5.5 0 0 1 7 9z"></path></symbol><symbol id="14x14_ticket" height="14" viewBox="0 0 14 14" width="14"><path d="M9.828 2.05L8.06.282l-2.828 2.83 1.414 1.413-.707.707-1.42-1.414L.282 8.06 2.05 9.83a1.5 1.5 0 0 1 2.122 2.122L5.94 13.72l4.24-4.243L8.77 8.06l.707-.706 1.414 1.414 2.83-2.83-1.768-1.766A1.5 1.5 0 0 1 9.828 2.05zm-1.06 4.596l-.707.708L6.65 5.94l.708-.708L8.77 6.646z"></path></symbol><symbol id="14x14_triangle_down" height="14" viewBox="0 0 14 14" width="14"><path d="M7 9L3.5 5h7L7 9z"></path></symbol><symbol id="14x14_triangle_left" height="14" viewBox="0 0 14 14" width="14"><path d="M5 7l4-3.5v7L5 7z"></path></symbol><symbol id="14x14_triangle_right" height="14" viewBox="0 0 14 14" width="14"><path d="M9 7l-4 3.5v-7L9 7z"></path></symbol><symbol id="14x14_triangle_up" height="14" viewBox="0 0 14 14" width="14"><path d="M7 5l3.5 4h-7L7 5z"></path></symbol><symbol id="14x14_update" height="14" viewBox="0 0 14 14" width="14"><path d="M12.167 7A5.173 5.173 0 0 1 7 12.167c-1.423 0-2.75-.57-3.738-1.605l.724-.69A4.127 4.127 0 0 0 7 11.166 4.172 4.172 0 0 0 11.166 7H9.333l2.334-2.667L14 7h-1.833zM7 2.833A4.172 4.172 0 0 0 2.834 7h1.833L2.333 9.667 0 7h1.833A5.173 5.173 0 0 1 7 1.833c1.423 0 2.75.57 3.738 1.605l-.724.69A4.127 4.127 0 0 0 7 2.834z"></path></symbol><symbol id="14x14_walk" height="14" viewBox="0 0 14 14" width="14"><path d="M10.45 6.83l-1.98-.34-.792-1.386-.37 2.51 1.3 1.692 1.076 2.667a.597.597 0 0 1-.365.79l-.047.016a.598.598 0 0 1-.74-.337L7.45 9.883l-1.146-1.21-1.452 3.957a.566.566 0 0 1-1.073-.358l1.31-4.378.21-2.89-1.036.587-.314 2.097-.572-.007.013-2.596 2.02-1.436c.648-.467 2.418-.178 2.64.125.423.715.937 1.86.937 1.86l1.633.644-.17.554zM6.982 3.094a1.047 1.047 0 1 1 0-2.095 1.047 1.047 0 0 1 0 2.092z"></path></symbol><symbol id="18x18_add" height="18" viewBox="0 0 18 18" width="18"><path d="M16 10h-6v6H8v-6H2V8h6V2h2v6h6v2z"></path></symbol><symbol id="18x18_add_calendar" height="18" viewBox="0 0 18 18" width="18"><path d="M16 16v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-1-9H3v6.5c0 .828.627 1.5 1.4 1.5H10v1H4.4C3.077 16 2 14.88 2 13.5v-9C2 3.12 3.077 2 4.4 2H5a1 1 0 0 1 2 0h4a1 1 0 0 1 2 0h.6C14.923 2 16 3.12 16 4.5V10h-1V7z"></path></symbol><symbol id="18x18_add_friend" height="18" viewBox="0 0 18 18" width="18"><g><path d="M5.827 9.647l-2.013 4.127c-.448.922-1.18.915-1.628-.007L.173 9.65C-.275 8.73.178 8 1.18 8h3.64c1.002 0 1.455.725 1.007 1.647zM3 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path><path d="M12.827 9.647l-2.013 4.127c-.448.922-1.18.915-1.628-.007L7.173 9.65C6.725 8.73 7.178 8 8.18 8h3.64c1.002 0 1.455.725 1.007 1.647zM10 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" opacity=".502"></path><path d="M18 14h-2v-2h-2v2h-2v2h2v2h2v-2h2v-2z"></path></g></symbol><symbol id="18x18_add_photo" height="18" viewBox="0 0 18 18" width="18"><path d="M15 15H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zM9 4.75a4.25 4.25 0 1 0 0 8.5 4.25 4.25 0 0 0 0-8.5zM11 10h-1v1a1 1 0 0 1-2 0v-1H7a1 1 0 0 1 0-2h1V7a1 1 0 0 1 2 0v1h1a1 1 0 0 1 0 2z"></path></symbol><symbol id="18x18_apple" height="18" viewBox="0 0 18 18" width="18"><path d="M13.023 8.44c.02 2.404 1.953 3.2 1.977 3.208a8.305 8.305 0 0 1-1.028 2.256c-.606.976-1.24 1.93-2.25 1.947-.98.027-1.308-.62-2.432-.62-1.133 0-1.484.605-2.424.647-.96.038-1.694-1.042-2.322-2.01-1.255-1.974-2.232-5.564-.922-8.007.635-1.2 1.792-1.97 3.03-1.99.96-.022 1.853.698 2.444.698.58 0 1.682-.862 2.82-.733.475.015 1.83.203 2.703 1.575-.073.045-1.615 1.02-1.598 3.03zM8.98 3.652c-.107-.904.31-1.866.775-2.452.527-.665 1.44-1.175 2.173-1.21.096.94-.25 1.866-.755 2.546-.527.67-1.37 1.183-2.193 1.117z"></path></symbol><symbol id="18x18_arrow_down" height="18" viewBox="0 0 18 18" width="18"><path d="M3 8l6 7 6-7h-4V3H7v5H3z"></path></symbol><symbol id="18x18_arrow_up" height="18" viewBox="0 0 18 18" width="18"><path d="M15 10L9 3l-6 7h4v5h4v-5h4z"></path></symbol><symbol id="18x18_back" height="18" viewBox="0 0 18 18" width="18"><path d="M13 11.5c-2.2 0-4-1.8-4-4V7h3L8 3 4 7h3v.5c0 3.308 2.692 6 6 6h1v-2h-1z"></path></symbol><symbol id="18x18_background" height="18" viewBox="0 0 18 18" width="18"><path d="M15.708 12.192l-3.516 3.516a.998.998 0 0 1-.705.292h-.01c-.888 0-1.333-1.074-.705-1.702l3.526-3.526c.628-.628 1.702-.183 1.702.705v.01a.998.998 0 0 1-.292.705zm-9.176 3.516a.998.998 0 0 1-.705.292c-.888 0-1.333-1.074-.705-1.702l9.176-9.176C14.926 4.494 16 4.94 16 5.827a.998.998 0 0 1-.292.705l-9.176 9.176zm-2.83-2.83a.998.998 0 0 1-1.41-1.41l9.176-9.176A.998.998 0 0 1 12.173 2c.888 0 1.333 1.074.705 1.702l-9.176 9.176zm0-5.65C3.074 7.856 2 7.41 2 6.523v-.01c0-.264.105-.518.292-.705l3.516-3.516A.998.998 0 0 1 6.513 2h.01c.888 0 1.333 1.074.705 1.702L3.702 7.228z"></path></symbol><symbol id="18x18_badge" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zm-2.944 9.897a.328.328 0 0 1-.278-.193 1.172 1.172 0 0 1-.093-.395c-.053-.52.01-1.3.163-1.54.07-.12.175-.18.29-.17.077 0 .144.02 1.65.65l.44.18c.16.06.256.23.245.42-.01.182-.115.33-.27.37l-.626.2c-1.4.458-1.446.47-1.52.467zm3.19.956c-.004 1.492-.006 1.54-.03 1.613a.33.33 0 0 1-.266.21c-.375.065-1.548-.373-1.79-.668a.34.34 0 0 1-.07-.332c.025-.074.07-.13 1.125-1.39l.307-.37a.397.397 0 0 1 .466-.105c.17.07.272.22.263.38v.67zM8.994 8.73c-.077.023-.31.094-.593-.373 0 0-1.92-3.07-1.96-3.166-.03-.1.01-.22.1-.32.29-.3 1.84-.74 2.247-.64a.34.34 0 0 1 .256.24c.023.13.21 2.98.24 3.62.026.55-.206.62-.28.648zm2.6 4.217a.32.32 0 0 1-.333-.036c-.05-.04-.12-.14-.95-1.51l-.24-.41a.413.413 0 0 1 .042-.48c.114-.142.284-.2.43-.14.008.007.624.21.624.21 1.4.468 1.445.487 1.504.53a.34.34 0 0 1 .115.32c-.054.386-.825 1.38-1.18 1.526zm1.18-4.29a.38.38 0 0 1-.16.31c-.148.105-1.98.535-2.197.576-.217.042-.342-.043-.446-.202-.09-.15-.09-.33.01-.45l.39-.54c.86-1.18.91-1.24.97-1.28a.35.35 0 0 1 .35-.014c.34.168 1.09 1.2 1.09 1.597v.013z"></path></symbol><symbol id="18x18_baron" height="18" viewBox="0 0 18 18" width="18"><path d="M15.168 13h.582c.483 0 .875.517.875 1s-.392 1-.875 1H2.25c-.483 0-.875-.517-.875-1s.392-1 .875-1h.582c-.276-1-2.494-3.28-1.636-5.08.456-.956 1.2-1.303 1.982-1.303 1.673 0 2.162.64 5.822.64s4.148-.663 5.822-.663c.78 0 1.526.374 1.982 1.33.858 1.8-1.36 4.076-1.636 5.076zM4.5 10a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5zm3 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5zm3 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5zm3 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5zM9 6.372a1.625 1.625 0 1 1 0-3.25 1.625 1.625 0 0 1 0 3.25z"></path></symbol><symbol id="18x18_bed" height="18" viewBox="0 0 18 18" width="18"><path d="M15 15v-3H3v3H1V3h2v7h14v5h-2zM9 6h6a2 2 0 0 1 2 2v1H9V6zM4 7.635a2 2 0 0 1 4 0V9H4V7.635z"></path></symbol><symbol id="18x18_biz" height="18" viewBox="0 0 18 18" width="18"><path d="M15 15V6a1 1 0 0 0-1-1h-3a1 1 0 0 0-1 1v9H9V3a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12H1v1h16v-1h-2zm-4-8h3v1h-3V7zm0 3h3v1h-3v-1zm0 3h3v1h-3v-1zM4 4h4v1H4V4zm0 3h4v1H4V7zm0 3h4v1H4v-1zm0 3h4v1H4v-1z"></path></symbol><symbol id="18x18_blob" height="18" viewBox="0 0 18 18" width="18"><path d="M16.714 7.144l-4.707-.8.613-4.815-3.548 3.245-3.318-3.49.282 4.848-4.75.463 3.9 2.798-2.606 4.068 4.582-1.36 1.5 4.61 1.813-4.49 4.478 1.68-2.32-4.244 4.08-2.516z"></path></symbol><symbol id="18x18_bookmark" height="18" viewBox="0 0 18 18" width="18"><path d="M14 2H4v14l5-4 5 4V2zm-3.13 7.957L8.978 8.794 7.148 10 7.5 7.926 6 6.458l2.074-.303L8.977 4l.948 2.155L12 6.458l-1.5 1.468.37 2.03z"></path></symbol><symbol id="18x18_bookmark_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 12l-5 4V4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v12l-5-4zm4-8c0-.55-.45-1-1-1H6c-.55 0-1 .45-1 1v9.92l3.375-2.7.625-.5.625.5L13 13.92V4zM8.977 8.794L7.147 10 7.5 7.926 6 6.458l2.074-.303L8.977 4l.948 2.155L12 6.458l-1.5 1.468.37 2.03-1.893-1.162z"></path></symbol><symbol id="18x18_bullhorn" height="18" viewBox="0 0 18 18" width="18"><path d="M16 15a1 1 0 0 1-1-1V4a1 1 0 0 1 2 0v10a1 1 0 0 1-1 1zm-6 0H5v-3.25l-2-.5v.25a1 1 0 0 1-2 0v-5a1 1 0 0 1 2 0v.25L14 4v10l-4-1v2zm-1-2.25L6 12v2h3v-1.25z"></path></symbol><symbol id="18x18_camera" height="18" viewBox="0 0 18 18" width="18"><path d="M15 15H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2h2a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2zM9 5a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm0 6.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="18x18_cash_back" height="18" viewBox="0 0 18 18" width="18"><path d="M9.556 8.312c1.175.23 2.18.824 2.18 2.24 0 1.37-1.023 2.263-2.682 2.424l.007.725h-.984v-.717c-2.008-.138-2.722-1.29-2.74-2.35H7c.024.502.395.934 1.11 1.032V9.63l-.52-.108c-1.133-.236-2.102-.92-2.102-2.24 0-1.393 1.14-2.164 2.598-2.296V4.25h.992v.74c1.536.168 2.486 1.1 2.504 2.293H9.964c-.012-.432-.33-.882-.915-.984v1.903l.505.108zm-.507 3.346c.57-.046.984-.403.984-.933 0-.455-.29-.755-.88-.916-.036-.007-.07-.018-.106-.025v1.872zm-.94-5.366c-.52.058-.905.375-.905.86 0 .4.266.69.774.844a.73.73 0 0 0 .13.04V6.292zM15.2 10l-2.25-3h1.482c-.836-2.466-3.162-4.25-5.907-4.25A6.257 6.257 0 0 0 2.275 9a6.257 6.257 0 0 0 6.25 6.25c2.746 0 5.08-1.783 5.916-4.25h1.565c-.885 3.305-3.898 5.75-7.48 5.75-4.273 0-7.75-3.477-7.75-7.75s3.477-7.75 7.75-7.75c3.58 0 6.588 2.445 7.473 5.75h1.453l-2.25 3z"></path></symbol><symbol id="18x18_chair" height="18" viewBox="0 0 18 18" width="18"><path d="M13.67 8.035l-7.044.702L5.398 1.99a1.23 1.23 0 0 0-1.424-.983 1.22 1.22 0 0 0-.987 1.42l1.43 7.857c.012.07.047.126.07.19.023.06.037.124.068.18.042.077.1.14.158.204.037.043.067.09.11.128.075.065.163.11.25.154.037.02.065.048.103.063l-1.36 4.747a.815.815 0 0 0 .785 1.04.82.82 0 0 0 .788-.592l1.5-5.23 3.5-.35 1.6 5.58a.818.818 0 0 0 1.01.56.814.814 0 0 0 .56-1.008l-1.517-5.297 1.876-.187a1.222 1.222 0 1 0-.244-2.43z"></path></symbol><symbol id="18x18_chat" height="18" viewBox="0 0 18 18" width="18"><path d="M9 3C5.41 3 2.5 5.24 2.5 8c0 1.6.98 3.02 2.5 3.936V16l4-3c3.59 0 6.5-2.24 6.5-5S12.59 3 9 3z"></path></symbol><symbol id="18x18_chat_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 4c3.033 0 5.5 1.794 5.5 4s-2.467 4-5.5 4h-.333l-.267.2L6 14v-2.63l-.484-.29C4.236 10.306 3.5 9.184 3.5 8c0-2.206 2.467-4 5.5-4m0-1C5.41 3 2.5 5.24 2.5 8c0 1.6.98 3.02 2.5 3.936V16l4-3c3.59 0 6.5-2.24 6.5-5S12.59 3 9 3z"></path></symbol><symbol id="18x18_check_in" height="18" viewBox="0 0 18 18" width="18"><path d="M18 9l-2.136-1.84.932-2.66-2.772-.525-.524-2.77-2.66.93L8.997 0 7.163 2.136 4.5 1.206l-.525 2.77-2.77.524.932 2.66L0 9l2.137 1.84-.932 2.66 2.77.525.526 2.77 2.664-.932L8.998 18l1.84-2.137 2.662.932.524-2.77 2.772-.524-.932-2.66L18 9zm-9.85 3.23L5.324 9.4l1.13-1.13 1.698 1.696 3.396-3.395 1.13 1.134-4.525 4.525z"></path></symbol><symbol id="18x18_checkmark" height="18" viewBox="0 0 18 18" width="18"><path d="M7.232 14.273L1.93 8.97a1 1 0 1 1 1.413-1.414l3.89 3.89 7.424-7.426a1 1 0 0 1 1.414 1.414l-8.837 8.84z"></path></symbol><symbol id="18x18_checkmark_badged" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zm3.96 6.28l-4.808 4.807-3.112-3.11a.8.8 0 1 1 1.13-1.132l1.982 1.98 3.677-3.677a.8.8 0 1 1 1.13 1.13z"></path></symbol><symbol id="18x18_clapper" height="18" viewBox="0 0 18 18" width="18"><path d="M14.002 7h-5.21l6.385-2.295L13.487 0 .31 4.735 2.003 9.44V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7h-2zm-1.89-4.912l.675 1.882-1.882.677-.676-1.882 1.88-.677zM8.346 3.44l.676 1.883L7.14 6l-.676-1.883 1.883-.676zM4.582 4.795l.677 1.882-1.884.677L2.7 5.47l1.882-.676zM4.002 11V9h2v2h-2zm4 0V9h2v2h-2zm6 0h-2V9h2v2z"></path></symbol><symbol id="18x18_clock" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17A8 8 0 1 1 9 1a8 8 0 0 1 0 16zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm3.223 10.098a.998.998 0 0 1-.588-.192L8 9.256V5a1 1 0 0 1 2 0v3.24l2.812 2.05a1 1 0 0 1-.59 1.808z"></path></symbol><symbol id="18x18_close" height="18" viewBox="0 0 18 18" width="18"><path d="M10.414 9l4.043-4.043a1 1 0 0 0-1.414-1.414L9 7.586 4.957 3.543a1 1 0 0 0-1.414 1.414L7.586 9l-4.043 4.043a1 1 0 0 0 1.414 1.414L9 10.414l4.043 4.043a.997.997 0 0 0 1.414 0 1 1 0 0 0 0-1.414L10.414 9z"></path></symbol><symbol id="18x18_coffee" height="18" viewBox="0 0 18 18" width="18"><path d="M13 11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5h10a3 3 0 0 1 0 6zm0-4.8v3.6c.992 0 1.8-.808 1.8-1.8 0-.993-.808-1.8-1.8-1.8zm2 7.8a1 1 0 0 1 0 2H3a1 1 0 0 1 0-2h12z"></path></symbol><symbol id="18x18_comment" height="18" viewBox="0 0 18 18" width="18"><path d="M9 3C5.41 3 2.5 5.24 2.5 8c0 1.6.98 3.02 2.5 3.936V16l4-3c3.59 0 6.5-2.24 6.5-5S12.59 3 9 3z"></path></symbol><symbol id="18x18_compliment" height="18" viewBox="0 0 18 18" width="18"><path d="M14.5 6.75a5.5 5.5 0 0 0-11 0 5.495 5.495 0 0 0 2.993 4.892L5.5 16.75l3.505-2 3.495 2-.993-5.108A5.495 5.495 0 0 0 14.5 6.75zm-5.5 4c-2.206 0-4-1.794-4-4s1.794-4 4-4 4 1.794 4 4-1.794 4-4 4z"></path></symbol><symbol id="18x18_cool" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1C4.59 1 1 4.59 1 9s3.59 8 8 8 8-3.59 8-8-3.59-8-8-8zm0 13.146a4.28 4.28 0 0 1-3.958-2.657A6.81 6.81 0 0 0 9 12.75a6.81 6.81 0 0 0 3.958-1.265A4.28 4.28 0 0 1 9 14.145zM12.29 10h-.003c-1.343 0-2.515-.9-3.05-2.224-.096-.24-.38-.24-.476 0C8.23 9.1 7.06 10 5.717 10H5.71c-1.67 0-3.107-1.15-3.35-3.018l-.104-.734c-.058-.305.212-.25.526-.248h12.44c.323 0 .558-.04.524.248l-.103.517C15.353 8.612 13.96 10 12.29 10z"></path></symbol><symbol id="18x18_cool_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm6.026 5.335C14.766 8.797 13.5 10 11.986 10h-.003c-1.218 0-2.282-.764-2.767-1.813-.088-.19-.344-.242-.432-.052C8.3 9.185 7.234 10 6.016 10h-.003C4.5 10 3.195 8.83 2.973 7.35l-.093-.84c-.053-.242.192-.51.477-.51h11.286c.294 0 .508.332.477.56l-.094.775zm-2.068 4.154A4.28 4.28 0 0 1 9 14.144a4.28 4.28 0 0 1-3.958-2.657A6.81 6.81 0 0 0 9 12.753a6.81 6.81 0 0 0 3.958-1.265z"></path></symbol><symbol id="18x18_deal" height="18" viewBox="0 0 18 18" width="18"><path d="M14.473 1.86l-4.213.016a1.963 1.963 0 0 0-1.397.573L2.066 9.23a1.96 1.96 0 0 0 0 2.77l4.295 4.286a1.97 1.97 0 0 0 2.78 0l6.798-6.783c.37-.37.546-.996.543-1.518l.013-4.143c-.003-1.075-.94-1.98-2.017-1.984zM13.06 7.076a1.51 1.51 0 0 1-2.133 0 1.5 1.5 0 0 1 0-2.127 1.51 1.51 0 0 1 2.132 0 1.5 1.5 0 0 1 0 2.123z"></path></symbol><symbol id="18x18_denied" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zm4 9H5V8h8v2z"></path></symbol><symbol id="18x18_desktop" height="18" viewBox="0 0 18 18" width="18"><path d="M14 1H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3v2H5v1h8v-1h-2v-2h3a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm1 8a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v6z"></path></symbol><symbol id="18x18_directions" height="18" viewBox="0 0 18 18" width="18"><path d="M16.444 7.556l-5.957-5.958a2.145 2.145 0 0 0-3.034 0L1.598 7.453a2.145 2.145 0 0 0 0 3.034l5.958 5.957a2 2 0 0 0 2.828 0l6.06-6.06a2 2 0 0 0 0-2.828zM9.97 11.47v-2.5h-3v3h-1v-4h4v-2.5l3 3-3 3z"></path></symbol><symbol id="18x18_dish" height="18" viewBox="0 0 18 18" width="18"><path d="M1 15v-2h16v2H1zm1.08-3H2v-1a7 7 0 0 1 14 0v1H2.08zM9 5.5a5.516 5.516 0 0 0-5.39 4.4.5.5 0 1 0 .98.2A4.512 4.512 0 0 1 9 6.5a.5.5 0 0 0 0-1zM8 3a1 1 0 1 1 2 0 1 1 0 0 1-2 0z"></path></symbol><symbol id="18x18_download" height="18" viewBox="0 0 18 18" width="18"><path d="M15 15H3v-2h12v2zM8 9V3h2v6h3l-4 4-4-4h3z"></path></symbol><symbol id="18x18_draft" height="18" viewBox="0 0 18 18" width="18"><path d="M16.942.942c-.777-.04-1.443.04-2.237.15C12.925 1.348 11 2.025 10 2.94v2.286L8.71 3.8C6.663 5.5 5.164 7.86 4.6 10.492l5.98-4.663-9.404 9.95c-.608.64.314 1.56.955.955l3.278-3.093c.41-.016.815-.048 1.232-.103 3.07-.438 5.696-2.1 7.53-4.29L11.958 8h3.062c1.352-2 2.065-4.454 1.92-7.058z"></path></symbol><symbol id="18x18_drafts" height="18" viewBox="0 0 18 18" width="18"><path d="M16.08 5.63c-1.045-.16-2.05-.215-2.918-.127.797.145 1.63.5 2.504.948a7.144 7.144 0 0 1-.11.19c-1.594-.223-3.12-.284-4.455-.15 1.2.22 2.44.678 3.735 1.258-1.903 2.582-5.284 4.92-10.975 4.526C7.405 8.18 12.16 4.7 15.486 2.606c-4.132 1.178-9.278 4.96-12.202 8.8.47-4.812 3.428-7.27 6.572-8.486-.083.86-.215 1.672-.438 2.42.528-.8 1.007-1.74 1.426-2.765.217-.066.433-.127.65-.184-.03.577-.1 1.117-.245 1.6a10 10 0 0 0 .89-1.754c1.94-.427 3.736-.475 4.82-.415.136.444-.06 2.016-.88 3.81zM3.857 12.273C2.767 13.533 1.785 14.847 1 16.2c.173-1.472 1.023-3.138 2.284-4.794a13.28 13.28 0 0 0-.056.82c.215.02.42.03.63.046z"></path></symbol><symbol id="18x18_duke" height="18" viewBox="0 0 18 18" width="18"><path d="M17 9.75a1 1 0 1 0-1.708.705c-.596.908-1.074 1.472-1.646 1.28-.528-.178-.496-1.375-.303-2.804.52-.15.907-.61.907-1.18a1.25 1.25 0 0 0-2.5 0c0 .44.24.807.58 1.03-.264 1.154-.574 2.57-1.348 2.57-.645 0-1.085-1.84-1.306-2.985A1.75 1.75 0 1 0 7.25 6.75c0 .71.426 1.32 1.036 1.594-.22 1.146-.66 3.006-1.31 3.006-.768 0-1.08-1.397-1.343-2.547.362-.22.617-.6.617-1.053a1.25 1.25 0 0 0-2.5 0c0 .554.366 1.008.864 1.172.194 1.434.227 2.634-.302 2.812-.567.192-1.043-.363-1.632-1.26A.988.988 0 0 0 3 9.75a1 1 0 0 0-2 0c0 .5.375.9.857.97L2.78 13H2.5c-.483 0-.875.517-.875 1s.392 1 .875 1h13c.483 0 .875-.517.875-1s-.392-1-.875-1h-.322l.922-2.27a.99.99 0 0 0 .9-.98z"></path></symbol><symbol id="18x18_embed" height="18" viewBox="0 0 18 18" width="18"><path d="M12.503 13.76a.717.717 0 0 1-.526.23.717.717 0 0 1-.526-.23.822.822 0 0 1 0-1.117l3.444-3.652-3.444-3.65a.822.822 0 0 1 0-1.116.714.714 0 0 1 1.053 0l4.495 4.77-4.495 4.767zm-5.954 0a.717.717 0 0 1-.528.23.718.718 0 0 1-.526-.23L1.002 8.99l4.495-4.768a.714.714 0 0 1 1.052 0c.29.308.29.808 0 1.116L3.105 8.99l3.442 3.653c.29.308.29.808 0 1.116z"></path></symbol><symbol id="18x18_envelope" height="18" viewBox="0 0 18 18" width="18"><path d="M16.772 13.863l-4.89-4.892 4.862-4.81c.12.257.256.54.256.843v8c0 .31-.087.6-.228.864zM7.812 9.49L1.706 3.383c.33-.24.73-.383 1.168-.383h12c.438 0 .84.144 1.168.382L9.936 9.49a1.505 1.505 0 0 1-2.122 0zM1.12 13.716A2.235 2.235 0 0 1 1 13V5c0-.302.01-.586.13-.843l4.75 4.8-4.76 4.76zm5.985-3.52a2.507 2.507 0 0 0 3.538.002l.527-.524 4.93 4.932a2.182 2.182 0 0 1-1.227.394h-12c-.468 0-.87-.168-1.185-.437L6.583 9.67l.522.527z"></path></symbol><symbol id="18x18_envelope_open" height="18" viewBox="0 0 18 18" width="18"><path d="M16.822 15.816l-4.802-4.8L17 7v8c0 .292-.066.567-.178.816zm-15.644 0A1.982 1.982 0 0 1 1 15V7l4.98 4.015-4.802 4.8zM7.823 1.388c.628-.517 1.725-.517 2.354 0L17 7H1l6.823-5.612zm-.59 10.88c.47.472 1.1.732 1.767.732.668 0 1.296-.26 1.768-.732l.545-.546L16.19 16.6c-.333.248-.742.4-1.19.4H3c-.448 0-.857-.152-1.19-.4l4.877-4.878.545.546z"></path></symbol><symbol id="18x18_event" height="18" viewBox="0 0 18 18" width="18"><path d="M13.6 16H4.4C3.077 16 2 14.88 2 13.5v-9C2 3.12 3.077 2 4.4 2H5a1 1 0 0 1 2 0h4a1 1 0 0 1 2 0h.6C14.923 2 16 3.12 16 4.5v9c0 1.38-1.077 2.5-2.4 2.5zM15 7H3v6.5c0 .828.627 1.5 1.4 1.5h9.2c.773 0 1.4-.672 1.4-1.5V7zm-4.825 5.48l-.425.627L9 14.214l-.75-1.107-.425-.627A2.49 2.49 0 0 1 9 7.786a2.49 2.49 0 0 1 1.175 4.694zM9 9.214a1.07 1.07 0 1 0 0 2.142 1.07 1.07 0 0 0 0-2.142z"></path></symbol><symbol id="18x18_exclamation" height="18" viewBox="0 0 18 18" width="18"><path d="M9 10.5a2 2 0 0 1-2-2v-5a2 2 0 0 1 4 0v5a2 2 0 0 1-2 2zm0 2a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="18x18_external_link" height="18" viewBox="0 0 18 18" width="18"><path d="M14 15H4c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3v1H4v10h10v-3h1v3c0 .55-.45 1-1 1zm-5.12-4.465L7.463 9.12l3.83-3.827L9 3h6v6l-2.293-2.293-3.828 3.828z"></path></symbol><symbol id="18x18_facebook" height="18" viewBox="0 0 18 18" width="18"><path d="M10.5 5H13V2h-2a4 4 0 0 0-4 4v1H5v3h2v6h3v-6h2l1-3h-3V5.5a.5.5 0 0 1 .5-.5z"></path></symbol><symbol id="18x18_fast_responder" height="18" viewBox="0 0 18 18" width="18"><path d="M16 12v4l-5-4H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2zM0 10h4v1H0v-1zm1-3h3v1H1V7zm1-3h2v1H2V4z"></path></symbol><symbol id="18x18_feed" height="18" viewBox="0 0 18 18" width="18"><path d="M14 3H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zM4 6.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-3zM14 12H4v-1h10v1zm0-5h-4V6h4v1zm0 2h-4V8h4v1z"></path></symbol><symbol id="18x18_file" height="18" viewBox="0 0 18 18" width="18"><path d="M3 17V1h6v6h6v10H3zm9-7H6v1h6v-1zm0 3H6v1h6v-1zM10 1l5 5h-5V1z"></path></symbol><symbol id="18x18_filter" height="18" viewBox="0 0 18 18" width="18"><path d="M15 7h-5V5h5a1 1 0 0 1 0 2zm-2 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm-3 0c0 .55.45 1 1 1s1-.45 1-1-.45-1-1-1-1 .45-1 1zM7 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0-3c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zM2 6a1 1 0 0 1 1-1h1v2H3a1 1 0 0 1-1-1zm1 5h5v2H3a1 1 0 0 1 0-2zm13 1a1 1 0 0 1-1 1h-1v-2h1a1 1 0 0 1 1 1z"></path></symbol><symbol id="18x18_first" height="18" viewBox="0 0 18 18" width="18"><path d="M18 9l-2.136-1.84.932-2.66-2.772-.525-.524-2.77-2.66.93L8.997 0 7.163 2.136 4.5 1.206l-.525 2.77-2.77.524.932 2.66L0 9l2.137 1.84-.932 2.66 2.77.525.526 2.77 2.664-.932L8.998 18l1.84-2.137 2.662.932.524-2.77 2.772-.524-.932-2.66L18 9zm-7 4H7v-1h1V6.667L7 7V6l3-1v7h1v1z"></path></symbol><symbol id="18x18_flag" height="18" viewBox="0 0 18 18" width="18"><path d="M6 10V3c4.976 1.098 4.024-1 8 0v7c-4.024-.976-3.024 1.024-8 0zM4 2h1v14H4V2z"></path></symbol><symbol id="18x18_flame" height="18" viewBox="0 0 18 18" width="18"><path d="M11.508 3.743c1.173 2.43-.465 2.27-.696 3.88C10.082 2.758 5.947 1.5 5.947 1.5c2.045 2.697-1.9 4.784-3.63 8.33-1.47 3.016 2.533 5.44 4.67 6.67-2.15-2.993-.563-5.02 1.612-6.793-.81 2.448.5 2.934 1.043 3.944.71-.31 1.028-1.3 1.1-1.79.954 1.31 1.465 2.97-.248 4.64 8.302-3.77 5.977-9.743 1.007-12.752z"></path></symbol><symbol id="18x18_followers" height="18" viewBox="0 0 18 18" width="18"><path d="M15 14h-2v2l-4-3 4-3v2h3l-1 2zm-7.925 1.383c-.443.817-1.707.817-2.15 0L2.128 9.605C1.728 8.868 2.31 8 3.203 8h5.594c.893 0 1.474.868 1.075 1.605l-2.797 5.778zM6 7a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="18x18_following" height="18" viewBox="0 0 18 18" width="18"><path d="M16 13l-4 3v-2H9l1-2h2v-2l4 3zm-8.925 2.383c-.443.817-1.707.817-2.15 0L2.128 9.605C1.728 8.868 2.31 8 3.203 8h5.594c.893 0 1.474.868 1.075 1.605l-2.797 5.778zM6 7a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="18x18_food" height="18" viewBox="0 0 18 18" width="18"><path d="M13.61 17h-.007a1.39 1.39 0 0 1-1.376-1.587L13 10l-2-1c0-5.373 1.375-8 3.25-8 .497 0 .75.336.75.75v13.86A1.39 1.39 0 0 1 13.61 17zM6.557 9.912l.35 5.59a1.41 1.41 0 1 1-2.813 0l.35-5.59A1.994 1.994 0 0 1 3 8V1.5a.5.5 0 0 1 1 0v5a.5.5 0 0 0 1 0v-5a.5.5 0 0 1 1 0v5a.5.5 0 0 0 1 0v-5a.5.5 0 0 1 1 0V8c0 .91-.61 1.67-1.443 1.912z"></path></symbol><symbol id="18x18_friends" height="18" viewBox="0 0 18 18" width="18"><g><path d="M7.904 9.43l-2.098 4.697a.9.9 0 0 1-1.612 0L2.096 9.43a.902.902 0 0 1 .806-1.305h4.196c.67 0 1.105.705.806 1.305zM5 7.375a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path><path d="M15.904 9.43l-2.098 4.697a.89.89 0 0 1-.806.498.89.89 0 0 1-.806-.498L10.096 9.43a.902.902 0 0 1 .806-1.305h4.195c.67 0 1.106.705.807 1.305zM13 7.375a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" opacity=".502"></path></g></symbol><symbol id="18x18_funny" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zm2.5 4.625a1.376 1.376 0 1 1 0 2.75 1.376 1.376 0 0 1 0-2.75zm-5 0a1.376 1.376 0 1 1 0 2.75 1.376 1.376 0 0 1 0-2.75zM9 14a4.87 4.87 0 0 1-4.787-4h9.574A4.87 4.87 0 0 1 9 14z"></path></symbol><symbol id="18x18_funny_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm0 12a4.87 4.87 0 0 1-4.787-4h9.574A4.87 4.87 0 0 1 9 14zm2.5-5.625a1.376 1.376 0 1 1 0-2.75 1.376 1.376 0 0 1 0 2.75zm-5 0a1.376 1.376 0 1 1 0-2.75 1.376 1.376 0 0 1 0 2.75z"></path></symbol><symbol id="18x18_gift" height="18" viewBox="0 0 18 18" width="18"><path d="M16 9h-6V7H8v2H2V7h4.5A2.5 2.5 0 1 1 9 4.5 2.5 2.5 0 1 1 11.5 7H16v2zM8 4.5C8 3.673 7.327 3 6.5 3S5 3.673 5 4.5 5.673 6 6.5 6H8V4.5zm5 0c0-.827-.673-1.5-1.5-1.5S10 3.673 10 4.5V6h1.5c.827 0 1.5-.673 1.5-1.5zM8 16H5a2 2 0 0 1-2-2v-4h5v6zm7-2a2 2 0 0 1-2 2h-3v-6h5v4z"></path></symbol><symbol id="18x18_grid" height="18" viewBox="0 0 18 18" width="18"><path d="M10 15v-5h5v5h-5zm0-12h5v5h-5V3zm-7 7h5v5H3v-5zm0-7h5v5H3V3z"></path></symbol><symbol id="18x18_heart" height="18" viewBox="0 0 18 18" width="18"><path d="M11.94 3.51c-1.24 0-2.325.672-2.94 1.68-.615-1.008-1.7-1.68-2.94-1.68-1.92 0-3.477 1.605-3.477 3.584 0 3.45 4.474 4.865 6.417 7.416 1.943-2.55 6.417-3.967 6.417-7.416 0-1.98-1.557-3.584-3.476-3.584z"></path></symbol><symbol id="18x18_ice_cream" height="18" viewBox="0 0 18 18" width="18"><path d="M13.352 5.217l-.125-.072a4.228 4.228 0 0 0-8.453 0l-.126.072c-1.277.737-1.893 2.328-1.284 3.67a2.79 2.79 0 0 0 2.317 1.637l2.42 5.868c.335.81 1.48.81 1.816 0l2.41-5.868a2.788 2.788 0 0 0 2.318-1.636c.61-1.343-.007-2.934-1.284-3.67zm-.255 3.11c-.21.367-.595.586-1.027.586-.076 0-.153-.007-.228-.022l-.866-.16-.61.64a1.88 1.88 0 0 1-2.73 0l-.612-.635-.866.164a1.167 1.167 0 0 1-.228.022 1.17 1.17 0 0 1-1.027-.586c-.33-.57-.133-1.3.436-1.63l.24-.143.794-.46.02-.915A2.616 2.616 0 0 1 9 2.63a2.616 2.616 0 0 1 2.6 2.55l.018.917.795.46.248.142c.57.33.77 1.06.44 1.63z"></path></symbol><symbol id="18x18_info" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17A8 8 0 1 1 9 1a8 8 0 0 1 0 16zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zM8 8h2v5H8V8zm0-3h2v2H8V5z"></path></symbol><symbol id="18x18_key" height="18" viewBox="0 0 18 18" width="18"><path d="M16 7H9.578A4.998 4.998 0 0 0 0 9a4.998 4.998 0 0 0 9.578 2H11v1h2v-1h1v1h2v-1a2 2 0 0 0 0-4zM5 10.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path></symbol><symbol id="18x18_king" height="18" viewBox="0 0 18 18" width="18"><path d="M15.245 13h.505c.483 0 .874.517.874 1s-.39 1-.874 1H2.25c-.483 0-.874-.517-.874-1s.39-1 .874-1h.505C2.318 11.407.262 8.52 1.28 6.954c.356-.55.777-1.204 2.092-1.204 2.265 0 3.504.916 5.628.916s3.363-.916 5.628-.916c1.315 0 1.736.655 2.092 1.204 1.018 1.567-1.038 4.453-1.475 6.046zM5.25 8.75L4.125 9.875 5.25 11l1.125-1.125L5.25 8.75zM9 8.375l-1.5 1.5 1.5 1.5 1.5-1.5-1.5-1.5zm3.75.375l-1.125 1.125L12.75 11l1.125-1.125L12.75 8.75zM9 6.25A1.626 1.626 0 1 1 9 3a1.626 1.626 0 0 1 0 3.25z"></path></symbol><symbol id="18x18_light_bulb" height="18" viewBox="0 0 18 18" width="18"><path d="M11 11.62V14H7v-2.38A5.498 5.498 0 0 1 9 1a5.498 5.498 0 0 1 2 10.62zM8 4a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm3 11.07A1.93 1.93 0 0 1 9.07 17h-.14A1.93 1.93 0 0 1 7 15.07V15h4v.07z"></path></symbol><symbol id="18x18_light_bulb_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M11 11.62V14H7v-2.38A5.498 5.498 0 0 1 9 1a5.498 5.498 0 0 1 2 10.62zM9 2C6.52 2 4.5 4.02 4.5 6.5a4.472 4.472 0 0 0 2.864 4.188l.636.248V13h2v-2.064l.636-.248A4.472 4.472 0 0 0 13.5 6.5C13.5 4.02 11.48 2 9 2zM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm3 9.07A1.93 1.93 0 0 1 9.07 17h-.14A1.93 1.93 0 0 1 7 15.07V15h4v.07z"></path></symbol><symbol id="18x18_lightning_bolt" height="18" viewBox="0 0 18 18" width="18"><path d="M9.456 7.677l1.71-5.58c.077-.258-.25-.44-.427-.24L3.87 9.584a.25.25 0 0 0 .187.416h4.248a.25.25 0 0 1 .24.323l-1.71 5.58c-.078.258.248.44.426.24l6.87-7.727A.25.25 0 0 0 13.944 8H9.695a.25.25 0 0 1-.24-.323z"></path></symbol><symbol id="18x18_like" height="18" viewBox="0 0 18 18" width="18"><path d="M15.98 9.283l-.602 3.2A2 2 0 0 1 13.438 14H6V9h1.203L9 5V2.5c4.11 0 2.5 4.5 2.5 4.5h2.597c1.217 0 2.055 1.078 1.883 2.283zM2 9h3v6H3L2 9z"></path></symbol><symbol id="18x18_like_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M15.98 9.283l-.602 3.2A2 2 0 0 1 13.438 14H6V9h1.203L9 5V2.5c4.738 0 3 4.5 3 4.5h2.097c1.217 0 2.055 1.078 1.883 2.283zm-1.217-.988A.856.856 0 0 0 14.097 8H12a1 1 0 0 1-.933-1.36c.162-.43.475-1.71-.027-2.435-.204-.295-.552-.498-1.04-.608V5a1 1 0 0 1-.088.41l-1.797 4a1 1 0 0 1-.912.59H7v3h6.437c.452 0 .845-.3.964-.735l.6-3.167a1.035 1.035 0 0 0-.234-.803zM2 9h3v6H3L2 9z"></path></symbol><symbol id="18x18_linkedin" height="18" viewBox="0 0 18 18" width="18"><path d="M13 16l.055-4.544c0-1.055.183-2.292-1.263-2.292-1.47 0-1.764 1.105-1.764 2.292v4.542H7V7h3.028l-.004 1.145c.377-.716 1.298-1.47 2.67-1.47C15.55 6.675 16 8.558 16 11.01v4.995L13 16zM3.5 6a2 2 0 1 1-.003-3.998A2 2 0 0 1 3.5 6zM5 16H2V7h3v9z"></path></symbol><symbol id="18x18_list" height="18" viewBox="0 0 18 18" width="18"><path d="M6 14v-2h10v2H6zM6 4h10v2H6V4zm-4 8h2v2H2v-2zm0-4h2v2H2V8zm0-4h2v2H2V4zm12 6H6V8h8v2z"></path></symbol><symbol id="18x18_location" height="18" viewBox="0 0 18 18" width="18"><path d="M1.5 9.203l15-7.703-7.703 15-.614-6.683L1.5 9.203z"></path></symbol><symbol id="18x18_lock" height="18" viewBox="0 0 18 18" width="18"><path d="M13 8V6c0-2.206-1.794-4-4-4S5 3.794 5 6v2H4v8h10V8h-1zM7 6a2 2 0 0 1 4 0v2H7V6z"></path></symbol><symbol id="18x18_lock_tempory" height="18" viewBox="0 0 18 18" width="18"><path d="M13.5 18c-1.956 0-3.605-1.256-4.225-3H3V7h1V5c0-2.206 1.794-4 4-4s4 1.794 4 4v2h1v2.05c.166-.018.33-.05.5-.05a4.5 4.5 0 0 1 0 9zM10 5a2 2 0 0 0-4 0v2h4V5zm3.5 5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zm2 4h-2a.5.5 0 0 1-.5-.5V11a.5.5 0 0 1 1 0v2h1.5a.5.5 0 0 1 0 1z"></path></symbol><symbol id="18x18_mail" height="18" viewBox="0 0 18 18" width="18"><path d="M16.772 13.863l-4.89-4.892 4.862-4.81c.12.257.256.54.256.843v8c0 .31-.087.6-.228.864zM7.812 9.49L1.706 3.383c.33-.24.73-.383 1.168-.383h12c.438 0 .84.144 1.168.382L9.936 9.49a1.505 1.505 0 0 1-2.122 0zM1.12 13.716A2.235 2.235 0 0 1 1 13V5c0-.302.01-.586.13-.843l4.75 4.8-4.76 4.76zm5.985-3.52a2.507 2.507 0 0 0 3.538.002l.527-.524 4.93 4.932a2.182 2.182 0 0 1-1.227.394h-12c-.468 0-.87-.168-1.185-.437L6.583 9.67l.522.527z"></path></symbol><symbol id="18x18_mail_open" height="18" viewBox="0 0 18 18" width="18"><path d="M16.822 15.816l-4.802-4.8L17 7v8c0 .292-.066.567-.178.816zm-15.644 0A1.982 1.982 0 0 1 1 15V7l4.98 4.015-4.802 4.8zM7.823 1.388c.628-.517 1.725-.517 2.354 0L17 7H1l6.823-5.612zm-.59 10.88c.47.472 1.1.732 1.767.732.668 0 1.296-.26 1.768-.732l.545-.546L16.19 16.6c-.333.248-.742.4-1.19.4H3c-.448 0-.857-.152-1.19-.4l4.877-4.878.545.546z"></path></symbol><symbol id="18x18_marker" height="18" viewBox="0 0 18 18" width="18"><path d="M14 7A5 5 0 0 0 4 7c0 1.97 1.15 3.658 2.806 4.472h-.17L9 16l2.363-4.528h-.17C12.85 10.658 14 8.97 14 7zM9 5a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="18x18_medical" height="18" viewBox="0 0 18 18" width="18"><path d="M15 7h-4V3H7v4H3v4h4v4h4v-4h4V7z"></path></symbol><symbol id="18x18_menu" height="18" viewBox="0 0 18 18" width="18"><path d="M14 16H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h3V1h4v1h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2zm1-12c0-.55-.45-1-1-1h-2v2H6V3H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h10c.55 0 1-.45 1-1V4zm-4 7h2v1h-2v-1zm0-2h2v1h-2V9zm0-2h2v1h-2V7zm-6 4h5v1H5v-1zm0-2h5v1H5V9zm0-2h5v1H5V7z"></path></symbol><symbol id="18x18_message" height="18" viewBox="0 0 18 18" width="18"><path d="M2 4v6a2 2 0 0 0 2 2h1v3l4-3h5a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"></path></symbol><symbol id="18x18_mobile" height="18" viewBox="0 0 18 18" width="18"><path d="M12 17H6a2 2 0 0 1-2-2V2C4 .895 5.078-.016 6 0h6a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2zm-3-1a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm4-13a1 1 0 0 0-1-1H6a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V3z"></path></symbol><symbol id="18x18_music" height="18" viewBox="0 0 18 18" width="18"><path d="M7 5v7.692c-.57-.06-1.316.076-2.067.427-1.345.624-2.18 1.68-1.867 2.35.313.672 1.657.71 3 .082 1.19-.554 1.976-1.44 1.93-2.102L8 13.448V8.375l6-2.25v4.567c-.57-.06-1.316.076-2.068.427-1.344.625-2.18 1.68-1.866 2.35.313.672 1.657.71 3.002.082 1.187-.554 1.974-1.44 1.927-2.102l.005-.003V2L7 5z"></path></symbol><symbol id="18x18_nightlife" height="18" viewBox="0 0 18 18" width="18"><path d="M15.55 3.66c.565-.648.105-1.66-.754-1.66H3.204a1 1 0 0 0-.753 1.66L8 9v5H6a1 1 0 0 0 0 2h6a1 1 0 0 0 0-2h-2V9l5.55-5.34zM11 3a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></symbol><symbol id="18x18_nope" height="18" viewBox="0 0 18 18" width="18"><path d="M14.657 3.343A8 8 0 1 0 3.343 14.658 8 8 0 0 0 14.657 3.343zm-.707.707c2.61 2.61 2.717 6.78.335 9.528L4.422 3.715C7.17 1.333 11.34 1.44 13.95 4.05zm-9.9 9.9c-2.61-2.61-2.717-6.78-.335-9.528l9.863 9.863C10.83 16.667 6.66 16.56 4.05 13.95z"></path></symbol><symbol id="18x18_order" height="18" viewBox="0 0 18 18" width="18"><g><path d="M4 4V3h3v1H4m4-2H3v2H2a1 1 0 0 0-1 1v7h9V5a1 1 0 0 0-1-1H8V2" opacity=".502"></path><path d="M17 10.93L15 9.5V4h-5v8H7.49a2.49 2.49 0 0 0-1.99-1 2.49 2.49 0 0 0-1.99 1H1v2h2.05a2.502 2.502 0 0 0 4.9 0h3.1a2.5 2.5 0 0 0 4.9 0H17v-3.07zM5.5 14.75a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5zM12 6h1v3h-1V6zm1.5 8.75a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5z"></path></g></symbol><symbol id="18x18_overflow" height="18" viewBox="0 0 18 18" width="18"><path d="M15 11a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-6 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-6 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path></symbol><symbol id="18x18_paper_plane" height="18" viewBox="0 0 18 18" width="18"><path d="M17 3l-.362.108.016-.016-.026.02L1 7.787l4.407 2.08 7.728-4.128-6.133 5.197-1.488 3.822 2.92-2.374L11 15l6-12z"></path></symbol><symbol id="18x18_pdf" height="18" viewBox="0 0 18 18" width="18"><path d="M3 17H1V1h6v6h6v2h4v8H3zm13-7H4v6h12v-6zm-8 2.39v.22A1.39 1.39 0 0 1 6.61 14H6v1H5v-4h1.61c.77 0 1.39.622 1.39 1.39zM6 13h.61a.39.39 0 0 0 .39-.39v-.22a.39.39 0 0 0-.39-.39H6v1zm6-.45v.9A1.55 1.55 0 0 1 10.45 15H9v-4h1.45c.856 0 1.55.694 1.55 1.55zM10 14h.45a.55.55 0 0 0 .55-.55v-.9a.55.55 0 0 0-.55-.55H10v2zm5.5-2H14v.5h1v1h-1V15h-1v-4h2.5v1zM8 1l5 5H8V1z"></path></symbol><symbol id="18x18_pencil" height="18" viewBox="0 0 18 18" width="18"><path d="M15.96 4.505a2.094 2.094 0 0 0-.577-1.89 2.103 2.103 0 0 0-2.973.002l-1.487 1.487-7.436 7.436L2 16l4.46-1.487 7.437-7.436 1.487-1.487c.308-.308.5-.688.577-1.085zm-10.067 9.09l-2.23.742.743-2.23 7.26-7.26 1.487 1.487-7.26 7.26z"></path></symbol><symbol id="18x18_phone" height="18" viewBox="0 0 18 18" width="18"><path d="M15.862 12.526l-2.91-1.68a.442.442 0 0 0-.486.087l-1.58 1.687a.857.857 0 0 1-.52.232s-1.083.03-3.13-1.985c-2.046-2.015-2.054-3.12-2.054-3.12 0-.17.094-.41.21-.533L6.85 5.656a.49.49 0 0 0 .08-.504L5.295 2.14c-.073-.155-.228-.18-.345-.058L2.26 4.924a1.07 1.07 0 0 0-.248.53s-.34 2.927 3.75 6.955c4.093 4.025 6.96 3.59 6.96 3.59.167-.027.4-.148.516-.27l2.684-2.845c.117-.123.09-.285-.062-.36z"></path></symbol><symbol id="18x18_pin" height="18" viewBox="0 0 18 18" width="18"><path d="M1.142 6.34l5.23-5.21c.293-.29.812-.138.932.274a4.97 4.97 0 0 1 .112 2.303l3.263 3.25a5.825 5.825 0 0 1 3.133.03c.478.14.67.75.333 1.087l-2.328 2.318 5.06 6.077c.21.254.04.67-.22.46l-6.22-5.16-2.328 2.314c-.338.337-.95.144-1.09-.332a5.74 5.74 0 0 1-.03-3.124L3.728 7.38a5.01 5.01 0 0 1-2.313-.112C1 7.148.847 6.632 1.14 6.34z"></path></symbol><symbol id="18x18_plane" height="18" viewBox="0 0 18 18" width="18"><path d="M16.152 8.065l-2.944.977L9.503 7.15l4.455-4.706-.702-.327a1.668 1.668 0 0 0-1.57.087L6.27 5.498 3.9 4.288c-.8-.426-2.547-.446-2.93.375-.383.82.756 2.148 1.596 2.487l2.46 1.097.947 6.206c.085.55.44 1.023.944 1.26l.702.326.724-6.313 3.95 1.763 1.04 2.617.954.445.652-3.373 2.164-2.67-.954-.446z"></path></symbol><symbol id="18x18_play_badged" height="18" viewBox="0 0 18 18" width="18"><path d="M9 16A7 7 0 1 1 9 2a7 7 0 0 1 0 14zM9 3a6 6 0 1 0 0 12A6 6 0 0 0 9 3zM7 6l5 3-5 3V6z"></path></symbol><symbol id="18x18_popular" height="18" viewBox="0 0 18 18" width="18"><path d="M2 4v7a2 2 0 0 0 2 2h1v3l4-3h5a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2zm8.507 5.384C9.743 9.926 9.09 10.69 9.012 11c-.092-.316-.678-1.058-1.503-1.6-.85-.56-2.13-1.083-2.12-2.483-.01-2.288 2.68-2.64 3.62-.445.89-2.108 3.563-1.814 3.61.43.01 1.4-1.28 1.888-2.118 2.482z"></path></symbol><symbol id="18x18_popular_biz" height="18" viewBox="0 0 18 18" width="18"><path d="M15.653 16.216c-.843.598-1.563 1.442-1.65 1.784-.1-.35-.748-1.168-1.658-1.768-.938-.617-2.347-1.195-2.337-2.74-.01-2.527 2.96-2.916 3.994-.492.985-2.327 3.936-2.003 3.986.476.012 1.545-1.414 2.084-2.335 2.74zm-7.648-2.738A3.968 3.968 0 0 0 8.85 16H0v-1h1.998V2h6.996v3h4.997v4.57c-.6-.362-1.28-.56-1.99-.56-1.92 0-3.972 1.565-3.993 4.468zM6.995 4h-3v1h3V4zm0 3h-3v1h3V7zm0 3h-3v1h3v-1zm0 3h-3v1h3v-1zm4.997-6H8.994v1h2.998V7z"></path></symbol><symbol id="18x18_printer" height="18" viewBox="0 0 18 18" width="18"><path d="M14 11v5H4v-5H2V6c0-1.1.9-2 2-2V2h10v2c1.1 0 2 .9 2 2v5h-2zm-1-8H5v2h8V3zm0 5H5v7h8V8zm-1 3H6v-1h6v1zm0 2H6v-1h6v1z"></path></symbol><symbol id="18x18_profile" height="18" viewBox="0 0 18 18" width="18"><path d="M2.002 16h13.996a9.87 9.87 0 0 0-5.66-2.786V12.08c.898-.655 1.733-1.75 1.79-2.46 1.016-.495 1.228-1.723.506-1.994l-.017.024c.326-.458.527-1.04.527-1.706 0-.863-.156-1.66-.79-2.182C11.914 2.72 10.998 2 9.934 2c-.625 0-1.198.25-1.656.664a.955.955 0 0 0-.612-.23c-.4 0-.747.268-.934.662-1.005.37-1.738 1.505-1.738 2.848 0 .615.154 1.186.417 1.66-.78.307-.52 1.477.463 2.015.057.71.89 1.804 1.79 2.46v1.133A9.87 9.87 0 0 0 2.003 16z"></path></symbol><symbol id="18x18_public_service" height="18" viewBox="0 0 18 18" width="18"><path d="M16 9V7h-.778L9 2 2.778 7H2v2h2v5H2v2h14v-2h-2V9h2zM6 9h2v5H6V9zm6 5h-2V9h2v5z"></path></symbol><symbol id="18x18_regular" height="18" viewBox="0 0 18 18" width="18"><path d="M1.714 3.22C1.884 8.75 1.28 12.83 9 16c7.278-2.62 6.435-7.458 6.49-12.605C10.356 1.458 6.845 1.64 1.713 3.22zM7.7 11.67l-1.204-1.225L4.69 8.608l1.204-1.225L7.7 9.22l3.61-3.675 1.2 1.225-4.81 4.9z"></path></symbol><symbol id="18x18_reply" height="18" viewBox="0 0 18 18" width="18"><path d="M2 8.625l7-5v3.55c4 .416 6.676 3.55 7 7.2-1.38-2.5-4-3.962-7-4.2v3.45l-7-5z"></path></symbol><symbol id="18x18_reservation" height="18" viewBox="0 0 18 18" width="18"><path d="M13.6 16H4.4C3.077 16 2 14.88 2 13.5v-9C2 3.12 3.077 2 4.4 2H5a1 1 0 0 1 2 0h4a1 1 0 0 1 2 0h.6C14.923 2 16 3.12 16 4.5v9c0 1.38-1.077 2.5-2.4 2.5zM15 7H3v6.5c0 .828.627 1.5 1.4 1.5h9.2c.773 0 1.4-.672 1.4-1.5V7zm-5 3h3v3h-3v-3z"></path></symbol><symbol id="18x18_review" height="18" viewBox="0 0 18 18" width="18"><path d="M13 3H5c-1.1 0-2 .9-2 2v8c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-1.505 9.643l-2.526-1.55L6.526 12.7 7 9.934 5 7.977l2.766-.404L8.97 4.7l1.264 2.873L13 7.977l-2 1.957.495 2.71z"></path></symbol><symbol id="18x18_search_small" height="18" viewBox="0 0 18 18" width="18"><path d="M15.913 14.224a1.324 1.324 0 0 0-.3-.466h.01l-3.378-3.376a5.49 5.49 0 0 0 .802-2.857 5.523 5.523 0 1 0-5.522 5.52 5.49 5.49 0 0 0 2.856-.8l3.37 3.368.006.003a1.364 1.364 0 0 0 .93.384C15.41 16 16 15.41 16 14.684c0-.163-.032-.317-.086-.46zM7.525 10.94a3.422 3.422 0 0 1-3.418-3.416 3.422 3.422 0 0 1 3.418-3.417 3.422 3.422 0 0 1 3.416 3.417 3.42 3.42 0 0 1-3.413 3.416z"></path></symbol><symbol id="18x18_settings" height="18" viewBox="0 0 18 18" width="18"><path d="M15.91 7.936c.054.348.09.7.09 1.064 0 .363-.036.715-.09 1.063l-2.214.332a4.91 4.91 0 0 1-.386.94l1.33 1.8a7.04 7.04 0 0 1-.684.808l-.013.013c-.25.25-.522.474-.807.682l-1.8-1.33a4.87 4.87 0 0 1-.94.388l-.333 2.215a6.74 6.74 0 0 1-1.05.09h-.025a6.72 6.72 0 0 1-1.05-.09l-.333-2.21a4.912 4.912 0 0 1-.94-.387l-1.8 1.33a6.738 6.738 0 0 1-.808-.683l-.013-.013a7.04 7.04 0 0 1-.684-.808l1.33-1.8a4.974 4.974 0 0 1-.386-.94l-2.215-.333C2.032 9.714 2 9.364 2 9s.036-.716.09-1.064l2.214-.333c.098-.327.226-.642.387-.94l-1.325-1.8a7.05 7.05 0 0 1 1.5-1.503l1.8 1.33c.297-.16.61-.288.94-.386l.333-2.215C8.284 2.032 8.638 2 9 2s.716.036 1.063.09l.332 2.214c.33.098.644.226.94.386l1.8-1.33a7.05 7.05 0 0 1 1.503 1.504l-1.33 1.8c.162.297.29.612.388.94l2.214.332zM9 6.666a2.332 2.332 0 1 0 0 4.666 2.332 2.332 0 0 0 0-4.665z"></path></symbol><symbol id="18x18_share" height="18" viewBox="0 0 18 18" width="18"><path d="M17.714 6.43L13 10.356v-3.03c-1 0-5.097 1.47-6.286 3.62.274-3.08 4.286-5.5 6.286-5.5V2.5l4.714 3.93zM3 4v10h11v-2.5l1-1V15H2V3h8.5l-1 1H3z"></path></symbol><symbol id="18x18_shopping" height="18" viewBox="0 0 18 18" width="18"><path d="M12 5V1H6v4H3v10a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V5h-3zM7 2h4v3H7V2z"></path></symbol><symbol id="18x18_similar" height="18" viewBox="0 0 18 18" width="18"><path d="M16 12l-5 4v-2H8v-4h3V8l5 4zm-9-2L2 6l5-4v2h3v4H7v2z"></path></symbol><symbol id="18x18_speech" height="18" viewBox="0 0 18 18" width="18"><path d="M2 4v6a2 2 0 0 0 2 2h1v3l4-3h5a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"></path></symbol><symbol id="18x18_speech_round" height="18" viewBox="0 0 18 18" width="18"><path d="M9 3C5.41 3 2.5 5.24 2.5 8c0 1.6.98 3.02 2.5 3.936V16l4-3c3.59 0 6.5-2.24 6.5-5S12.59 3 9 3z"></path></symbol><symbol id="18x18_star" height="18" viewBox="0 0 18 18" width="18"><path d="M8.94 1l2.373 5.387 5.187.758-3.75 3.67.928 5.077-4.737-2.907L4.367 16l.885-5.186-3.75-3.67 5.187-.757L8.94 1z"></path></symbol><symbol id="18x18_suitcase" height="18" viewBox="0 0 18 18" width="18"><path d="M14 15V6h2v9h-2zM5 6h1V2h6v4h1v9H5V6zm2 0h4V3H7v3zM2 6h2v9H2V6z"></path></symbol><symbol id="18x18_talk" height="18" viewBox="0 0 18 18" width="18"><path d="M15 13.182V16l-3.377-2.026c-2.198-.133-3.995-1.393-4.482-3.067C9.907 10.46 12 8.432 12 6c2.76 0 5 1.79 5 4 0 1.304-.792 2.452-2 3.182zM6.385 9.97L3 12V9.182C1.792 8.452 1 7.304 1 6c0-2.21 2.24-4 5-4s5 1.79 5 4c0 2.104-2.037 3.81-4.615 3.97z"></path></symbol><symbol id="18x18_target" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zm1 14.415V13a1 1 0 0 0-2 0v2.415A6.505 6.505 0 0 1 2.585 10H5a1 1 0 0 0 0-2H2.585A6.505 6.505 0 0 1 8 2.585V5a1 1 0 0 0 2 0V2.585A6.505 6.505 0 0 1 15.415 8H13a1 1 0 0 0 0 2h2.415A6.505 6.505 0 0 1 10 15.415z"></path></symbol><symbol id="18x18_television" height="18" viewBox="0 0 18 18" width="18"><path d="M14 4.99H8.742l2.072-2.36a.75.75 0 0 0-1.128-.99L7.5 4.132 5.314 1.64a.75.75 0 0 0-1.128.99l2.072 2.36H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2zm-3 7a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v4zm2.5 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm0-3c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"></path></symbol><symbol id="18x18_tennis" height="18" viewBox="0 0 18 18" width="18"><path d="M14.903 9.534a5.716 5.716 0 0 1-3.05 1.605l.004.026a13.69 13.69 0 0 0-4.974 1.554l.163.164-3.712 3.712-1.93-1.93 3.71-3.713.164.163a13.69 13.69 0 0 0 1.555-4.974l.036.004a5.71 5.71 0 0 1 1.593-3.05c1.12-1.12 2.556-1.694 3.918-1.694 1.13 0 2.208.395 3.014 1.2 1.778 1.778 1.557 4.88-.493 6.93zm-7.53-.284a14.8 14.8 0 0 1-1.002 2.38 14.85 14.85 0 0 1 2.39-1.006 3.87 3.87 0 0 1-.786-.596 3.94 3.94 0 0 1-.6-.778zm6.963-5.586c-.63-.63-1.41-.76-1.953-.76-1.018 0-2.06.456-2.857 1.254-1.462 1.462-1.683 3.62-.494 4.81.63.63 1.41.76 1.953.76 1.018 0 2.06-.456 2.857-1.254 1.462-1.462 1.684-3.62.494-4.81zM14 12.616c.827 0 1.5.548 1.5 1.375a1.5 1.5 0 0 1-3 0c0-.824.672-1.372 1.5-1.372z"></path></symbol><symbol id="18x18_ticket" height="18" viewBox="0 0 18 18" width="18"><path d="M11.853 9.563l.707-.707 1.538 1.538 2.892-2.892-2.256-2.256a1.4 1.4 0 0 1-1.98 0 1.4 1.4 0 0 1 0-1.98L10.498 1.01 7.606 3.902 9.144 5.44l-.707.707L6.9 4.61l-5.89 5.888 2.256 2.256a1.4 1.4 0 0 1 1.98 0 1.4 1.4 0 0 1 0 1.98l2.256 2.256 5.89-5.89-1.54-1.537zm-.93-.93L9.366 7.078l.707-.708 1.556 1.556-.71.707z"></path></symbol><symbol id="18x18_tools" height="18" viewBox="0 0 18 18" width="18"><path d="M12.772 8.594c-.337 0-.656-.067-.962-.164l-6.99 7.116a1.472 1.472 0 0 1-2.11 0 1.538 1.538 0 0 1 0-2.15L9.697 6.28a3.34 3.34 0 0 1-.16-.98c0-1.82 1.447-3.294 3.234-3.294.338 0 .657.068.963.165L11.93 4.01l2.11 2.15 1.806-1.837c.095.312.162.637.162.98 0 1.82-1.45 3.294-3.236 3.294zM4.955 6.198L3.54 5.21 1.998 3.64l1.565-1.59 1.54 1.57.905 1.508L7.71 6.86 6.658 7.932 4.955 6.198zm10.006 7.198a1.54 1.54 0 0 1 0 2.15 1.475 1.475 0 0 1-2.11 0l-3.314-3.374 2.11-2.15 3.316 3.374z"></path></symbol><symbol id="18x18_transit" height="18" viewBox="0 0 18 18" width="18"><path d="M14.805 17.212l-2.35-2.362V13h.497c.55 0 .993-.448.993-1V3c0-1.105-.89-2-1.987-2h-.276c-.344-.595-.977-1-1.71-1h-1.99c-.732 0-1.366.405-1.71 1h-.275A1.994 1.994 0 0 0 4.01 3v9c0 .552.444 1 .993 1H5.5v1.85l-2.35 2.362a.464.464 0 0 0 0 .653.457.457 0 0 0 .648 0L6.648 15h.84v-.844L7.64 14h2.67l.156.156V15h.84l2.848 2.865a.457.457 0 0 0 .65 0 .464.464 0 0 0 0-.653zM11.71 11a.997.997 0 0 1-.994-1c0-.552.445-1 .994-1 .548 0 .993.448.993 1s-.445 1-.993 1zM5.003 4c0-.552.445-1 .994-1h5.96c.55 0 .995.448.995 1v4h-7.95V4zm.248 6c0-.552.447-1 .996-1 .55 0 .994.448.994 1s-.446 1-.995 1a.997.997 0 0 1-.994-1z"></path></symbol><symbol id="18x18_trash" height="18" viewBox="0 0 18 18" width="18"><path d="M3 5V3h4V2h4v1h4v2H3zm11 9c0 1.1-.9 2-2 2H6c-1.1 0-2-.9-2-2V6h10v8zM8 8.5a.5.5 0 0 0-.5-.5.5.5 0 0 0-.5.5v5a.5.5 0 0 0 .5.5.5.5 0 0 0 .5-.5v-5zm3 0a.5.5 0 0 0-.5-.5.5.5 0 0 0-.5.5v5a.5.5 0 0 0 .5.5.5.5 0 0 0 .5-.5v-5z"></path></symbol><symbol id="18x18_trending" height="18" viewBox="0 0 18 18" width="18"><path d="M16.2 5h-3.67c-.71 0-1.068.88-.564 1.393l1.268 1.295L9.8 11.192l-4-4.08-4.566 4.657a.828.828 0 0 0 0 1.152.79.79 0 0 0 1.132 0L5.8 9.42l4 4.08 4.566-4.658 1.268 1.294c.504.514 1.366.15 1.366-.577V5.814A.808.808 0 0 0 16.2 5z"></path></symbol><symbol id="18x18_triangle_down" height="18" viewBox="0 0 18 18" width="18"><path d="M9 11.994L4.5 7.008h9L9 11.994z"></path></symbol><symbol id="18x18_twitter" height="18" viewBox="0 0 18 18" width="18"><path d="M16.5 4.42a6.252 6.252 0 0 1-1.768.477 3.05 3.05 0 0 0 1.353-1.677 6.2 6.2 0 0 1-1.954.736A3.095 3.095 0 0 0 11.89 3c-1.7 0-3.077 1.356-3.077 3.03 0 .236.027.467.08.69A8.778 8.778 0 0 1 2.55 3.553a2.982 2.982 0 0 0-.417 1.524c0 1.05.54 1.978 1.37 2.522a3.107 3.107 0 0 1-1.397-.38v.033c0 1.468 1.06 2.692 2.468 2.97a3.134 3.134 0 0 1-1.386.053 3.074 3.074 0 0 0 2.874 2.104 6.233 6.233 0 0 1-3.82 1.298 6.37 6.37 0 0 1-.736-.04A8.81 8.81 0 0 0 6.22 15c5.66 0 8.755-4.616 8.755-8.62 0-.13-.003-.262-.01-.392A6.22 6.22 0 0 0 16.5 4.42z"></path></symbol><symbol id="18x18_unfollow" height="18" viewBox="0 0 18 18" width="18"><path d="M16 14.5L14.5 16 13 14.5 11.5 16 10 14.5l1.5-1.5-1.5-1.5 1.5-1.5 1.5 1.5 1.5-1.5 1.5 1.5-1.5 1.5 1.5 1.5zm-8.925.883c-.443.817-1.707.817-2.15 0L2.128 9.605C1.728 8.868 2.31 8 3.203 8h5.594c.893 0 1.474.868 1.075 1.605l-2.797 5.778zM6 7a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="18x18_unknown" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1C4.58 1 1 4.58 1 9s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm0 12.75a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5zm1.76-5.76c-.14.14-.3.28-.44.4-.12.09-.25.19-.32.29-.11.13-.18.4-.18.57 0 .23-.1.46-.27.63a.75.75 0 0 1-.55.24c-.48 0-.83-.45-.83-.86-.01-.54.19-1.1.52-1.5.19-.23.4-.42.54-.53.11-.1.21-.18.28-.27.35-.37.36-.94.03-1.29-.14-.15-.37-.22-.62-.22-.25.01-.48.11-.6.27a.42.42 0 0 0-.09.27c0 .43-.38.78-.83.78-.46 0-.83-.35-.83-.78 0-.44.14-.85.41-1.2.42-.55 1.1-.88 1.86-.91.77-.04 1.47.24 1.94.74.44.47.65 1.06.65 1.67 0 .61-.22 1.22-.67 1.7z"></path></symbol><symbol id="18x18_unknown_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17A8 8 0 1 1 9 1a8 8 0 0 1 0 16zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1.32 6.39c-.12.09-.25.19-.32.29-.11.13-.18.4-.18.57 0 .23-.1.46-.27.63a.75.75 0 0 1-.55.24c-.48 0-.83-.45-.83-.86-.01-.54.19-1.1.52-1.5.19-.23.4-.42.54-.53.11-.1.21-.18.28-.27.35-.37.36-.94.03-1.29-.14-.15-.37-.22-.62-.22-.25.01-.48.11-.6.27a.42.42 0 0 0-.09.27c0 .43-.38.78-.83.78-.46 0-.83-.35-.83-.78 0-.44.14-.85.41-1.2.42-.55 1.1-.88 1.86-.91.77-.04 1.47.24 1.94.74.44.47.65 1.06.65 1.67 0 .61-.22 1.22-.67 1.7-.14.14-.3.28-.44.4zM9 11.25a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5z"></path></symbol><symbol id="18x18_unlock" height="18" viewBox="0 0 18 18" width="18"><path d="M12 1.91c-2.206 0-4 1.88-4 4.188V8H2v8h9V8h-1V6.098c0-1.206.897-2.187 2-2.187s2 .984 2 2.19v2.99a1 1 0 0 0 2 0V6.1c0-2.31-1.794-4.187-4-4.187z"></path></symbol><symbol id="18x18_update" height="18" viewBox="0 0 18 18" width="18"><path d="M15.25 9A6.257 6.257 0 0 1 9 15.25a6.19 6.19 0 0 1-4.52-1.942l1.084-1.035A4.705 4.705 0 0 0 9 13.75c2.62 0 4.75-2.13 4.75-4.75H11.5l3-3 3 3h-2.25zM9 4.25C6.38 4.25 4.25 6.38 4.25 9H6.5l-3 3-3-3h2.25A6.257 6.257 0 0 1 9 2.75c1.723 0 3.33.69 4.52 1.942l-1.085 1.035A4.7 4.7 0 0 0 9 4.25z"></path></symbol><symbol id="18x18_useful" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-.003-2.003h.006A1.997 1.997 0 0 0 11 13H7c0 1.103.894 1.997 1.997 1.997zM9 2.947a4 4 0 0 0-4 4c0 1.477.81 2.752 2 3.445V12h4v-1.608c1.19-.693 2-1.968 2-3.445a4 4 0 0 0-4-4zM8 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5z"></path></symbol><symbol id="18x18_useful_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M9 17c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM9 2C5.14 2 2 5.14 2 9s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm2 8.392V12H7v-1.608a3.982 3.982 0 0 1-2-3.445 4 4 0 0 1 8 0c0 1.477-.81 2.752-2 3.445zM8 5.25a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5zm1.003 9.747h-.006A1.997 1.997 0 0 1 7 13h4a1.997 1.997 0 0 1-1.997 1.997z"></path></symbol><symbol id="18x18_video" height="18" viewBox="0 0 18 18" width="18"><path d="M13 11.095v-4.19L17 4.2v9.6l-4-2.705zM10 15H3a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2z"></path></symbol><symbol id="18x18_warning" height="18" viewBox="0 0 18 18" width="18"><path d="M9 1a8 8 0 1 0 0 16A8 8 0 0 0 9 1zM8 5a1 1 0 0 1 2 0v4a1 1 0 0 1-2 0V5zm1 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path></symbol><symbol id="18x18_write_more" height="18" viewBox="0 0 18 18" width="18"><path d="M9 18v-8h8v8H9zm6-5h-1v-1a1 1 0 0 0-2 0v1h-1a1 1 0 0 0 0 2h1v1a1 1 0 0 0 2 0v-1h1a1 1 0 0 0 0-2zm-3.644-4l1.43-1.4-2.536-.37-.82-.12-.336-.76L7.972 3.8 6.915 6.326l-.328.782-.84.123-2.533.37L5.05 9.398l.56.55-.13.774-.364 2.128 1.996-1.315.04-.027.043-.024.805-.458v1.727l-.062.035L3.056 16 4 10.47 0 6.553l5.53-.808L7.94 0l2.53 5.746 5.53.808L13.5 9h-2.144z"></path></symbol><symbol id="24x24_activity" height="24" viewBox="0 0 24 24" width="24"><path d="M12.5 19h-.048a1 1 0 0 1-.9-.684l-3.108-9.32-2.007 5.356A1 1 0 0 1 5.5 15H3a1 1 0 0 1 0-2h1.807l2.756-7.35a1 1 0 0 1 1.886.035l3.18 9.552 2.953-6.643a1.002 1.002 0 0 1 1.843.034L19.176 13H21a1 1 0 0 1 0 2h-2.5c-.41 0-.776-.25-.93-.63l-1.12-2.8-3.036 6.836A1 1 0 0 1 12.5 19z"></path></symbol><symbol id="24x24_activity_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12.5 20h-.025c-.206 0-.397-.407-.456-.612L8.49 6.92l-2.01 6.784c-.063.213-.258.297-.48.297H2a.5.5 0 0 1 0-1h3.626L8.02 4.86a.5.5 0 0 1 .48-.36c.197-.042.42.148.48.363l3.6 12.593 3.456-8.64c.078-.197.27-.306.48-.316a.5.5 0 0 1 .46.342L18.36 13H22a.5.5 0 0 1 0 1h-4a.502.502 0 0 1-.475-.342l-1.068-3.205-3.493 8.982c-.076.19-.26.565-.464.565z"></path></symbol><symbol id="24x24_add" height="24" viewBox="0 0 24 24" width="24"><path d="M21 13h-8v8h-2v-8H3v-2h8V3h2v8h8v2z"></path></symbol><symbol id="24x24_add_biz" height="24" viewBox="0 0 24 24" width="24"><path d="M22 21v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-6-1c0 .34.03.68.1 1H1V5c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2v12h2V9c0-1.1.9-2 2-2h2c1.1 0 2 .9 2 2v6.41c-1.76.78-3 2.54-3 4.59zM5 6H3v2h2V6zm0 4H3v2h2v-2zm0 4H3v2h2v-2zm4-8H7v2h2V6zm0 4H7v2h2v-2zm0 4H7v2h2v-2zm8-4h-2v2h2v-2zm0 4h-2v2h2v-2z"></path></symbol><symbol id="24x24_add_biz_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M22 22v2h-1v-2h-2v-1h2v-2h1v2h2v1h-2zM0 5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v12h2V9a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v12H0V5zm1 15h16V9c0-.55-.45-1-1-1h-2c-.55 0-1 .45-1 1v9H9V5c0-.55-.45-1-1-1H2c-.55 0-1 .45-1 1v15zM4 8H2V6h2v2zm0 4H2v-2h2v2zm0 4H2v-2h2v2zm4-8H6V6h2v2zm0 4H6v-2h2v2zm0 4H6v-2h2v2zm8-4h-2v-2h2v2zm0 4h-2v-2h2v2z"></path></symbol><symbol id="24x24_add_calendar" height="24" viewBox="0 0 24 24" width="24"><path d="M21 21v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-2-5.9V8H5v10c0 .55.45 1 1 1h9.1a4.995 4.995 0 0 0 0 2H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v9.1a4.995 4.995 0 0 0-2 0z"></path></symbol><symbol id="24x24_add_event" height="24" viewBox="0 0 24 24" width="24"><path d="M21 21v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-7.634-5.277L12 18l-1.366-2.277a3.5 3.5 0 1 1 2.732 0zM12 11.25a1.25 1.25 0 1 0 0 2.5 1.25 1.25 0 0 0 0-2.5zm7 3.85V8H5v10c0 .55.45 1 1 1h9.1a4.995 4.995 0 0 0 0 2H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v9.1a4.995 4.995 0 0 0-2 0z"></path></symbol><symbol id="24x24_add_friend" height="24" viewBox="0 0 24 24" width="24"><g><path d="M8.824 13.817l-2.482 5.946c-.69 1.65-2.995 1.65-3.684 0L.176 13.817C-.382 12.48.586 11 2.018 11h4.964c1.432 0 2.4 1.48 1.842 2.817zM4.5 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"></path><path d="M22 21v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-2.24-5.84a5 5 0 0 0-3.66 5.83c-.78.04-1.58-.37-1.94-1.23l-2.48-5.94c-.56-1.34.41-2.82 1.84-2.82h4.96c1.43 0 2.4 1.48 1.84 2.82l-.56 1.34zM16 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" opacity=".502"></path><path d="M24 19h-2v-2h-2v2h-2v2h2v2h2v-2h2v-2z"></path></g></symbol><symbol id="24x24_add_friend_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M22.01 22v2h-1.002v-2h-2.002v-1h2.002v-2h1v2h2.003v1h-2zm-5.664-2.237A1.974 1.974 0 0 1 14.502 21c-.75 0-1.5-.412-1.844-1.237l-2.486-5.946C9.614 12.48 10.582 11 12.016 11h4.97c1.434 0 2.403 1.48 1.845 2.817l-2.48 5.946zm1.47-7.316a.972.972 0 0 0-.82-.447h-4.98a.982.982 0 0 0-.826.447c-.197.296-.23.655-.094.984l2.486 5.95a.98.98 0 0 0 .92.62.98.98 0 0 0 .92-.62l2.487-5.943a1.03 1.03 0 0 0-.098-.985zM14.503 9A3.002 3.002 0 0 1 11.5 6a3 3 0 0 1 3.003-3 3.002 3.002 0 0 1 3.003 3c0 1.657-1.345 3-3.003 3zm0-5A2.003 2.003 0 0 0 12.5 6a2.003 2.003 0 0 0 4.004 0c0-1.103-.898-2-2.002-2zm-8.17 15.763A1.973 1.973 0 0 1 4.49 21c-.75 0-1.5-.412-1.844-1.237L.16 13.817C-.397 12.48.57 11 2.006 11h4.97c1.434 0 2.403 1.48 1.844 2.817l-2.486 5.946zm1.473-7.316A.974.974 0 0 0 6.984 12h-4.98a.98.98 0 0 0-.825.447 1.028 1.028 0 0 0-.1.984l2.486 5.95a.98.98 0 0 0 .92.626.98.98 0 0 0 .92-.622l2.49-5.947c.136-.33.104-.69-.093-.985zM4.49 9a3 3 0 0 1 0-6 3 3 0 0 1 0 6zm0-5a2.003 2.003 0 0 0-2.002 2 2.003 2.003 0 0 0 4.004 0c0-1.103-.898-2-2.002-2z"></path></symbol><symbol id="24x24_add_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21 11.5h-8.5V3a.5.5 0 0 0-1 0v8.5H3a.5.5 0 0 0 0 1h8.5V21a.5.5 0 0 0 1 0v-8.5H21a.5.5 0 0 0 0-1z"></path></symbol><symbol id="24x24_add_photo" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H5a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3h2.184A2.99 2.99 0 0 1 10 4h4a2.99 2.99 0 0 1 2.816 2H19a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3zM12.005 8.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9zM13 14v1a1 1 0 0 1-2 0v-1h-1a1 1 0 0 1 0-2h1v-1a1 1 0 0 1 2 0v1h1a1 1 0 0 1 0 2h-1z"></path></symbol><symbol id="24x24_add_photo_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H5a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3h2.184A2.99 2.99 0 0 1 10 4h4a2.99 2.99 0 0 1 2.816 2H19a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3zm2-11c0-1.103-.897-2-2-2h-2.89l-.236-.665A1.998 1.998 0 0 0 14 5h-4c-.837 0-1.59.536-1.874 1.335L7.89 7H5c-1.103 0-2 .897-2 2v8c0 1.103.897 2 2 2h14c1.103 0 2-.897 2-2V9zm-8.995 8.5a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9zm0-8c-1.93 0-3.5 1.57-3.5 3.5s1.57 3.5 3.5 3.5 3.5-1.57 3.5-3.5-1.57-3.5-3.5-3.5zm.493 5.5h-.996v-1.502H10v-.996h1.502V11h.996v1.502H14v.996h-1.502V15z"></path></symbol><symbol id="24x24_ages_allowed" height="24" viewBox="0 0 24 24" width="24"><path d="M20 19H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2zm0-12H4v10h16V7zm-8 5.8c1.617 0 2.94 1.295 3.052 3.2H8.948c.11-1.905 1.435-3.2 3.052-3.2zm0-.8a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path></symbol><symbol id="24x24_alignment_suspension_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M19.965 4.635a.5.5 0 0 0-.693.142l-1.63 2.47a52.3 52.3 0 0 0-1.707-1.13 53.35 53.35 0 0 1-1.627-1.077l1.74-2.637a.5.5 0 1 0-.836-.55l-.64.972c-1.455-.522-2.654-.826-3.025-.038-.38.812.273 1.632 1.396 2.504l-.45.69c-1.472-.53-2.69-.842-3.064-.05-.39.82.28 1.65 1.42 2.53l-.578.876c-1.4-.495-2.543-.76-2.903.007-.37.787.237 1.58 1.3 2.425L6.972 14.34l2.086 1.376-1.68 2.547a3 3 0 0 0-3.71 1.085.5.5 0 1 0 .832.553 2 2 0 1 1 3.34 2.208.5.5 0 0 0 .834.55 3 3 0 0 0-.46-3.837l1.68-2.55 2.084 1.378.777-1.175a4.14 4.14 0 0 0 1.533.395 1.326 1.326 0 0 0 .507-.088.893.893 0 0 0 .514-.55c.178-.618-.25-1.2-1.13-1.906l.79-1.198a3.893 3.893 0 0 0 1.377.327 1.326 1.326 0 0 0 .505-.087.893.893 0 0 0 .51-.55c.167-.584-.214-1.14-1.006-1.797l.692-1.048a3.936 3.936 0 0 0 1.415.344 1.326 1.326 0 0 0 .507-.087.893.893 0 0 0 .513-.55c.17-.59-.225-1.157-1.038-1.82l1.664-2.527a.5.5 0 0 0-.146-.692zM12.437 3.3a5.198 5.198 0 0 1 1.565.386l-.502.76c-.594-.46-1.05-.888-1.063-1.145zm-2.12 3.138a5.407 5.407 0 0 1 1.606.4l-.51.77c-.61-.47-1.08-.91-1.095-1.17zm-2.05 3.41a5.21 5.21 0 0 1 1.444.343l-.47.73c-.544-.43-.95-.82-.964-1.07zm3.435 6.404l-3.34-2.203 1.12-1.7c.533.37 1.127.75 1.744 1.15.465.293 1.052.672 1.594 1.05zm2.626-.39a3.252 3.252 0 0 1-1.005-.25l.304-.462a2.594 2.594 0 0 1 .7.71zm-2.562-3.2a50.913 50.913 0 0 1-1.73-1.15L11.67 9.04c.497.34 1.042.692 1.607 1.054a51.32 51.32 0 0 1 1.73 1.148l-1.635 2.478a56.85 56.85 0 0 0-1.606-1.058zm4.613-.21a2.997 2.997 0 0 1-.85-.19l.27-.416a2.198 2.198 0 0 1 .57.605zm-2.57-3.2A53.925 53.925 0 0 1 12.22 8.2l1.53-2.32c.507.35 1.064.707 1.64 1.078.497.317 1.13.725 1.7 1.124l-1.534 2.325a50.688 50.688 0 0 0-1.74-1.155zm4.68.062a3.016 3.016 0 0 1-.888-.202l.283-.43a2.3 2.3 0 0 1 .603.632z"></path></symbol><symbol id="24x24_amazon" height="24" viewBox="0 0 24 24" width="24"><path d="M19.818 23.2c-.164.135-.318.063-.246-.117.238-.594.77-1.924.52-2.247-.254-.323-1.668-.153-2.303-.076-.2.022-.23-.146-.05-.268 1.12-.792 2.97-.563 3.19-.298.21.268-.06 2.12-1.12 3.005zm-3.557-3.88v-.007a.56.56 0 0 1-.64.064c-.902-.752-1.064-1.1-1.56-1.813-1.49 1.52-2.55 1.977-4.48 1.977-2.29 0-4.07-1.41-4.07-4.23 0-2.21 1.195-3.71 2.9-4.444 1.476-.65 3.537-.764 5.114-.942v-.35c0-.65.05-1.414-.33-1.973-.332-.5-.967-.706-1.526-.706-1.04 0-1.96.533-2.187 1.633-.047.244-.226.49-.47.5l-2.646-.29c-.22-.05-.47-.23-.404-.57C6.56 4.967 9.45 4 12.034 4c1.325 0 3.056.352 4.098 1.353 1.322 1.236 1.195 2.885 1.195 4.68v4.24c0 1.272.52 1.83 1.02 2.52.173.244.21.54-.01.72a126.62 126.62 0 0 0-2.086 1.806zm-2.74-7.226c-1.964 0-4.042.42-4.042 2.738 0 1.176.61 1.972 1.653 1.972.765 0 1.45-.47 1.883-1.237.535-.942.51-1.825.51-2.885v-.588zm5.47 9.218c.336-.142.61.22.29.46C17.3 23.228 14.447 24 11.987 24c-3.45 0-6.558-1.274-8.9-3.396-.19-.167-.02-.394.2-.265 2.53 1.47 5.67 2.36 8.902 2.36a17.74 17.74 0 0 0 6.793-1.39z"></path></symbol><symbol id="24x24_ambience" height="24" viewBox="0 0 24 24" width="24"><path d="M12 23c-4.963 0-9-4.037-9-9 0-3.91 2.51-7.235 6-8.475V2a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3.525c3.49 1.24 6 4.565 6 8.475 0 4.963-4.037 9-9 9zM9.5 13c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zM11 7.08V12h2V7.08A7.014 7.014 0 0 0 12 7c-.34 0-.673.033-1 .08zM13.5 14c0 .55.45 1 1 1s1-.45 1-1-.45-1-1-1-1 .45-1 1zm.5-6.706V12h.5a2 2 0 1 1-2 2c0-.366.106-.705.277-1h-1.554c.17.295.277.634.277 1a2 2 0 1 1-2-2h.5V7.294A7 7 0 0 0 12 21a7 7 0 0 0 2-13.706z"></path></symbol><symbol id="24x24_android" height="24" viewBox="0 0 24 24" width="24"><path d="M7 17.01c0 .457.375.998.833.998H8v2.745C8 21.443 8.308 22 9 22s1-.557 1-1.247V18h4v2.753c0 .69.308 1.247 1 1.247s1-.557 1-1.247v-2.745h.167c.458 0 .833-.54.833-.998V9.025H7v7.985zM5 8.692c-.692 0-1 .558-1 1.248v4.822c0 .69.308 1.248 1 1.248s1-.557 1-1.248V9.94c0-.69-.308-1.248-1-1.248zm14 0c-.692 0-1 .558-1 1.248v4.822c0 .69.308 1.248 1 1.248s1-.557 1-1.248V9.94c0-.69-.308-1.248-1-1.248zm-4.058-4.774l1.083-1.123a.435.435 0 0 0 0-.61.413.413 0 0 0-.592-.012L14.2 3.4a4.87 4.87 0 0 0-2.2-.53c-.8 0-1.55.19-2.217.523l-1.24-1.23a.413.413 0 0 0-.593-.002.41.41 0 0 0 0 .59l1.092 1.174C7.808 4.834 7 6.004 7 8h10c0-1.996-.808-3.175-2.058-4.082zM11 6.03h-1v-.998h1v.998zm3 0h-1v-.998h1v.998z"></path></symbol><symbol id="24x24_apple" height="24" viewBox="0 0 24 24" width="24"><path d="M17.028 11.613a4.21 4.21 0 0 0 2.472 3.894c-.014.068-.38 1.392-1.286 2.737-.757 1.184-1.55 2.34-2.81 2.362-1.225.03-1.637-.753-3.04-.753-1.418 0-1.857.732-3.03.783-1.202.046-2.12-1.264-2.904-2.437-1.57-2.398-2.79-6.754-1.152-9.717.793-1.454 2.24-2.39 3.787-2.415 1.2-.027 2.316.847 3.055.847.724 0 2.103-1.045 3.524-.89.595.02 2.288.247 3.38 1.91-.088.056-2.016 1.24-1.996 3.676zm-5.052-5.806c-.135-1.097.385-2.264.968-2.975.658-.808 1.802-1.427 2.716-1.47.12 1.14-.312 2.264-.944 3.09-.66.813-1.714 1.435-2.74 1.355z"></path></symbol><symbol id="24x24_arrow_down" height="24" viewBox="0 0 24 24" width="24"><path d="M5 11l7 8 7-8h-4V5H9v6H5z"></path></symbol><symbol id="24x24_arrow_up" height="24" viewBox="0 0 24 24" width="24"><path d="M19 13l-7-8-7 8h4v6h6v-6h4z"></path></symbol><symbol id="24x24_auto_repair" height="24" viewBox="0 0 24 24" width="24"><path d="M19 15v-1h1V9c0-.786-.458-1.46-1.117-1.786l-.757-4.544A1.995 1.995 0 0 0 16.153 1H7.847c-.982 0-1.812.703-1.972 1.672l-.758 4.542A1.99 1.99 0 0 0 4 9v5h1v1H2v2h9v6h2v-6h9v-2h-3zM16.153 3l.667 4H7.18l.667-4h8.306zM7 11a1.25 1.25 0 1 1 0-2.5A1.25 1.25 0 0 1 7 11zm9 4H8v-1h8v1zm1-4a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5z"></path></symbol><symbol id="24x24_back" height="24" viewBox="0 0 24 24" width="24"><path d="M13 17c-1.103 0-2-.898-2-2v-5h4l-5-5-5 5h4v5c0 2.206 1.794 4 4 4h6v-2h-6z"></path></symbol><symbol id="24x24_badge" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zM8.375 13.917c-.05-.094-.084-.253-.104-.444-.06-.58.02-1.455.19-1.73.08-.128.2-.196.33-.19.087 0 .163.028 1.856.737l.496.204c.178.068.288.257.275.47-.01.207-.13.37-.303.416l-.7.228c-1.577.516-1.628.53-1.71.526a.37.37 0 0 1-.315-.217zm3.902 1.292c-.005 1.67-.007 1.73-.035 1.81a.37.37 0 0 1-.298.232c-.422.072-1.74-.42-2.014-.75a.388.388 0 0 1-.097-.22.322.322 0 0 1 .018-.155c.03-.084.08-.148 1.27-1.564l.35-.415c.12-.15.33-.198.525-.12.19.074.307.24.297.42l-.006.752zm-.284-3.52c-.087.023-.348.103-.666-.42 0 0-2.165-3.457-2.215-3.56-.032-.12.008-.258.11-.37.325-.337 2.072-.834 2.528-.72a.38.38 0 0 1 .288.27c.027.15.24 3.355.27 4.073.03.614-.23.697-.315.724zm2.924 4.742a.364.364 0 0 1-.374-.04c-.066-.054-.137-.164-1.072-1.705l-.27-.46a.46.46 0 0 1 .05-.545c.127-.16.32-.22.485-.155l.7.237c1.576.524 1.627.545 1.69.594a.384.384 0 0 1 .13.365c-.062.43-.93 1.552-1.33 1.714zm1.33-4.828a.423.423 0 0 1-.182.35c-.166.117-2.228.6-2.47.647-.245.05-.386-.046-.503-.225-.11-.174-.107-.375.008-.515l.442-.607c.958-1.33 1.016-1.4 1.086-1.445.11-.078.26-.08.395-.018.378.19 1.223 1.35 1.223 1.797v.013z"></path></symbol><symbol id="24x24_baron" height="24" viewBox="0 0 24 24" width="24"><path d="M22.02 11.95L22 12l-2 4h.33a1 1 0 0 1 0 2H3.67a1 1 0 0 1 0-2H4l-2-4-.02-.05c-.87-2.17.97-4.46 3.28-4.07l1.33.22c3.58.6 7.24.6 10.82 0l1.33-.22c2.31-.39 4.15 1.9 3.28 4.07zM6 12c-.55 0-1 .45-1 1 0 .56.45 1 1 1s1-.44 1-1c0-.55-.45-1-1-1zm4 0c-.55 0-1 .45-1 1 0 .56.45 1 1 1s1-.44 1-1c0-.55-.45-1-1-1zm4 0c-.55 0-1 .45-1 1 0 .56.45 1 1 1s1-.44 1-1c0-.55-.45-1-1-1zm4 0c-.55 0-1 .45-1 1 0 .56.45 1 1 1s1-.44 1-1c0-.55-.45-1-1-1zm-6-4a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path></symbol><symbol id="24x24_bars" height="24" viewBox="0 0 24 24" width="24"><path d="M18.05 21H16V3h4v18h-1.95zM10 8h4v13h-4V8zm-6 5h4v8H4v-8z"></path></symbol><symbol id="24x24_beauty" height="24" viewBox="0 0 24 24" width="24"><path d="M21.7 2.3c-.34-.33-.86-.39-1.26-.13L9.614 9.262A4.478 4.478 0 0 0 6.5 8c-2.386 0-4.318 1.862-4.47 4.21A5.11 5.11 0 0 0 0 13.924l1.546 1.144c.2-.296.478-.607.802-.835A4.502 4.502 0 0 0 6.5 17c.19 0 .372-.033.556-.056-.023.184-.056.366-.056.556a4.5 4.5 0 0 0 9 0 4.48 4.48 0 0 0-1.262-3.114L21.83 3.56c.26-.4.2-.92-.13-1.26zM6.5 15C5.122 15 4 13.88 4 12.5S5.122 10 6.5 10 9 11.12 9 12.5 7.878 15 6.5 15zm5 5C10.12 20 9 18.878 9 17.5s1.12-2.5 2.5-2.5c1.378 0 2.5 1.122 2.5 2.5S12.878 20 11.5 20zm1.56-6.706A4.457 4.457 0 0 0 11.5 13c-.19 0-.372.033-.556.056.023-.184.056-.366.056-.556a4.46 4.46 0 0 0-.294-1.56l6.824-4.47-4.47 6.824z"></path></symbol><symbol id="24x24_bed" height="24" viewBox="0 0 24 24" width="24"><path d="M20 20v-3H4v3H2V6h2v8h18v6h-2zM10 8h10a2 2 0 0 1 2 2v3H10V8zm-5 3a2 2 0 0 1 4 0v2H5v-2z"></path></symbol><symbol id="24x24_bicycle" height="24" viewBox="0 0 24 24" width="24"><path d="M19.5 11c-.086 0-.167.02-.252.025l-1.58-5.566A2.007 2.007 0 0 0 15.742 4H13v2l2.743.002.605 2.13a8.886 8.886 0 0 0-5.146 4.637L9.067 8H11V6H5v2h1.876l3.134 7H8.95c-.252-2.247-2.136-4-4.45-4a4.5 4.5 0 0 0 0 9c1.956 0 3.605-1.256 4.224-3h2.18l.183.408a1 1 0 0 0 1.826-.816l-.642-1.434a7.12 7.12 0 0 1 4.555-5.35l.503 1.774C15.948 12.35 15 13.807 15 15.5a4.5 4.5 0 1 0 4.5-4.5zm-15 7.25a2.754 2.754 0 0 1-2.75-2.75 2.754 2.754 0 0 1 2.75-2.75 2.754 2.754 0 0 1 2.75 2.75 2.754 2.754 0 0 1-2.75 2.75zm15 0a2.754 2.754 0 0 1-2.75-2.75 2.754 2.754 0 0 1 2.75-2.75 2.754 2.754 0 0 1 2.75 2.75 2.754 2.754 0 0 1-2.75 2.75z"></path></symbol><symbol id="24x24_billiards" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-15a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm1.98 5.27c.187.25.28.556.28.92 0 .307-.062.574-.185.8a1.68 1.68 0 0 1-.49.56 2.2 2.2 0 0 1-.694.334c-.25.074-.52.11-.79.11-.28 0-.55-.033-.81-.102a2.102 2.102 0 0 1-.7-.325 1.67 1.67 0 0 1-.49-.562 1.65 1.65 0 0 1-.185-.808c0-.368.095-.676.285-.923.19-.247.457-.413.804-.495v-.02a1.066 1.066 0 0 1-.637-.44 1.32 1.32 0 0 1-.215-.75c0-.26.058-.49.173-.688a1.62 1.62 0 0 1 .45-.496 1.98 1.98 0 0 1 .624-.296c.23-.067.463-.1.7-.1.356 0 .66.055.905.164.25.11.448.244.6.4.15.16.26.325.325.504a1.344 1.344 0 0 1-.11 1.233 1.16 1.16 0 0 1-.63.46v.02c.344.078.61.24.797.49zm-1.055-1.84a.704.704 0 0 0-.392-.465 1.01 1.01 0 0 0-.44-.083c-.116 0-.228.018-.336.054a.89.89 0 0 0-.284.152.7.7 0 0 0-.194.248.794.794 0 0 0-.07.346c0 .248.08.436.26.565a1 1 0 0 0 .62.194.967.967 0 0 0 .61-.19c.165-.13.247-.31.247-.56 0-.076-.01-.16-.03-.25zm.086 2.342a.95.95 0 0 0-.52-.482 1.085 1.085 0 0 0-.38-.066c-.286 0-.528.08-.726.235-.2.15-.297.38-.297.68a.966.966 0 0 0 .3.71.94.94 0 0 0 .328.2 1.15 1.15 0 0 0 .79 0 .957.957 0 0 0 .313-.2.87.87 0 0 0 .21-.31c.05-.12.074-.25.074-.4a.876.876 0 0 0-.08-.376z"></path></symbol><symbol id="24x24_biz" height="24" viewBox="0 0 24 24" width="24"><path d="M21 9a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v8h-2V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v16h18V9zM7 16H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V6h2v2zm4 8H9v-2h2v2zm0-4H9v-2h2v2zm0-4H9V6h2v2zm8 8h-2v-2h2v2zm0-4h-2v-2h2v2z"></path></symbol><symbol id="24x24_bizhouse" height="24" viewBox="0 0 24 24" width="24"><path d="M19.125 13.375a2.874 2.874 0 0 1-2.375-1.257 2.874 2.874 0 0 1-4.75 0 2.873 2.873 0 0 1-4.75 0A2.873 2.873 0 0 1 2 10.5c0-.054.01-.107.026-.158l2-6A.5.5 0 0 1 4.5 4h15c.215 0 .406.138.475.342l2 6c.016.05.025.104.025.158a2.88 2.88 0 0 1-2.875 2.875zm-9.5 1A3.86 3.86 0 0 0 12 13.56a3.86 3.86 0 0 0 2.375.815 3.86 3.86 0 0 0 2.375-.815 3.853 3.853 0 0 0 2.25.804V20h-5v-4h-4v4H5v-5.636a3.853 3.853 0 0 0 2.25-.804 3.86 3.86 0 0 0 2.375.815z"></path></symbol><symbol id="24x24_bizhouse_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.975 10.342l-2-6A.502.502 0 0 0 19.5 4h-15a.5.5 0 0 0-.474.342l-2 6A.498.498 0 0 0 2 10.5a2.88 2.88 0 0 0 2.875 2.875c.043 0 .082-.014.125-.016V20h5v-4h4v4h5v-6.64c.043 0 .082.015.125.015A2.88 2.88 0 0 0 22 10.5a.527.527 0 0 0-.025-.158zM18 19h-3v-4H9v4H6v-5.876a2.872 2.872 0 0 0 1.25-1.006 2.873 2.873 0 0 0 4.75 0 2.873 2.873 0 0 0 4.75 0c.307.45.746.79 1.25 1.006V19zm1.125-6.625A1.877 1.877 0 0 1 17.25 10.5a.5.5 0 0 0-1 0c0 1.034-.84 1.875-1.875 1.875A1.877 1.877 0 0 1 12.5 10.5a.5.5 0 0 0-1 0c0 1.034-.84 1.875-1.875 1.875A1.877 1.877 0 0 1 7.75 10.5a.5.5 0 0 0-1 0c0 1.034-.84 1.875-1.875 1.875A1.88 1.88 0 0 1 3 10.575L4.86 5h14.28l1.858 5.576c-.04 1-.865 1.8-1.873 1.8z"></path></symbol><symbol id="24x24_bone" height="24" viewBox="0 0 24 24" width="24"><path d="M16.956 14.106l-7.07-7.07A2.5 2.5 0 0 0 6.35 3.498a2.49 2.49 0 0 0-.698 2.13 2.493 2.493 0 0 0-2.13.697A2.5 2.5 0 0 0 7.057 9.86l7.07 7.07a2.5 2.5 0 0 0 3.536 3.538 2.49 2.49 0 0 0 .698-2.13 2.49 2.49 0 0 0 2.134-.7 2.5 2.5 0 1 0-3.536-3.534z"></path></symbol><symbol id="24x24_book" height="24" viewBox="0 0 24 24" width="24"><path d="M9.994 18H19v1H9.993v-1zm7.004-1H8.493c-.827 0-1.5.673-1.5 1.5s.673 1.5 1.5 1.5h9.505a1 1 0 0 1 0 2h-9.28c-1.812 0-3.467-1.277-3.7-3.075-.09-.7-.027-1.925-.027-1.925V4a2 2 0 0 1 2.004-2H17a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2z"></path></symbol><symbol id="24x24_bookmark" height="24" viewBox="0 0 24 24" width="24"><path d="M16 2H8a3 3 0 0 0-3 3v17l7-5 7 5V5a3 3 0 0 0-3-3zm-1.817 10.45l-2.21-1.357L9.837 12.5l.413-2.42L8.5 8.367l2.42-.353L11.973 5.5l1.107 2.514 2.42.353-1.75 1.713.433 2.37z"></path></symbol><symbol id="24x24_bookmark_attach" height="24" viewBox="0 0 24 24" width="24"><path d="M5 0v22l7-5 7 5V0m-4.817 12.45l-2.21-1.357L9.837 12.5l.413-2.42L8.5 8.367l2.42-.353L11.973 5.5l1.107 2.514 2.42.353-1.75 1.713.433 2.37z"></path></symbol><symbol id="24x24_bookmark_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 17l-7 5V5a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v17l-7-5zm6-12c0-1.103-.897-2-2-2H8c-1.103 0-2 .897-2 2v15.057l5.42-3.87.58-.416.58.417 5.42 3.87V5zm-6.027 6.093L9.837 12.5l.413-2.42L8.5 8.367l2.42-.353L11.973 5.5l1.107 2.514 2.42.353-1.75 1.713.433 2.37-2.21-1.357z"></path></symbol><symbol id="24x24_brake_temporary" height="24" viewBox="0 0 24 24" width="24"><circle cx="12.75" cy="12.75" r="2"></circle><path d="M13.25 3.775V2.25h-.5a10.512 10.512 0 0 0-10.5 10.5c0 .126.008.25.017.374l.034.626h1.52a8.994 8.994 0 1 0 9.434-9.975zm-1-.512v2.004a7.51 7.51 0 0 0-7 7.483h-2a9.512 9.512 0 0 1 9-9.487zm.5 17.487a7.998 7.998 0 0 1-7.93-7h.955l.534-.063-.04-.536a5.276 5.276 0 0 1-.02-.4 6.508 6.508 0 0 1 6.5-6.5h.5V4.778a7.995 7.995 0 0 1-.5 15.975z"></path></symbol><symbol id="24x24_broadcast_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20.328 8.712a8.462 8.462 0 0 1-1.28 3.04.498.498 0 0 1-.694.135.5.5 0 0 1-.134-.694c.27-.402.504-.83.69-1.274a7.452 7.452 0 0 0 .438-4.435 7.46 7.46 0 0 0-1.128-2.68.5.5 0 1 1 .828-.56 8.48 8.48 0 0 1 1.28 6.464zm-3.26.428c-.14.33-.31.645-.508.936a.498.498 0 0 1-.694.134.5.5 0 0 1-.134-.695 4.427 4.427 0 0 0 .676-1.607 4.534 4.534 0 0 0-.26-2.66 4.493 4.493 0 0 0-.416-.763.5.5 0 0 1 .828-.56 5.497 5.497 0 0 1 .83 1.967 5.567 5.567 0 0 1 0 2.216 5.6 5.6 0 0 1-.323 1.032zm-4.41-.8l4.81 12.986a.5.5 0 0 1-.937.348l-.99-2.682c-.012 0-.023.008-.04.008h-7c-.01 0-.022-.007-.035-.008l-.993 2.682a.5.5 0 1 1-.937-.348L11.34 8.34A1.495 1.495 0 0 1 12 5.5 1.5 1.5 0 0 1 13.5 7c0 .59-.344 1.096-.84 1.34zM8.83 18h6.343l-1.11-3H9.94l-1.11 3zm1.483-4h3.38L12 9.44 10.31 14zM7.855 8.752c.113.267.252.524.414.763a.5.5 0 0 1-.83.56A5.482 5.482 0 0 1 6.5 7a5.44 5.44 0 0 1 .94-3.076.5.5 0 1 1 .828.56A4.463 4.463 0 0 0 7.5 7a4.458 4.458 0 0 0 .354 1.752zM5.09 9.92c.187.444.42.872.69 1.272a.5.5 0 0 1-.828.56 8.444 8.444 0 0 1-1.28-3.04 8.543 8.543 0 0 1 .496-5.02c.213-.505.477-.99.784-1.445a.5.5 0 0 1 .828.56A7.456 7.456 0 0 0 4.5 7a7.468 7.468 0 0 0 .59 2.92z"></path></symbol><symbol id="24x24_bug_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21 11.5h-2.317A8.098 8.098 0 0 0 17 7.465l2.702-1.8a.5.5 0 1 0-.555-.83l-2.6 1.73A4.873 4.873 0 0 0 12 3.43a4.873 4.873 0 0 0-4.546 3.138l-2.6-1.732a.5.5 0 1 0-.556.832l2.7 1.8A8.107 8.107 0 0 0 5.32 11.5H3a.5.5 0 0 0 0 1h2.25c.007 1.532.456 3.074 1.215 4.396-.007.004-.015.004-.02.008l-2.147 1.43a.5.5 0 1 0 .555.832L7 17.736c.003-.002.005-.007.01-.01 1.234 1.684 3.01 2.846 4.99 2.846 1.98 0 3.756-1.162 4.99-2.847.005.003.007.008.012.01l2.145 1.43a.498.498 0 0 0 .694-.138.5.5 0 0 0-.134-.693l-2.145-1.43c-.007-.004-.015-.004-.022-.01.76-1.32 1.21-2.862 1.214-4.394H21a.5.5 0 0 0 0-1zm-14.75.972a7.04 7.04 0 0 1 2.1-5 11.42 11.42 0 0 0 3.077.567l-.407 11.4c-2.564-.65-4.77-3.73-4.77-6.97zm6.73 6.97L12.573 8.04a11.37 11.37 0 0 0 3.076-.57 7.04 7.04 0 0 1 2.1 5c0 3.243-2.21 6.32-4.77 6.97z"></path></symbol><symbol id="24x24_bullhorn" height="24" viewBox="0 0 24 24" width="24"><path d="M20.5 19a1.5 1.5 0 0 1-1.5-1.5v-11a1.5 1.5 0 0 1 3 0v11a1.5 1.5 0 0 1-1.5 1.5zM13 19H6v-4.43L4 14v1a1 1 0 0 1-2 0V9a1 1 0 0 1 2 0v1l14-4v12l-5-1.43V19zm-2-3l-3-.857V17h3v-1z"></path></symbol><symbol id="24x24_bullhorn_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.803 5.102a.497.497 0 0 0-.437-.084L4 9.842V9.25a1 1 0 0 0-2 0v5.5a1 1 0 0 0 2 0v-.592L7.033 15H7v4h6v-2.343l8.366 2.324A.5.5 0 0 0 22 18.5v-13a.5.5 0 0 0-.197-.398zM12 18H8v-2.73l4 1.11V18zm6-.99L4 13.12v-2.24l14-3.89v10.02zm3 .832l-2-.556V6.713l2-.555v11.684z"></path></symbol><symbol id="24x24_byob" height="24" viewBox="0 0 24 24" width="24"><path d="M21 20v2h-6v-2h2v-3.184A2.99 2.99 0 0 1 15 14V8h6v6a2.99 2.99 0 0 1-2 2.816V20h2zm-2-10h-2v3h2v-3zM3 10a3.99 3.99 0 0 1 3-3.86V2h2v4.14A3.99 3.99 0 0 1 11 10v12H3V10zm2 8h4v-7H5v7z"></path></symbol><symbol id="24x24_camera" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H5a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3h2.184A2.99 2.99 0 0 1 10 4h4a2.99 2.99 0 0 1 2.816 2H19a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3zM12.005 8.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9zm0 7a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="24x24_camera_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H5a3 3 0 0 1-3-3V9a3 3 0 0 1 3-3h2.184A2.99 2.99 0 0 1 10 4h4a2.99 2.99 0 0 1 2.816 2H19a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3zm2-11c0-1.103-.897-2-2-2h-2.89l-.236-.665A1.998 1.998 0 0 0 14 5h-4c-.837 0-1.59.536-1.874 1.335L7.89 7H5c-1.103 0-2 .897-2 2v8c0 1.103.897 2 2 2h14c1.103 0 2-.897 2-2V9zm-8.995 8.5a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9zm0-8c-1.93 0-3.5 1.57-3.5 3.5s1.57 3.5 3.5 3.5 3.5-1.57 3.5-3.5-1.57-3.5-3.5-3.5z"></path></symbol><symbol id="24x24_car" height="24" viewBox="0 0 24 24" width="24"><path d="M21 12c0-.924-.63-1.694-1.48-1.923l-1.106-5.42C18.17 3.677 17.384 3 16.49 3H7.51c-.894 0-1.68.677-1.924 1.658l-1.105 5.42A1.99 1.99 0 0 0 3 12v6h1v1.5a1.5 1.5 0 0 0 3 0V18h10v1.5a1.5 1.5 0 0 0 3 0V18h1v-6zM7.526 5.143A.404.404 0 0 1 7.59 5h8.82c.02.027.047.074.064.143L17.44 10H6.56l.964-4.857zM6 14.5A1.25 1.25 0 1 1 6 12a1.25 1.25 0 0 1 0 2.5zM18 12a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5z"></path></symbol><symbol id="24x24_cart" height="24" viewBox="0 0 24 24" width="24"><path d="M20 16H6L5 5H1V3h7v4h14l-2 9zM7 17a2 2 0 1 1 0 4 2 2 0 0 1 0-4zm12 0a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="24x24_cash_back" height="24" viewBox="0 0 24 24" width="24"><path d="M13.632 11.153c1.49.283 2.765 1.012 2.765 2.752 0 1.683-1.296 2.78-3.402 2.978l.008.89H11.75v-.883c-2.547-.17-3.453-1.584-3.476-2.886h2.113c.03.616.502 1.146 1.41 1.267v-2.495l-.66-.133c-1.44-.29-2.668-1.13-2.668-2.75 0-1.713 1.443-2.66 3.294-2.823v-.91h1.26v.913c1.948.204 3.154 1.35 3.176 2.815h-2.05c-.016-.53-.42-1.083-1.163-1.21v2.34l.645.135zm-.645 4.11c.727-.057 1.252-.495 1.252-1.146 0-.56-.37-.927-1.12-1.125-.045-.006-.09-.02-.135-.028v2.3zm-1.19-6.592c-.66.074-1.148.46-1.148 1.057 0 .494.335.85.98 1.04.052.02.104.036.164.05V8.67zm9.13 4.12l-3.062-3.95h2.06c-1.27-2.854-4.193-4.862-7.603-4.862-4.57 0-8.29 3.6-8.29 8.024 0 4.426 3.72 8.026 8.29 8.026 3.566 0 6.604-2.195 7.772-5.26h2.148C21 18.936 17.026 22 12.322 22c-5.696 0-10.33-4.486-10.33-10S6.626 2 12.322 2c4.554 0 8.418 2.872 9.788 6.84h1.877l-3.06 3.95z"></path></symbol><symbol id="24x24_cash_back_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12.55 11.402c1.417.35 2.45 1.033 2.45 2.657 0 1.71-1.244 2.73-3 2.91V18h-1v-1.03c-2.19-.18-2.968-1.608-3-2.82h1.39c.07.717.612 1.332 1.61 1.503v-3.115l-.496-.124C9.34 12.12 8.26 11.387 8.26 9.834c0-1.63 1.237-2.595 2.74-2.792V6h1v1.03c1.552.15 2.86 1.11 2.89 2.76h-1.368c-.066-.718-.56-1.33-1.522-1.472v2.945l.55.14zM12 15.68c.99-.122 1.584-.67 1.584-1.48 0-.738-.486-1.14-1.5-1.392l-.084-.02v2.89zm-1-7.337c-.793.15-1.317.628-1.317 1.37 0 .634.424 1.084 1.3 1.295l.017.004v-2.67zm9.25 4.157L17.75 9h1.975c-1.24-3.49-4.565-6-8.475-6-4.963 0-9 4.037-9 9s4.037 9 9 9c3.91 0 7.235-2.51 8.475-6h1.066a9.998 9.998 0 0 1-9.54 7c-5.52 0-10-4.477-10-10s4.48-10 10-10a9.998 9.998 0 0 1 9.54 7h1.96l-2.5 3.5z"></path></symbol><symbol id="24x24_casual" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3h-3a3.25 3.25 0 0 1-6 0H6L1.803 5.984 3.576 9.53 5 8.896 6 6v15h12V6l1 2.896 1.424.634 1.773-3.546L18 3zm-2 8l-2 1-2-1V8h4v3z"></path></symbol><symbol id="24x24_chat" height="24" viewBox="0 0 24 24" width="24"><path d="M12 3c-4.97 0-9 3.134-9 7 0 2.427 1.59 4.564 4 5.82V21l5-4c4.97 0 9-3.134 9-7s-4.03-7-9-7z"></path></symbol><symbol id="24x24_chat_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 4c4.41 0 8 2.692 8 6s-3.59 6-8 6h-.35l-.275.22L8 18.92v-3.707l-.538-.28C5.294 13.803 4 11.96 4 10c0-3.308 3.59-6 8-6m0-1c-4.97 0-9 3.134-9 7 0 2.427 1.588 4.564 4 5.82V21l5-4c4.97 0 9-3.134 9-7s-4.03-7-9-7z"></path></symbol><symbol id="24x24_check_in" height="24" viewBox="0 0 24 24" width="24"><path d="M23 12l-2.61-2.25 1.138-3.25-3.388-.64-.64-3.387-3.253 1.138L11.997 1 9.755 3.61 6.5 2.474 5.86 5.86l-3.385.64 1.14 3.25L1 12l2.612 2.248-1.14 3.253 3.386.643.643 3.385 3.255-1.14L11.998 23l2.25-2.612 3.252 1.14.64-3.386 3.388-.64-1.14-3.254L23 12zm-12.114 4.237L9.4 14.752l-2.226-2.227L8.66 11.04l2.226 2.228 4.455-4.455 1.487 1.485-5.94 5.94z"></path></symbol><symbol id="24x24_check_in_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M23 12l-2.61 2.248 1.138 3.253-3.388.65-.64 3.386-3.253-1.14-2.25 2.61-2.243-2.61L6.5 21.53l-.64-3.387-3.383-.64 1.14-3.254L1 12l2.612-2.25-1.14-3.25 3.386-.64.643-3.387L9.76 3.61 11.998 1l2.25 2.61L17.5 2.474l.64 3.386 3.388.64-1.14 3.25L23 12zm-5.046-5.158l-.67-.127-.126-.67-.424-2.244-2.157.76-.643.228-.444-.516L12 2.534l-1.487 1.73-.445.516-.644-.228L7.267 3.8 6.84 6.046l-.126.67-.67.126-2.243.424.76 2.155.23.65-.515.448L2.535 12l1.73 1.49.52.445-.22.644-.76 2.15 2.244.42.67.126.123.67.427 2.243 2.16-.756.644-.226.446.52L12 21.463l1.49-1.73.444-.517.644.22 2.156.753.424-2.244.126-.67.67-.127 2.246-.427-.755-2.155-.226-.647.51-.442 1.73-1.49-1.73-1.49-.52-.445.225-.644.755-2.153-2.246-.424zM9.4 14.752l-2.226-2.227L8.66 11.04l2.226 2.227 4.455-4.454 1.49 1.485-5.94 5.94L9.4 14.75z"></path></symbol><symbol id="24x24_checkmark" height="24" viewBox="0 0 24 24" width="24"><path d="M19.698 7.748L9.895 17.994 4.292 12.14a1.07 1.07 0 0 1 0-1.464.96.96 0 0 1 1.4 0l4.203 4.39 8.403-8.782a.96.96 0 0 1 1.4 0c.387.405.387 1.06 0 1.464z"></path></symbol><symbol id="24x24_checkmark_badged" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.95 7.85l-6.01 6.01-3.89-3.89a1 1 0 1 1 1.414-1.414l2.475 2.474 4.595-4.596A1 1 0 0 1 16.95 9.85z"></path></symbol><symbol id="24x24_chevron_android" height="24" viewBox="0 0 24 24" width="24"><path d="M8.464 3.515L7.05 4.93 14.12 12l-7.07 7.07 1.414 1.415L16.95 12 8.464 3.515z"></path></symbol><symbol id="24x24_chevron_down" height="24" viewBox="0 0 24 24" width="24"><path d="M18.364 9.525L16.95 8.11 12 13.06 7.05 8.11 5.636 9.526 12 15.89l6.364-6.365z"></path></symbol><symbol id="24x24_chevron_left" height="24" viewBox="0 0 24 24" width="24"><path d="M14.475 18.364l1.414-1.414L10.94 12l4.95-4.95-1.415-1.414L8.11 12l6.365 6.364z"></path></symbol><symbol id="24x24_chevron_right" height="24" viewBox="0 0 24 24" width="24"><path d="M9.525 5.636L8.11 7.05 13.06 12l-4.95 4.95 1.415 1.414L15.89 12 9.524 5.636z"></path></symbol><symbol id="24x24_chevron_up" height="24" viewBox="0 0 24 24" width="24"><path d="M5.636 14.475L7.05 15.89 12 10.94l4.95 4.95 1.414-1.415L12 8.11l-6.364 6.365z"></path></symbol><symbol id="24x24_classic_car_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M9.53 9.77a.5.5 0 0 1-.373-.833L10.884 7H9.53a.5.5 0 0 1-.414-.78l1.97-2.918a.5.5 0 1 1 .828.56L10.47 6H12a.5.5 0 0 1 .373.833l-2.47 2.77a.5.5 0 0 1-.373.167zm11.033 5.546l-3.86-.494-4.64-3.713a.502.502 0 0 0-.313-.11H7.28a.5.5 0 0 0-.474.342L5.62 14.958l-2.194.33A.5.5 0 0 0 3 15.78v3.72a.5.5 0 0 0 .5.5h2.278a1.982 1.982 0 0 0 3.444 0h5.556a1.982 1.982 0 0 0 3.444 0H20.5a.5.5 0 0 0 .5-.5v-3.688a.5.5 0 0 0-.437-.496zM7.5 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm9 0a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm3.5-1h-1.5a2 2 0 0 0-4 0h-5a2 2 0 0 0-4 0H4v-2.788l2.074-.31a.503.503 0 0 0 .402-.34L7.644 12h3.93l4.613 3.69a.506.506 0 0 0 .25.106l3.563.456z"></path></symbol><symbol id="24x24_clipboard" height="24" viewBox="0 0 24 24" width="24"><path d="M17 22H7a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3h1V4h2V3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v1h2v1h1a3 3 0 0 1 3 3v11a3 3 0 0 1-3 3zm1-15h-2v2H8V7H6v13h12V7zm-2 5H8v-1h8v1zm0 3H8v-1h8v1zm0 3H8v-1h8v1z"></path></symbol><symbol id="24x24_clipboard_add" height="24" viewBox="0 0 24 24" width="24"><path d="M18 20v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zM16 5h-2v2H8V5H6v13h6v2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h2V2h6v1h2a2 2 0 0 1 2 2v9h-2V5zm-2 11H8v-1h6v1zM8 9h6v1H8V9zm6 4H8v-1h6v1z"></path></symbol><symbol id="24x24_clock" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-18c-4.41 0-8 3.59-8 8s3.59 8 8 8 8-3.59 8-8-3.59-8-8-8zm3 11c-.19 0-.384-.055-.555-.168L11 12.535V7a1 1 0 0 1 2 0v4.465l2.555 1.703A1 1 0 0 1 15 15z"></path></symbol><symbol id="24x24_close" height="24" viewBox="0 0 24 24" width="24"><path d="M17.657 19.07L12 13.415 6.343 19.07 4.93 17.658 10.585 12 4.93 6.343 6.342 4.93 12 10.585l5.657-5.657L19.07 6.34 13.416 12l5.657 5.657-1.413 1.414z"></path></symbol><symbol id="24x24_coat_check" height="24" viewBox="0 0 24 24" width="24"><path d="M22.763 17.27L13 10.477V9a1 1 0 0 0-1-1 1.003 1.003 0 0 1-.978-1.215c.073-.366.388-.685.75-.76a.998.998 0 0 1 1.157.603l1.853-.745a3.01 3.01 0 0 0-3.42-1.817 3.006 3.006 0 0 0-2.304 2.33A3.01 3.01 0 0 0 11 9.83v.648l-9.764 6.79a1.495 1.495 0 0 0-.573 1.682c.197.628.772 1.05 1.432 1.05h19.81c.66 0 1.235-.422 1.432-1.05a1.494 1.494 0 0 0-.574-1.68zM3.69 18L12 12.22 20.31 18H3.69z"></path></symbol><symbol id="24x24_coffee" height="24" viewBox="0 0 24 24" width="24"><path d="M19 13h-1a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V5h15a3 3 0 0 1 3 3v2a3 3 0 0 1-3 3zm1-5c0-.55-.45-1-1-1h-1v4h1c.55 0 1-.45 1-1V8zm2 10a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h18a1 1 0 0 1 1 1z"></path></symbol><symbol id="24x24_collection" height="24" viewBox="0 0 24 24" width="24"><path d="M22.72 11.3l-4.65 9.968a3.003 3.003 0 0 1-3.986 1.45L6.108 19H14c.406 0 .79-.08 1.16-.192l1.52.708 4.226-9.063a1 1 0 0 0-.483-1.33L18 7.996V5.788l3.268 1.524c1.5.7 2.15 2.487 1.45 3.987zM14 18H4c-1.654 0-3-1.346-3-3V4c0-1.654 1.346-3 3-3h10c1.654 0 3 1.346 3 3v11c0 1.654-1.346 3-3 3zm1-14a1 1 0 0 0-1-1H4c-.55 0-1 .45-1 1v10h12V4zm-6 .5a2.857 2.857 0 0 1 2.857 2.857c0 1.07-.596 1.993-1.468 2.483L9 12.5 7.61 9.84a2.846 2.846 0 0 1-1.467-2.483A2.857 2.857 0 0 1 9 4.5zm0 3.857a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"></path></symbol><symbol id="24x24_collection_add" height="24" viewBox="0 0 24 24" width="24"><path d="M21 21v2h-2v-2h-2v-2h2v-2h2v2h2v2h-2zm-6-2H5c-1.654 0-3-1.346-3-3V5c0-1.654 1.346-3 3-3h10c1.654 0 3 1.346 3 3v11c0 1.654-1.346 3-3 3zm1-14a1 1 0 0 0-1-1H5c-.55 0-1 .45-1 1v10h12V5zm-6 .5a2.857 2.857 0 0 1 2.857 2.857c0 1.07-.596 1.993-1.468 2.483L10 13.5l-1.39-2.66a2.846 2.846 0 0 1-1.467-2.483A2.857 2.857 0 0 1 10 5.5zm0 3.857a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"></path></symbol><symbol id="24x24_collections_tab" height="24" viewBox="0 0 24 24" width="24"><path d="M3 21V7h18v14H3zM19 9H5v10h14V9zm-7 1.023c1.654 0 3 1.32 3 2.94 0 1.523-2.474 4.41-2.755 4.733l-.245.28-.245-.28C11.475 17.372 9 14.486 9 12.964c0-1.622 1.346-2.94 3-2.94zm0 3.892a.973.973 0 1 0 0-1.946.973.973 0 0 0 0 1.944zM6 5h13v1H6V5zm1-2h11v1H7V3z"></path></symbol><symbol id="24x24_collections_tab_outline" height="18" viewBox="0 0 18 18" width="18"><path d="M0 18V4h18v14H0zM17 5H1v12h16V5zM9 6.167c2.067 0 3.75 1.65 3.75 3.678 0 1.887-3.027 5.42-3.373 5.816L9 16.1l-.377-.434c-.346-.396-3.373-3.93-3.373-5.816 0-2.032 1.683-3.68 3.75-3.68zm0 8.392c1.192-1.45 2.75-3.69 2.75-4.72 0-1.48-1.233-2.68-2.75-2.68s-2.75 1.2-2.75 2.68c0 1.03 1.558 3.263 2.75 4.712zm0-6.43c.928 0 1.682.752 1.682 1.68a1.683 1.683 0 0 1-3.364 0c0-.928.754-1.68 1.682-1.68zm0 2.37a.682.682 0 1 0 0-1.364.682.682 0 0 0 0 1.362zM3 2h13v1H3V2zm1-2h11v1H4V0z"></path></symbol><symbol id="24x24_comment" height="24" viewBox="0 0 24 24" width="24"><path d="M12 3.5c-4.97 0-9 3.134-9 7 0 2.07 1.163 3.925 3 5.207V22l4.594-4.594c.46.056.926.094 1.406.094 4.97 0 9-3.134 9-7s-4.03-7-9-7z"></path></symbol><symbol id="24x24_compass" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zM6.65 17.374l3.678-7.07 7.07-3.678-3.676 7.07-7.07 3.678zm5.684-6.762l1.08 1.08 1.167-2.248-2.245 1.168z"></path></symbol><symbol id="24x24_compliment" height="24" viewBox="0 0 24 24" width="24"><path d="M19 9A7 7 0 0 0 5 9a6.995 6.995 0 0 0 3.957 6.297L8 21.992 12.005 19 16 21.992l-.957-6.695A6.995 6.995 0 0 0 19 9zm-7 5c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z"></path></symbol><symbol id="24x24_complimentary_carwash_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M12 10a2.503 2.503 0 0 1-2.5-2.5c0-1.2 1.74-3.78 2.088-4.284a.52.52 0 0 1 .824 0C12.76 3.72 14.5 6.3 14.5 7.5A2.503 2.503 0 0 1 12 10zm0-5.596A9.73 9.73 0 0 0 10.5 7.5a1.5 1.5 0 0 0 3 0A9.717 9.717 0 0 0 12 4.404zm8.563 10.912l-3.86-.494-4.64-3.713a.5.5 0 0 0-.313-.11H7.28a.5.5 0 0 0-.474.342L5.62 14.958l-2.194.33A.5.5 0 0 0 3 15.78v3.72a.5.5 0 0 0 .5.5h2.278a1.982 1.982 0 0 0 3.444 0h5.556a1.982 1.982 0 0 0 3.444 0H20.5a.5.5 0 0 0 .5-.5v-3.688a.5.5 0 0 0-.437-.496zM7.5 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm9 0a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm3.5-1h-1.5a2 2 0 0 0-4 0h-5a2 2 0 0 0-4 0H4v-2.788l2.074-.31a.5.5 0 0 0 .4-.34L7.644 12h3.93l4.614 3.69a.502.502 0 0 0 .25.106l3.563.456z"></path></symbol><symbol id="24x24_compose" height="24" viewBox="0 0 24 24" width="24"><path d="M3 21V3h9a1 1 0 0 1 0 2H5v14h14v-7a1 1 0 0 1 2 0v9H3zm9.46-6.487L8 16l1.487-4.46 5.993-5.995 2.975 2.975-5.994 5.993zm6.88-6.878L16.364 4.66l1.045-1.044a2.103 2.103 0 0 1 2.973 2.974L19.34 7.635z"></path></symbol><symbol id="24x24_compose_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20.384 6.59l-1.487 1.487-7.436 7.436L7 17l1.487-4.46 7.436-7.437 1.487-1.487a2.103 2.103 0 1 1 2.974 2.974zm-3.718-.743l-7.26 7.26-.743 2.23 2.23-.743 7.26-7.26-1.487-1.487zM3.97 20.03h14.06V11h.94v9.97H3.03V5.03H13v.94H3.97v14.06z"></path></symbol><symbol id="24x24_contacts" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H7V3h11a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2zm-3.5-5.98V14c.658-.48 1.214-1.146 1.256-1.668.744-.36.9-1.26.37-1.46l-.012.018c.24-.336.386-.76.386-1.25 0-.632-.114-1.217-.578-1.6-.322-.763-.994-1.29-1.775-1.29-.457 0-.877.183-1.212.487a.695.695 0 0 0-.448-.17c-.294 0-.548.197-.685.486-.737.272-1.273 1.103-1.273 2.087 0 .45.11.87.303 1.217-.57.225-.38 1.082.34 1.475.04.522.668 1.187 1.326 1.668v1.02c-1.41.22-2.455.908-3.5 1.918h9c-1.047-1.01-2.09-1.697-3.5-1.917zM4 3h2v18H4V3z"></path></symbol><symbol id="24x24_cool" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm0 16.5a5.405 5.405 0 0 1-5-3.357 8.6 8.6 0 0 0 5 1.6 8.6 8.6 0 0 0 5-1.6 5.405 5.405 0 0 1-5 3.357zm3.96-5.5h-.002c-1.617 0-3.028-.9-3.67-2.224a.32.32 0 0 0-.575 0C11.07 12.1 9.66 13 8.043 13H8.04c-2.01 0-3.74-1.15-4.035-3.018l-.124-.734c-.07-.305.257-.25.634-.248h14.972c.39 0 .673-.04.632.248l-.124.517C19.647 11.612 17.97 13 15.96 13z"></path></symbol><symbol id="24x24_cool_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm7.994 6.765C19.647 11.612 17.97 13 15.96 13h-.002c-1.617 0-3.028-.9-3.67-2.224a.32.32 0 0 0-.575 0C11.07 12.1 9.66 13 8.043 13H8.04c-2.01 0-3.74-1.15-4.035-3.018l-.124-.734c-.07-.305.257-.25.634-.248h14.972c.39 0 .673-.04.632.248l-.124.517zM17 15.143a5.405 5.405 0 0 1-5 3.357 5.405 5.405 0 0 1-5-3.357 8.6 8.6 0 0 0 5 1.6 8.6 8.6 0 0 0 5-1.6z"></path></symbol><symbol id="24x24_copy" height="24" viewBox="0 0 24 24" width="24"><path d="M7 22v-5H3V2h14v5h4v15H7zm8-18H5v11h2V7h8V4zm4 5H9v11h10V9zm-2 3h-6v-1h6v1zm0 3h-6v-1h6v1zm0 3h-6v-1h6v1z"></path></symbol><symbol id="24x24_copy_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M7 22v-5H3V2h14v5h4v15H7zm9-19H4v13h3V7h9V3zm4 5H8v13h12V8zm-3 4h-6v-1h6v1zm0 3h-6v-1h6v1zm0 3h-6v-1h6v1z"></path></symbol><symbol id="24x24_counter_order" height="24" viewBox="0 0 24 24" width="24"><path d="M1 20a3 3 0 0 1 3-3h16a3 3 0 0 1 3 3H1zM12 7a9 9 0 0 1 9 9H3a9 9 0 0 1 9-9zm-6.852 7.48a.5.5 0 0 0 .622-.336C6.588 11.408 9.15 9.5 12 9.5a.5.5 0 0 0 0-1c-3.29 0-6.246 2.203-7.188 5.357a.5.5 0 0 0 .336.622zM14 6h-4a1 1 0 0 1 0-2h4a1 1 0 0 1 0 2z"></path></symbol><symbol id="24x24_credit_card" height="24" viewBox="0 0 24 24" width="24"><path d="M19 19H5c-1.654 0-3-1.346-3-3V8c0-1.654 1.346-3 3-3h14c1.654 0 3 1.346 3 3v8c0 1.654-1.346 3-3 3zM4 16a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3H4v3zm16-8a1 1 0 0 0-1-1H5c-.55 0-1 .45-1 1v1h16V8z"></path></symbol><symbol id="24x24_croissant" height="24" viewBox="0 0 24 24" width="24"><path d="M20.634 8.5H19.1c.09-.295.15-.602.15-.926v-2.12c.718.34 1.39.76 2.003 1.253.74.597.332 1.793-.62 1.793zm-4.86 1.055a5.58 5.58 0 0 0-.712-.05L13.748 3.58a10.957 10.957 0 0 1 3.425.138c.477.094.827.5.827 1.324v2.534c0 1.195-1.043 2.15-2.225 1.98zm-2.43 1.81a4.005 4.005 0 0 0-1.98 1.98c-.202.442-.664.702-1.138.597l-6.89-1.528a1.013 1.013 0 0 1-.737-1.3A13.018 13.018 0 0 1 11.112 2.6a1.013 1.013 0 0 1 1.3.735l1.527 6.89c.106.475-.154.937-.597 1.14zM9.506 15.06c.003.242.016.48.05.713C9.722 16.957 8.768 18 7.573 18H4.7c-.485 0-.89-.35-.984-.827a10.957 10.957 0 0 1-.138-3.425l5.928 1.314zM8.5 19.1v1.534c0 .95-1.196 1.36-1.792.62a9.997 9.997 0 0 1-1.253-2.004h2.12c.318 0 .626-.062.925-.15z"></path></symbol><symbol id="24x24_dancing" height="24" viewBox="0 0 24 24" width="24"><path d="M20.992 12.827l-1.803.987-1.36 2.478-1.355-2.478L14 12.458l2.478-1.355 1.355-2.478 1.356 2.478 1.76.963A8.998 8.998 0 0 0 13 4.06V2h-2v2.06C6.5 4.556 3 8.367 3 13a9 9 0 0 0 9 9 9 9 0 0 0 9-9c0-.058-.007-.115-.008-.173zm-11.98 4.726l-.93 1.697-.927-1.697-1.697-.928 1.697-.928L8.083 14l.928 1.697 1.7.928-1.696.928zm4.214-8.8L12 8.083l1.226-.67.67-1.224.67 1.222 1.226.67-1.226.67-.67 1.226-.67-1.227z"></path></symbol><symbol id="24x24_dash" height="24" viewBox="0 0 24 24" width="24"><path d="M5 11h14v2H5v-2z"></path></symbol><symbol id="24x24_deal" height="24" viewBox="0 0 24 24" width="24"><path d="M22 5.004a3 3 0 0 0-3.004-3l-5.426.008a2.17 2.17 0 0 0-1.544.634l-9.39 9.375a2.185 2.185 0 0 0 .013 3.096l6.223 6.214c.86.858 2.247.863 3.1.013l9.39-9.375c.41-.408.638-.963.636-1.54V5.003zM18.22 8.52a1.997 1.997 0 0 1-3.44 0 1.993 1.993 0 0 1 0-2.04 1.997 1.997 0 0 1 3.44 0 1.99 1.99 0 0 1 0 2.04z"></path></symbol><symbol id="24x24_demographics_20s" height="24" viewBox="0 0 24 24" width="24"><path d="M19 2H5C3.34 2 2 3.34 2 5v14c0 1.66 1.34 3 3 3h14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3zm-7.45 14.17H5.73c.02-.61.15-1.16.4-1.67.23-.56.8-1.16 1.68-1.8.77-.55 1.27-.94 1.5-1.18.35-.37.52-.78.52-1.22 0-.36-.1-.66-.3-.9-.2-.23-.48-.35-.86-.35-.5 0-.85.19-1.03.57-.11.21-.17.56-.19 1.04H5.83c.02-.72.16-1.31.39-1.75.45-.85 1.24-1.28 2.38-1.28.9 0 1.61.25 2.14.75s.8 1.16.8 1.98c0 .63-.19 1.19-.56 1.68-.25.32-.66.68-1.22 1.08l-.67.47c-.42.3-.7.52-.86.65-.15.13-.28.29-.39.46h3.71v1.47zm6.06-.92c-.43.75-1.19 1.13-2.27 1.13-1.09 0-1.84-.38-2.28-1.13-.44-.76-.65-1.84-.65-3.24 0-1.41.21-2.49.65-3.25.44-.76 1.19-1.14 2.28-1.14 1.08 0 1.84.38 2.27 1.14.44.76.66 1.84.66 3.25 0 1.4-.22 2.48-.66 3.24zm-2.27-6.26c-.5 0-.83.25-.99.74-.16.49-.24 1.25-.24 2.28 0 .97.08 1.72.24 2.24.16.51.49.77.99.77.49 0 .82-.26.97-.77.16-.52.23-1.27.23-2.24 0-1.03-.07-1.79-.23-2.28-.15-.49-.48-.74-.97-.74z"></path></symbol><symbol id="24x24_demographics_30s" height="24" viewBox="0 0 24 24" width="24"><path d="M19 2H5C3.34 2 2 3.34 2 5v14c0 1.66 1.34 3 3 3h14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3zm-8.17 13.57c-.5.54-1.24.81-2.21.81-1.2 0-2.04-.39-2.51-1.17-.24-.42-.38-.97-.41-1.65h1.64c0 .34.06.63.17.85.2.41.57.61 1.1.61.33 0 .62-.11.86-.33.24-.23.36-.55.36-.97 0-.56-.22-.93-.67-1.12-.26-.11-.66-.16-1.22-.16v-1.2c.54 0 .92-.06 1.14-.15.36-.17.55-.5.55-1 0-.32-.09-.59-.28-.79-.19-.2-.46-.31-.8-.31-.39 0-.68.13-.87.38-.18.25-.27.58-.26 1H5.86c.01-.42.08-.82.21-1.2.14-.33.35-.64.65-.92.22-.2.47-.35.78-.46.3-.1.66-.16 1.1-.16.81 0 1.47.21 1.97.63.49.42.74.99.74 1.7 0 .5-.15.92-.44 1.26-.19.22-.39.36-.59.44.15 0 .37.13.66.39.42.4.64.94.64 1.62 0 .72-.25 1.35-.75 1.9zm6.81-.32c-.43.75-1.19 1.13-2.27 1.13-1.09 0-1.84-.38-2.28-1.13-.44-.76-.65-1.84-.65-3.24 0-1.41.21-2.49.65-3.25.44-.76 1.19-1.14 2.28-1.14 1.08 0 1.84.38 2.27 1.14.44.76.66 1.84.66 3.25 0 1.4-.22 2.48-.66 3.24zm-2.27-6.26c-.5 0-.83.25-.99.74-.16.49-.24 1.25-.24 2.28 0 .97.08 1.72.24 2.24.16.51.49.77.99.77.49 0 .82-.26.97-.77.16-.52.23-1.27.23-2.24 0-1.03-.07-1.79-.23-2.28-.15-.49-.48-.74-.97-.74z"></path></symbol><symbol id="24x24_demographics_40s" height="24" viewBox="0 0 24 24" width="24"><path d="M19 22H5a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3h14a3 3 0 0 1 3 3v14a3 3 0 0 1-3 3zm-7.162-9.142h-1.116V7.806H9.198L5.55 12.702v1.56h3.553v1.944h1.62v-1.944h1.115v-1.404zm6.366-2.946c-.164-.556-.387-1.002-.672-1.338a2.428 2.428 0 0 0-.985-.72 3.27 3.27 0 0 0-1.193-.216c-.416 0-.81.072-1.182.216a2.388 2.388 0 0 0-.978.72c-.28.336-.502.782-.666 1.338-.164.556-.246 1.242-.246 2.058 0 .84.082 1.542.246 2.106.164.564.387 1.014.666 1.35.28.336.605.576.978.72.37.144.766.216 1.182.216a3.27 3.27 0 0 0 1.193-.216c.373-.144.7-.384.985-.72.285-.336.508-.786.672-1.35.164-.564.246-1.266.246-2.106 0-.816-.082-1.502-.246-2.058zm-1.63 3.912a2.08 2.08 0 0 1-.41.81c-.187.224-.458.336-.81.336-.344 0-.607-.112-.79-.336a2.084 2.084 0 0 1-.403-.81 4.675 4.675 0 0 1-.15-.984 20.29 20.29 0 0 1-.016-1.392 6.93 6.93 0 0 1 .04-.63c.026-.216.065-.43.122-.642.054-.212.133-.402.234-.57.1-.168.226-.304.382-.408.156-.104.35-.156.582-.156.232 0 .428.052.588.156.16.104.293.24.396.408.104.168.182.358.235.57a6.092 6.092 0 0 1 .168 1.272 18.935 18.935 0 0 1-.017 1.392 4.74 4.74 0 0 1-.15.984zm-7.51-3.882h.038v2.916H6.895l2.17-2.916z"></path></symbol><symbol id="24x24_denied" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm5 11H7v-2h10v2z"></path></symbol><symbol id="24x24_desktop" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3H6a3 3 0 0 0-3 3v8a3 3 0 0 0 3 3h4v2H7v2h10v-2h-3v-2h4a3 3 0 0 0 3-3V6a3 3 0 0 0-3-3zm1 10a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v7z"></path></symbol><symbol id="24x24_directions" height="24" viewBox="0 0 24 24" width="24"><path d="M21.586 10.586l-8.172-8.172a2 2 0 0 0-2.828 0l-8.172 8.172a2 2 0 0 0 0 2.828l8.172 8.172a2 2 0 0 0 2.828 0l8.172-8.172a2 2 0 0 0 0-2.828zM13 15v-3h-3v3H8v-5h5V7l4 4-4 4z"></path></symbol><symbol id="24x24_discovery" height="24" viewBox="0 0 24 24" width="24"><path d="M20.914 7.5l1.414 1.414a1 1 0 1 1-1.414 1.414L19.5 8.914l-1.414 1.414a.997.997 0 0 1-1.414 0 1 1 0 0 1 0-1.414L18.086 7.5l-1.414-1.414a1 1 0 1 1 1.414-1.414L19.5 6.086l1.414-1.414a1 1 0 1 1 1.414 1.414L20.914 7.5zm-2.216 9.253a.998.998 0 0 1-.103 1.41c-.597.515-1.28.89-2.03 1.11a1.002 1.002 0 0 1-1.244-.674 1.002 1.002 0 0 1 .675-1.245 3.44 3.44 0 0 0 1.293-.707.998.998 0 0 1 1.41.102zm-6.088 2.062a.99.99 0 0 1-.53-.153 5.56 5.56 0 0 1-1.66-1.613 1 1 0 0 1 1.665-1.11c.274.41.64.763 1.057 1.025a1 1 0 0 1-.532 1.848zm-2.11-4.987a1 1 0 0 1-1-1v-1.91a1 1 0 0 1 2 0v1.91a1 1 0 0 1-1 1zm-.696-5.584a.998.998 0 0 1-.826-.435 3.02 3.02 0 0 0-1.054-.95 1 1 0 0 1 .95-1.76 5.03 5.03 0 0 1 1.754 1.58.998.998 0 0 1-.824 1.562zm-5.72-.523a1 1 0 0 1-1.61-1.185 5.032 5.032 0 0 1 1.81-1.516 1 1 0 0 1 .886 1.79 3.02 3.02 0 0 0-1.086.91zM3.5 10.778v1.91a1 1 0 0 1-2 0v-1.91a1 1 0 0 1 2 0zm-1 4.725a1 1 0 0 1 1 1v1a1 1 0 0 1-2 0v-1a1 1 0 0 1 1-1zm16-1.5v-1a1 1 0 0 1 2 0v1a1 1 0 0 1-2 0z"></path></symbol><symbol id="24x24_discovery_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20.207 7.5l1.768 1.768a.5.5 0 0 1-.707.707L19.5 8.207l-1.768 1.768a.498.498 0 0 1-.707 0 .5.5 0 0 1 0-.707L18.793 7.5l-1.768-1.768a.5.5 0 0 1 .707-.707L19.5 6.793l1.768-1.768a.5.5 0 0 1 .707.707L20.207 7.5zm-2.584 10.19a.5.5 0 0 1-.193.68 4.934 4.934 0 0 1-2.018.612l-.042.002a.5.5 0 0 1-.04-.998 3.97 3.97 0 0 0 1.613-.49.5.5 0 0 1 .68.194zm-4.135 1.05a.49.49 0 0 1-.167-.03 5.015 5.015 0 0 1-1.79-1.11.5.5 0 1 1 .695-.72c.408.393.903.7 1.43.89a.5.5 0 0 1-.167.97zm-2.485-2.61a.5.5 0 0 1-.65-.28A4.968 4.968 0 0 1 10 14v-.208a.5.5 0 0 1 1 0V14c0 .51.095 1.01.282 1.478a.5.5 0 0 1-.28.65zm-.503-3.75a.5.5 0 0 1-.5-.5V9.966a.5.5 0 0 1 1 0v1.912a.5.5 0 0 1-.5.5zm-.08-3.827a.5.5 0 0 1-.644-.29 3.525 3.525 0 0 0-.938-1.367.5.5 0 0 1 .668-.745c.535.483.95 1.09 1.204 1.76a.5.5 0 0 1-.29.644zM7.503 6.127a.506.506 0 0 1-.126-.016A3.556 3.556 0 0 0 5.72 6.09a.5.5 0 0 1-.22-.975 4.55 4.55 0 0 1 2.13.03.5.5 0 0 1-.126.985zm-4.24 2.04a.5.5 0 1 1-.926-.38 4.522 4.522 0 0 1 1.256-1.722.5.5 0 1 1 .645.764c-.427.36-.765.822-.977 1.336zM3 9.85v1.913a.5.5 0 0 1-1 0V9.85a.5.5 0 0 1 1 0zm-.5 3.326a.5.5 0 0 1 .5.5v1.912a.5.5 0 0 1-1 0v-1.912a.5.5 0 0 1 .5-.5zM2.5 17a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 .5-.5zm17-3.5a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 1 0v1a.5.5 0 0 1-.5.5zm-.59 1.35a.5.5 0 1 1 .977.21 4.965 4.965 0 0 1-.872 1.92.498.498 0 0 1-.7.104.5.5 0 0 1-.103-.7c.343-.46.577-.977.698-1.534z"></path></symbol><symbol id="24x24_download" height="24" viewBox="0 0 24 24" width="24"><path d="M5 21v-2h14v2H5zm2-9h4V3h2v9h4l-5 5-5-5z"></path></symbol><symbol id="24x24_download_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M5 20.5v-1h14v1H5zM7 12h4.5V3h1v9H17l-5 5-5-5z"></path></symbol><symbol id="24x24_drafts" height="24" viewBox="0 0 24 24" width="24"><path d="M21.98 2c-.97-.05-1.96-.02-2.95.12-2.22.32-4.26 1.1-6.03 2.25v2.87l-1.45-1.79a15.036 15.036 0 0 0-5.053 8.402L14 7.998 2.284 20.493c-.758.8.402 1.96 1.203 1.2L7.58 17.81c.51-.02 1.02-.06 1.54-.13 3.83-.55 7.11-2.5 9.4-5.25L15.76 11h3.82c1.69-2.6 2.58-5.73 2.4-9z"></path></symbol><symbol id="24x24_dress" height="24" viewBox="0 0 24 24" width="24"><path d="M19 8l-2-.845V5l-2.558 5H9.558L7 5v2.155L5 8 3 6l4.753-2.99v-.005L7.75 3h1.434C9.597 4 10.696 4.998 12 4.998c1.303 0 2.4-.998 2.815-1.998h1.433L21 5.998 19 8zm-3.99 3l4.96 8.1c-.12.144-.285.454-.5.535-.5.19-.998.054-1.103-.275-.11-.33-.582-.467-1.058-.336-.48.133-.81.493-.737.832.08.337-.273.71-.794.803-.52.09-.98-.13-1.025-.478-.05-.343-.486-.565-.975-.52-.49.043-.874.34-.86.685.016.346-.396.65-.924.65s-.94-.305-.922-.65c.013-.347-.374-.643-.863-.687-.49-.043-.922.177-.972.52-.044.343-.505.565-1.025.47-.52-.095-.874-.473-.793-.81.074-.34-.256-.71-.73-.842-.478-.13-.95-.014-1.06.315-.105.33-.6.42-1.1.23-.07-.025-.127-.156-.188-.19L9.01 11h6z"></path></symbol><symbol id="24x24_dressy" height="24" viewBox="0 0 24 24" width="24"><path d="M17.385 16l-3.618-1.703L12.307 7h.75l5.088 5.838-.76 3.162zM6.855 4.667L7.55 2h3.61l.695 2.667L9.355 6l-2.5-1.333zm2.5 2.466l1.55-.826 1.95 11.836L9.355 22l-3.5-3.857L7.77 6.29l1.585.843z"></path></symbol><symbol id="24x24_drip" height="24" viewBox="0 0 24 24" width="24"><path d="M13 16v1h1a1 1 0 0 1 0 2h-1v3h-2v-3h-1a1 1 0 0 1 0-2h1v-1a6 6 0 0 1-6-6V2h2v8a4 4 0 0 0 4 4h2a4 4 0 0 0 4-4V2h2v8a6 6 0 0 1-6 6zm0-3h-2c-1.654 0-3-1.346-3-3h3V9H8V7h3V6H8V4h8v6c0 1.654-1.346 3-3 3z"></path></symbol><symbol id="24x24_drive_thru" height="24" viewBox="0 0 24 24" width="24"><path d="M19 21V5H3V3h18v18h-2zM4 6h13v2H4V6zm-.042 8.326l.65-3.893A1.707 1.707 0 0 1 6.298 9h7.12c.84 0 1.55.602 1.69 1.43l.65 3.896c.563.28 1.24.857 1.24 1.53v4.13h-1V21h-2v-1.013H6V21H4v-1.013H3v-4.13c0-.674.392-1.25.958-1.53zm9.433-3.342L6.25 11l-.524 3.143h8.262l-.597-3.16zm.755 6.587a1.07 1.07 0 0 0 0-2.14 1.07 1.07 0 0 0 0 2.14zm-8.572 0a1.07 1.07 0 1 0 .003-2.14 1.07 1.07 0 0 0-.002 2.14z"></path></symbol><symbol id="24x24_drugstores" height="24" viewBox="0 0 24 24" width="24"><path d="M20 7h-3.19l1.003-3.74a1 1 0 1 0-1.932-.518L14.74 7H4a1 1 0 0 0 0 2l1.518 7.588A2.998 2.998 0 0 0 8.458 19H6a1 1 0 0 0 0 2h12a1 1 0 0 0 0-2h-2.46a3 3 0 0 0 2.942-2.412L20 9a1 1 0 0 0 0-2zm-5 8h-2v2h-2v-2H9v-2h2v-2h2v2h2v2z"></path></symbol><symbol id="24x24_duke" height="24" viewBox="0 0 24 24" width="24"><path d="M21 13.5a1.5 1.5 0 1 0-1.5-1.5c0 .46.21.865.536 1.14l-.767.908a1 1 0 0 1-1.58-.604l-.398-1.974A1.994 1.994 0 0 0 19 9.5a2 2 0 0 0-4 0 2 2 0 0 0 1.314 1.872l-.42.84a1 1 0 0 1-1.788 0L12.91 9.82A2.497 2.497 0 0 0 12 5a2.497 2.497 0 0 0-.91 4.823L9.893 12.21a1 1 0 0 1-1.788 0l-.42-.838A1.996 1.996 0 0 0 7 7.5a2 2 0 0 0-2 2c0 1.004.742 1.827 1.706 1.97l-.395 1.974a1 1 0 0 1-1.58.604l-.764-.907A1.494 1.494 0 0 0 3 10.5a1.5 1.5 0 0 0 0 3 1.5 1.5 0 0 0 .363-.05L4 16h-.33a1 1 0 0 0 0 2h16.66a1 1 0 0 0 0-2H20l.637-2.55c.117.03.237.05.363.05z"></path></symbol><symbol id="24x24_electric_car_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M20.563 15.316l-3.86-.494-4.64-3.713a.5.5 0 0 0-.313-.11H7.28a.5.5 0 0 0-.474.34l-.626 1.91h-.485a1.336 1.336 0 0 1 0-2.676H7.21A2.34 2.34 0 0 0 9.547 8.24v-.684a1.99 1.99 0 0 0 .84-2.43l-.335-.874a.5.5 0 0 0-.646-.287l-.243.093-.476-1.24a.5.5 0 0 0-.934.36l.476 1.235-1.06.406-.48-1.24a.5.5 0 1 0-.934.36l.48 1.24-.246.09a.5.5 0 0 0-.286.645l.335.873a1.975 1.975 0 0 0 2.503 1.18v.27A1.337 1.337 0 0 1 7.21 9.58H5.696a2.336 2.336 0 0 0 0 4.672h.158l-.232.708-2.194.33a.5.5 0 0 0-.428.49v3.72a.5.5 0 0 0 .5.5h2.278a1.982 1.982 0 0 0 3.444 0h5.556a1.982 1.982 0 0 0 3.444 0H20.5a.5.5 0 0 0 .5-.5v-3.688a.5.5 0 0 0-.437-.496zM7.503 6.992a.992.992 0 0 1-.526-.555L6.82 6.03l2.233-.858h.002l.243-.093.156.4a1 1 0 0 1-.574 1.29l-.61.234a.992.992 0 0 1-.77-.02zM7.5 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm9 0a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm3.5-1h-1.5a2 2 0 0 0-4 0h-5a2 2 0 0 0-4 0H4v-2.788l2.074-.31a.5.5 0 0 0 .4-.34L7.644 12h3.93l4.614 3.69a.502.502 0 0 0 .25.106l3.563.456z"></path></symbol><symbol id="24x24_engine_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M21.5 11H19V8.5a.5.5 0 0 0-.5-.5H15v-.5a.5.5 0 0 0-.5-.5H12V5h2.5a.5.5 0 0 0 0-1h-8a.5.5 0 0 0 0 1H9v2H7.5a.5.5 0 0 0-.5.5V9H4.5a.5.5 0 0 0-.5.5V12H3V8.5a.5.5 0 0 0-1 0v8a.5.5 0 0 0 1 0V13h1v3.5a.5.5 0 0 0 .5.5h6.793l1.854 1.854A.5.5 0 0 0 13.5 19h8a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5zM10 5h1v2h-1zm11 13h-7.293l-1.854-1.854A.5.5 0 0 0 11.5 16H5v-6h2.5a.5.5 0 0 0 .5-.5V8h6v.5a.5.5 0 0 0 .5.5H18v2.5a.5.5 0 0 0 .5.5H21z"></path></symbol><symbol id="24x24_envelope" height="24" viewBox="0 0 24 24" width="24"><path d="M21.44 17.734L15.708 12l5.734-5.734c.35.49.56 1.086.56 1.734v8a2.97 2.97 0 0 1-.56 1.734zm-11.208-5.21L3.266 5.56A2.97 2.97 0 0 1 5 5h14c.648 0 1.244.21 1.734.56l-6.966 6.965a2.503 2.503 0 0 1-3.536 0zm-7.673 5.21A2.977 2.977 0 0 1 2 16V8c0-.648.21-1.244.56-1.734L8.292 12 2.56 17.734zm6.963-4.502A3.487 3.487 0 0 0 12 14.256a3.49 3.49 0 0 0 2.475-1.024l.525-.525 5.734 5.734A2.97 2.97 0 0 1 19 19H5a2.97 2.97 0 0 1-1.734-.56L9 12.71l.525.525z"></path></symbol><symbol id="24x24_envelope_open" height="24" viewBox="0 0 24 24" width="24"><path d="M21.44 20.734L15.708 15 22 10v9a2.97 2.97 0 0 1-.56 1.734zm-18.88 0A2.977 2.977 0 0 1 2 19v-9l6.293 5-5.734 5.734zM9.992 2.806a3 3 0 0 1 4.014 0L22 10H2l7.993-7.194zm-.468 13.426A3.49 3.49 0 0 0 12 17.256c.897 0 1.792-.34 2.475-1.024l.525-.525 5.734 5.734A2.97 2.97 0 0 1 19 22H5a2.97 2.97 0 0 1-1.734-.56L9 15.71l.525.525z"></path></symbol><symbol id="24x24_envelope_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M19 5H5a3 3 0 0 0-3 3v8a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V8a3 3 0 0 0-3-3zm2 3v8c0 .402-.122.774-.326 1.088l-4.967-4.967 5.052-5.05c.146.28.24.594.24.93zM5 6h14c.402 0 .774.12 1.088.326l-6.32 6.32a2.505 2.505 0 0 1-3.536 0l-6.32-6.32A1.987 1.987 0 0 1 5 6zM3 8c0-.338.092-.65.24-.93l5.053 5.05-4.967 4.968A1.987 1.987 0 0 1 3 16V8zm2 10a1.97 1.97 0 0 1-.93-.24L9 12.827l.525.525A3.49 3.49 0 0 0 12 14.377a3.49 3.49 0 0 0 2.475-1.024l.525-.525 4.93 4.93A1.95 1.95 0 0 1 19 18H5z"></path></symbol><symbol id="24x24_event" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm1-13H5v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V8zm-5.634 7.723L12 18l-1.366-2.277a3.5 3.5 0 1 1 2.732 0zM12 11.25a1.25 1.25 0 1 0 0 2.5 1.25 1.25 0 0 0 0-2.5z"></path></symbol><symbol id="24x24_event_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm2-15c0-1.103-.897-2-2-2H6c-1.103 0-2 .897-2 2v1h16V6zm0 2H4v10c0 1.103.897 2 2 2h12c1.103 0 2-.897 2-2V8zm-6.634 8.223L12 18.5l-1.366-2.277a3.5 3.5 0 1 1 2.732 0zM12 11.75a1.25 1.25 0 1 0 0 2.5 1.25 1.25 0 0 0 0-2.5z"></path></symbol><symbol id="24x24_exclamation" height="24" viewBox="0 0 24 24" width="24"><path d="M12 15a2 2 0 0 1-2-2V4a2 2 0 0 1 4 0v9a2 2 0 0 1-2 2zm0 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="24x24_external_link" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h5v2H6c-.55 0-1 .45-1 1v12c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-5h2v5a3 3 0 0 1-3 3zm-4.466-8.935L12.12 10.65l4.265-4.265L13 3h8v8l-3.2-3.2-4.266 4.265z"></path></symbol><symbol id="24x24_facebook" height="24" viewBox="0 0 24 24" width="24"><path d="M13 21v-8h3.15l.412-3H13V7.547C13 6.62 13.65 6 14.98 6H17V3.126C16 3.086 15.493 3 14.323 3 11.88 3 10 4.49 10 7.23V10H7v3h3v8h3z"></path></symbol><symbol id="24x24_fast_responder" height="24" viewBox="0 0 24 24" width="24"><path d="M20 15h-1v5l-5-5h-4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2v7c0 1.1-.9 2-2 2zM1 12h5v1H1v-1zm1-3h4v1H2V9zm1-3h3v1H3V6z"></path></symbol><symbol id="24x24_feed" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3H6a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3V6a3 3 0 0 0-3-3zm-7 7h6v1h-6v-1zm-2 0H6V7h3v3zm9-2h-7V7h7v1zm-7 8h6v1h-6v-1zm-2 0H6v-3h3v3zm9-2h-7v-1h7v1z"></path></symbol><symbol id="24x24_feed_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm2-15c0-1.103-.897-2-2-2H6c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h12c1.103 0 2-.897 2-2V6zm-9 7h7v1h-7v-1zm0-6h7v1h-7V7zm-5 6h3v3H6v-3zm0-6h3v3H6V7zm11 4h-6v-1h6v1zm0 6h-6v-1h6v1z"></path></symbol><symbol id="24x24_file" height="24" viewBox="0 0 24 24" width="24"><path d="M5 22V2h7v7h7v13H5zm11-9H8v1h8v-1zm0 3H8v1h8v-1zM13 2l6 6h-6V2z"></path></symbol><symbol id="24x24_filter" height="24" viewBox="0 0 24 24" width="24"><path d="M21 9h-8.14c.082-.32.14-.653.14-1s-.058-.68-.14-1H21a1 1 0 0 1 0 2zm-6 4a3 3 0 1 1 0 6 3 3 0 0 1 0-6zm0 4c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1zm-6-6a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0-4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zM3 9a1 1 0 0 1 0-2h2.14c-.08.32-.14.653-.14 1s.058.68.14 1H3zm0 6h8.14c-.082.32-.14.653-.14 1s.058.68.14 1H3a1 1 0 0 1 0-2zm18 0a1 1 0 0 1 0 2h-2.14c.082-.32.14-.653.14-1s-.058-.68-.14-1H21z"></path></symbol><symbol id="24x24_fine" height="24" viewBox="0 0 24 24" width="24"><path d="M17 24a6.497 6.497 0 0 1-6.475-6H1V2h16v9a6.5 6.5 0 0 1 0 13zM15 4H3v12h7.68A6.505 6.505 0 0 1 15 11.317V4zm3 10a1 1 0 0 0-2 0v3a1 1 0 0 0 2 0v-3zm-1 5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zM5 9h8v1H5V9zm0-3h8v1H5V6zm6 7H5v-1h6v1z"></path></symbol><symbol id="24x24_first" height="24" viewBox="0 0 24 24" width="24"><path d="M23 12l-2.61-2.25 1.138-3.25-3.388-.64-.64-3.387-3.253 1.137L11.997 1 9.755 3.61 6.5 2.473 5.86 5.86l-3.385.64 1.14 3.25L1 12l2.612 2.248-1.14 3.253 3.386.643.643 3.385 3.255-1.14L11.998 23l2.25-2.612 3.252 1.14.64-3.386 3.388-.64-1.14-3.254L23 12zm-9 4h-4v-1h1V9.667L10 10V9l3-1v7h1v1z"></path></symbol><symbol id="24x24_fit" height="24" viewBox="0 0 24 24" width="24"><path d="M19.58 3h-4.994l2.497 2.497L12 10.58 6.917 5.497 9.414 3H3v6.414l2.497-2.497L10.58 12l-5.083 5.083L3 14.586V21h6.414l-2.497-2.497L12 13.42l5.083 5.083L14.586 21H21v-6.414l-2.497 2.497L13.42 12l5.083-5.083L21 9.414V3h-1.42z"></path></symbol><symbol id="24x24_flag" height="24" viewBox="0 0 24 24" width="24"><path d="M8 13.43V3.57c3.667 1.972 7.333-1.973 11 0v9.86c-3.667-1.972-7.333 1.973-11 0zM6 21a1 1 0 0 1-1-1V4a1 1 0 0 1 2 0v16a1 1 0 0 1-1 1z"></path></symbol><symbol id="24x24_flame" height="24" viewBox="0 0 24 24" width="24"><path d="M14.63 15.432c1.16 1.57 1.78 3.56-.303 5.568C24.43 16.47 21.6 9.302 15.554 5.692c1.427 2.914-.567 2.723-.847 4.656C13.817 4.51 8.787 3 8.787 3c2.488 3.236-2.313 5.74-4.415 9.996-1.79 3.62 3.08 6.53 5.68 8.004-2.617-3.592-.684-6.024 1.962-8.152-.98 2.94.61 3.52 1.277 4.733.866-.374 1.25-1.564 1.34-2.147z"></path></symbol><symbol id="24x24_followers" height="24" viewBox="0 0 24 24" width="24"><path d="M20.324 13.817l-2.482 5.946c-.69 1.65-2.995 1.65-3.684 0l-2.482-5.946c-.558-1.337.41-2.817 1.842-2.817h4.964c1.432 0 2.4 1.48 1.842 2.817zM16 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6zM8 21l-5-4 5-4v3h2.42l.835 2H8v3z"></path></symbol><symbol id="24x24_following" height="24" viewBox="0 0 24 24" width="24"><path d="M21 17l-6 4v-3h-2.255l.835-2H15v-3l6 4zM9.842 19.763c-.69 1.65-2.995 1.65-3.684 0l-2.482-5.946C3.118 12.48 4.086 11 5.518 11h4.964c1.432 0 2.4 1.48 1.842 2.817l-2.482 5.946zM8 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"></path></symbol><symbol id="24x24_food" height="24" viewBox="0 0 24 24" width="24"><path d="M17.22 22a1.78 1.78 0 0 1-1.74-2.167l1.298-4.98L14 13l1.756-9.657A1.635 1.635 0 0 1 19 3.635V20.22A1.78 1.78 0 0 1 17.22 22zm-7.138-9.156l.697 7.168a1.79 1.79 0 1 1-3.56 0l.7-7.178A3.985 3.985 0 0 1 5 9V3a1 1 0 0 1 2 0v5.5c0 .28.22.5.5.5s.5-.22.5-.5V3a1 1 0 0 1 2 0v5.5c0 .28.22.5.5.5s.5-.22.5-.5V3a1 1 0 0 1 2 0v5.83c0 1.85-1.2 3.518-2.918 4.014z"></path></symbol><symbol id="24x24_formal" height="24" viewBox="0 0 24 24" width="24"><path d="M20.42 17.877L15 12.915v-1.83l5.42-4.962a1 1 0 0 1 1.58.815v10.124a1 1 0 0 1-1.58.815zM13 14h-2a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1zM2 17.062V6.938a1 1 0 0 1 1.58-.815L9 11.085v1.83l-5.42 4.962A1 1 0 0 1 2 17.062z"></path></symbol><symbol id="24x24_free_estimate_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M12.108 2.73a.358.358 0 0 1 .36.362v.184a3.05 3.05 0 0 1 1.3.46.448.448 0 0 1 .25.403.46.46 0 0 1-.468.46.487.487 0 0 1-.252-.08 3.06 3.06 0 0 0-.862-.37v1.61c1.273.32 1.817.83 1.817 1.725 0 .92-.72 1.53-1.784 1.632v.502a.358.358 0 0 1-.367.36.364.364 0 0 1-.368-.36V9.1a3.633 3.633 0 0 1-1.72-.653.46.46 0 0 1-.224-.403.454.454 0 0 1 .46-.46.462.462 0 0 1 .278.092 2.97 2.97 0 0 0 1.24.56V6.59c-1.223-.32-1.794-.78-1.794-1.725a1.684 1.684 0 0 1 1.76-1.6V3.09a.364.364 0 0 1 .367-.36zm-.335 2.858V4.105c-.536.05-.803.335-.803.704 0 .35.16.563.803.773zm.663 1.164v1.525c.536-.06.83-.327.83-.73 0-.367-.186-.593-.83-.795zm8.127 8.564l-3.86-.494-4.64-3.713a.502.502 0 0 0-.313-.11H7.28a.5.5 0 0 0-.474.34L5.62 14.96l-2.194.33a.5.5 0 0 0-.426.49v3.72a.5.5 0 0 0 .5.5h2.278a1.982 1.982 0 0 0 3.444 0h5.556a1.982 1.982 0 0 0 3.444 0H20.5a.5.5 0 0 0 .5-.5v-3.688a.5.5 0 0 0-.437-.496zM7.5 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm9 0a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm3.5-1h-1.5a2 2 0 0 0-4 0h-5a2 2 0 0 0-4 0H4v-2.788l2.074-.31a.503.503 0 0 0 .402-.34L7.644 12h3.93l4.613 3.69a.506.506 0 0 0 .25.106l3.563.456z"></path></symbol><symbol id="24x24_friends" height="24" viewBox="0 0 24 24" width="24"><g><path d="M10.824 13.817l-2.482 5.946c-.69 1.65-2.995 1.65-3.684 0l-2.482-5.946C1.618 12.48 2.586 11 4.018 11h4.964c1.432 0 2.4 1.48 1.842 2.817zM6.5 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"></path><path d="M21.824 13.817l-2.482 5.946c-.69 1.65-2.995 1.65-3.684 0l-2.482-5.946c-.558-1.337.41-2.817 1.842-2.817h4.964c1.432 0 2.4 1.48 1.842 2.817zM17.5 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" opacity=".502"></path></g></symbol><symbol id="24x24_funny" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm3.5 6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zm-7 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zM12 18a5.5 5.5 0 0 1-5.288-4h10.576A5.5 5.5 0 0 1 12 18z"></path></symbol><symbol id="24x24_funny_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm0 15a5.5 5.5 0 0 1-5.288-4h10.576A5.5 5.5 0 0 1 12 18zm3.5-7a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm-7 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path></symbol><symbol id="24x24_gas_station" height="24" viewBox="0 0 24 24" width="24"><path d="M20.707 5.743L16.464 1.5l-.707.707L18 4.45v3.586c0 .532.432.964.964.964H20v9.036a1 1 0 0 1-2 0v-5.5A1.54 1.54 0 0 0 16.464 11H15V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v14H3v2h13v-2h-1v-7h1.5a.5.5 0 0 1 .5.5v5.422c0 .997.678 1.923 1.662 2.086A2.003 2.003 0 0 0 21 18.036V6.45a.997.997 0 0 0-.293-.707zM6 6.5a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-6a.5.5 0 0 1-.5-.5v-4z"></path></symbol><symbol id="24x24_gender_neutral" height="24" viewBox="0 0 24 24" width="24"><path d="M14.303 2l1.64 1.642-1.862 1.863a5.83 5.83 0 0 0-3.08-.88 5.873 5.873 0 0 0-1 11.66V18H8v2h2v2h2v-2h2v-2h-2v-1.716a5.873 5.873 0 0 0 4.875-5.784 5.85 5.85 0 0 0-1.29-3.67l1.773-1.774L19 6.696V2h-4.697zM11 14.375A3.88 3.88 0 0 1 7.125 10.5 3.88 3.88 0 0 1 11 6.625a3.88 3.88 0 0 1 3.875 3.875A3.88 3.88 0 0 1 11 14.375z"></path></symbol><symbol id="24x24_gift" height="24" viewBox="0 0 24 24" width="24"><path d="M21 9v3h-8V9h-2v3H3V9h6a3 3 0 1 1 3-3 3 3 0 1 1 3 3h6zM10.5 6c0-.827-.673-1.5-1.5-1.5S7.5 5.173 7.5 6 8.173 7.5 9 7.5h1.5V6zm6 0c0-.827-.673-1.5-1.5-1.5s-1.5.673-1.5 1.5v1.5H15c.827 0 1.5-.673 1.5-1.5zM11 21H6.683A2.683 2.683 0 0 1 4 18.317V13h7v8zm9-2.683A2.68 2.68 0 0 1 17.317 21H13v-8h7v5.317z"></path></symbol><symbol id="24x24_github" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.362 2 11.743c0 4.303 2.865 7.955 6.84 9.243.5.09.682-.21.682-.47 0-.23-.01-.843-.014-1.656-2.782.588-3.37-1.306-3.37-1.306-.453-1.126-1.11-1.425-1.11-1.425-.907-.61.07-.6.07-.6 1.002.07 1.532 1.003 1.532 1.003.892 1.49 2.34 1.06 2.91.81.09-.63.35-1.06.635-1.303-2.22-.245-4.555-1.08-4.555-4.814a3.71 3.71 0 0 1 1.03-2.61c-.104-.25-.447-1.24.097-2.58 0 0 .84-.263 2.75 1A9.833 9.833 0 0 1 12 6.71c.85.005 1.705.113 2.504.33 1.91-1.262 2.747-1 2.747-1 .55 1.342.21 2.332.1 2.58a3.7 3.7 0 0 1 1.03 2.613c0 3.742-2.34 4.566-4.56 4.807.36.3.68.895.68 1.804 0 1.302-.013 2.353-.013 2.673 0 .26.18.563.688.468 3.97-1.29 6.834-4.94 6.834-9.242C22 6.363 17.523 2 12 2z"></path></symbol><symbol id="24x24_google" height="24" viewBox="0 0 24 24" width="24"><path d="M21 13v2h-2v-2h-2v-2h2V9h2v2h2v2h-2zM8 19c-3.87 0-7-3.13-7-7s3.13-7 7-7c1.89 0 3.47.69 4.69 1.83l-1.9 1.83c-.52-.5-1.43-1.08-2.79-1.08-2.39 0-4.34 1.98-4.34 4.42S5.61 16.42 8 16.42c2.77 0 3.81-1.99 3.97-3.02H8V11h6.61c.06.35.11.7.11 1.16 0 4-2.68 6.84-6.72 6.84z"></path></symbol><symbol id="24x24_grid" height="24" viewBox="0 0 24 24" width="24"><path d="M13 21v-8h8v8h-8zm0-18h8v8h-8V3zM3 13h8v8H3v-8zM3 3h8v8H3V3z"></path></symbol><symbol id="24x24_groups" height="24" viewBox="0 0 24 24" width="24"><path d="M6.087 20c.215-3.69 2.78-6.2 5.913-6.2 3.133 0 5.698 2.51 5.913 6.2H6.087zM12 12a3.875 3.875 0 1 1 0-7.75A3.875 3.875 0 0 1 12 12z"></path><path d="M18 13.375a3.124 3.124 0 0 1-2.86-1.874 4.6 4.6 0 0 0 1.485-3.373c0-.217-.035-.424-.064-.634A3.094 3.094 0 0 1 18 7.126a3.125 3.125 0 0 1 0 6.25zm-12 0a3.125 3.125 0 0 1 0-6.25 3.1 3.1 0 0 1 1.44.366c-.03.21-.065.42-.065.637A4.6 4.6 0 0 0 8.86 11.5 3.124 3.124 0 0 1 6 13.376zm0 1.812c.384 0 .753.057 1.11.142-1.015 1.196-1.665 2.793-1.772 4.624L5.336 20h-4.15A4.813 4.813 0 0 1 6 15.187zM22.812 20h-4.148l-.002-.044c-.107-1.83-.757-3.428-1.773-4.627a4.79 4.79 0 0 1 1.11-.145A4.812 4.812 0 0 1 22.81 20z"></path></symbol><symbol id="24x24_guide" height="24" viewBox="0 0 24 24" width="24"><path d="M15 22V8h3V6a.5.5 0 0 1 1 0v2h3v14h-7zm4.75-12h-2.5a.5.5 0 0 0 0 1h2.5a.5.5 0 0 0 0-1zm0 3h-2.5a.5.5 0 0 0 0 1h2.5a.5.5 0 0 0 0-1zm0 3h-2.5a.5.5 0 0 0 0 1h2.5a.5.5 0 0 0 0-1zM10 14.5a.5.5 0 0 0-.5-.5H5V6.545l9-4.163V22h-4v-7.5zM11.5 8h-4a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1zm.5 3.5a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 0 0 1h4a.5.5 0 0 0 .5-.5zM9 22H2v-7h7v7z"></path></symbol><symbol id="24x24_guide_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M22.5 23h-21a.5.5 0 0 1-.5-.5v-8a.5.5 0 0 1 .5-.5H4V6.225a.5.5 0 0 1 .29-.454l10-4.622A.5.5 0 0 1 15 1.6V7h3V5.5a.5.5 0 0 1 1 0V7h3.5a.5.5 0 0 1 .5.5v15a.5.5 0 0 1-.5.5zM4 15H2v7h7v-7H4zm10-7.5V2.382L5 6.545V14h4.5a.5.5 0 0 1 .5.5V22h4V7.5zm8 .5h-7v14h7V8zm-4.75 2h2.5a.5.5 0 0 1 0 1h-2.5a.5.5 0 0 1 0-1zm0 3h2.5a.5.5 0 0 1 0 1h-2.5a.5.5 0 0 1 0-1zm0 3h2.5a.5.5 0 0 1 0 1h-2.5a.5.5 0 0 1 0-1zM7 11.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zM11.5 9h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 1 0 1z"></path></symbol><symbol id="24x24_hamburger" height="24" viewBox="0 0 24 24" width="24"><path d="M3 18v-2h18v2H3zm0-7h18v2H3v-2zm0-5h18v2H3V6z"></path></symbol><symbol id="24x24_hamburger_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21 12.5H3a.5.5 0 0 1 0-1h18a.5.5 0 0 1 0 1zm0-5H3a.5.5 0 0 1 0-1h18a.5.5 0 0 1 0 1zm-18 9h18a.5.5 0 0 1 0 1H3a.5.5 0 0 1 0-1z"></path></symbol><symbol id="24x24_happy_hour" height="24" viewBox="0 0 24 24" width="24"><path d="M19 19h-2v1a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6h13v2h2c1.103 0 2 .898 2 2v7c0 1.102-.897 2-2 2zM8 9.5a.5.5 0 0 0-1 0v8a.5.5 0 0 0 1 0v-8zm3 0a.5.5 0 0 0-1 0v8a.5.5 0 0 0 1 0v-8zm3 0a.5.5 0 0 0-1 0v8a.5.5 0 0 0 1 0v-8zm5 .5h-2v7h2v-7zM4 4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1H4V4z"></path></symbol><symbol id="24x24_heart" height="24" viewBox="0 0 24 24" width="24"><path d="M16.125 5c-1.74 0-3.262.916-4.125 2.29A4.863 4.863 0 0 0 7.875 5 4.88 4.88 0 0 0 3 9.886C3 14.59 9.275 16.52 12 20c2.725-3.48 9-5.41 9-10.114A4.88 4.88 0 0 0 16.125 5z"></path></symbol><symbol id="24x24_heart_chat" height="24" viewBox="0 0 24 24" width="24"><path d="M19 4H5c-1.1 0-2 .9-2 2v9c0 1.1.9 2 2 2h1v5l5-5h8c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-5.34 8.31c-.846.566-1.568 1.366-1.655 1.69-.102-.33-.75-1.107-1.663-1.676C9.402 11.74 8 10.98 8 9.514c0-1.76 2.965-2.298 4 0 .987-2.206 4-1.794 4 0 0 1.465-1.418 2.173-2.34 2.795z"></path></symbol><symbol id="24x24_hike" height="24" viewBox="0 0 24 24" width="24"><path d="M18.44 11.608l-3.205-.564-1.285-2.298-.6 4.163 2.106 2.8 1.744 4.42a1 1 0 0 1-.592 1.31l-.07.023a.964.964 0 0 1-1.2-.554l-1.76-4.244-1.85-2.013-2.355 6.56a.912.912 0 0 1-1.16.564.943.943 0 0 1-.578-1.156l2.127-7.26.34-4.795-1.677.974-.507 3.47-.93-.01.022-4.3 3.27-2.383c.034-.023.073-.043.11-.065l-2.293-2.42c.197.48.35.994.35 1.466 0 .79-.627 1.43-1.397 1.43S5.653 6.09 5.653 5.3c0-1.35 1.387-3.33 1.387-3.33l3.864 4.082c1.276-.342 3.348.06 3.65.484.683 1.186 1.517 3.083 1.517 3.083l2.65 1.07-.273.91zM12.822 5.41c-.936 0-1.695-.776-1.695-1.735 0-.96.76-1.736 1.695-1.736.936 0 1.695.77 1.695 1.73s-.76 1.733-1.695 1.733z"></path></symbol><symbol id="24x24_history_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M14 7v4.465l2.555 1.703a1 1 0 0 1-1.11 1.664L12 12.535V7a1 1 0 0 1 2 0zm8.215 8.893a9.988 9.988 0 0 1-2.144 3.178A9.975 9.975 0 0 1 13 22a9.97 9.97 0 0 1-3.893-.785.5.5 0 0 1 .39-.922 9.076 9.076 0 0 0 7.007 0 8.968 8.968 0 0 0 2.86-1.93 8.997 8.997 0 0 0 1.93-2.86A8.938 8.938 0 0 0 22 12a8.983 8.983 0 0 0-2.636-6.364 8.99 8.99 0 0 0-2.86-1.93 9.076 9.076 0 0 0-7.007 0 8.96 8.96 0 0 0-2.86 1.93A8.96 8.96 0 0 0 4 12c0 .865.126 1.71.364 2.524l.957-1.605a.5.5 0 0 1 .86.51l-1.5 2.52c-.01.016-.025.026-.037.042a.448.448 0 0 1-.147.127c-.018.01-.03.026-.05.034-.013.005-.027.003-.04.007-.012.005-.02.014-.033.017a.495.495 0 0 1-.122.016.505.505 0 0 1-.23-.062c-.007-.004-.02-.002-.026-.007L1.38 14.57a.5.5 0 1 1 .512-.86l1.458.87A9.95 9.95 0 0 1 3 12a9.964 9.964 0 0 1 2.93-7.07 9.964 9.964 0 0 1 3.177-2.144 10.08 10.08 0 0 1 7.787 0A9.954 9.954 0 0 1 20.07 4.93 9.974 9.974 0 0 1 23 12c0 1.35-.265 2.66-.785 3.893z"></path></symbol><symbol id="24x24_hospital" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-18c-4.41 0-8 3.59-8 8s3.59 8 8 8 8-3.59 8-8-3.59-8-8-8zm2 13h-4v-3H7v-4h3V7h4v3h3v4h-3v3z"></path></symbol><symbol id="24x24_hospital_readmission" height="24" viewBox="0 0 24 24" width="24"><path d="M14 7v3h3v4h-3v3h-4v-3H7v-4h3V7h4zm4.193-.193A8.11 8.11 0 0 0 12 3.905c-4.464 0-8.095 3.63-8.095 8.095 0 4.463 3.63 8.095 8.095 8.095 4.463 0 8.095-3.632 8.095-8.095H22c0 5.514-4.486 10-10 10S2 17.514 2 12 6.486 2 12 2a10.01 10.01 0 0 1 7.545 3.455L22 3v6h-6l2.193-2.193z"></path></symbol><symbol id="24x24_house" height="24" viewBox="0 0 24 24" width="24"><path d="M12 3l-8.48 9.327C2.938 12.97 3.393 14 4.26 14H5v7h5v-5h4v5h5v-7h.74c.868 0 1.323-1.03.74-1.673L12 3z"></path></symbol><symbol id="24x24_hybrid_car_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M7.71 8.4a.483.483 0 0 0 .15-.02l1.663-.515a2.682 2.682 0 0 0 3.17 1.315C13.915 8.804 16.62 6 17.15 5.443a.5.5 0 0 0-.255-.834c-.752-.165-4.566-.957-5.787-.578a2.687 2.687 0 0 0-1.88 2.875l-1.663.513a.5.5 0 0 0 .147.978zm2.694-2.583a1.686 1.686 0 0 1 .998-.827 2.272 2.272 0 0 1 .61-.06 24.542 24.542 0 0 1 3.777.477 15.467 15.467 0 0 1-3.39 2.818 1.67 1.67 0 0 1-1.89-.665l1.535-.475a.5.5 0 1 0-.295-.955l-1.536.475a1.677 1.677 0 0 1 .188-.788zm10.16 9.5l-3.86-.496-4.64-3.71a.504.504 0 0 0-.314-.11H7.28a.5.5 0 0 0-.474.347l-1.186 3.61-2.194.33A.5.5 0 0 0 3 15.78v3.72a.5.5 0 0 0 .5.5h2.278a1.982 1.982 0 0 0 3.444 0h5.556a1.982 1.982 0 0 0 3.444 0H20.5a.5.5 0 0 0 .5-.5v-3.688a.5.5 0 0 0-.437-.496zM7.5 20a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm9 0a1 1 0 1 1 1-1 1 1 0 0 1-1 1zm3.5-1h-1.5a2 2 0 0 0-4 0h-5a2 2 0 0 0-4 0H4v-2.788l2.074-.312a.5.5 0 0 0 .4-.338L7.644 12h3.93l4.614 3.69a.498.498 0 0 0 .25.106l3.563.457z"></path></symbol><symbol id="24x24_ice_cream" height="24" viewBox="0 0 24 24" width="24"><path d="M17.5 7.27l-.305-.176A5.198 5.198 0 0 0 12 2a5.198 5.198 0 0 0-5.195 5.094L6.5 7.27a3.466 3.466 0 0 0-1.268 4.735 3.43 3.43 0 0 0 2.688 1.7l3.155 7.675c.34.827 1.51.827 1.85 0l3.155-7.674a3.43 3.43 0 0 0 2.688-1.7 3.466 3.466 0 0 0-1.27-4.736zm-.464 3.735c-.26.45-.732.72-1.263.72a1.46 1.46 0 0 1-.28-.026l-1.065-.204-.75.78a2.308 2.308 0 0 1-3.355 0l-.75-.78-1.066.202a1.46 1.46 0 0 1-.28.025 1.44 1.44 0 0 1-1.263-.72c-.404-.7-.163-1.6.537-2.003l.306-.176.977-.564.023-1.128A3.214 3.214 0 0 1 12 4a3.214 3.214 0 0 1 3.195 3.134l.023 1.128.977.564.304.176c.7.404.94 1.303.535 2.003z"></path></symbol><symbol id="24x24_info" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14c0 .55-.45 1-1 1s-1-.45-1-1v-4c0-.55.45-1 1-1s1 .45 1 1v4zm-1-6c-.83 0-1.5-.67-1.5-1.5S11.17 7 12 7s1.5.67 1.5 1.5S12.83 10 12 10z"></path></symbol><symbol id="24x24_info_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.48 22 2 17.52 2 12S6.48 2 12 2s10 4.48 10 10-4.48 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm0 7c-.83 0-1.5-.67-1.5-1.5S11.17 7 12 7s1.5.67 1.5 1.5S12.83 10 12 10zm0 1c.55 0 1 .45 1 1v4c0 .55-.45 1-1 1s-1-.45-1-1v-4c0-.55.45-1 1-1z"></path></symbol><symbol id="24x24_instagram" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3H6a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3V6a3 3 0 0 0-3-3zm-6 5.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zm7 9.5c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-8h1.894a5.416 5.416 0 0 0-.394 2c0 3.033 2.467 5.5 5.5 5.5s5.5-2.467 5.5-5.5c0-.708-.148-1.378-.394-2H19v8zm0-11a1 1 0 0 1-1 1h-1a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1v1z"></path></symbol><symbol id="24x24_insurance" height="24" viewBox="0 0 24 24" width="24"><path d="M19 19H5a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3h14a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3zm1-11a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v8c0 .55.45 1 1 1h14c.55 0 1-.45 1-1V8zm-7 8h-2v-3H8v-2h3V8h2v3h3v2h-3v3z"></path></symbol><symbol id="24x24_key" height="24" viewBox="0 0 24 24" width="24"><path d="M21 10h-8.35A5.996 5.996 0 0 0 1 12a5.996 5.996 0 0 0 11.65 2H14v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h1v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1a2 2 0 0 0 0-4zM7 14a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path></symbol><symbol id="24x24_keyboard_active" height="24" viewBox="0 0 24 24" width="24"><path d="M20.532 18.993v-1.23h-.12c-.373.704-1.192 1.378-2.653 1.378-1.93 0-3.26-1.133-3.26-3 0-1.775 1.235-2.95 3.525-2.95h2.384v-.85c0-.88-.605-1.313-1.555-1.313-.96 0-1.415.417-1.527 1.008h-2.47c.094-1.6 1.22-3.032 4.04-3.032C21.166 9 23 9.898 23 12.42v6.573h-2.468zm-.12-4.252h-1.78c-1.032 0-1.535.5-1.535 1.206 0 .84.736 1.266 1.536 1.266.968 0 1.78-.61 1.78-1.47v-1zM9.722 16H5.08l-1.065 3H1L5.716 5h3.59L14 19h-3.234l-1.043-3zm-2.24-8H7.35l-1.525 5h3.162L7.482 8z"></path></symbol><symbol id="24x24_keyboard_inactive" height="24" viewBox="0 0 24 24" width="24"><path d="M21.214 18.98v-1.43h-.056c-.398.725-1.31 1.59-2.924 1.59-1.876 0-3.157-1.166-3.157-2.974 0-1.676 1.15-2.825 3.352-2.825h2.737v-1.156c0-1.47-.92-2.12-2.33-2.12-1.46 0-2.053.65-2.23 1.357h-1.14C15.597 9.924 16.84 9 18.892 9c1.94 0 3.454.904 3.454 3.126v6.855h-1.133zm-.046-4.632h-2.72c-1.524 0-2.155.763-2.155 1.79 0 1.28.994 1.968 2.2 1.968 1.496 0 2.675-1.036 2.675-2.468v-1.29zM10.188 15H4.65l-1.547 4H1.776L6.798 5h1.304l5.023 14h-1.388l-1.548-4zm-2.73-8h-.064l-2.42 7h4.893l-2.41-7z"></path></symbol><symbol id="24x24_kids" height="24" viewBox="0 0 24 24" width="24"><path d="M20.533 6.8A2.136 2.136 0 0 0 18.4 8.933V9h-2.133v-.067a4.27 4.27 0 0 1 4.266-4.266 1.066 1.066 0 0 1 0 2.133zm-4.69 9.043a3.46 3.46 0 0 0-1.484-.343c-1.565 0-2.895 1.083-3.343 2.5H9.7c-.457-1.405-1.787-2.5-3.34-2.5a3.47 3.47 0 0 0-1.44.318A7.97 7.97 0 0 1 2.4 10c0-4.25 3.408-7.716 7.6-7.975V11h8.32a8.005 8.005 0 0 1-2.476 4.843zM6.36 16.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 3.5a1 1 0 1 0-.002-2 1 1 0 0 0 0 2zm8-3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 3.5a1 1 0 1 0-.002-2 1 1 0 0 0 0 2z"></path></symbol><symbol id="24x24_king" height="24" viewBox="0 0 24 24" width="24"><path d="M18.74 6.88l-6.154 1.023A1.994 1.994 0 0 0 12 4a1.994 1.994 0 0 0-.586 3.903L5.26 6.88c-2.31-.39-4.15 1.9-3.28 4.07L2 11l2 5h-.33a1 1 0 0 0 0 2h16.66a1 1 0 0 0 0-2H20l2-5 .02-.05c.87-2.17-.97-4.46-3.28-4.07zM17 10.5l1.5 1.5-1.5 1.5-1.5-1.5 1.5-1.5zm-5-.5l2 2-2 2-2-2 2-2zm-5 .5L8.5 12 7 13.5 5.5 12 7 10.5z"></path></symbol><symbol id="24x24_light_bulb" height="24" viewBox="0 0 24 24" width="24"><path d="M15 15.32V18H9v-2.68C6.64 14.19 5 11.79 5 9c0-3.87 3.13-7 7-7s7 3.13 7 7c0 2.79-1.64 5.19-4 6.32zM10.5 6C9.67 6 9 6.67 9 7.5S9.67 9 10.5 9 12 8.33 12 7.5 11.33 6 10.5 6zM13 22h-2a2 2 0 0 1-2-2h6a2 2 0 0 1-2 2z"></path></symbol><symbol id="24x24_light_bulb_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M15 15.32V18H9v-2.68C6.64 14.19 5 11.79 5 9c0-3.87 3.13-7 7-7s7 3.13 7 7c0 2.79-1.64 5.19-4 6.32zM12 3C8.692 3 6 5.69 6 9c0 2.293 1.347 4.42 3.432 5.418l.568.272V17h4v-2.31l.568-.272C16.653 13.42 18 11.293 18 9c0-3.31-2.692-6-6-6zm-1.5 6C9.67 9 9 8.33 9 7.5S9.67 6 10.5 6s1.5.67 1.5 1.5S11.33 9 10.5 9zM13 22h-2a2 2 0 0 1-2-2h6a2 2 0 0 1-2 2z"></path></symbol><symbol id="24x24_lightning_bolt" height="24" viewBox="0 0 24 24" width="24"><path d="M18.63 11.692l-9.65 10.07c-.823.857-2.188-.18-1.584-1.202L11.273 14h-5.18c-.88 0-1.33-1.056-.722-1.692l9.65-10.07c.825-.857 2.19.18 1.586 1.202L12.726 10h5.18c.88 0 1.33 1.056.723 1.692z"></path></symbol><symbol id="24x24_like" height="24" viewBox="0 0 24 24" width="24"><path d="M21.164 12.236c.05.164.086.334.086.514 0 .66-.37 1.23-.91 1.527.1.22.16.464.16.723 0 .66-.37 1.23-.91 1.527.1.22.16.464.16.723A1.75 1.75 0 0 1 18 19H7v-9h1c.37 0 1.257-2.37 2.104-3.345.89-1.017 1.234-1.782 1.457-2.513C11.785 3.412 12 2 12 2s2.388.11 2.388 2.9c0 1.39-.758 3.1-.388 4.1h6.25c.966 0 1.75.784 1.75 1.75 0 .63-.336 1.178-.836 1.486zM2 10h4v10H2V10z"></path></symbol><symbol id="24x24_like_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.164 12.236c.05.164.086.334.086.514 0 .66-.37 1.23-.91 1.527.1.22.16.464.16.723 0 .66-.37 1.23-.91 1.527.1.22.16.464.16.723A1.75 1.75 0 0 1 18 19H7v-9h1c.37 0 1.257-2.37 2.104-3.345.89-1.017 1.234-1.782 1.457-2.513C11.785 3.412 12 2 12 2s2.388.11 2.388 2.9c0 1.39-.758 3.1-.388 4.1h6.25c.966 0 1.75.784 1.75 1.75 0 .63-.336 1.178-.836 1.486zM20.25 10h-6.946l-.242-.653c-.316-.855-.11-1.862.09-2.835.117-.56.236-1.14.236-1.61 0-.844-.283-1.314-.608-1.577-.076.387-.168.797-.262 1.107-.228.748-.604 1.673-1.66 2.88-.336.386-.744 1.166-1.072 1.794C9.146 10.326 8.796 11 8 11v7h10a.75.75 0 0 0 .75-.75.75.75 0 0 0-.07-.308l-.385-.843.812-.45A.74.74 0 0 0 19.5 15a.75.75 0 0 0-.07-.308l-.385-.843.812-.45a.74.74 0 0 0 .393-.65.793.793 0 0 0-.04-.22l-.23-.74.66-.406A.746.746 0 0 0 20.25 10zM2 10h4v10H2V10z"></path></symbol><symbol id="24x24_line" height="24" viewBox="0 0 24 24" width="24"><path d="M19.855 15.57c-2.096 2.41-6.788 5.347-7.856 5.795-1.07.45-.91-.285-.87-.537l.142-.855c.033-.255.068-.65-.032-.902-.11-.272-.554-.42-.88-.49C5.558 17.948 2 14.59 2 10.59c0-4.465 4.486-8.097 10-8.097 5.513 0 10 3.632 10 8.097 0 1.787-.694 3.397-2.145 4.98zM7.51 11.966H6.05V8.523a.524.524 0 0 0-1.05 0v3.965c0 .29.235.524.525.524H7.51a.524.524 0 0 0 0-1.047zm2.54-3.442a.525.525 0 0 0-1.05 0v3.965a.525.525 0 0 0 1.05 0V8.52zm4.98 0a.525.525 0 0 0-1.05 0v2.454L11.944 8.21a.527.527 0 0 0-.586-.183.523.523 0 0 0-.358.496v3.965a.525.525 0 0 0 1.048 0v-2.452l2.037 2.766a.525.525 0 0 0 .944-.314V8.523zm3.48 2.506a.524.524 0 0 0 0-1.047h-1.46v-.936h1.463a.524.524 0 0 0 0-1.047h-1.986a.524.524 0 0 0-.524.523v3.965c0 .29.235.524.524.524h1.987a.525.525 0 0 0 0-1.047H17.05v-.936h1.463z"></path></symbol><symbol id="24x24_linkedin" height="24" viewBox="0 0 24 24" width="24"><path d="M8 19H5V9h3v10zM6.5 8a2 2 0 0 1 0-4 2 2 0 0 1 0 4zM20 19h-3v-4.98c0-1.16-.277-2.656-1.875-2.656-1.62 0-2.125 1.266-2.125 2.574V19h-3V9h3v1h.212c.415-1 1.484-1.497 3-1.497C19.364 8.503 20 10.7 20 13.398V19z"></path></symbol><symbol id="24x24_list" height="24" viewBox="0 0 24 24" width="24"><path d="M7 18v-2h14v2H7zM7 6h14v2H7V6zM3 16h2v2H3v-2zm0-5h2v2H3v-2zm0-5h2v2H3V6zm14 7H7v-2h10v2z"></path></symbol><symbol id="24x24_location" height="24" viewBox="0 0 24 24" width="24"><path d="M3 12.73L20 4l-8.73 17-.696-7.574L3 12.73z"></path></symbol><symbol id="24x24_location_android" height="24" viewBox="0 0 24 24" width="24"><path d="M21 13h-1.574A7.494 7.494 0 0 1 13 19.426V21a1 1 0 0 1-2 0v-1.574A7.494 7.494 0 0 1 4.574 13H3a1 1 0 0 1 0-2h1.574A7.494 7.494 0 0 1 11 4.574V3a1 1 0 0 1 2 0v1.574A7.494 7.494 0 0 1 19.426 11H21a1 1 0 0 1 0 2zm-9-6.5A5.506 5.506 0 0 0 6.5 12c0 3.033 2.467 5.5 5.5 5.5s5.5-2.467 5.5-5.5-2.467-5.5-5.5-5.5zm0 8.5a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"></path></symbol><symbol id="24x24_location_outline" height="20" viewBox="0 0 20 20" width="20"><path d="M17.69 2.31l-7.28 14.175-.503-5.488-.076-.828-.827-.078-5.486-.504L17.69 2.31M20 0L0 10.27l8.91.82.82 8.91L20 0z"></path></symbol><symbol id="24x24_magic_wand" height="24" viewBox="0 0 24 24" width="24"><path d="M6.343 21.9L2.1 17.656 17.658 2.1 21.9 6.343 6.342 21.9zm8.485-14.143l1.415 1.414 2.828-2.826L17.66 4.93l-2.83 2.827zM6 10L4.865 7.135 2 6l2.865-1.135L6 2l1.135 2.865L10 6 7.135 7.135 6 10zm12.5 5.5l.85 2.15 2.15.85-2.15.85-.85 2.15-.85-2.15-2.15-.85 2.15-.85.85-2.15z"></path></symbol><symbol id="24x24_mail" height="24" viewBox="0 0 24 24" width="24"><path d="M21.44 17.734L15.708 12l5.734-5.734c.35.49.56 1.086.56 1.734v8a2.97 2.97 0 0 1-.56 1.734zm-11.208-5.21L3.266 5.56A2.97 2.97 0 0 1 5 5h14c.648 0 1.244.21 1.734.56l-6.966 6.965a2.503 2.503 0 0 1-3.536 0zm-7.673 5.21A2.977 2.977 0 0 1 2 16V8c0-.648.21-1.244.56-1.734L8.292 12 2.56 17.734zm6.963-4.502A3.487 3.487 0 0 0 12 14.256a3.49 3.49 0 0 0 2.475-1.024l.525-.525 5.734 5.734A2.97 2.97 0 0 1 19 19H5a2.97 2.97 0 0 1-1.734-.56L9 12.71l.525.525z"></path></symbol><symbol id="24x24_mail_open" height="24" viewBox="0 0 24 24" width="24"><path d="M21.44 20.734L15.708 15 22 10v9a2.97 2.97 0 0 1-.56 1.734zm-18.88 0A2.977 2.977 0 0 1 2 19v-9l6.293 5-5.734 5.734zM9.992 2.806a3 3 0 0 1 4.014 0L22 10H2l7.993-7.194zm-.468 13.426A3.49 3.49 0 0 0 12 17.256c.897 0 1.792-.34 2.475-1.024l.525-.525 5.734 5.734A2.97 2.97 0 0 1 19 22H5a2.97 2.97 0 0 1-1.734-.56L9 15.71l.525.525z"></path></symbol><symbol id="24x24_mail_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M19 5H5a3 3 0 0 0-3 3v8a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V8a3 3 0 0 0-3-3zm2 3v8c0 .402-.122.774-.326 1.088l-4.967-4.967 5.052-5.05c.146.28.24.594.24.93zM5 6h14c.402 0 .774.12 1.088.326l-6.32 6.32a2.505 2.505 0 0 1-3.536 0l-6.32-6.32A1.987 1.987 0 0 1 5 6zM3 8c0-.338.092-.65.24-.93l5.053 5.05-4.967 4.968A1.987 1.987 0 0 1 3 16V8zm2 10a1.97 1.97 0 0 1-.93-.24L9 12.827l.525.525A3.49 3.49 0 0 0 12 14.377a3.49 3.49 0 0 0 2.475-1.024l.525-.525 4.93 4.93A1.95 1.95 0 0 1 19 18H5z"></path></symbol><symbol id="24x24_map" height="24" viewBox="0 0 24 24" width="24"><path d="M15 18.576V3.288l6 2.182v15.288l-6-2.182zm-5-12.91L14 3v15.258l-4 2.667V5.667zM3 3.532l6 2.183V21l-6-2.182V3.53z"></path></symbol><symbol id="24x24_map_marker" height="24" viewBox="0 0 24 24" width="24"><path d="M17 18.576V3.288l6 2.182v15.288l-6-2.182zm-5-12.91L16 3v15.258l-4 2.667V5.667zM9 16a5 5 0 0 0-4-4.9V3.29l6 2.182V20.76l-3.44-1.25A4.98 4.98 0 0 0 9 16zm-2 0a3 3 0 0 1-1.327 2.49L4 21l-1.674-2.51A3 3 0 1 1 7 16zm-3-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"></path></symbol><symbol id="24x24_marker" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C8.13 2 5 5.13 5 9c0 2.61 1.43 4.88 3.54 6.08L12 22l3.46-6.92A6.987 6.987 0 0 0 19 9c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 0 1 0-5 2.5 2.5 0 0 1 0 5z"></path></symbol><symbol id="24x24_marker_grouped" height="24" viewBox="0 0 24 24" width="24"><g><path d="M20.755 15.578L19 19l-1.755-3.422a4.05 4.05 0 0 1-1.18-.887 7.025 7.025 0 0 0 1.593-1.58c.32.39.8.64 1.342.64a1.75 1.75 0 0 0 0-3.5l-.12.014c.075-.41.12-.83.12-1.262a7.05 7.05 0 0 0-.078-.99L19 8a4 4 0 0 1 4 4c0 1.576-.92 2.926-2.245 3.578zM5 19l-1.755-3.422A3.988 3.988 0 0 1 1 12a4 4 0 0 1 4-4l.078.008A7.05 7.05 0 0 0 5 9c0 .432.045.852.12 1.262L5 10.25a1.75 1.75 0 0 0 0 3.5c.543 0 1.02-.252 1.342-.64a6.98 6.98 0 0 0 1.592 1.58 4.05 4.05 0 0 1-1.18.888L5 19z" opacity=".502"></path><path d="M18 9a6 6 0 1 0-8.863 5.274L12 21l2.863-6.726A5.998 5.998 0 0 0 18 9zm-6-2.5a2.5 2.5 0 0 1 0 5 2.5 2.5 0 0 1 0-5z"></path></g></symbol><symbol id="24x24_massage" height="24" viewBox="0 0 24 24" width="24"><path d="M24 5h-9V4a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v1H6v-.5a2.5 2.5 0 0 0-5 0V5H0v4h2v12h2v-3h16v3h2V9h2V5zM9 5h4v7H9V5zm11 11H4V9h3v4a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V9h5v7z"></path></symbol><symbol id="24x24_medical" height="24" viewBox="0 0 24 24" width="24"><path d="M15 9V4H9v5H4v6h5v5h6v-5h5V9h-5z"></path></symbol><symbol id="24x24_menu" height="24" viewBox="0 0 24 24" width="24"><path d="M3 22V2h18v20H3zM19 4H5v16h14V4zm-6 5H7V7h6v2zm0 4H7v-2h6v2zm0 4H7v-2h6v2zm4-8h-2V7h2v2zm0 4h-2v-2h2v2zm0 4h-2v-2h2v2z"></path></symbol><symbol id="24x24_menu_filled" height="24" viewBox="0 0 24 24" width="24"><path d="M3 2v20h18V2H3zm10 15H7v-2h6v2zm0-4H7v-2h6v2zm0-4H7V7h6v2zm4 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V7h2v2z"></path></symbol><symbol id="24x24_menu_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M3 22V2h18v20H3zM20 3H4v18h16V3zm-7 5.5H7v-1h6v1zm0 4H7v-1h6v1zm0 4H7v-1h6v1zm4-8h-2v-1h2v1zm0 4h-2v-1h2v1zm0 4h-2v-1h2v1z"></path></symbol><symbol id="24x24_merge" height="24" viewBox="0 0 24 24" width="24"><path d="M16 14c-2.757 0-5-2.243-5-5V8h4l-5-5-5 5h4v13h2v-7.11A6.977 6.977 0 0 0 16 16h3v-2h-3z"></path></symbol><symbol id="24x24_message" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3H6C4.34 3 3 4.34 3 6v7c0 1.66 1.34 3 3 3h2v5l5-5h5c1.66 0 3-1.34 3-3V6c0-1.66-1.34-3-3-3z"></path></symbol><symbol id="24x24_message_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 4c1.103 0 2 .897 2 2v7c0 1.103-.897 2-2 2h-5.414l-.293.293L9 18.586V15H6c-1.103 0-2-.897-2-2V6c0-1.103.897-2 2-2h12m0-1H6C4.34 3 3 4.34 3 6v7c0 1.66 1.34 3 3 3h2v5l5-5h5c1.66 0 3-1.34 3-3V6c0-1.66-1.34-3-3-3z"></path></symbol><symbol id="24x24_messenger" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2.92c-4.965 0-8.99 3.763-8.99 8.405 0 2.64 1.303 4.998 3.34 6.54v3.216l3.068-1.7a9.57 9.57 0 0 0 2.582.35c4.965 0 8.99-3.76 8.99-8.403 0-4.642-4.025-8.406-8.99-8.406zm.947 11.27l-2.325-2.414-4.478 2.476 4.91-5.21 2.324 2.416 4.478-2.476-4.91 5.21z"></path></symbol><symbol id="24x24_mobile" height="24" viewBox="0 0 24 24" width="24"><path d="M17 22H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2zm-5-1a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5-16a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V5z"></path></symbol><symbol id="24x24_money" height="24" viewBox="0 0 24 24" width="24"><path d="M6 19v-2h14V9h2v10H6zM2 5h16v10H2V5zm8 7.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z"></path></symbol><symbol id="24x24_monocle" height="24" viewBox="0 0 24 24" width="24"><path d="M20.992 19a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0-3a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm-1-3H17.73c-.89 3.45-4.012 6-7.738 6a8 8 0 0 1-8-8 8 8 0 0 1 8-8c3.726 0 6.848 2.55 7.738 6h2.262a2 2 0 0 1 0 4zm-10-8c-3.31 0-6 2.692-6 6s2.69 6 6 6c3.308 0 6-2.692 6-6s-2.692-6-6-6zm11 15a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></symbol><symbol id="24x24_monocle_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21 19a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0-3a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm-1-3h-2.262c-.89 3.45-4.012 6-7.738 6a8 8 0 0 1 0-16c3.726 0 6.848 2.55 7.738 6H20a2 2 0 0 1 0 4zM10 4c-3.86 0-7 3.14-7 7s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm11 16a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></symbol><symbol id="24x24_moon" height="24" viewBox="0 0 24 24" width="24"><path d="M17.445 16.555c-5.523 0-10-4.477-10-10a9.95 9.95 0 0 1 .89-4.11c-3.47 1.57-5.89 5.053-5.89 9.11 0 5.523 4.477 10 10 10 4.057 0 7.54-2.42 9.11-5.89a9.95 9.95 0 0 1-4.11.89z"></path></symbol><symbol id="24x24_more" height="24" viewBox="0 0 24 24" width="24"><path d="M20 14a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-8 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-8 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"></path></symbol><symbol id="24x24_more_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20 11c.6 0 1 .4 1 1s-.4 1-1 1-1-.4-1-1 .4-1 1-1m-8 0c.6 0 1 .4 1 1s-.4 1-1 1-1-.4-1-1 .4-1 1-1m-8 0c.6 0 1 .4 1 1s-.4 1-1 1-1-.4-1-1 .4-1 1-1m16-1c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-8 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-8 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></symbol><symbol id="24x24_music" height="24" viewBox="0 0 24 24" width="24"><path d="M8 6v11.01a4.68 4.68 0 0 0-1.707.235c-1.61.53-2.598 1.744-2.208 2.713.39.97 2.013 1.326 3.622.797 1.38-.453 2.3-1.408 2.293-2.282V11.5l8-2v5.51a4.68 4.68 0 0 0-1.707.235c-1.61.53-2.598 1.744-2.208 2.713.39.97 2.013 1.326 3.622.797 1.346-.442 2.258-1.363 2.293-2.22V3L8 6z"></path></symbol><symbol id="24x24_nearby" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-18c-4.41 0-8 3.59-8 8s3.59 8 8 8 8-3.59 8-8-3.59-8-8-8zm-1.034 9.084l-3.96-.364 8.888-4.564-4.564 8.888-.364-3.96z"></path></symbol><symbol id="24x24_nearby_filled" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm-.67 15.044l-.364-3.96-3.96-.364 8.888-4.564-4.564 8.888z"></path></symbol><symbol id="24x24_nearby_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm-1.034 10.084l-3.96-.364 8.888-4.564-4.564 8.888-.364-3.96z"></path></symbol><symbol id="24x24_night" height="24" viewBox="0 0 24 24" width="24"><path d="M15 15.98a7.5 7.5 0 0 1-7.5-7.5 7.49 7.49 0 0 1 3.703-6.46C6.053 2.428 2 6.726 2 11.98c0 5.523 4.477 10 10 10s10-4.477 10-10c0-.245-.02-.485-.037-.725A7.497 7.497 0 0 1 15 15.98z"></path></symbol><symbol id="24x24_nightlife" height="24" viewBox="0 0 24 24" width="24"><path d="M19.215 3H4.785C3.095 3 2.29 5.08 3.54 6.22L11 13v6H8a1 1 0 0 0 0 2h8a1 1 0 0 0 0-2h-3v-6l7.46-6.78C21.71 5.08 20.905 3 19.214 3zM15 4.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z"></path></symbol><symbol id="24x24_no_bars" height="24" viewBox="0 0 24 24" width="24"><path d="M24 20.586L22.586 22l-2.122-2.12-2.12 2.12-1.415-1.414 2.12-2.122-2.12-2.12 1.41-1.415 2.12 2.12 2.123-2.12L24 16.34l-2.12 2.12L24 20.587zM14.5 18.5c0 .89.19 1.74.55 2.5H13V3h4v10.63a5.993 5.993 0 0 0-2.5 4.87zM7 8h4v13H7V8zm-6 5h4v8H1v-8z"></path></symbol><symbol id="24x24_no_cash" height="24" viewBox="0 0 24 24" width="24"><path d="M23.535 20.12l-1.414 1.416L20 19.414l-2.12 2.122-1.416-1.415L18.586 18l-2.122-2.12 1.415-1.416L20 16.586l2.12-2.122 1.415 1.415-2.12 2.12 2.12 2.12zM20 9h2v3.35a5.97 5.97 0 0 0-2-.35V9zm-5.19 6H2V5h16v7.35A6.01 6.01 0 0 0 14.81 15zM10 7.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM14 18c0 .342.035.674.09 1H6v-2h8.09c-.055.326-.09.658-.09 1z"></path></symbol><symbol id="24x24_nope" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm8 10a7.95 7.95 0 0 1-1.688 4.898L7.102 5.688A7.95 7.95 0 0 1 12 4c4.41 0 8 3.59 8 8zM4 12a7.95 7.95 0 0 1 1.688-4.898l11.21 11.21A7.953 7.953 0 0 1 12 20c-4.41 0-8-3.59-8-8z"></path></symbol><symbol id="24x24_notification" height="24" viewBox="0 0 24 24" width="24"><path d="M20.984 17.177A1 1 0 0 1 20 18H4a1 1 0 0 1-.348-1.938c2.43-.9 3.74-4.605 3.74-7.634 0-1.75 1.07-3.253 2.608-3.97V4a2 2 0 0 1 4 0v.457c1.538.718 2.61 2.22 2.61 3.97 0 3.03 1.31 6.734 3.738 7.635a1 1 0 0 1 .636 1.115zM12 22a3 3 0 0 1-3-3h6a3 3 0 0 1-3 3z"></path></symbol><symbol id="24x24_notification_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20.984 17.177A1 1 0 0 1 20 18H4a1 1 0 0 1-.348-1.938c2.43-.9 3.74-4.605 3.74-7.634 0-1.75 1.07-3.253 2.608-3.97V4a2 2 0 0 1 4 0v.457c1.538.718 2.61 2.22 2.61 3.97 0 3.03 1.31 6.734 3.738 7.635a1 1 0 0 1 .636 1.115zm-5.375-8.75C15.61 6.537 13.99 5 12 5c-1.993 0-3.61 1.535-3.61 3.428C8.39 11.87 6.873 15.934 4 17h16c-2.872-1.066-4.39-5.13-4.39-8.572zM12 22a3 3 0 0 1-3-3h6a3 3 0 0 1-3 3z"></path></symbol><symbol id="24x24_oem_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M21.755 5.262l-.24-.38-3.384 3.383c0 .005-.6.532-1.33.532-.45 0-.875-.197-1.264-.587-1.23-1.23-.18-2.468-.065-2.592l3.44-3.44-.47-.217c-.04-.01-.94-.42-2.285-.42-1.18 0-2.96.33-4.757 1.89-2.55 2.22-1.33 5.477-.912 6.395-1.123 1.1-2.6 2.383-4.027 3.623-1.523 1.325-3.097 2.69-4.26 3.855l-.043.053c-.704 1.035-.782 2.245-.213 3.32.578 1.09 1.718 1.796 2.906 1.796.644 0 1.263-.2 1.84-.59l.05-.042c1.16-1.16 2.54-2.714 3.874-4.218 1.267-1.43 2.576-2.903 3.69-4.03a7.05 7.05 0 0 0 2.023.295c1.53 0 2.9-.522 3.967-1.508 3.72-3.445 1.485-7.077 1.462-7.113zM19.8 11.846c-.945.874-2.115 1.317-3.478 1.317-1.133 0-1.986-.32-1.994-.323l-.218-.083-.165.165c-1.16 1.16-2.54 2.714-3.874 4.217-1.31 1.48-2.68 3.02-3.82 4.16a2.518 2.518 0 0 1-1.4.44c-.922 0-1.813-.558-2.27-1.417-.433-.82-.38-1.75.156-2.553 1.14-1.14 2.695-2.49 4.197-3.794 1.517-1.32 3.086-2.68 4.245-3.84l.19-.19-.13-.238c-.02-.036-1.91-3.538.638-5.75 1.307-1.137 2.75-1.713 4.284-1.713.61 0 1.12.097 1.47.19l-2.68 2.68c-.584.636-1.318 2.207.076 3.6.53.53 1.128.798 1.776.798 1.025 0 1.79-.692 1.834-.732l2.723-2.72c.4.95 1.03 3.393-1.554 5.783z"></path><path d="M5.094 17.33c-.893 0-1.62.728-1.62 1.62 0 .894.727 1.62 1.62 1.62.893 0 1.62-.726 1.62-1.62 0-.893-.727-1.62-1.62-1.62zm0 2.52a.9.9 0 0 1-.9-.9c0-.495.404-.9.9-.9s.9.405.9.9a.9.9 0 0 1-.9.9z"></path></symbol><symbol id="24x24_oil_change_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M11.53 18.5A2.532 2.532 0 0 1 9 15.97c0-1.215 1.765-3.83 2.118-4.343a.52.52 0 0 1 .823 0c.356.512 2.12 3.128 2.12 4.344a2.532 2.532 0 0 1-2.53 2.53zm0-5.685A9.896 9.896 0 0 0 10 15.97a1.53 1.53 0 0 0 3.06 0 9.903 9.903 0 0 0-1.53-3.155z"></path><path d="M18.5 2h-6a.5.5 0 0 0-.5.5v2a.5.5 0 0 0 .5.5h.5v.187l-7.832 6.94A.5.5 0 0 0 5 12.5v9a.5.5 0 0 0 .5.5h12a.5.5 0 0 0 .5-.5V5h.5a.5.5 0 0 0 .5-.5v-2a.5.5 0 0 0-.5-.5zM17 21H6v-8.275l7.832-6.94A.5.5 0 0 0 14 5.41V5h3zm1-17h-5V3h5z"></path></symbol><symbol id="24x24_order" height="24" viewBox="0 0 24 24" width="24"><g><path d="M19 10V4h-6v10H9.444a3.485 3.485 0 0 0-4.888 0H2v3h1.55A3.49 3.49 0 0 0 7 20a3.49 3.49 0 0 0 3.45-3h3.1c.24 1.69 1.69 3 3.45 3 1.76 0 3.21-1.31 3.45-3H22v-5l-3-2zM7 18a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm8-12h2v3h-2V6zm2 12c-.83 0-1.5-.67-1.5-1.5S16.17 15 17 15s1.5.67 1.5 1.5S17.83 18 17 18z"></path><path d="M6 7V6c0-.55.45-1 1-1h1c.55 0 1 .45 1 1v1H6m2-4H7a3 3 0 0 0-3 3v1H2v7h11V7h-2V6a3 3 0 0 0-3-3" opacity=".502"></path></g></symbol><symbol id="24x24_order_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M22 12l-3-2V4h-6v2h-3V3H5v3H2v11h2.55a2.5 2.5 0 1 0 4.9 0h5.1a2.5 2.5 0 1 0 4.9 0H22v-5zM6 4h3v2H6V4zm1 15c-.827 0-1.5-.673-1.5-1.5S6.173 16 7 16s1.5.673 1.5 1.5S7.827 19 7 19zm6-3H8.99A2.49 2.49 0 0 0 7 15a2.49 2.49 0 0 0-1.99 1H3V7h10v9zm2-7V6h2v3h-2zm2 10c-.827 0-1.5-.673-1.5-1.5S16.173 16 17 16s1.5.673 1.5 1.5S17.827 19 17 19z"></path></symbol><symbol id="24x24_outdoor_seating" height="24" viewBox="0 0 24 24" width="24"><path d="M21 11V7.704l-.16-.248C18.824 4.353 15.52 2.5 12 2.5c-3.522 0-6.826 1.853-8.84 4.956L3 7.704V11h8v8H8v2h8v-2h-3v-8h8zM5 8.304C6.653 5.916 9.25 4.5 12 4.5s5.346 1.416 7 3.804V9H5v-.696z"></path></symbol><symbol id="24x24_palette" height="24" viewBox="0 0 24 24" width="24"><path d="M11.85 3c-4.73.08-8.7 3.99-8.85 8.72-.02.62.03 1.23.13 1.82A3.003 3.003 0 0 0 6.09 16H11c.55 0 1 .45 1 1v.19c0 2.3 2.49 3.76 4.49 2.61A9.002 9.002 0 0 0 11.85 3zM8 11.5c-.83 0-1.5-.67-1.5-1.5S7.17 8.5 8 8.5s1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4-3c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm3 8c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm1-5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"></path></symbol><symbol id="24x24_paper_plane" height="24" viewBox="0 0 24 24" width="24"><path d="M22 5L2 10.5l5.508 2.507L17.455 8l-8.382 5.87-1.618 4.63 3.41-2.95 3.86 3.45L22 5z"></path></symbol><symbol id="24x24_parking" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm4.308-13.282a3.13 3.13 0 0 0-.604-1.126 3.016 3.016 0 0 0-1.074-.794c-.442-.2-.974-.298-1.603-.298H8.5v11h2.207v-3.943h2.32c.63 0 1.16-.102 1.603-.3.44-.202.8-.467 1.074-.795.277-.328.477-.707.604-1.132.13-.427.192-.86.192-1.303 0-.45-.063-.888-.192-1.31zm-2.537 2.657a1.55 1.55 0 0 1-.612.238 4.115 4.115 0 0 1-.73.063H10.71V8.378h1.715c.253 0 .497.02.73.063.234.04.44.12.618.24.18.12.322.29.43.5.11.22.16.5.16.85s-.05.63-.16.85a1.26 1.26 0 0 1-.43.5z"></path></symbol><symbol id="24x24_party" height="24" viewBox="0 0 24 24" width="24"><path d="M15.14 14.96L17 18h-2v5h-1v-5h-2l1.86-3.04C10.85 14.586 8.5 11.616 8.5 8c0-3.87 2.69-7 6-7s6 3.13 6 7c0 3.617-2.35 6.587-5.36 6.96zM12.39 3.55c-.54-.14-1.14.39-1.36 1.19-.21.8.05 1.57.58 1.71.54.14 1.14-.39 1.36-1.19.21-.8-.05-1.57-.58-1.71zm-.45 11.89a4.737 4.737 0 0 1-2.82 1.49L10.5 19H9v4H8v-4H6.5l1.367-2.05c-2.53-.365-4.487-2.88-4.487-5.93 0-3.1 2.02-5.66 4.61-5.95-.32.91-.49 1.9-.49 2.93 0 3.38 1.84 6.27 4.44 7.44z"></path></symbol><symbol id="24x24_paypal" height="24" viewBox="0 0 24 24" width="24"><path d="M19.5 11.445C18.855 14.758 16.647 16 13.827 16h-.436a.7.7 0 0 0-.69.59l-.61 3.82a.7.7 0 0 1-.69.59H8.6l1.16-7.178c.017-.12.06-.185.072-.195 0 0 .026-.014.104-.014h1.642c.962 0 1.84-.113 2.61-.334 2.078-.6 3.48-1.97 4.168-4.08.16-.49.267-.95.343-1.39.98.852 1.05 2.35.8 3.63zm-5.587.873c-.687.197-1.465.295-2.335.295H9.936c-.768 0-1.087.55-1.165 1.055l-.843 5.335h-3.07a.48.48 0 0 1-.473-.555L6.71 3.676A.802.802 0 0 1 7.5 3h5.21c1.926 0 3.418.42 4.266 1.357.84.93 1.167 2.27.43 4.533-.587 1.797-1.755 2.93-3.493 3.428z"></path></symbol><symbol id="24x24_pdf" height="24" viewBox="0 0 24 24" width="24"><path d="M21 20h-4v2H3V2h7v7h7v2h4v9zm-1-8H6v7h14v-7zM9 13a1.5 1.5 0 0 1 0 3H8v2H7v-5h2zm-1 2.065h1c.31 0 .565-.254.565-.565A.566.566 0 0 0 9 13.935H8v1.13zM15 15v1a2 2 0 0 1-2 2h-2v-5h2a2 2 0 0 1 2 2zm-3 2h1c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1v3zm7.5-4v1H17v1h2v1h-2v2h-1v-5h3.5zM11 2l6 6h-6V2z"></path></symbol><symbol id="24x24_pencil" height="24" viewBox="0 0 24 24" width="24"><path d="M20.546 4.868l-1.414-1.414a1.994 1.994 0 0 0-1.415-.586c-.51 0-1.023.195-1.414.586L4.99 14.768l-2.122 6.364 6.364-2.122L20.546 7.697a2 2 0 0 0 0-2.83zM8.152 17.262l-2.12.707.706-2.123 8.858-8.86 1.414 1.416-8.858 8.858z"></path></symbol><symbol id="24x24_phone" height="24" viewBox="0 0 24 24" width="24"><path d="M21.318 16.77l-3.952-2.277a.602.602 0 0 0-.66.117l-2.148 2.288a1.16 1.16 0 0 1-.704.314s-1.47.04-4.25-2.692c-2.78-2.733-2.79-4.23-2.79-4.23a1.194 1.194 0 0 1 .285-.725l1.975-2.113a.66.66 0 0 0 .11-.683L6.963 2.68c-.1-.21-.31-.244-.468-.078L2.845 6.46a1.47 1.47 0 0 0-.336.72s-.465 3.97 5.092 9.43c5.556 5.464 9.452 4.87 9.452 4.87.226-.033.54-.197.7-.364l3.645-3.858c.16-.166.12-.386-.084-.487z"></path></symbol><symbol id="24x24_pin" height="24" viewBox="0 0 24 24" width="24"><path d="M21.91 21.48l-6.2-7.418 3.01-3.01c.43-.428.184-1.208-.424-1.385a7.356 7.356 0 0 0-3.986-.04L10.164 5.48a6.36 6.36 0 0 0-.14-2.937c-.154-.526-.813-.722-1.185-.35l-6.65 6.65c-.373.37-.177 1.03.35 1.182a6.35 6.35 0 0 0 2.937.142l4.146 4.147a7.36 7.36 0 0 0 .04 3.987c.175.61.955.856 1.384.427l3.01-3.01 7.406 6.193c.33.266.71-.1.444-.43z"></path></symbol><symbol id="24x24_pinterest" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.236 2.636 7.855 6.356 9.312-.088-.79-.167-2.005.034-2.87.182-.78 1.173-4.97 1.173-4.97s-.3-.598-.3-1.484c0-1.39.807-2.428 1.81-2.428.854 0 1.266.64 1.266 1.408 0 .858-.55 2.14-.83 3.33-.237.995.5 1.807 1.48 1.807 1.78 0 3.143-1.874 3.143-4.58 0-2.394-1.72-4.068-4.177-4.068-2.846 0-4.516 2.134-4.516 4.34 0 .86.33 1.78.746 2.282.08.096.093.183.07.284l-.28 1.134c-.043.182-.144.22-.333.132-1.25-.58-2.03-2.407-2.03-3.873 0-3.156 2.292-6.053 6.607-6.053 3.47 0 6.166 2.472 6.166 5.776 0 3.446-2.173 6.22-5.19 6.22-1.012 0-1.965-.527-2.29-1.15l-.624 2.378c-.226.87-.835 1.96-1.243 2.623A9.98 9.98 0 0 0 12 22c5.522 0 10-4.478 10-10S17.522 2 12 2z"></path></symbol><symbol id="24x24_plane" height="24" viewBox="0 0 24 24" width="24"><path d="M20.4 13.61a1.924 1.924 0 0 0-1.825-.505l-2.203.55-3.228-3.227 5.973-4.887-.438-.436a1.92 1.92 0 0 0-2.117-.407L10.157 7.44 6.732 4.018c-.75-.75-2.644-1.43-3.394-.68-.75.75-.07 2.646.68 3.395l3.423 3.425-2.743 6.408a1.92 1.92 0 0 0 .407 2.114l.44.437 4.886-5.973 3.227 3.228-.55 2.203a1.92 1.92 0 0 0 .504 1.824l.59.586 2.717-4.073 4.073-2.716-.59-.59z"></path></symbol><symbol id="24x24_play" height="24" viewBox="0 0 24 24" width="24"><path d="M7 20V4l13 8-13 8z"></path></symbol><symbol id="24x24_polaroid" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6c-1.654 0-3-1.346-3-3V6c0-1.654 1.346-3 3-3h12c1.654 0 3 1.346 3 3v12c0 1.654-1.346 3-3 3zm1-15a1 1 0 0 0-1-1H6c-.55 0-1 .45-1 1v11h14V6zm-9 7.964l4-6.89L18 16H6l2.46-4.64L10 13.964zM8 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path></symbol><symbol id="24x24_printer" height="24" viewBox="0 0 24 24" width="24"><path d="M19 15v7H5v-7H2V8c0-1.66 1.34-3 3-3V2h14v3c1.66 0 3 1.34 3 3v7h-3zM17 4H7v2h10V4zm0 8H7v8h10v-8zm-2 3H9v-1h6v1zm0 3H9v-1h6v1z"></path></symbol><symbol id="24x24_professional" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H5a3 3 0 0 1-3-3v-4h8v3h4v-3h8v4a3 3 0 0 1-3 3zM2 7h6V4h8v3h6v5H2V7zm8 0h4V6h-4v1z"></path></symbol><symbol id="24x24_profile" height="24" viewBox="0 0 24 24" width="24"><path d="M3 21.002h18a12.703 12.703 0 0 0-7.28-3.583v-1.46c1.156-.845 2.23-2.25 2.302-3.168 1.307-.634 1.58-2.213.65-2.562l-.02.03c.42-.587.677-1.335.677-2.192 0-1.11-.2-2.136-1.017-2.806-.567-1.34-1.746-2.266-3.116-2.266-.804 0-1.54.32-2.13.854a1.223 1.223 0 0 0-.787-.297c-.514 0-.96.345-1.2.852-1.294.478-2.236 1.936-2.236 3.663 0 .79.198 1.526.536 2.136-1 .394-.666 1.9.595 2.59.074.915 1.147 2.322 2.302 3.166v1.457A12.725 12.725 0 0 0 3 21z"></path></symbol><symbol id="24x24_profile_badged" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.333 16.715a7.842 7.842 0 0 0-2.97-1.033v-1.178c.914-.682 1.763-1.82 1.82-2.56.78-.502 1.176-1.707.516-2.07l-.02.024c.333-.476.537-1.08.537-1.773 0-.898-.16-1.727-.804-2.27-.448-1.082-1.382-1.83-2.467-1.83-.637 0-1.22.26-1.686.69a.96.96 0 0 0-.622-.24c-.407 0-.76.28-.95.69-1.024.385-1.77 1.564-1.77 2.96 0 .64.157 1.233.424 1.726-.72.337-.324 1.58.472 2.096.058.74.907 1.878 1.82 2.56v1.178a7.848 7.848 0 0 0-2.97 1.033A7.994 7.994 0 0 1 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8a7.994 7.994 0 0 1-3.667 6.715z"></path></symbol><symbol id="24x24_profile_badged_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12a9.98 9.98 0 0 0 4.258 8.18A9.942 9.942 0 0 0 12 22c2.14 0 4.116-.677 5.742-1.82A9.982 9.982 0 0 0 22 12c0-5.523-4.477-10-10-10zm5.037 17.455a7.48 7.48 0 0 0-3.675-1.828v-1.123c.915-.682 1.764-1.82 1.822-2.56.78-.502 1.175-1.707.515-2.07l-.02.024c.333-.476.537-1.08.537-1.773 0-.898-.16-1.727-.804-2.27-.45-1.082-1.382-1.83-2.467-1.83-.637 0-1.22.26-1.686.69a.96.96 0 0 0-.622-.24c-.407 0-.76.28-.95.69-1.024.385-1.77 1.564-1.77 2.96 0 .64.157 1.233.425 1.726-.72.337-.325 1.58.47 2.097.058.74.908 1.877 1.822 2.56v1.122c-1.4.26-2.662.907-3.674 1.827A9 9 0 0 1 3 12c0-4.963 4.037-9 9-9s9 4.037 9 9a9 9 0 0 1-3.963 7.455z"></path></symbol><symbol id="24x24_profile_video" height="24" viewBox="0 0 24 24" width="24"><path d="M8.427 11l11.957-3.21L18.83 2 1.444 6.662 3 12.456V18c0 1.66 1.34 3 3 3h12c1.66 0 3-1.34 3-3v-7H8.427zm8.99-6.555l.517 1.93-1.93.52-.52-1.93 1.932-.52zM13.55 5.482l.52 1.932-1.933.518-.52-1.93 1.932-.52zM9.69 6.52l.518 1.93-1.932.52-.518-1.932 1.93-.52zM5.825 7.555l.52 1.932-1.933.52-.52-1.933 1.933-.52zM7 15H5v-2h2v2zm4 0H9v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2z"></path></symbol><symbol id="24x24_propublica" height="24" viewBox="0 0 24 24" width="24"><path d="M24 4.405v2.628l-.24.123a.43.43 0 0 1-.57-.167L22 4.83a.398.398 0 0 1 .174-.55L24 3.352v.64l-1.295.664.178.322L24 4.406zm-2.758 2.89c-.56.286-1.01.713-1.18 1.076.4.97.626 2.028.626 3.13 0 4.7-3.963 8.517-8.85 8.517-4.89 0-8.85-3.812-8.85-8.513 0-4.7 3.96-8.512 8.85-8.512 2.998 0 5.644 1.44 7.245 3.634l.002-.005c.408.068 1.04-.04 1.6-.326.562-.288.977-.68 1.146-1.046l.956 1.723c-.407-.07-.98.04-1.54.33zm-9.405-3.333C7.517 3.962 4 7.344 4 11.5c0 4.156 3.516 7.538 7.837 7.538 4.32 0 7.837-3.382 7.837-7.538 0-4.156-3.516-7.538-7.837-7.538zm.81 8.575c-.456 0-.897-.03-1.794-.102v2.63c0 1.02.395 1.108 1.004 1.108h.76v.53c-.85-.042-1.703-.086-2.555-.086-.76 0-1.52.044-2.28.087v-.53h.365c.592 0 1.018-.074 1.018-1.08V7.98c0-.99-.44-1.08-1.033-1.08-.107 0-.168 0-.26.016v-.53c.61.042 1.035.084 1.66.084h.986c.58 0 1.11-.042 1.84-.042 1.75 0 2.783.243 3.512 1.15.29.36.578.904.578 1.74 0 1.392-.76 3.22-3.8 3.22zm-.608-5.49c-.9 0-1.19.114-1.19.487v4.3a6.66 6.66 0 0 0 1.292.127c2.63 0 2.676-1.993 2.676-2.524 0-2.3-2.13-2.386-2.783-2.386z"></path></symbol><symbol id="24x24_public_service" height="24" viewBox="0 0 24 24" width="24"><path d="M21 11V9h-1l-8-6-8 6H3v2h2v7H4v1H3v2h18v-2h-1v-1h-1v-7h2zm-8 7h-2v-7h2v7zm-6-7h2v7H7v-7zm10 7h-2v-7h2v7z"></path></symbol><symbol id="24x24_regular" height="24" viewBox="0 0 24 24" width="24"><path d="M3.03 4.584c.224 7.093-1.084 12.336 8.99 16.4 9.5-3.358 8.918-9.575 8.99-16.174-6.7-2.483-11.28-2.25-17.98-.226zm7.837 10.778L9.33 13.826 7.027 11.52l1.537-1.535 2.304 2.304 4.61-4.61 1.537 1.535-6.147 6.146z"></path></symbol><symbol id="24x24_religion" height="24" viewBox="0 0 24 24" width="24"><path d="M18.5 11L16 14.5v-6L12 3 8 8.5v6L5.5 11 3 14.5V21h7v-4h4v4h7v-6.5L18.5 11z"></path></symbol><symbol id="24x24_reply" height="24" viewBox="0 0 24 24" width="24"><path d="M9 10V5l-7 7 7 7v-5c4.29 0 8.23 1.5 11.32 4.01A11.993 11.993 0 0 0 9 10z"></path></symbol><symbol id="24x24_reservation" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm1-13H5v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V8zm-6 5h4v4h-4v-4z"></path></symbol><symbol id="24x24_reservation_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm2-15c0-1.103-.897-2-2-2H6c-1.103 0-2 .897-2 2v1h16V6zm0 2H4v10c0 1.103.897 2 2 2h12c1.103 0 2-.897 2-2V8zm-7 5h4v4h-4v-4z"></path></symbol><symbol id="24x24_review" height="24" viewBox="0 0 24 24" width="24"><path d="M21 6a3 3 0 0 0-3-3H6a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3V6zm-5.88 10.428l-3.16-1.938-3.05 2.01.59-3.457L7 10.596l3.457-.505L11.96 6.5l1.582 3.59 3.458.506-2.5 2.447.62 3.385z"></path></symbol><symbol id="24x24_review_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm2-15c0-1.103-.897-2-2-2H6c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h12c1.103 0 2-.897 2-2V6zm-4.88 10.428l-3.16-1.938-3.05 2.01.59-3.457L7 10.596l3.457-.505L11.96 6.5l1.582 3.59 3.458.506-2.5 2.447.62 3.385z"></path></symbol><symbol id="24x24_rss" height="24" viewBox="0 0 24 24" width="24"><path d="M17.07 19c0-6.655-5.415-12.07-12.07-12.07V5c7.72 0 14 6.28 14 14h-1.93zm-2.898 0h-1.93c0-3.993-3.25-7.24-7.242-7.24V9.827c5.058 0 9.172 4.114 9.172 9.172zM7 15a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="24x24_sandwich" height="24" viewBox="0 0 24 24" width="24"><path d="M22 15H2a1 1 0 0 1 0-2h20a1 1 0 0 1 0 2zM7.5 5.165V7a.5.5 0 0 0 1 0V5.025C8.666 5.013 8.83 5 9 5h2.5v3a.5.5 0 0 0 1 0V5H15c.17 0 .334.013.5.025V7a.5.5 0 0 0 1 0V5.165A7 7 0 0 1 22 12H2a7 7 0 0 1 5.5-6.835zM22 17a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-1h20v1z"></path></symbol><symbol id="24x24_search" height="24" viewBox="0 0 24 24" width="24"><path d="M20.753 19.34l-4.295-4.297A7.46 7.46 0 0 0 18 10.5a7.5 7.5 0 1 0-7.5 7.5 7.46 7.46 0 0 0 4.543-1.542l4.296 4.295a1 1 0 1 0 1.412-1.414zM10.5 16A5.506 5.506 0 0 1 5 10.5C5 7.467 7.467 5 10.5 5S16 7.467 16 10.5 13.533 16 10.5 16z"></path></symbol><symbol id="24x24_search_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M20.803 20.096l-4.614-4.614c2.58-2.946 2.472-7.426-.338-10.235A7.5 7.5 0 1 0 5.247 15.854c2.81 2.81 7.29 2.916 10.235.335l4.614 4.612a.5.5 0 0 0 .707 0 .5.5 0 0 0 0-.707zm-14.85-4.95a6.508 6.508 0 0 1 0-9.192 6.508 6.508 0 0 1 9.193 0 6.506 6.506 0 0 1 0 9.192 6.506 6.506 0 0 1-9.192 0z"></path></symbol><symbol id="24x24_search_small" height="24" viewBox="0 0 24 24" width="24"><path d="M19.34 17.925l-3.953-3.952A5.968 5.968 0 0 0 16.5 10.5a6 6 0 1 0-6 6 5.968 5.968 0 0 0 3.473-1.113l3.952 3.952a1 1 0 0 0 1.414-1.416zM10.5 14.5c-2.206 0-4-1.794-4-4s1.794-4 4-4 4 1.794 4 4-1.794 4-4 4z"></path></symbol><symbol id="24x24_selfie" height="24" viewBox="0 0 24 24" width="24"><path d="M17 24c-3.165 0-5.842-2.112-6.705-5H5a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3h2.184C7.597 4 8.696 3 10 3h4c1.304 0 2.403 1 2.816 2H19a3 3 0 0 1 3 3v4.11A6.976 6.976 0 0 1 24 17c0 3.86-3.14 7-7 7zM12.03 8c-2.208 0-3.973 1.79-3.973 4 0 1.54.684 2.86 2.103 3.523a7.02 7.02 0 0 1 5.373-5.366C14.876 8.88 13.57 8 12.03 8zM17 12c-2.757 0-5 2.243-5 5s2.243 5 5 5 5-2.243 5-5-2.243-5-5-5zm0 8a3.652 3.652 0 0 1-3.59-3h7.18A3.652 3.652 0 0 1 17 20zm2-4a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm-4 0a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"></path></symbol><symbol id="24x24_settings" height="24" viewBox="0 0 24 24" width="24"><path d="M21.872 10.48c.076.497.128 1.002.128 1.52s-.05 1.022-.127 1.518l-3.165.475c-.14.47-.323.92-.552 1.343l1.9 2.57c-.3.408-.62.8-.976 1.156l-.018.018a10.05 10.05 0 0 1-1.154.975l-2.57-1.9a7 7 0 0 1-1.344.553l-.475 3.165a9.94 9.94 0 0 1-1.506.127h-.034c-.51 0-1.01-.052-1.5-.127l-.475-3.165a7 7 0 0 1-1.343-.553l-2.57 1.9c-.408-.3-.798-.62-1.155-.975l-.018-.018a10.068 10.068 0 0 1-.978-1.155l1.9-2.57a6.97 6.97 0 0 1-.552-1.344l-3.164-.475C2.052 13.022 2 12.518 2 12s.052-1.023.128-1.52l3.164-.475a7 7 0 0 1 .553-1.342l-1.9-2.57a10.035 10.035 0 0 1 2.148-2.15l2.57 1.9a7.015 7.015 0 0 1 1.343-.55l.475-3.166C10.98 2.052 11.486 2 12 2s1.023.052 1.52.127l.474 3.165c.47.14.92.323 1.342.552l2.57-1.9a10.044 10.044 0 0 1 2.15 2.148l-1.9 2.57c.23.424.412.874.552 1.343l3.164.475zM12 8.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7z"></path></symbol><symbol id="24x24_settings_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.873 13.518l-.056.364-3.063.46c-.093.27-.2.53-.32.78l1.84 2.49-.218.296c-.33.45-.65.827-.976 1.154-.35.347-.726.667-1.17.993l-.298.218-2.49-1.84a7.47 7.47 0 0 1-.78.32l-.46 3.065-.363.056a9.82 9.82 0 0 1-1.507.126c-.493 0-.97-.04-1.535-.126l-.364-.056-.46-3.064a7.47 7.47 0 0 1-.78-.32l-2.49 1.84-.296-.22a10.14 10.14 0 0 1-1.15-.974 10.117 10.117 0 0 1-.995-1.172l-.218-.297 1.84-2.49a7.114 7.114 0 0 1-.32-.78l-3.063-.455-.056-.364A9.914 9.914 0 0 1 2 12c0-.465.04-.962.127-1.52l.056-.364 3.064-.46c.092-.268.2-.53.32-.778l-1.84-2.49.218-.296a9.99 9.99 0 0 1 2.148-2.148l.297-.218 2.49 1.84c.248-.12.51-.227.778-.32l.46-3.063.363-.056c1.118-.17 1.928-.17 3.04 0l.366.056.46 3.063c.268.093.53.2.778.32l2.49-1.84.297.218a9.99 9.99 0 0 1 2.148 2.148l.218.297-1.84 2.485c.12.25.228.51.32.78l3.064.458.054.365c.085.557.127 1.054.127 1.52 0 .463-.04.96-.125 1.517zm-.938-2.523l-2.952-.443-.09-.305a6.043 6.043 0 0 0-.485-1.178l-.152-.28 1.77-2.4c-.418-.525-.894-1-1.42-1.42L15.21 6.74l-.28-.15a6.043 6.043 0 0 0-1.178-.485l-.305-.09-.443-2.952a7.67 7.67 0 0 0-2.008 0l-.443 2.95-.305.092c-.42.124-.815.287-1.178.485l-.28.153L6.394 4.97a9.008 9.008 0 0 0-1.42 1.42l1.77 2.398-.152.28c-.197.362-.36.758-.485 1.177l-.09.305-2.952.443A8.242 8.242 0 0 0 3 12c0 .316.02.642.065 1.003l2.95.443.092.305a6.1 6.1 0 0 0 .485 1.18l.152.28-1.772 2.4a7.956 7.956 0 0 0 1.42 1.42l2.4-1.77.277.15c.362.2.76.36 1.18.486l.302.09.443 2.953c.747.09 1.314.082 2.008 0l.443-2.953.305-.09a6.14 6.14 0 0 0 1.18-.486l.28-.152 2.398 1.772c.28-.22.524-.438.745-.658.23-.23.45-.48.672-.764l-1.772-2.4.152-.28a6.1 6.1 0 0 0 .485-1.18l.09-.303 2.952-.443A8.21 8.21 0 0 0 21 12c0-.317-.02-.643-.065-1.005zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm0-7c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3z"></path></symbol><symbol id="24x24_share" height="24" viewBox="0 0 24 24" width="24"><path d="M23.5 9L18 14.5v-3.93c-3 0-6.466 1.18-8.894 3.152C10.394 10.052 14 7.43 18 7.43V3.5L23.5 9zM5 6v12c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-2l2-2v4a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h10v2H6c-.55 0-1 .45-1 1z"></path></symbol><symbol id="24x24_share_android" height="24" viewBox="0 0 24 24" width="24"><path d="M17.333 15.556a2.64 2.64 0 0 0-1.712.638l-6.335-3.697a2.7 2.7 0 0 0 .05-.497c0-.17-.02-.336-.05-.497l6.338-3.697a2.64 2.64 0 0 0 1.713.638 2.666 2.666 0 1 0-2.616-2.17l-6.34 3.7a2.64 2.64 0 0 0-1.713-.64 2.667 2.667 0 0 0 0 5.334 2.64 2.64 0 0 0 1.712-.64l6.335 3.698a2.72 2.72 0 0 0-.05.497 2.667 2.667 0 1 0 2.666-2.666z"></path></symbol><symbol id="24x24_share_ios" height="24" viewBox="0 0 24 24" width="24"><path d="M16 22H8a3 3 0 0 1-3-3v-7a3 3 0 0 1 3-3h1v2H8c-.55 0-1 .45-1 1v7c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-7c0-.55-.45-1-1-1h-1V9h1a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3zM13 5.414V15h-2V5.414L9.207 7.207 7.793 5.793 12 1.586l4.207 4.207-1.414 1.414L13 5.414z"></path></symbol><symbol id="24x24_shopping" height="24" viewBox="0 0 24 24" width="24"><path d="M16 6V5a3 3 0 0 0-3-3h-2a3 3 0 0 0-3 3v1H5v13a3 3 0 0 0 3 3h8a3 3 0 0 0 3-3V6h-3zm-6-1c0-.55.45-1 1-1h2c.55 0 1 .45 1 1v1h-4V5z"></path></symbol><symbol id="24x24_shovel" height="24" viewBox="0 0 24 24" width="24"><path d="M17.687 2.004l-2.87 2.87a3.033 3.033 0 0 0-.584 3.453L9.108 13.45l-2.496-2.42-4.62 5.02L2 22h6l5.163-4.617-2.598-2.52 5.102-5.1a3.05 3.05 0 0 0 1.303.304c.778 0 1.557-.297 2.15-.89l2.87-2.87-4.303-4.303zm0 5.738a1.014 1.014 0 0 1-1.435-1.435l1.435-1.434 1.434 1.434-1.432 1.435z"></path></symbol><symbol id="24x24_sleep" height="24" viewBox="0 0 24 24" width="24"><path d="M20 20v-3H4v3H2V6h2v7h16v-2h2v9h-2zM15 7l4.25-4H15V1h7v2l-4.25 4H22v2h-7V7zm-6 3l2.625-3H9V6h4v1l-2.625 3H13v1H9v-1z"></path></symbol><symbol id="24x24_smog_check_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M12.5 15a.5.5 0 0 1-.354-.146l-4-4a.5.5 0 0 1 .707-.707l3.625 3.625 7.648-8.604a.5.5 0 0 1 .748.664l-8 9a.497.497 0 0 1-.36.168z"></path><path d="M12 21a9 9 0 1 1 4.603-16.735.5.5 0 1 1-.512.86A8 8 0 1 0 20 12a.5.5 0 0 1 1 0 9.01 9.01 0 0 1-9 9z"></path></symbol><symbol id="24x24_smoking" height="24" viewBox="0 0 24 24" width="24"><path d="M19 20H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h17v5z"></path><path d="M22 20h-2v-5h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1zm-4-10V4h1a4 4 0 0 1 4 4v6h-1a4 4 0 0 1-4-4z"></path></symbol><symbol id="24x24_sound_off" height="24" viewBox="0 0 24 24" width="24"><path d="M18.89 12l1.767 1.768a1 1 0 0 1-1.414 1.414l-1.768-1.768-1.768 1.768a1 1 0 1 1-1.414-1.414L16.06 12l-1.767-1.768a1 1 0 1 1 1.414-1.414l1.768 1.768 1.768-1.768a1 1 0 0 1 1.414 1.414L18.89 12zM3 15V9h3.75L12 4v16l-5.25-5H3z"></path></symbol><symbol id="24x24_sound_on" height="24" viewBox="0 0 24 24" width="24"><path d="M15.244 19.674c-.625.182-1.244-.32-1.244-.97v-.008c0-.43.273-.823.686-.944C17.176 17.022 19 14.722 19 12s-1.825-5.022-4.314-5.752A.977.977 0 0 1 14 5.304v-.008c0-.65.62-1.152 1.244-.97A7.996 7.996 0 0 1 21 12a7.996 7.996 0 0 1-5.756 7.674zM3 15V9h3.75L12 4v16l-5.25-5H3zm12.677-5.96A3.958 3.958 0 0 1 17 12a3.96 3.96 0 0 1-1.323 2.96c-.647.58-1.677.126-1.677-.742 0-.28.117-.547.326-.732A1.98 1.98 0 0 0 15 12a1.98 1.98 0 0 0-.674-1.486.975.975 0 0 1-.326-.732c0-.868 1.03-1.32 1.677-.74z"></path></symbol><symbol id="24x24_spa" height="24" viewBox="0 0 24 24" width="24"><path d="M18 17v-7a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v7h12z"></path><path d="M12.655 7.79c.312-.203.53-.525.53-.91 0-.618-1.185-2.238-1.185-2.238s-1.185 1.62-1.185 2.24c0 .383.218.705.53.907A2.285 2.285 0 0 1 9.77 5.6C9.77 4.33 12 1 12 1s2.23 3.33 2.23 4.6a2.285 2.285 0 0 1-1.575 2.19zM12 23C6.473 23 1.86 19.157.647 14h22.706C22.14 19.157 17.527 23 12 23z"></path></symbol><symbol id="24x24_speech" height="24" viewBox="0 0 24 24" width="24"><path d="M18 3H6C4.34 3 3 4.34 3 6v7c0 1.66 1.34 3 3 3h2v5l5-5h5c1.66 0 3-1.34 3-3V6c0-1.66-1.34-3-3-3z"></path></symbol><symbol id="24x24_speech_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M18 4c1.103 0 2 .897 2 2v7c0 1.103-.897 2-2 2h-5.414l-.293.293L9 18.586V15H6c-1.103 0-2-.897-2-2V6c0-1.103.897-2 2-2h12m0-1H6C4.34 3 3 4.34 3 6v7c0 1.66 1.34 3 3 3h2v5l5-5h5c1.66 0 3-1.34 3-3V6c0-1.66-1.34-3-3-3z"></path></symbol><symbol id="24x24_speech_round" height="24" viewBox="0 0 24 24" width="24"><path d="M12 3.5c-4.97 0-9 3.134-9 7 0 2.07 1.163 3.925 3 5.207V22l4.594-4.594c.46.056.926.094 1.406.094 4.97 0 9-3.134 9-7s-4.03-7-9-7z"></path></symbol><symbol id="24x24_stage" height="24" viewBox="0 0 24 24" width="24"><path d="M16 21v-2c0-1.643.808-3 2.032-4H21v6h-5zM13.498 6H21v7.997c-4-.05-7.503-3.61-7.502-7.997zM3 3h18v2H3V3zm5 16v2H3v-6h2.977C7.2 16 8 17.357 8 19zM3 6h7.502c.006 4.392-3.352 7.957-7.498 8.005L3 6z"></path></symbol><symbol id="24x24_star" height="24" viewBox="0 0 24 24" width="24"><path d="M12 1.5l2.61 6.727 6.89.53-5.278 4.688 1.65 7.055L12 16.67 6.13 20.5l1.648-7.055L2.5 8.757l6.89-.53L12 1.5z"></path></symbol><symbol id="24x24_star_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.5 8.757l-6.89-.53L12 1.5 9.39 8.226l-6.89.53 5.278 4.69-1.65 7.054L12 16.67l5.87 3.83-1.648-7.055L21.5 8.757zM16.33 18.3l-3.784-2.467-.546-.356-.546.356L7.67 18.3l1.082-4.627.135-.58-.445-.395-3.517-3.125 4.542-.35.628-.048.228-.587L12 4.265l1.677 4.323.228.587.628.048 4.542.35-3.517 3.125-.445.395.136.58 1.08 4.628z"></path></symbol><symbol id="24x24_stations" height="24" viewBox="0 0 24 24" width="24"><path d="M3 21v-4h18v4H3zm4-3H5v2h2v-2zm11-2H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3zm1-10a1 1 0 0 0-1-1H6a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V6z"></path></symbol><symbol id="24x24_support_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M21.48 8.84a9.945 9.945 0 0 0-6.32-6.32A9.74 9.74 0 0 0 12 2c-1.1 0-2.17.18-3.16.52a9.945 9.945 0 0 0-6.32 6.32A9.74 9.74 0 0 0 2 12c0 1.1.18 2.17.52 3.16a9.945 9.945 0 0 0 6.32 6.32c.99.34 2.06.52 3.16.52s2.17-.18 3.16-.52a9.945 9.945 0 0 0 6.32-6.32c.34-.99.52-2.06.52-3.16s-.18-2.17-.52-3.16zm-.95.32l-4.26 1.42a4.45 4.45 0 0 0-2.85-2.85l1.42-4.26a9 9 0 0 1 5.69 5.69zM15.5 12c0 .39-.06.76-.18 1.11a3.52 3.52 0 0 1-2.21 2.21 3.4 3.4 0 0 1-1.11.18 3.4 3.4 0 0 1-1.11-.18 3.52 3.52 0 0 1-2.21-2.21A3.4 3.4 0 0 1 8.5 12c0-.39.06-.76.18-1.11a3.52 3.52 0 0 1 2.21-2.21A3.4 3.4 0 0 1 12 8.5c.39 0 .76.06 1.11.18a3.52 3.52 0 0 1 2.21 2.21c.12.35.18.72.18 1.11zM9.16 3.47l1.42 4.26a4.45 4.45 0 0 0-2.85 2.85L3.47 9.16a9 9 0 0 1 5.69-5.69zM3.47 14.84l4.26-1.42a4.45 4.45 0 0 0 2.85 2.85l-1.42 4.26a9 9 0 0 1-5.69-5.69zm11.37 5.69l-1.42-4.26a4.45 4.45 0 0 0 2.85-2.85l4.26 1.42a9 9 0 0 1-5.69 5.69z"></path></symbol><symbol id="24x24_survival" height="24" viewBox="0 0 24 24" width="24"><path d="M19.66 6.323c-.846.567-1.568 1.367-1.655 1.692-.102-.33-.75-1.108-1.663-1.676C15.402 5.75 14 4.99 14 3.53c0-1.762 2.965-2.3 4 0 .987-2.207 4-1.796 4 0 0 1.463-1.418 2.172-2.34 2.793zm-4.723 2.68a.985.985 0 0 1 .938.513L17.805 13H20a1 1 0 0 1 0 2h-2.784a1 1 0 0 1-.875-.516l-1.19-2.157-3.22 8.044a1.002 1.002 0 0 1-1.903-.142L7.717 10.21 5.92 14.395A1 1 0 0 1 5 15H2a1 1 0 0 1 0-2h2.34l2.74-6.394c.17-.398.585-.634 1.01-.602.43.04.787.35.885.77l2.282 9.89L14.07 9.63a1 1 0 0 1 .867-.626z"></path></symbol><symbol id="24x24_talk" height="24" viewBox="0 0 24 24" width="24"><path d="M20 17.326V21l-3-3c-2.715 0-5.006-1.504-5.746-3.566C14.047 13.42 16 11.144 16 8.5c0-.142-.015-.282-.026-.422A7.19 7.19 0 0 1 17 8c3.314 0 6 2.24 6 5 0 1.85-1.208 3.46-3 4.326zM8 14c-.08 0-.158-.007-.238-.01L4 17v-3.99c-1.812-.994-3-2.642-3-4.51C1 5.462 4.134 3 8 3s7 2.462 7 5.5S11.866 14 8 14z"></path></symbol><symbol id="24x24_talk_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M17 8c-.707 0-1.383.107-2.013.295C14.847 5.353 11.777 3 8 3 4.134 3 1 5.462 1 8.5c0 1.868 1.188 3.516 3 4.51V17l3.762-3.01c.08.003.158.01.238.01 1.086 0 2.11-.2 3.027-.547C11.303 16.003 13.87 18 17 18l3 3v-3.674c1.792-.865 3-2.476 3-4.326 0-2.76-2.686-5-6-5zm-9.085 4.997l-.126-.006-.37-.01-.286.23L5 14.92v-2.502l-.52-.285C2.928 11.28 2 9.923 2 8.5 2 6.02 4.692 4 8 4s6 2.02 6 4.5c0 .06-.01.12-.012.18-1.577.766-2.695 2.11-2.935 3.687A7.5 7.5 0 0 1 8 13l-.085-.003zm11.65 3.428l-.565.273v1.888l-1.293-1.293-.293-.293H17c-2.753 0-4.992-1.79-5-3.99V13c0-.492.127-.958.33-1.394a4.07 4.07 0 0 1 1.283-1.53 5.19 5.19 0 0 1 1.29-.694A5.984 5.984 0 0 1 17 9c2.757 0 5 1.794 5 4 0 1.388-.933 2.7-2.435 3.425z"></path></symbol><symbol id="24x24_target" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm1 17.93V16a1 1 0 0 0-2 0v3.93A8.008 8.008 0 0 1 4.07 13H8a1 1 0 0 0 0-2H4.07A8.008 8.008 0 0 1 11 4.07V8a1 1 0 0 0 2 0V4.07A8.006 8.006 0 0 1 19.93 11H16a1 1 0 0 0 0 2h3.93A8.006 8.006 0 0 1 13 19.93z"></path></symbol><symbol id="24x24_television" height="24" viewBox="0 0 24 24" width="24"><path d="M19 6h-6.586l2.293-2.293a1 1 0 1 0-1.414-1.414L10 5.586 6.707 2.293a1 1 0 1 0-1.414 1.414L7.586 6H5a3 3 0 0 0-3 3v8a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V9a3 3 0 0 0-3-3zm-3 11c0 .55-.45 1-1 1H5c-.55 0-1-.45-1-1V9c0-.55.45-1 1-1h10c.55 0 1 .45 1 1v8zm3-4c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm0-3c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"></path></symbol><symbol id="24x24_tennis" height="24" viewBox="0 0 24 24" width="24"><path d="M19.7 12.785c-1.398 1.398-3.157 2.16-4.856 2.26a59.9 59.9 0 0 0-5.068 1.957l.025.025-4.95 4.95-2.82-2.827 4.95-4.95.026.02A59.555 59.555 0 0 0 8.96 9.15c.102-1.7.863-3.458 2.26-4.857 2.735-2.734 6.85-3.05 9.194-.708 2.34 2.343 2.024 6.46-.71 9.192zm-9.878-.152c-.34.883-.697 1.76-1.082 2.627a59.14 59.14 0 0 1 2.626-1.082 5.165 5.165 0 0 1-.858-.686 5.132 5.132 0 0 1-.686-.86zm9.17-7.626c-1.558-1.56-4.413-1.243-6.362.707-1.95 1.95-2.267 4.804-.708 6.364 1.56 1.56 4.415 1.242 6.364-.708 1.95-1.95 2.267-4.804.707-6.363zM18 17a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"></path></symbol><symbol id="24x24_ticket" height="24" viewBox="0 0 24 24" width="24"><path d="M17.303 6.697a2 2 0 0 1 0-2.83L14.12.687 10.056 4.75l2.122 2.12-1.06 1.062-2.122-2.12-8.31 8.307L3.87 17.3a2 2 0 1 1 2.83 2.83l3.18 3.18 8.31-8.308-2.123-2.12 1.06-1.062 2.122 2.122 4.064-4.066-3.182-3.183a2 2 0 0 1-2.83 0zm-1.59 3.712l-1.06 1.06-2.123-2.124 1.06-1.06 2.122 2.12z"></path></symbol><symbol id="24x24_tip_of_the_day" height="24" viewBox="0 0 24 24" width="24"><path d="M18 21H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3 1 1 0 0 1 2 0h8a1 1 0 0 1 2 0 3 3 0 0 1 3 3v12a3 3 0 0 1-3 3zm1-13H5v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V8zm-5.5 6.58V16h-3v-1.42C9.61 14.06 9 13.11 9 12c0-1.66 1.34-3 3-3s3 1.34 3 3c0 1.11-.61 2.06-1.5 2.58zm-2-3.83c-.41 0-.75.34-.75.75s.34.75.75.75.75-.34.75-.75-.34-.75-.75-.75zm2 7.25h-3v-1h3v1z"></path></symbol><symbol id="24x24_tire_wheel_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2a10 10 0 1 0 10 10A10.012 10.012 0 0 0 12 2zm.5 18.975V19.5a.5.5 0 0 0-1 0v1.475a8.992 8.992 0 0 1-7.174-4.296l1.12-.644a.5.5 0 1 0-.495-.867l-1.097.63a8.908 8.908 0 0 1-.076-7.44l1.4.762a.5.5 0 1 0 .478-.88l-1.42-.772A8.995 8.995 0 0 1 11.5 3.025V4.5a.5.5 0 0 0 1 0V3.025A8.992 8.992 0 0 1 19.408 6.9l-1.435.823a.5.5 0 1 0 .496.867l1.46-.837a8.945 8.945 0 0 1 .085 8.32l-1.192-.65a.5.5 0 0 0-.478.88l1.17.636a8.993 8.993 0 0 1-7.016 4.034z"></path><path d="M12 6a6 6 0 1 0 6 6 6.007 6.007 0 0 0-6-6zm0 11a5 5 0 1 1 5-5 5.006 5.006 0 0 1-5 5z"></path></symbol><symbol id="24x24_tools" height="24" viewBox="0 0 24 24" width="24"><path d="M19.725 10.71a4.342 4.342 0 0 1-4.53 1.077l-9.383 9.6a1.937 1.937 0 0 1-2.783 0 2.048 2.048 0 0 1 0-2.847l9.38-9.6c-.514-1.577-.175-3.38 1.05-4.635a4.34 4.34 0 0 1 4.53-1.076l-2.44 2.495 2.783 2.847 2.443-2.5c.513 1.577.174 3.38-1.052 4.636zM6.055 8.826l-1.98-1.318-2.09-2.136 2.088-2.135L6.16 5.372l1.28 2.022L9.985 10l-1.39 1.42-2.54-2.595zm13.67 9.715a2.05 2.05 0 0 1 0 2.85 1.937 1.937 0 0 1-2.783 0l-4.87-4.982 2.783-2.847 4.87 4.98z"></path></symbol><symbol id="24x24_towing_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M22.018 17.982l-15-15a.5.5 0 0 0-.707 0l-2.826 2.83a.5.5 0 0 0 0 .706l.89.888v6.102a.5.5 0 0 0 .5.5 1.996 1.996 0 1 1-1.494 3.32.5.5 0 1 0-.75.664 2.996 2.996 0 1 0 2.74-4.942V8.406l13.113 13.112a.5.5 0 0 0 .707-.707L4.542 6.167l2.12-2.12L21.31 18.69a.5.5 0 0 0 .708-.708z"></path></symbol><symbol id="24x24_transit" height="24" viewBox="0 0 24 24" width="24"><path d="M16 2h-1c0-.55-.45-1-1-1h-4c-.55 0-1 .45-1 1H8C6.34 2 5 3.34 5 5v11a2.99 2.99 0 0 0 2.52 2.95L6 22h2l1.5-3h5l1.5 3h2l-1.52-3.05A2.99 2.99 0 0 0 19 16V5c0-1.66-1.34-3-3-3zM9 16c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm6 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm2-4H7V5c0-.55.45-1 1-1h8c.55 0 1 .45 1 1v7z"></path></symbol><symbol id="24x24_transmission_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M20.25 5a2.25 2.25 0 1 0-2.75 2.19V12h-5V7.19a2.25 2.25 0 1 0-1 0V12h-5V7.19a2.25 2.25 0 1 0-1 0v9.62a2.25 2.25 0 1 0 1 0V13h5v3.81a2.25 2.25 0 1 0 1 0V13H18a.5.5 0 0 0 .5-.5V7.19A2.25 2.25 0 0 0 20.25 5zm-9.5 0A1.25 1.25 0 1 1 12 6.25 1.25 1.25 0 0 1 10.75 5zm-6 0A1.25 1.25 0 1 1 6 6.25 1.25 1.25 0 0 1 4.75 5zm2.5 14A1.25 1.25 0 1 1 6 17.75 1.25 1.25 0 0 1 7.25 19zm6 0A1.25 1.25 0 1 1 12 17.75 1.25 1.25 0 0 1 13.25 19zM18 6.25A1.25 1.25 0 1 1 19.25 5 1.25 1.25 0 0 1 18 6.25z"></path></symbol><symbol id="24x24_trash" height="24" viewBox="0 0 24 24" width="24"><path d="M5 7V5a1 1 0 0 1 1-1h4V3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v1h4a1 1 0 0 1 1 1v2H5zm13 12a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3V8h12v11zm-8-8H9v8h1v-8zm5 0h-1v8h1v-8z"></path></symbol><symbol id="24x24_trending" height="24" viewBox="0 0 24 24" width="24"><path d="M21 7h-4.586c-.89 0-1.337 1.077-.707 1.707l1.586 1.586L13 14.586l-5-5-5.707 5.707a1 1 0 0 0 1.414 1.414L8 12.414l5 5 5.707-5.707 1.586 1.586c.63.63 1.707.184 1.707-.707V8a1 1 0 0 0-1-1z"></path></symbol><symbol id="24x24_tumblr" height="24" viewBox="0 0 24 24" width="24"><path d="M17.418 20.116c-.626.67-2.078 1.123-3.378 1.145h-.143c-4.367 0-5.316-3.21-5.316-5.083V10.97H6.456a.36.36 0 0 1-.36-.36V8.15c0-.26.163-.49.407-.578 2.243-.788 3.354-2.493 3.46-3.98.027-.397.235-.59.58-.59h2.564c.2 0 .36.162.36.36v3.913h3.145c.2 0 .36.16.36.36v2.955c0 .2-.16.36-.36.36h-3.16v4.816c0 1.21.798 1.543 1.29 1.543a3.628 3.628 0 0 0 1.17-.25c.173-.07.325-.116.46-.08.128.03.21.12.267.283l.796 2.324c.064.186.12.388-.014.53z"></path></symbol><symbol id="24x24_twitter" height="24" viewBox="0 0 24 24" width="24"><path d="M21 6.417A7.364 7.364 0 0 1 18.88 7a3.708 3.708 0 0 0 1.623-2.044 7.41 7.41 0 0 1-2.346.896 3.693 3.693 0 0 0-6.292 3.368 10.483 10.483 0 0 1-7.612-3.858c-.318.545-.5 1.18-.5 1.856a3.69 3.69 0 0 0 1.643 3.074 3.674 3.674 0 0 1-1.673-.462v.047c0 1.79 1.273 3.28 2.962 3.62a3.714 3.714 0 0 1-1.667.064 3.697 3.697 0 0 0 3.45 2.57 7.41 7.41 0 0 1-4.587 1.58 7.8 7.8 0 0 1-.88-.05 10.45 10.45 0 0 0 5.66 1.66c6.8 0 10.51-5.627 10.51-10.507 0-.16 0-.32-.01-.48A7.496 7.496 0 0 0 21 6.418z"></path></symbol><symbol id="24x24_unfollow" height="24" viewBox="0 0 24 24" width="24"><path d="M20.535 19.12l-1.414 1.415-2.12-2.12-2.12 2.12-1.413-1.414 2.12-2.12-2.12-2.12 1.414-1.414 2.12 2.12 2.12-2.12 1.416 1.414-2.12 2.12 2.12 2.12zm-10.693.643c-.69 1.65-2.995 1.65-3.684 0l-2.482-5.946C3.118 12.48 4.086 11 5.518 11h4.964c1.432 0 2.4 1.48 1.842 2.817l-2.482 5.946zM8 9a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"></path></symbol><symbol id="24x24_unknown" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm0 16.05a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm2.08-6.84a5.76 5.76 0 0 1-.532.517c-.162.142-.315.276-.418.41-.16.207-.252.598-.25.87 0 .482-.39.993-.874.993h-.002c-.483 0-.874-.507-.875-.99-.005-.662.214-1.37.613-1.884a4.95 4.95 0 0 1 .647-.685 4.12 4.12 0 0 0 .37-.363c.486-.556.5-1.415.035-1.947-.203-.233-.535-.363-.894-.35-.356.017-.68.175-.863.427a.798.798 0 0 0-.143.465.874.874 0 0 1-1.75 0c0-.547.165-1.064.478-1.495.5-.688 1.304-1.106 2.2-1.147.906-.042 1.734.303 2.29.94 1.033 1.177 1.02 3.04-.03 4.243z"></path></symbol><symbol id="24x24_unknown_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm1.548 8.727c-.162.142-.315.276-.418.41-.16.207-.252.598-.25.87 0 .482-.39.993-.874.993h-.002c-.483 0-.874-.507-.875-.99-.005-.662.214-1.37.613-1.885.206-.267.44-.502.647-.684a4.12 4.12 0 0 0 .37-.363c.486-.556.5-1.415.035-1.947-.203-.233-.535-.363-.894-.35-.356.017-.68.175-.863.427a.798.798 0 0 0-.143.465.874.874 0 0 1-1.75 0c0-.547.165-1.064.478-1.495.5-.688 1.304-1.106 2.2-1.147.906-.042 1.734.303 2.29.94 1.033 1.177 1.02 3.04-.03 4.243a5.76 5.76 0 0 1-.533.517zM12 15.05a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z"></path></symbol><symbol id="24x24_update" height="24" viewBox="0 0 24 24" width="24"><path d="M21.5 12c0 5.238-4.262 9.5-9.5 9.5-3.03 0-5.725-1.43-7.466-3.645L5.88 16.32A7.49 7.49 0 0 0 12 19.5c4.136 0 7.5-3.364 7.5-7.5H17l3.5-4 3.5 4h-2.5zM12 4.5c-4.136 0-7.5 3.364-7.5 7.5H7l-3.5 4L0 12h2.5c0-5.238 4.262-9.5 9.5-9.5 3.03 0 5.725 1.43 7.466 3.645L18.12 7.68A7.49 7.49 0 0 0 12 4.5z"></path></symbol><symbol id="24x24_useful" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm-2-5.5a2 2 0 0 0 4 0V16h-4v.5zm2-10.833a4.278 4.278 0 0 0-4.278 4.278c0 1.635.93 3.04 2.278 3.76V15h4v-1.296c1.35-.72 2.278-2.124 2.278-3.76A4.278 4.278 0 0 0 12 5.668zM11 10a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"></path></symbol><symbol id="24x24_useful_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm2 10.704V15h-4v-1.296c-1.35-.72-2.278-2.124-2.278-3.76a4.278 4.278 0 0 1 8.556 0c0 1.636-.93 3.04-2.278 3.76zM11 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 6.5a2 2 0 0 1-4 0V16h4v.5z"></path></symbol><symbol id="24x24_veggie" height="24" viewBox="0 0 24 24" width="24"><path d="M19.106 21.78L8.69 16.736c-3.097-1.5-3.79-5.6-1.358-8.033L8.704 7.33c2.022-2.02 5.197-1.887 7.07 0l-3.513 3.516a.495.495 0 0 0 0 .707.5.5 0 0 0 .71 0l3.437-3.437 1.422 2.822-2.738 2.735a.495.495 0 0 0 0 .707.494.494 0 0 0 .707 0l2.49-2.49 3.492 7.214c.825 1.704-.97 3.5-2.675 2.673zM5.014 8.806c-1.657 0-3-.672-3-1.5 0-.83 1.343-1.5 3-1.5.302 0 .588.03.863.07-.04-.275-.07-.56-.07-.863 0-1.657.67-3 1.5-3 .828 0 1.5 1.343 1.5 3 0 1.293-2.5 3.793-3.793 3.793z"></path></symbol><symbol id="24x24_vehicle_air_conditioning_temporary" height="24" viewBox="0 0 24 24" width="24"><circle cx="12" cy="12" r="1"></circle><path d="M20.738 10.61a1.9 1.9 0 0 0-1.33-.878 2.89 2.89 0 0 0-2.385.933 2.653 2.653 0 0 1-1.575.798 3.504 3.504 0 0 0-.843-1.777c.893-.436 2.314-1.295 2.667-2.504a2.908 2.908 0 0 0-.098-2.286 4.243 4.243 0 0 0-2.69-1.647 4.983 4.983 0 0 0-3.848.11 1.902 1.902 0 0 0-.88 1.32 2.88 2.88 0 0 0 .933 2.385 2.793 2.793 0 0 1 .79 1.48 3.497 3.497 0 0 0-1.85.894 4.86 4.86 0 0 0-2.467-2.59 2.905 2.905 0 0 0-2.286.097 4.243 4.243 0 0 0-1.65 2.69 4.982 4.982 0 0 0 .11 3.85 1.9 1.9 0 0 0 1.33.877 2.263 2.263 0 0 0 .372.032 3.175 3.175 0 0 0 2.012-.965 2.753 2.753 0 0 1 1.503-.79 3.49 3.49 0 0 0 .9 1.746 4.57 4.57 0 0 0-2.47 2.21 2.905 2.905 0 0 0-.03 2.29 4.248 4.248 0 0 0 2.598 1.79 7.235 7.235 0 0 0 2.317.437 3.147 3.147 0 0 0 1.53-.34 1.9 1.9 0 0 0 .95-1.278 2.878 2.878 0 0 0-.8-2.435 2.54 2.54 0 0 1-.714-1.68 3.516 3.516 0 0 0 1.546-.84c.43.89 1.3 2.35 2.524 2.708a4.09 4.09 0 0 0 1.14.182 2.324 2.324 0 0 0 1.145-.28 4.247 4.247 0 0 0 1.65-2.69 4.98 4.98 0 0 0-.11-3.85zM8.534 11.63a3.58 3.58 0 0 0-2.112 1.036c-.61.506-1.015.81-1.583.716a.89.89 0 0 1-.65-.426 4.14 4.14 0 0 1 0-3.04c.34-1.203.69-1.827 1.17-2.09a1.985 1.985 0 0 1 1.52-.013c.92.267 1.71 1.717 2.06 2.507a3.434 3.434 0 0 0-.41 1.31zm2.925-5.194c-.51-.61-.82-1.014-.72-1.583a.892.892 0 0 1 .42-.648 4.143 4.143 0 0 1 3.04.004c1.202.34 1.826.69 2.09 1.17a1.986 1.986 0 0 1 .013 1.52c-.276.94-1.798 1.75-2.57 2.08a3.455 3.455 0 0 0-1.248-.43 3.58 3.58 0 0 0-1.037-2.12zm1.92 12.844a.893.893 0 0 1-.46.62 4.143 4.143 0 0 1-3.04-.17c-1.18-.41-1.786-.79-2.022-1.28a1.987 1.987 0 0 1 .07-1.52c.293-.84 1.603-1.515 2.437-1.848a3.453 3.453 0 0 0 1.464.398 3.574 3.574 0 0 0 .92 2.176c.47.636.754 1.056.63 1.62zM12 14.5a2.5 2.5 0 1 1 2.5-2.5 2.503 2.503 0 0 1-2.5 2.5zm7.888-.315c-.345 1.202-.694 1.827-1.17 2.09a1.985 1.985 0 0 1-1.522.013c-.98-.286-1.818-1.92-2.118-2.658a3.45 3.45 0 0 0 .374-1.158 3.506 3.506 0 0 0 2.21-1.037c.61-.507 1.012-.81 1.582-.716a.89.89 0 0 1 .65.42 4.138 4.138 0 0 1-.006 3.04z"></path></symbol><symbol id="24x24_vehicle_battery_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M18 12.5h-1v-1a.5.5 0 0 0-1 0v1h-1a.5.5 0 0 0 0 1h1v1a.5.5 0 0 0 1 0v-1h1a.5.5 0 0 0 0-1zm-9 0H6a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1z"></path><path d="M20 7V5.5a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 0-.5.5V7H9V5.5a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 0-.5.5V7H2v12h20V7zm-4-1h3v1h-3zM5 6h3v1H5zm16 12H3V8h18z"></path></symbol><symbol id="24x24_vehicle_electrical_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M6.5 22a.5.5 0 0 1-.468-.676L8.778 14H7.5a.5.5 0 0 1-.447-.724L9.69 8H8.5a.5.5 0 0 1-.43-.757l3-5A.498.498 0 0 1 11.5 2h5a.5.5 0 0 1 .416.777L15.434 5H17.5a.5.5 0 0 1 .384.82L13.567 11H15.5a.5.5 0 0 1 .372.835l-9 10A.5.5 0 0 1 6.5 22zm1.81-9H9.5a.5.5 0 0 1 .468.676L7.896 19.2l6.48-7.2H12.5a.5.5 0 0 1-.384-.82L16.433 6H14.5a.5.5 0 0 1-.416-.777L15.566 3h-3.783l-2.4 4H10.5a.5.5 0 0 1 .447.724z"></path></symbol><symbol id="24x24_vehicle_light_temporary" height="24" viewBox="0 0 24 24" width="24"><path d="M21.5 14h-7a.5.5 0 0 1 0-1h7a.5.5 0 0 1 0 1zm0-3h-7a.5.5 0 0 1 0-1h7a.5.5 0 0 1 0 1zm0 6h-7a.5.5 0 0 1 0-1h7a.5.5 0 0 1 0 1zm0-9h-7a.5.5 0 0 1 0-1h7a.5.5 0 0 1 0 1zM8.8 18.8a6.8 6.8 0 0 1 0-13.6c1.676 0 3.7 3.033 3.7 6.8s-2.024 6.8-3.7 6.8zm0-12.6a5.8 5.8 0 0 0 0 11.6c.925 0 2.7-2.45 2.7-5.8S9.725 6.2 8.8 6.2z"></path></symbol><symbol id="24x24_video" height="24" viewBox="0 0 24 24" width="24"><path d="M17 14.6V9.4L22 6v12l-5-3.4zM13 19H5a3 3 0 0 1-3-3V8a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v8a3 3 0 0 1-3 3z"></path></symbol><symbol id="24x24_visible" height="24" viewBox="0 0 24 24" width="24"><path d="M12 20c-5.078 0-9.4-3.337-11-8 1.6-4.663 5.922-8 11-8s9.4 3.337 11 8c-1.6 4.663-5.922 8-11 8zm0-14c-3.857 0-7.337 2.384-8.86 6 1.524 3.616 5.003 6 8.86 6 3.857 0 7.336-2.384 8.86-6-1.524-3.616-5.003-6-8.86-6zm0 10a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm-1-6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"></path></symbol><symbol id="24x24_waiter" height="24" viewBox="0 0 24 24" width="24"><path d="M21 18v1H3v-1H1v-2h22v2h-2zm-2.47-9.39A9.502 9.502 0 0 1 21.503 15H2.498a9.502 9.502 0 0 1 2.948-6.367l.024-.023a9.603 9.603 0 0 1 1.29-1.027c.042-.028.083-.057.126-.084a9.44 9.44 0 0 1 .6-.355c.057-.03.112-.063.17-.093.196-.1.398-.192.602-.28.068-.03.134-.062.203-.09.204-.08.41-.15.618-.217.075-.024.147-.053.223-.075a9.64 9.64 0 0 1 .66-.164c.07-.015.137-.035.207-.05.292-.056.59-.1.89-.13a1.227 1.227 0 0 1-.306-.797 1.25 1.25 0 0 1 2.5 0c0 .305-.122.58-.306.794.302.03.6.075.89.132.07.014.137.034.206.05.22.048.443.1.66.164.076.023.15.05.223.076.208.067.414.137.615.218.068.027.134.06.202.09a8.66 8.66 0 0 1 1.372.724c.043.026.084.055.126.083a9.615 9.615 0 0 1 .682.498c.21.168.414.344.61.53z"></path></symbol><symbol id="24x24_walk" height="24" viewBox="0 0 24 24" width="24"><path d="M17.803 11.497l-3.307-.568-1.326-2.32-.62 4.194 2.174 2.826 1.8 4.46a1 1 0 0 1-.61 1.323l-.074.024a1 1 0 0 1-1.237-.56L12.786 16.6l-1.91-2.03-2.43 6.617a.946.946 0 0 1-1.795-.6l2.2-7.317.35-4.832-1.73.983-.522 3.5-.96-.01.023-4.336 3.377-2.4c1.08-.78 4.04-.298 4.412.208.703 1.198 1.564 3.11 1.564 3.11l2.73 1.08-.286.925zM12.006 5.25a1.75 1.75 0 1 1 0-3.5 1.75 1.75 0 0 1 0 3.5z"></path></symbol><symbol id="24x24_warning" height="24" viewBox="0 0 24 24" width="24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm-1 5a1 1 0 0 1 2 0v5a1 1 0 0 1-2 0V7zm1 11a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"></path></symbol><symbol id="24x24_warning_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-19c-4.963 0-9 4.037-9 9s4.037 9 9 9 9-4.037 9-9-4.037-9-9-9zm0 15a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm0-5a1 1 0 0 1-1-1V7a1 1 0 0 1 2 0v5a1 1 0 0 1-1 1z"></path></symbol><symbol id="24x24_whatsapp" height="24" viewBox="0 0 24 24" width="24"><path d="M12.038 20.855h-.004a9.014 9.014 0 0 1-4.29-1.087l-4.757 1.24 1.273-4.625a8.893 8.893 0 0 1-1.198-4.464c.002-4.926 4.03-8.93 8.976-8.93 2.4 0 4.654.93 6.35 2.62a8.854 8.854 0 0 1 2.625 6.314c-.002 4.923-4.028 8.93-8.975 8.93zm5.277-14.18A7.426 7.426 0 0 0 12.04 4.5c-4.114 0-7.46 3.328-7.462 7.42a7.38 7.38 0 0 0 1.14 3.95l.178.28-.754 2.738 2.824-.737.272.164a7.483 7.483 0 0 0 3.797 1.035h.003c4.112 0 7.458-3.33 7.46-7.423a7.358 7.358 0 0 0-2.183-5.25zm-2.4 9.496a3.076 3.076 0 0 1-1.412-.086c-.326-.102-.744-.24-1.28-.47-2.25-.966-3.718-3.22-3.83-3.368-.112-.15-.916-1.21-.916-2.308 0-1.098.58-1.638.785-1.86a.826.826 0 0 1 .598-.28c.15 0 .3 0 .43.007.138.007.323-.052.505.383.187.447.635 1.545.69 1.657.057.11.095.242.02.39-.075.15-.112.243-.224.373s-.233.29-.334.39c-.112.112-.23.233-.098.456.13.223.58.954 1.247 1.546.857.76 1.58.994 1.804 1.106.223.112.354.093.485-.056.13-.15.56-.652.71-.876.15-.223.3-.186.504-.11.205.073 1.31.613 1.532.724.225.112.375.168.43.26.057.094.057.54-.13 1.062-.187.52-1.083.997-1.514 1.06z"></path></symbol><symbol id="24x24_wheelchair" height="24" viewBox="0 0 24 24" width="24"><path d="M21.948 16.684L20.72 13H18V8H9V6c0-2.206-1.794-4-4-4a1 1 0 0 0 0 2c1.102 0 2 .897 2 2v4.09A5.996 5.996 0 0 0 8 22a6 6 0 0 0 6-6c0-.34-.035-.674-.09-1H16v2.21A2.498 2.498 0 0 0 17 22a2.5 2.5 0 0 0 1-4.79V15h1.28l.772 2.316a1 1 0 1 0 1.896-.632zM8 20c-2.206 0-4-1.794-4-4s1.794-4 4-4 4 1.794 4 4-1.794 4-4 4zm5.19-7A5.996 5.996 0 0 0 9 10.09V10h7v3h-2.81z"></path></symbol><symbol id="24x24_wifi" height="24" viewBox="0 0 24 24" width="24"><path d="M20.534 10.877c-4.706-4.706-12.362-4.706-17.068 0L2.1 9.51c5.46-5.457 14.34-5.457 19.8 0l-1.366 1.367zm-2.048 2.048L17.12 14.29c-2.823-2.823-7.417-2.823-10.24 0l-1.366-1.365c3.576-3.576 9.396-3.576 12.972 0zm-5.072 2.243a2 2 0 1 1-2.83 2.83 2 2 0 0 1 2.83-2.83z"></path></symbol><symbol id="24x24_windows" height="24" viewBox="0 0 24 24" width="24"><path d="M11 19.875v-6.87h10V21l-10-1.125zm0-14.75L21 4v8.004H11v-6.88zm-8 7.88h7v6.745L3 19v-5.996zM3 6l7-.75v6.754H3V6z"></path></symbol><symbol id="24x24_yelp" height="24" viewBox="0 0 24 24" width="24"><path d="M18.803 12.49l-4.162 1.194c-.8.23-1.45-.666-.98-1.357l2.42-3.59a.893.893 0 0 1 1.33-.172 7.66 7.66 0 0 1 1.97 2.71.894.894 0 0 1-.572 1.215zm-4.187 2.627l4.117 1.338a.893.893 0 0 1 .53 1.233 7.762 7.762 0 0 1-2.058 2.64.894.894 0 0 1-1.326-.216l-2.3-3.674c-.44-.706.24-1.578 1.03-1.32zm-3.996-3.64l-4.07-7.05a.893.893 0 0 1 .388-1.25A12.475 12.475 0 0 1 11.324 2c.518-.04.96.37.96.89v8.138c0 .913-1.208 1.236-1.664.446zm-.714 3.475L5.704 16a.894.894 0 0 1-1.103-.767 7.68 7.68 0 0 1 .358-3.33.892.892 0 0 1 1.237-.516l3.89 1.898c.75.365.635 1.466-.173 1.667zm.738 1.23c.557-.62 1.584-.205 1.555.627l-.158 4.322c-.02.54-.51.94-1.04.85A7.76 7.76 0 0 1 7.9 20.73a.893.893 0 0 1-.156-1.333l2.897-3.22z"></path></symbol><symbol id="24x24_yelp_outline" height="24" viewBox="0 0 24 24" width="24"><path d="M19.043 15.504l-3.34-1.085 3.376-.97a1.895 1.895 0 0 0 1.21-2.58 8.627 8.627 0 0 0-2.23-3.06 1.892 1.892 0 0 0-2.82.36l-1.967 2.91V2.89a1.893 1.893 0 0 0-2.037-1.886 13.51 13.51 0 0 0-4.74 1.27 1.894 1.894 0 0 0-.82 2.653l4.067 7.046.03.052-3.154-1.54A1.89 1.89 0 0 0 4 11.58a8.62 8.62 0 0 0-.395 3.764 1.893 1.893 0 0 0 2.338 1.623l3.407-.85L7 18.727a1.893 1.893 0 0 0 .336 2.826 8.823 8.823 0 0 0 3.503 1.418 1.886 1.886 0 0 0 2.2-1.8l.12-3.51 1.86 2.98a1.89 1.89 0 0 0 2.81.46 8.818 8.818 0 0 0 2.327-2.98 1.89 1.89 0 0 0-1.123-2.61zm-5.388-3.177l2.422-3.59a.893.893 0 0 1 1.33-.172c.83.732 1.51 1.65 1.968 2.71a.894.894 0 0 1-.572 1.215l-4.162 1.194a.923.923 0 0 1-.25.036c-.67 0-1.14-.778-.73-1.393zM6.55 4.43a.893.893 0 0 1 .388-1.252A12.475 12.475 0 0 1 11.395 2c.487 0 .89.397.89.893v8.137c0 .556-.45.893-.903.893a.867.867 0 0 1-.763-.447L6.55 4.43zM5.705 16a.895.895 0 0 1-1.103-.767 7.68 7.68 0 0 1 .35-3.33.89.89 0 0 1 1.24-.516l3.89 1.898c.75.365.634 1.466-.174 1.668L5.704 16zm6.344 5.138a.894.894 0 0 1-1.04.85 7.758 7.758 0 0 1-3.11-1.256.893.893 0 0 1-.16-1.333l2.896-3.22a.89.89 0 0 1 1.554.62l-.152 4.33zm1.24-6.747v-.02l.01.017c-.005.004-.01.01-.016.013zm5.97 3.3a7.762 7.762 0 0 1-2.06 2.64.89.89 0 0 1-1.328-.21l-2.294-3.68c-.388-.62.09-1.366.75-1.366a.9.9 0 0 1 .282.047l4.118 1.33a.893.893 0 0 1 .53 1.235z"></path></symbol><symbol id="24x24_youtube" height="24" viewBox="0 0 24 24" width="24"><path d="M21.8 15.973s-.195 1.372-.795 1.976c-.76.79-1.613.79-2.004.84-2.79.2-7 .21-7 .21s-5.2-.05-6.8-.2c-.44-.09-1.44-.06-2.2-.85-.6-.61-.792-1.98-.792-1.98s-.2-1.61-.2-3.22v-1.51c0-1.61.2-3.228.2-3.228S2.4 6.642 3 6.04c.757-.79 1.61-.793 2-.84C7.798 5 11.996 5 11.996 5h.008S16.2 5 19 5.2c.392.048 1.245.052 2.005.845.6.604.795 1.975.795 1.975s.2 1.61.2 3.222v1.51c0 1.61-.2 3.22-.2 3.22zM10 9v6l5.5-3L10 9z"></path></symbol><symbol id="28x28_search" height="28" viewBox="0 0 28 28" width="28"><path d="M24.53 23.47l-5.557-5.558c-.035-.034-.078-.05-.116-.077 2.953-3.477 2.796-8.71-.485-11.99a8.798 8.798 0 0 0-6.264-2.595 8.79 8.79 0 0 0-6.263 2.595 8.795 8.795 0 0 0-2.595 6.263c0 2.366.92 4.59 2.595 6.264a8.826 8.826 0 0 0 6.263 2.59c2.042 0 4.08-.706 5.727-2.105.027.04.043.082.077.116l5.558 5.557c.146.147.338.22.53.22a.75.75 0 0 0 .53-1.28zM6.905 17.31a7.31 7.31 0 0 1-2.155-5.2c0-1.965.766-3.813 2.155-5.203a7.314 7.314 0 0 1 5.203-2.155 7.31 7.31 0 0 1 5.203 2.155c2.87 2.87 2.87 7.537 0 10.406-2.865 2.87-7.534 2.87-10.403 0z"></path></symbol><symbol id="30x30_activity" height="30" viewBox="0 0 30 30" width="30"><path d="M16 26h-.038a1 1 0 0 1-.932-.758L10.958 8.955l-1.993 7.308A1 1 0 0 1 8 17H2a1 1 0 0 1 0-2h5.236l2.8-10.263A1 1 0 0 1 11 4h.01a1 1 0 0 1 .96.757l4.168 16.67 3.914-11.743a.998.998 0 0 1 1.896 0L23.72 15H28a1 1 0 0 1 0 2h-5a.998.998 0 0 1-.948-.684L21 13.162l-4.052 12.154A.997.997 0 0 1 16 26z"></path></symbol><symbol id="30x30_activity_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M16 25.5h-.02a.5.5 0 0 1-.465-.38L10.98 6.98l-2.5 9.152A.5.5 0 0 1 8 16.5H2a.5.5 0 0 1 0-1h5.618l2.9-10.63c.06-.22.255-.398.487-.37a.5.5 0 0 1 .48.38l4.583 18.333 4.457-13.37c.137-.41.813-.41.95 0L23.36 15.5H28a.5.5 0 0 1 0 1h-5a.502.502 0 0 1-.475-.342L21 11.58l-4.525 13.58a.5.5 0 0 1-.475.34z"></path></symbol><symbol id="30x30_add" height="30" viewBox="0 0 30 30" width="30"><path d="M26 14H16V4a1 1 0 0 0-2 0v10H4a1 1 0 0 0 0 2h10v10a1 1 0 0 0 2 0V16h10a1 1 0 0 0 0-2z"></path></symbol><symbol id="30x30_add_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26 14.5H15.5V4a.5.5 0 0 0-1 0v10.5H4a.5.5 0 0 0 0 1h10.5V26a.5.5 0 0 0 1 0V15.5H26a.5.5 0 0 0 0-1z"></path></symbol><symbol id="30x30_basket" height="30" viewBox="0 0 30 30" width="30"><path d="M25 16H5a2 2 0 0 1-2-2v-1a2 2 0 0 1 2-2h2.975l4.37-7.864a.75.75 0 1 1 1.31.728L9.692 11h10.62l-3.966-7.136a.75.75 0 1 1 1.312-.728L22.026 11H25a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2zm-1.81 9.242a1 1 0 0 1-.97.758H7.78a1 1 0 0 1-.97-.758L4.75 17h20.5l-2.06 8.242z"></path></symbol><symbol id="30x30_basket_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M25 11h-3.26l-4.303-7.743a.5.5 0 1 0-.874.486L20.595 11H9.405l4.032-7.257a.5.5 0 1 0-.874-.486L8.26 11H5a2 2 0 0 0-2 2v1c0 .924.63 1.694 1.48 1.923l2.33 9.32a1 1 0 0 0 .97.757h14.44a1 1 0 0 0 .97-.757l2.33-9.32c.85-.23 1.48-1 1.48-1.923v-1a2 2 0 0 0-2-2zm-2.78 14H7.78l-2.25-9h18.94l-2.25 9zM26 14c0 .55-.45 1-1 1H5c-.55 0-1-.45-1-1v-1c0-.55.45-1 1-1h20c.55 0 1 .45 1 1v1z"></path></symbol><symbol id="30x30_bell" height="30" viewBox="0 0 30 30" width="30"><path d="M26.634 21H26.5c0-5.658-4.11-10.363-9.5-11.314V8h.5c.827 0 1.5-.673 1.5-1.5S18.327 5 17.5 5h-5c-.827 0-1.5.673-1.5 1.5S11.673 8 12.5 8h.5v1.686c-5.39.95-9.5 5.656-9.5 11.314h-.134C2.613 21 2 21.613 2 22.366V25h26v-2.634c0-.753-.613-1.366-1.366-1.366zM12 6.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zM14 8h2v1.55c-.33-.028-.662-.05-1-.05-.338 0-.67.022-1 .05V8zm1 2.5c5.79 0 10.5 4.71 10.5 10.5h-21c0-5.79 4.71-10.5 10.5-10.5zM27 24H3v-1.634c0-.202.164-.366.366-.366h23.268c.202 0 .366.164.366.366V24z"></path></symbol><symbol id="30x30_bell_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M2 25v-2.634C2 21.613 2.613 21 3.366 21h23.268c.753 0 1.366.613 1.366 1.366V25H2zM14 9.55V8h-1.5c-.827 0-1.5-.673-1.5-1.5S11.673 5 12.5 5h5c.827 0 1.5.673 1.5 1.5S18.327 8 17.5 8H16v1.55c5.544.48 9.97 4.907 10.452 10.45H3.548C4.028 14.457 8.456 10.03 14 9.55z"></path></symbol><symbol id="30x30_bizhouse" height="30" viewBox="0 0 30 30" width="30"><path d="M25.927 15.152a3.54 3.54 0 0 1-4.844-1.236 3.54 3.54 0 0 1-6.082 0 3.542 3.542 0 0 1-6.08 0 3.54 3.54 0 0 1-4.842 1.236c-1.382-.818-1.947-2.626-1.316-4.205.363-.906.9-1.964 1.42-2.987.425-.838.827-1.63 1.045-2.174A1.25 1.25 0 0 1 6.392 5H23.61c.518 0 .978.31 1.17.792l2.447 5.12.012.03c.63 1.582.07 3.393-1.316 4.21zM11.96 16.645c1.13 0 2.215-.432 3.04-1.174a4.563 4.563 0 0 0 3.042 1.178c1.13 0 2.216-.432 3.04-1.174A4.562 4.562 0 0 0 24 16.634V25h-7v-5h-4v5H6v-8.367a4.56 4.56 0 0 0 2.918-1.162 4.567 4.567 0 0 0 3.042 1.178z"></path></symbol><symbol id="30x30_bizhouse_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M27.25 11.965l-2.47-6.173A1.256 1.256 0 0 0 23.61 5H6.39c-.518 0-.976.31-1.168.786L2.75 11.974c-.573 1.43-.18 3.046.958 3.928a3.504 3.504 0 0 0 2.17.743c.04 0 .08-.007.122-.01V25h7v-5h4v5h7v-8.364c.042.002.082.01.124.01.79 0 1.54-.257 2.165-.74 1.14-.883 1.533-2.503.96-3.94zM23 24h-5v-5h-6v5H7v-7.546a3.552 3.552 0 0 0 1.918-1.538 3.543 3.543 0 0 0 3.04 1.73A3.542 3.542 0 0 0 15 14.916a3.542 3.542 0 0 0 3.043 1.73 3.54 3.54 0 0 0 3.04-1.73A3.55 3.55 0 0 0 23 16.454V24zm2.678-8.885a2.544 2.544 0 0 1-4.095-2.012.5.5 0 0 0-1 0c0 1.4-1.14 2.54-2.54 2.54a2.544 2.544 0 0 1-2.542-2.54.5.5 0 0 0-1 0c0 1.4-1.14 2.54-2.54 2.54-1.4 0-2.54-1.14-2.54-2.54a.5.5 0 0 0-1 0 2.544 2.544 0 0 1-4.097 2.01c-.785-.61-1.05-1.75-.643-2.768l2.475-6.187A.25.25 0 0 1 6.393 6H23.61a.26.26 0 0 1 .24.164l2.47 6.172c.41 1.026.146 2.168-.643 2.78z"></path></symbol><symbol id="30x30_bizhouse_switch" height="30" viewBox="0 0 30 30" width="30"><path d="M29.354 19.854l-1.5 1.5a.498.498 0 0 1-.708 0 .502.502 0 0 1 0-.708l.647-.646H22.5a.5.5 0 0 1 0-1h5.293l-.647-.646a.5.5 0 0 1 .707-.707l1.5 1.5a.502.502 0 0 1 0 .707zm-5.5 1.792a.502.502 0 0 1 0 .708l-.647.646H28.5a.5.5 0 0 1 0 1h-5.293l.647.647a.5.5 0 1 1-.707.706l-1.5-1.5a.502.502 0 0 1 0-.707l1.5-1.5a.5.5 0 0 1 .707 0zm-5.25-7.776a3.034 3.034 0 0 1-2.535-1.367 3.033 3.033 0 0 1-5.07 0 3.034 3.034 0 0 1-5.07 0 3.034 3.034 0 0 1-4.333.776c-1.022-.757-1.38-2.175-.87-3.45l2.048-5.12c.173-.432.585-.71 1.05-.71h14.35c.467 0 .88.28 1.05.714l2.048 5.113c.51 1.278.153 2.697-.87 3.452a3.01 3.01 0 0 1-1.8.59zm-12.672.104a4.023 4.023 0 0 0 2.534.896c.937 0 1.826-.323 2.535-.896a4.023 4.023 0 0 0 2.536.896c.937 0 1.826-.322 2.534-.896a4.017 4.017 0 0 0 2.533.896c.134 0 .265-.018.397-.03V21h-7v-4h-2v4H3v-6.16c.132.012.263.03.397.03.937 0 1.827-.323 2.535-.896z"></path></symbol><symbol id="30x30_bizhouse_switch_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M29.354 19.854l-1.5 1.5a.498.498 0 0 1-.708 0 .502.502 0 0 1 0-.708l.647-.646H22.5a.5.5 0 0 1 0-1h5.293l-.647-.646a.5.5 0 0 1 .707-.707l1.5 1.5a.502.502 0 0 1 0 .707zm-5.5 1.792a.502.502 0 0 1 0 .708l-.647.646H28.5a.5.5 0 0 1 0 1h-5.293l.647.647a.5.5 0 1 1-.707.706l-1.5-1.5a.502.502 0 0 1 0-.707l1.5-1.5a.5.5 0 0 1 .707 0zM19 13.84V21h-7v-4h-2v4H3v-7.16a3.002 3.002 0 0 1-1.402-.56C.575 12.523.216 11.105.728 9.83l2.047-5.12c.173-.432.585-.71 1.05-.71h14.35c.467 0 .88.28 1.05.714l2.048 5.113c.51 1.278.153 2.697-.87 3.452a2.995 2.995 0 0 1-1.403.56zM4 20h5v-4h4v4h5v-6.207a3.03 3.03 0 0 1-1.93-1.29 3.033 3.033 0 0 1-5.07 0 3.034 3.034 0 0 1-5.07 0A3.033 3.033 0 0 1 4 13.793V20zm16.345-9.802L18.3 5.084A.136.136 0 0 0 18.174 5H3.827a.125.125 0 0 0-.122.08l-2.05 5.12c-.336.84-.11 1.796.537 2.273a2.037 2.037 0 0 0 3.24-1.64.5.5 0 0 1 1 0c0 1.122.913 2.035 2.034 2.035a2.036 2.036 0 0 0 2.034-2.034.5.5 0 0 1 1 0c0 1.12.913 2.034 2.035 2.034a2.036 2.036 0 0 0 2.034-2.034.5.5 0 0 1 1 0 2.036 2.036 0 0 0 3.24 1.64c.644-.478.87-1.436.533-2.278z"></path></symbol><symbol id="30x30_bookmark" height="30" viewBox="0 0 30 30" width="30"><path d="M20 3H10a3 3 0 0 0-3 3v21l8-6 8 6V6a3 3 0 0 0-3-3zm-2.505 11.943l-2.526-1.55L12.526 15 13 12.234l-2-1.957 2.766-.404L14.97 7l1.264 2.873 2.766.404-2 1.957.495 2.71z"></path></symbol><symbol id="30x30_bookmark_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M15 21l-8 6V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v21l-8-6zm7-15c0-1.103-.897-2-2-2H10c-1.103 0-2 .897-2 2v19l6.4-4.8.6-.45.6.45L22 25V6zm-7.03 7.392L12.527 15 13 12.234l-2-1.957 2.766-.404L14.97 7l1.264 2.873 2.766.404-2 1.957.495 2.71-2.526-1.552z"></path></symbol><symbol id="30x30_bookmark_outline_temporary" height="30" viewBox="0 0 30 30" width="30"><path d="M20 3H10a3 3 0 0 0-3 3v21l8-6 8 6V6a3 3 0 0 0-3-3zm2 22l-6.4-4.8-.6-.45-.6.45L8 25V6c0-1.103.897-2 2-2h10c1.103 0 2 .897 2 2v19z"></path></symbol><symbol id="30x30_bookmark_temporary" height="30" viewBox="0 0 30 30" width="30"><path d="M20 3H10a3 3 0 0 0-3 3v21l8-6 8 6V6a3 3 0 0 0-3-3z"></path></symbol><symbol id="30x30_bullhorn" height="30" viewBox="0 0 30 30" width="30"><path d="M25.5 24a1.5 1.5 0 0 1-1.5-1.5v-15a1.5 1.5 0 0 1 3 0v15a1.5 1.5 0 0 1-1.5 1.5zM17 24H8v-6.125l-3-.834V18a1 1 0 0 1-2 0v-6a1 1 0 0 1 2 0v.958l18-5V22.04l-6-1.664V24zm-2-4.18l-5-1.39V22h5v-2.18z"></path></symbol><symbol id="30x30_bullhorn_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26.803 5.958a.49.49 0 0 0-.437-.083L5 11.81V11a1 1 0 0 0-2 0v7a1 1 0 0 0 2 0v-.935l4 1.11V23h8v-2.602L26.366 23a.507.507 0 0 0 .437-.083.502.502 0 0 0 .197-.398V6.354a.502.502 0 0 0-.197-.398zM5 12.848l17-4.722V20.75L5 16.027v-3.18zM16 22h-6v-3.546l6 1.667V22zm10-.14l-3-.833V7.847l3-.832V21.86z"></path></symbol><symbol id="30x30_camera_flip_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M23.5 25h-17C4.57 25 3 23.43 3 21.5v-10C3 9.57 4.57 8 6.5 8h2.536A3.505 3.505 0 0 1 12.5 5h5c1.76 0 3.22 1.306 3.465 3H23.5c1.93 0 3.5 1.57 3.5 3.5v10c0 1.93-1.57 3.5-3.5 3.5zM26 11.5c0-1.378-1.12-2.5-2.5-2.5H20v-.5C20 7.122 18.88 6 17.5 6h-5A2.503 2.503 0 0 0 10 8.5V9H6.5A2.503 2.503 0 0 0 4 11.5v10C4 22.878 5.122 24 6.5 24h17c1.38 0 2.5-1.122 2.5-2.5v-10zm-11 10a5.487 5.487 0 0 1-4.35-2.15l.717-.717A4.487 4.487 0 0 0 15 20.5c2.48 0 4.5-2.02 4.5-4.5H18l2-2 2 2h-1.5c0 3.033-2.468 5.5-5.5 5.5zm0-10c-2.48 0-4.5 2.02-4.5 4.5H12l-2 2-2-2h1.5c0-3.033 2.467-5.5 5.5-5.5a5.49 5.49 0 0 1 4.35 2.15l-.717.717A4.487 4.487 0 0 0 15 11.5z"></path></symbol><symbol id="30x30_cart" height="30" viewBox="0 0 30 30" width="30"><path d="M27.846 11.77l-3.333 8A2 2 0 0 1 22.667 21H9.75a2 2 0 0 1-1.98-1.736L6 6H3.5a1.5 1.5 0 0 1 0-3h2.96a3 3 0 0 1 2.958 2.507L10 9h16a2 2 0 0 1 1.846 2.77zM25.5 24c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3 3 1.346 3 3zm-3-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-13-2c1.654 0 3 1.346 3 3s-1.346 3-3 3-3-1.346-3-3 1.346-3 3-3zm0 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"></path></symbol><symbol id="30x30_cart_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M27.846 11.77l-3.333 8A2 2 0 0 1 22.667 21H9.75a2 2 0 0 1-1.98-1.736L6 6H3.5a1.5 1.5 0 0 1 0-3h2.96a3 3 0 0 1 2.958 2.507L10 9h16a2 2 0 0 1 1.846 2.77zm-1.014-1.325A.985.985 0 0 0 26 10H9.153l-.14-.836L8.43 5.67A1.993 1.993 0 0 0 6.46 4H3.5a.5.5 0 0 0 0 1h3.376l.115.868 1.77 13.264c.068.495.494.868.99.868h12.92a.998.998 0 0 0 .923-.615l3.334-8a.985.985 0 0 0-.09-.94zM9.5 22a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 4c.827 0 1.5-.673 1.5-1.5S10.327 23 9.5 23 8 23.673 8 24.5 8.673 26 9.5 26zm13-4a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zm0 4c.827 0 1.5-.673 1.5-1.5s-.673-1.5-1.5-1.5-1.5.673-1.5 1.5.673 1.5 1.5 1.5z"></path></symbol><symbol id="30x30_chat" height="30" viewBox="0 0 30 30" width="30"><path d="M15 4C8.925 4 4 7.83 4 12.556c0 2.965 2.053 5.578 5 7.112V26l6-4.89c6.075 0 11-3.83 11-8.554C26 7.83 21.075 4 15 4z"></path></symbol><symbol id="30x30_chat_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M15 5c5.514 0 10 3.39 10 7.556s-4.486 7.555-10 7.555h-.356l-.276.227L10 23.897V19.06l-.538-.28C6.668 17.326 5 15 5 12.556 5 8.39 9.486 5 15 5m0-1C8.925 4 4 7.83 4 12.556c0 2.965 2.053 5.578 5 7.112V26l6-4.89c6.075 0 11-3.83 11-8.554C26 7.83 21.075 4 15 4z"></path></symbol><symbol id="30x30_checkmark_badged" height="30" viewBox="0 0 30 30" width="30"><path d="M15 3C8.373 3 3 8.373 3 15s5.373 12 12 12 12-5.373 12-12S21.627 3 15 3zm5.93 9.425l-7.21 7.208-4.65-4.63a1.2 1.2 0 1 1 1.694-1.7l2.953 2.94 5.516-5.516a1.203 1.203 0 0 1 1.698 0 1.2 1.2 0 0 1 0 1.698z"></path></symbol><symbol id="30x30_close" height="30" viewBox="0 0 30 30" width="30"><path d="M23.485 22.07L16.415 15l7.07-7.07a1 1 0 1 0-1.414-1.415L15 13.585l-7.07-7.07A1 1 0 0 0 6.514 7.93l7.07 7.07-7.07 7.07a1 1 0 1 0 1.414 1.415l7.07-7.07 7.07 7.07a1 1 0 1 0 1.415-1.414z"></path></symbol><symbol id="30x30_close_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M23.132 22.425L15.707 15l7.425-7.425a.5.5 0 0 0-.707-.707L15 14.293 7.575 6.868a.5.5 0 0 0-.707.707L14.293 15l-7.425 7.425a.5.5 0 0 0 .707.707L15 15.707l7.425 7.425a.5.5 0 0 0 .707-.707z"></path></symbol><symbol id="30x30_collections_tab" height="30" viewBox="0 0 30 30" width="30"><path d="M4 27V7h22v20H4zM24 9H6v16h18V9zm-9 2c2.55 0 4.625 2.033 4.625 4.533 0 2.347-3.814 6.796-4.248 7.295l-.377.434-.377-.434c-.435-.5-4.248-4.948-4.248-7.295C10.375 13.033 12.45 11 15 11zm0 6a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM7 5h17v1H7V5zm2-2h13v1H9V3z"></path></symbol><symbol id="30x30_collections_tab_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M4 27V7h22v20H4zM25 8H5v18h20V8zm-10 3c2.55 0 4.625 2.033 4.625 4.533 0 2.347-3.814 6.796-4.248 7.295l-.377.434-.377-.434c-.435-.5-4.248-4.948-4.248-7.295C10.375 13.033 12.45 11 15 11zm0 10.727c1.278-1.542 3.625-4.686 3.625-6.194C18.625 13.585 17 12 15 12s-3.625 1.585-3.625 3.533c0 1.51 2.347 4.652 3.625 6.194zm0-8.227c1.102 0 2 .897 2 2s-.898 2-2 2c-1.103 0-2-.897-2-2s.897-2 2-2zm0 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM7 5h17v1H7V5zm2-2h13v1H9V3z"></path></symbol><symbol id="30x30_discovery" height="30" viewBox="0 0 30 30" width="30"><path d="M27.414 9l1.414 1.414a1 1 0 1 1-1.414 1.414L26 10.414l-1.414 1.414a.997.997 0 0 1-1.414 0 1 1 0 0 1 0-1.414L24.586 9l-1.414-1.414a1 1 0 1 1 1.414-1.414L26 7.586l1.414-1.414a1 1 0 1 1 1.414 1.414L27.414 9zm-2.28 11.54a1 1 0 0 1 .28 1.387c-.69 1.044-1.608 1.873-2.65 2.4a1 1 0 0 1-.902-1.786c.744-.37 1.378-.95 1.887-1.72a.997.997 0 0 1 1.38-.28zm-6.83 4.17a.983.983 0 0 1-.33-.057c-1.12-.39-2.136-1.11-2.936-2.086a1 1 0 1 1 1.547-1.267c.565.69 1.272 1.195 2.046 1.465a.998.998 0 0 1-.32 1.944zm-3.945-5.538a1 1 0 0 1-1.16-.81c-.14-.74-.2-1.53-.2-2.35 0-.29-.01-.572-.03-.845a1 1 0 0 1 .93-1.064c.54-.025 1.03.38 1.06.93.02.318.032.644.032.98 0 .702.056 1.375.167 2a1 1 0 0 1-.81 1.16zm-1.46-7.028a1 1 0 0 1-.88-.522c-.45-.82-1.03-1.465-1.72-1.92a1 1 0 0 1 1.09-1.674c.975.64 1.776 1.526 2.38 2.638a1 1 0 0 1-.877 1.478zM7.11 9.097a4.45 4.45 0 0 0-2.17 1.223.994.994 0 0 1-1.415 0 1 1 0 0 1 0-1.413A6.45 6.45 0 0 1 6.68 7.145a1 1 0 1 1 .433 1.952zM3.28 13.45A10.88 10.88 0 0 0 3 16.01v.275a1 1 0 0 1-2 0v-.275c0-1.077.115-2.098.343-3.035.13-.537.675-.866 1.208-.736a1 1 0 0 1 .74 1.21zM2 19.5a1 1 0 0 1 1 1V22a1 1 0 0 1-2 0v-1.5a1 1 0 0 1 1-1zm22.922-2.118c.052-.44.078-.905.078-1.382a1 1 0 0 1 2 0c0 .554-.03 1.098-.092 1.616a1 1 0 1 1-1.986-.234z"></path></symbol><symbol id="30x30_discovery_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26.707 9l1.768 1.768a.5.5 0 0 1-.707.707L26 9.707l-1.768 1.768a.498.498 0 0 1-.707 0 .5.5 0 0 1 0-.707L25.293 9l-1.768-1.768a.5.5 0 0 1 .707-.707L26 8.293l1.768-1.768a.5.5 0 0 1 .707.707L26.707 9zm-2.033 12.266a.5.5 0 0 1 .102.7c-.672.903-1.535 1.607-2.496 2.034a.5.5 0 0 1-.406-.914c.816-.362 1.52-.94 2.1-1.717a.5.5 0 0 1 .7-.106zm-5.526 3.158a.476.476 0 0 1-.084-.007 5.857 5.857 0 0 1-2.912-1.41.5.5 0 1 1 .662-.748 4.87 4.87 0 0 0 2.414 1.17.5.5 0 0 1-.08.992zM14.97 20.66a.497.497 0 0 1-.656-.263c-.387-.908-.64-1.933-.75-3.048a.502.502 0 1 1 .996-.1c.1 1.012.327 1.94.674 2.752a.5.5 0 0 1-.263.656zm-1.013-5.858a.5.5 0 0 1-.562-.428c-.138-1.007-.404-1.92-.793-2.714a.5.5 0 0 1 .9-.44c.434.89.73 1.907.882 3.02a.5.5 0 0 1-.428.562zm-2.755-5.186a.5.5 0 0 1-.305-.104A4.783 4.783 0 0 0 8.41 8.52a.5.5 0 1 1 .09-.997c1.08.098 2.12.512 3.008 1.197a.5.5 0 0 1-.306.896zm-7.39 1.307a.497.497 0 0 1-.69.145.498.498 0 0 1-.145-.692C3.602 9.42 4.39 8.68 5.323 8.18a.5.5 0 1 1 .473.88c-.783.422-1.45 1.048-1.983 1.863zM2.5 16.013v.38a.5.5 0 0 1-1 0v-.38c0-.96.095-1.87.28-2.71a.5.5 0 0 1 .976.216 11.58 11.58 0 0 0-.256 2.49zm-.5 2.88a.5.5 0 0 1 .5.5V22a.5.5 0 0 1-1 0v-2.608a.5.5 0 0 1 .5-.5zM25.5 16a.5.5 0 0 1 1 0 12.14 12.14 0 0 1-.378 3.097.5.5 0 1 1-.967-.256c.23-.862.345-1.82.345-2.84z"></path></symbol><symbol id="30x30_food" height="30" viewBox="0 0 30 30" width="30"><path d="M23 26c0 1.103-.897 2-2 2s-2-.897-2-2V16h2.16C19.235 14.377 18 11.41 18 8.32c0-1.942.76-3.823 2.32-5.753a1.502 1.502 0 0 1 1.685-.48c.604.215.995.77.995 1.413v12.434c0 .023-.01.044-.013.066H23v10zM12 13.933V16h1v10c0 1.103-.897 2-2 2s-2-.897-2-2V16h1v-2.093a3.82 3.82 0 0 1-3-3.724V3a1 1 0 0 1 2 0v6h1V3a1 1 0 0 1 2 0v6h1V3a1 1 0 0 1 2 0v7.337a3.663 3.663 0 0 1-3 3.596z"></path></symbol><symbol id="30x30_food_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M23 25.5c0 1.378-1.122 2.5-2.5 2.5a2.503 2.503 0 0 1-2.5-2.5V16h2.16C18.235 14.377 17 11.41 17 8.32c0-1.942.76-3.823 2.32-5.753a1.502 1.502 0 0 1 1.685-.48c.604.215.995.77.995 1.413v12.434c0 .023-.01.044-.013.066H23v9.5zm-2-22a.48.48 0 0 0-.33-.47.543.543 0 0 0-.18-.03.49.49 0 0 0-.392.196C18.666 4.964 18 6.593 18 8.32c0 2.912 1.173 5.694 2.99 7.085l.01.01V3.5zM22 17h-3v8.5c0 .827.673 1.5 1.5 1.5s1.5-.673 1.5-1.5V17zm-11.01-3.042c.003.014.01.027.01.042v2h2v9.5c0 1.378-1.122 2.5-2.5 2.5A2.503 2.503 0 0 1 8 25.5V16h2v-2c0-.02.01-.037.01-.057C8.31 13.673 7 12.206 7 10.43V3a.5.5 0 0 1 1 0v6h2V3a.5.5 0 0 1 1 0v6h2V3a.5.5 0 0 1 1 0v7.57c0 1.748-1.318 3.178-3.01 3.388zM9 17v8.5c0 .827.673 1.5 1.5 1.5s1.5-.673 1.5-1.5V17H9zm4-7H8v.43A2.573 2.573 0 0 0 10.57 13 2.43 2.43 0 0 0 13 10.57V10z"></path></symbol><symbol id="30x30_guide" height="30" viewBox="0 0 30 30" width="30"><path d="M18 27V10h4V7a.5.5 0 0 1 1 0v3h4v17h-9zm6-14h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm0 3h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm0 3h-3a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1zm-11-1.5a.5.5 0 0 0-.5-.5H6V8.095l11-5.3V27h-4v-9.5zm1-7.5H9a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zm.5 3.5a.5.5 0 0 0-.5-.5H9a.5.5 0 0 0 0 1h5a.5.5 0 0 0 .5-.5zM12 27H3v-9h9v9z"></path></symbol><symbol id="30x30_guide_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M27.5 28h-25a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5H5V7.78a.5.5 0 0 1 .283-.45l12-5.78A.5.5 0 0 1 18 2v7h4V7a.5.5 0 0 1 1 0v2h4.5a.5.5 0 0 1 .5.5v18a.5.5 0 0 1-.5.5zM3 18v9h9v-9H3zm14-8V2.796l-11 5.3V17h6.5a.5.5 0 0 1 .5.5V27h4V10zm10 0h-9v17h9V10zm-6 3h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1 0-1zm0 3h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1 0-1zm0 3h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1 0-1zM8.5 13.5A.5.5 0 0 1 9 13h5a.5.5 0 0 1 0 1H9a.5.5 0 0 1-.5-.5zM14 11H9a.5.5 0 0 1 0-1h5a.5.5 0 0 1 0 1z"></path></symbol><symbol id="30x30_hamburger" height="30" viewBox="0 0 30 30" width="30"><path d="M26 16H4a1 1 0 0 1 0-2h22a1 1 0 0 1 0 2zm0-7H4a1 1 0 0 1 0-2h22a1 1 0 0 1 0 2zM4 21h22a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path></symbol><symbol id="30x30_hamburger_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26 15.5H4a.5.5 0 0 1 0-1h22a.5.5 0 0 1 0 1zm0-7H4a.5.5 0 0 1 0-1h22a.5.5 0 0 1 0 1zm-22 13h22a.5.5 0 0 1 0 1H4a.5.5 0 0 1 0-1z"></path></symbol><symbol id="30x30_heart_outline_temporary" height="30" viewBox="0 0 30 30" width="30"><path d="M20.413 5.373a5.52 5.52 0 0 1 3.933 1.63 5.568 5.568 0 0 1 0 7.864l-.773.774L15 24.216 6.427 15.64l-.773-.773a5.526 5.526 0 0 1-1.63-3.933c0-1.485.58-2.882 1.63-3.932a5.524 5.524 0 0 1 3.933-1.63 5.53 5.53 0 0 1 3.933 1.63l.773.773.707.707.707-.707.774-.773a5.522 5.522 0 0 1 3.935-1.63m0-1a6.54 6.54 0 0 0-4.64 1.923L15 7.068l-.773-.773a6.54 6.54 0 0 0-4.64-1.922c-1.68 0-3.36.64-4.64 1.922a6.56 6.56 0 0 0 0 9.28l.773.773 9.28 9.28 9.28-9.28.773-.774a6.56 6.56 0 0 0 0-9.28 6.537 6.537 0 0 0-4.64-1.92z"></path></symbol><symbol id="30x30_heart_temporary" height="30" viewBox="0 0 30 30" width="30"><path d="M25.053 6.295a6.56 6.56 0 0 0-9.28 0L15 7.068l-.773-.773a6.56 6.56 0 0 0-9.28 0 6.56 6.56 0 0 0 0 9.28l.773.773 9.28 9.28 9.28-9.28.773-.774a6.56 6.56 0 0 0 0-9.28z"></path></symbol><symbol id="30x30_history" height="30" viewBox="0 0 30 30" width="30"><path d="M16 8v6.466l5.05 3.38a1 1 0 0 1-.557 1.832 1 1 0 0 1-.556-.17l-5.493-3.677c-.027-.013-.042-.042-.067-.062a1.024 1.024 0 0 1-.247-.3.968.968 0 0 1-.11-.37c-.004-.033-.02-.06-.02-.094V8a1 1 0 0 1 2 0zm10.546 11.782a12.415 12.415 0 0 1-6.764 6.764c-1.542.64-3.162.958-4.782.958s-3.24-.32-4.783-.958a1 1 0 0 1 .766-1.848 10.446 10.446 0 0 0 8.034 0 10.43 10.43 0 0 0 5.68-5.68 10.42 10.42 0 0 0 0-8.035 10.43 10.43 0 0 0-5.68-5.68 10.42 10.42 0 0 0-8.034 0 10.425 10.425 0 0 0-5.68 5.68 10.41 10.41 0 0 0-.62 5.95l.663-1.11a1 1 0 1 1 1.718 1.024L5.237 19.91c-.02.034-.053.055-.077.086a.9.9 0 0 1-.134.15c-.05.043-.106.076-.165.11-.03.02-.06.05-.1.067-.02.01-.042.006-.07.014-.02.008-.04.026-.063.032a.973.973 0 0 1-.245.03h-.005c-.004 0-.008-.007-.013-.007a1.006 1.006 0 0 1-.4-.1c-.03-.013-.063-.02-.092-.038l-3.176-1.89a1 1 0 1 1 1.025-1.72l.99.592a12.412 12.412 0 0 1 .744-7.025 12.418 12.418 0 0 1 6.763-6.763 12.42 12.42 0 0 1 9.565 0 12.413 12.413 0 0 1 6.766 6.762 12.42 12.42 0 0 1 0 9.565z"></path></symbol><symbol id="30x30_history_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M15.5 8v6.733l5.272 3.53c.23.153.292.464.137.693a.498.498 0 0 1-.698.137l-5.494-3.677c-.014-.01-.02-.024-.034-.034a.483.483 0 0 1-.16-.236.564.564 0 0 1-.02-.1c0-.016-.008-.03-.008-.046V8a.5.5 0 0 1 1 0zm10.584 11.59a11.92 11.92 0 0 1-6.493 6.494c-1.48.613-3.03.92-4.59.92s-3.11-.307-4.59-.92a.5.5 0 1 1 .386-.924 10.933 10.933 0 0 0 8.416 0 10.922 10.922 0 0 0 5.95-5.952 10.927 10.927 0 0 0 0-8.417 10.926 10.926 0 0 0-5.95-5.95 10.924 10.924 0 0 0-8.416 0 10.926 10.926 0 0 0-5.952 5.95c-.99 2.398-1.104 5-.35 7.448l1.287-2.155a.5.5 0 1 1 .86.51l-1.83 3.064c-.01.018-.03.028-.04.044a.5.5 0 0 1-.065.07.52.52 0 0 1-.083.056c-.015.01-.03.026-.05.034-.01.004-.023.003-.035.01-.01 0-.02.01-.032.012a.487.487 0 0 1-.35-.048c-.01-.005-.02-.003-.027-.008L.95 17.936a.5.5 0 0 1 .51-.86l2.005 1.196a11.91 11.91 0 0 1 .45-7.864 11.92 11.92 0 0 1 6.494-6.494 11.912 11.912 0 0 1 9.18 0 11.918 11.918 0 0 1 6.49 6.493 11.912 11.912 0 0 1 0 9.18z"></path></symbol><symbol id="30x30_message" height="30" viewBox="0 0 30 30" width="30"><path d="M22 5H8a4 4 0 0 0-4 4v8a4 4 0 0 0 4 4h2v5l6-5h6a4 4 0 0 0 4-4V9a4 4 0 0 0-4-4z"></path></symbol><symbol id="30x30_message_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M22 5H8a4 4 0 0 0-4 4v8a4 4 0 0 0 4 4h2v5l6-5h6a4 4 0 0 0 4-4V9a4 4 0 0 0-4-4zm3 12c0 1.654-1.346 3-3 3h-6.362l-.278.232L11 23.865V20H8c-1.654 0-3-1.346-3-3V9c0-1.654 1.346-3 3-3h14c1.654 0 3 1.346 3 3v8z"></path></symbol><symbol id="30x30_monocle" height="30" viewBox="0 0 30 30" width="30"><path d="M26 23a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0-3a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm-1-4h-1.696c-.937 4.836-5.198 8.5-10.304 8.5-5.79 0-10.5-4.71-10.5-10.5S7.21 3.5 13 3.5c5.106 0 9.367 3.664 10.304 8.5H25a2 2 0 0 1 0 4zM13 5.5c-4.687 0-8.5 3.813-8.5 8.5 0 4.686 3.813 8.5 8.5 8.5 4.686 0 8.5-3.814 8.5-8.5 0-4.687-3.814-8.5-8.5-8.5zM26 24a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></symbol><symbol id="30x30_monocle_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26 23a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm0-3a1 1 0 1 1 0-2 1 1 0 0 1 0 2zm-1-4h-2.2v-.005C21.87 20.555 17.83 24 13 24 7.486 24 3 19.514 3 14S7.486 4 13 4c4.83 0 8.87 3.443 9.8 8.004V12H25a2 2 0 0 1 0 4zM13 5c-4.962 0-9 4.038-9 9 0 4.963 4.038 9 9 9 4.963 0 9-4.037 9-9 0-4.962-4.037-9-9-9zm13 19a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></symbol><symbol id="30x30_nearby_filled" height="30" viewBox="0 0 30 30" width="30"><path d="M15 3C8.373 3 3 8.373 3 15s5.373 12 12 12 12-5.373 12-12S21.627 3 15 3zm-.595 17.955l-.454-4.95L9 15.55l11.11-5.706-5.705 11.11z"></path></symbol><symbol id="30x30_nearby_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M15 27C8.373 27 3 21.627 3 15S8.373 3 15 3s12 5.373 12 12-5.373 12-12 12zm0-23C8.935 4 4 8.935 4 15s4.935 11 11 11 11-4.935 11-11S21.065 4 15 4zm-1.05 12.005L9 15.55l11.11-5.705-5.705 11.11-.454-4.95z"></path></symbol><symbol id="30x30_no_flash" height="30" viewBox="0 0 30 30" width="30"><path d="M23.104 22.853a.5.5 0 0 1-.707 0l-15-15a.5.5 0 1 1 .707-.706l4.086 4.086 5.87-6.117c.834-.87 2.217.187 1.605 1.224L15.737 13h5.248c.892 0 1.35 1.053.73 1.698L18.75 17.79l4.356 4.356a.5.5 0 0 1 0 .707zm-12.565-9.9l6.556 6.558-5.158 5.375c-.834.87-2.217-.187-1.605-1.223L14.263 17H9.015c-.892 0-1.35-1.054-.73-1.698l2.254-2.35z"></path></symbol><symbol id="30x30_order" height="30" viewBox="0 0 30 30" width="30"><g><path d="M25 15V6h-8v16h-4.557c-.693-1.19-1.97-2-3.443-2-1.474 0-2.75.81-3.443 2H2v2h3c0 2.206 1.794 4 4 4s4-1.794 4-4h5c0 2.206 1.794 4 4 4s4-1.794 4-4h2v-5l-3-4zM9 26c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2zm11-16h2v4h-2v-4zm2 16c-1.103 0-2-.897-2-2s.897-2 2-2 2 .897 2 2-.897 2-2 2z"></path><path d="M7 9V6.5a2.5 2.5 0 0 1 5 0V9H7m2.5-7C7.02 2 5 4.02 5 6.5V9H2v13h15V9h-3V6.5C14 4.02 11.98 2 9.5 2" opacity=".502"></path></g></symbol><symbol id="30x30_order_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M25 24a3 3 0 0 1-6 0h-7a3 3 0 0 1-6 0H2V9h4V6a3 3 0 0 1 3-3h1a3 3 0 0 1 3 3v3h3V6h9v9l3 4v5h-3zM9 26c1.103 0 2-.897 2-2s-.897-2-2-2-2 .897-2 2 .897 2 2 2zm3-20c0-1.103-.897-2-2-2H9c-1.103 0-2 .897-2 2v3h5V6zm4 4H3v13h3.184A2.992 2.992 0 0 1 9 21c1.304 0 2.403.838 2.816 2H16V10zm6 16c1.103 0 2-.897 2-2s-.897-2-2-2-2 .897-2 2 .897 2 2 2zm5-6.667l-3-4V7h-7v16h2.184A2.992 2.992 0 0 1 22 21c1.304 0 2.403.838 2.816 2H27v-3.667zM19 9h3v6h-3V9zm1 5h1v-4h-1v4z"></path></symbol><symbol id="30x30_profile_badged" height="30" viewBox="0 0 30 30" width="30"><path d="M15 3C8.373 3 3 8.373 3 15s5.373 12 12 12 12-5.373 12-12S21.627 3 15 3zm0 22a9.935 9.935 0 0 1-5.37-1.577 8.417 8.417 0 0 1 3.73-1.763v-1.25c-1.09-.82-2.11-2.19-2.18-3.08-.96-.61-1.43-2.11-.57-2.51-.32-.59-.51-1.3-.51-2.07 0-1.68.9-3.09 2.13-3.55.23-.5.65-.83 1.14-.83.28 0 .53.11.75.29.56-.52 1.26-.83 2.02-.83 1.3 0 2.42.9 2.96 2.2.77.65.96 1.64.96 2.72 0 .82-.23 1.54-.62 2.1.79.43.32 1.88-.62 2.48-.07.89-1.09 2.26-2.18 3.08v1.25a8.42 8.42 0 0 1 3.73 1.763A9.935 9.935 0 0 1 15 25z"></path></symbol><symbol id="30x30_profile_badged_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M15 3C8.37 3 3 8.37 3 15c0 4.11 2.06 7.73 5.21 9.9A11.92 11.92 0 0 0 15 27c2.52 0 4.86-.77 6.79-2.1C24.94 22.73 27 19.11 27 15c0-6.63-5.37-12-12-12zm6.14 21.13a8.358 8.358 0 0 0-4.5-2.47v-1.25c1.09-.82 2.11-2.19 2.18-3.08.94-.6 1.41-2.05.62-2.48.39-.56.62-1.28.62-2.1 0-1.08-.19-2.07-.96-2.72-.54-1.3-1.66-2.2-2.96-2.2-.76 0-1.46.31-2.02.83-.22-.18-.47-.29-.75-.29-.49 0-.91.33-1.14.83-1.23.46-2.13 1.87-2.13 3.55 0 .77.19 1.48.51 2.07-.86.4-.39 1.9.57 2.51.07.89 1.09 2.26 2.18 3.08v1.25a8.358 8.358 0 0 0-4.5 2.47A11.004 11.004 0 0 1 4 15C4 8.93 8.93 4 15 4s11 4.93 11 11c0 3.8-1.93 7.15-4.86 9.13z"></path></symbol><symbol id="30x30_reservation" height="24" viewBox="0 0 30 24" width="30"><path d="M22 24H8c-2.2 0-4-1.8-4-4V5c0-2.2 1.8-4 4-4a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1h8a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1c2.2 0 4 1.8 4 4v15c0 2.2-1.8 4-4 4zm2-16H6v12c0 1.103.897 2 2 2h14c1.103 0 2-.897 2-2V8zm-8 6h5v5h-5v-5z"></path></symbol><symbol id="30x30_reservation_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M22 27H8c-2.2 0-4-1.8-4-4V8c0-2.2 1.8-4 4-4a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1h8a1 1 0 0 1 1-1h1a1 1 0 0 1 1 1c2.2 0 4 1.8 4 4v15c0 2.2-1.8 4-4 4zm3-19c0-1.654-1.346-3-3-3H8C6.346 5 5 6.346 5 8v2h20V8zm0 3H5v12c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3V11zm-9 6h5v5h-5v-5z"></path></symbol><symbol id="30x30_review" height="30" viewBox="0 0 30 30" width="30"><path d="M26 8a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v14a4 4 0 0 0 4 4h14a4 4 0 0 0 4-4V8zm-6.946 12.907l-4.105-2.52L10.98 21l.767-4.494-3.25-3.18 4.493-.658L14.95 8l2.055 4.668 4.495.657-3.25 3.18.804 4.402z"></path></symbol><symbol id="30x30_review_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M22 26H8a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4h14a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4zm3-18c0-1.654-1.346-3-3-3H8C6.346 5 5 6.346 5 8v14c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3V8zm-5.946 12.907l-4.105-2.52L10.98 21l.767-4.494-3.25-3.18 4.493-.658L14.95 8l2.055 4.668 4.495.657-3.25 3.18.804 4.402z"></path></symbol><symbol id="30x30_search" height="30" viewBox="0 0 30 30" width="30"><path d="M26.925 25.51l-6.4-6.4c3.212-3.924 2.99-9.738-.67-13.4-3.9-3.898-10.244-3.898-14.144 0-3.896 3.9-3.896 10.244 0 14.143a9.97 9.97 0 0 0 7.073 2.925 9.977 9.977 0 0 0 6.33-2.253l6.4 6.4a.997.997 0 0 0 1.413 0 1 1 0 0 0 0-1.414zm-19.8-7.07c-3.12-3.12-3.12-8.195 0-11.314a7.973 7.973 0 0 1 5.658-2.34c2.048 0 4.097.78 5.656 2.34 3.12 3.12 3.12 8.194 0 11.313-3.12 3.12-8.196 3.12-11.315 0z"></path></symbol><symbol id="30x30_search_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M26.57 25.864l-6.734-6.735c3.353-3.727 3.25-9.48-.336-13.066-3.703-3.705-9.732-3.704-13.435 0-3.704 3.704-3.704 9.73 0 13.435a9.47 9.47 0 0 0 6.718 2.777c2.275 0 4.546-.82 6.346-2.442l6.733 6.735a.5.5 0 1 0 .707-.706zm-19.798-7.07c-3.314-3.315-3.314-8.708 0-12.022a8.474 8.474 0 0 1 6.01-2.486c2.177 0 4.354.83 6.01 2.486 3.315 3.314 3.315 8.707 0 12.02-3.312 3.315-8.706 3.315-12.02 0z"></path></symbol><symbol id="30x30_speech" height="30" viewBox="0 0 30 30" width="30"><path d="M22 5H8a4 4 0 0 0-4 4v8a4 4 0 0 0 4 4h2v5l6-5h6a4 4 0 0 0 4-4V9a4 4 0 0 0-4-4z"></path></symbol><symbol id="30x30_speech_outline" height="30" viewBox="0 0 30 30" width="30"><path d="M22 5H8a4 4 0 0 0-4 4v8a4 4 0 0 0 4 4h2v5l6-5h6a4 4 0 0 0 4-4V9a4 4 0 0 0-4-4zm3 12c0 1.654-1.346 3-3 3h-6.362l-.278.232L11 23.865V20H8c-1.654 0-3-1.346-3-3V9c0-1.654 1.346-3 3-3h14c1.654 0 3 1.346 3 3v8z"></path></symbol><symbol id="36x36_apple_pay" height="36" viewBox="0 0 36 36" width="36"><path d="M31.5 27h-27A1.5 1.5 0 0 1 3 25.5v-15A1.5 1.5 0 0 1 4.5 9h27a1.5 1.5 0 0 1 1.5 1.5v15a1.5 1.5 0 0 1-1.5 1.5zm.5-16.5a.5.5 0 0 0-.5-.5h-27a.5.5 0 0 0-.5.5v15a.5.5 0 0 0 .5.5h27a.5.5 0 0 0 .5-.5v-15zm-6.568 12.12c-.08 0-.342-.01-.413-.03v-.82c.06.008.22.017.31.017.47 0 .73-.2.9-.712l.09-.304-1.8-4.98h1.11l1.25 4.05h.023l1.253-4.045h1.083l-1.867 5.238c-.43 1.2-.918 1.597-1.953 1.597zm-2.3-2.685h-.024c-.28.537-.898.874-1.567.874-.98 0-1.67-.59-1.67-1.48 0-.88.67-1.38 1.908-1.46l1.325-.08v-.38c0-.556-.366-.86-1.016-.86-.537 0-.927.275-1.007.7h-.96c.03-.89.866-1.536 1.996-1.536 1.215 0 2.01.636 2.01 1.624v3.41h-.985v-.82zm-.038-1.424l-1.183.08c-.66.04-1.01.29-1.01.72 0 .42.36.69.93.69.72 0 1.27-.46 1.27-1.1v-.38zm-5.782-.09H15.84v2.34h-1.064v-6.85h2.57c1.33 0 2.255.92 2.255 2.25 0 1.34-.94 2.266-2.28 2.266zm-.247-3.61H15.84v2.72h1.22c.926 0 1.453-.5 1.453-1.36s-.527-1.358-1.448-1.358zm-5.92 6.004c-.493.01-.658-.293-1.224-.293-.56 0-.74.283-1.21.3-.49.02-.86-.484-1.18-.94-.64-.923-1.12-2.604-.46-3.737a1.81 1.81 0 0 1 1.535-.932c.484-.01.93.32 1.224.32.293 0 .813-.382 1.425-.346.235.018.92.09 1.36.74-.038.027-.814.475-.805 1.416.01 1.12.985 1.496.994 1.505-.01.03-.154.53-.51 1.05-.31.46-.63.906-1.14.916zM9.758 15.1c-.055-.423.155-.87.393-1.146.27-.32.73-.55 1.1-.57.05.44-.12.873-.38 1.194-.26.31-.682.558-1.103.522z"></path></symbol><symbol id="36x36_bookmark_outline_temporary" height="36" viewBox="0 0 36 36" width="36"><path d="M24 6c.55 0 1 .45 1 1v20.91l-5.772-4.49L18 22.467l-1.228.955L11 27.91V7c0-.55.45-1 1-1h12m0-2H12a3 3 0 0 0-3 3v25l9-7 9 7V7a3 3 0 0 0-3-3z"></path></symbol><symbol id="36x36_bookmark_temporary" height="36" viewBox="0 0 36 36" width="36"><path d="M27 32l-9-7-9 7V7a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v25z"></path></symbol><symbol id="36x36_camera" height="36" viewBox="0 0 36 36" width="36"><path d="M29 32H7c-2.685 0-5-2.225-5-4.97V13c0-2.744 2.315-5 5-5h3c.923-1.717 2.315-3.008 4.254-3.008L22 5c1.94 0 3.077 1.283 4 3h3c2.685 0 5 2.256 5 5v14c0 2.744-2.315 5-5 5zm3-19c0-1.57-1.332-3.03-2.87-3.03h-4.236C24.606 8.35 23.562 7 22 7h-8c-1.56 0-2.71 1.38-3 3H7c-1.537 0-3 1.43-3 3v14c0 1.57 1.463 3 3 3h22c1.537 0 3-1.43 3-3V13zM18 27.03c-3.842 0-6.957-3.182-6.957-7.108 0-3.927 3.115-7.11 6.957-7.11 3.842 0 6.957 3.183 6.957 7.11 0 3.926-3.115 7.11-6.957 7.11zm0-12.085c-2.685 0-4.87 2.233-4.87 4.977s2.185 4.976 4.87 4.976 4.87-2.232 4.87-4.976c0-2.744-2.185-4.977-4.87-4.977z"></path></symbol><symbol id="36x36_profile_badged" height="36" viewBox="0 0 36 36" width="36"><path d="M18 2.01C9.17 2.01 2.01 9.17 2.01 18S9.17 33.99 18 33.99 33.99 26.83 33.99 18 26.83 2.01 18 2.01zm8.108 27.144c-1.8-1.573-3.86-2.372-6.075-2.677V24.72c1.364-1.018 2.63-2.715 2.718-3.82 1.164-.75 1.755-2.547.77-3.09l-.026.038c.496-.71.8-1.612.8-2.646 0-1.338-.235-2.575-1.197-3.384-.67-1.617-2.062-2.732-3.68-2.732-.95 0-1.82.386-2.514 1.03a1.425 1.425 0 0 0-.93-.36c-.608 0-1.135.417-1.418 1.03-1.528.575-2.64 2.334-2.64 4.416 0 .954.233 1.84.632 2.576-1.075.497-.484 2.356.703 3.123.086 1.106 1.353 2.803 2.717 3.82v1.758c-2.215.305-4.274 1.105-6.075 2.677-3.448-2.513-5.7-6.57-5.7-11.154C4.19 10.386 10.384 4.19 18 4.19S31.81 10.386 31.81 18c0 4.583-2.254 8.64-5.702 11.154z"></path></symbol><symbol id="36x36_review" height="36" viewBox="0 0 36 36" width="36"><path d="M27.333 32H8.667A4.672 4.672 0 0 1 4 27.333V8.667A4.672 4.672 0 0 1 8.668 4h18.666A4.672 4.672 0 0 1 32 8.667v18.666A4.672 4.672 0 0 1 27.332 32zM30 8.667A2.667 2.667 0 0 0 27.333 6H8.667A2.667 2.667 0 0 0 6 8.667v18.666A2.667 2.667 0 0 0 8.667 30h18.666A2.667 2.667 0 0 0 30 27.333V8.667zm-7.01 16.55l-5.052-3.1-4.88 3.216.942-5.53-4-3.916 5.53-.808 2.408-5.747 2.53 5.745 5.532.807-4 3.915.99 5.416z"></path></symbol><symbol id="48x48_add_photo_circle_container" height="48" viewBox="0 0 48 48" width="48"><path d="M24 48C10.745 48 0 37.255 0 24S10.745 0 24 0s24 10.745 24 24-10.745 24-24 24zm0-46C11.87 2 2 11.87 2 24s9.87 22 22 22 22-9.87 22-22S36.13 2 24 2zm9 32H15a3 3 0 0 1-3-3V20a3 3 0 0 1 3-3h3a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3h3a3 3 0 0 1 3 3v11a3 3 0 0 1-3 3zm-9-15a6 6 0 1 0 0 12 6 6 0 0 0 0-12zm3 7h-2v1.565c0 .516-.42.935-.935.935h-.13a.935.935 0 0 1-.935-.935V26h-2a1 1 0 0 1 0-2h2v-1.565c0-.516.42-.935.935-.935h.13c.516 0 .935.42.935.935V24h2a1 1 0 0 1 0 2z"></path></symbol><symbol id="48x48_beauty" height="48" viewBox="0 0 48 48" width="48"><path d="M11.743 23.317c0-.78.218-1.555.692-2.226.582-.88 1.528-1.48 2.622-1.692 1.056-.213 2.15 0 3.096.565.91.6 1.53 1.52 1.748 2.54a3.96 3.96 0 0 1-.58 3c-1.275 1.84-3.863 2.37-5.755 1.134-1.166-.78-1.82-2.05-1.82-3.317zm6.955 11.328c0-.88.257-1.764.8-2.54 1.46-2.122 4.407-2.683 6.595-1.272 2.188 1.41 2.803 4.272 1.35 6.39-.694 1.023-1.786 1.73-3.027 1.977a4.888 4.888 0 0 1-3.57-.67c-1.09-.71-1.82-1.73-2.04-2.965a3.76 3.76 0 0 1-.108-.92zm14.97-19.2L22.74 26.987l-.62.03c.877-1.338 1.205-2.893 1.06-4.442l10.487-7.132zM3 25.01l2.478 2.007c.035-.03 1.748-1.937 3.386-1.62.474 1.52 1.455 2.93 2.915 3.848 1.526.99 3.31 1.34 5.023 1.13-1.203 1.73-1.602 3.776-1.203 5.827.438 2.044 1.64 3.775 3.424 4.94 1.783 1.127 3.933 1.55 6.012 1.127a7.81 7.81 0 0 0 5.1-3.32c2.438-3.563 1.454-8.4-2.22-10.768a12.502 12.502 0 0 0-1.314-.636L44.872 6.4c.376-.433-.156-1.054-.643-.75L22.083 19.467a7.542 7.542 0 0 0-2.147-2.12c-3.39-2.186-7.977-1.27-10.235 2.013a7.012 7.012 0 0 0-1.093 2.823C6.17 22.148 3.984 23.808 3 25.01z"></path></symbol><symbol id="48x48_camera" height="48" viewBox="0 0 48 48" width="48"><path d="M38 40H10a6 6 0 0 1-6-6V18a6 6 0 0 1 6-6h4.367C15.194 9.675 17.39 8 20 8h8c2.61 0 4.806 1.675 5.633 4H38a6 6 0 0 1 6 6v16a6 6 0 0 1-6 6zM24.01 17a9 9 0 0 0-9 9 9 9 0 1 0 9-9zm0 14a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"></path></symbol><symbol id="48x48_check_in_circle_container" height="48" viewBox="0 0 48 48" width="48"><path d="M24 48C10.745 48 0 37.255 0 24S10.745 0 24 0s24 10.745 24 24-10.745 24-24 24zm0-46C11.87 2 2 11.87 2 24s9.87 22 22 22 22-9.87 22-22S36.13 2 24 2zm9.152 24.453L34.394 30l-3.696.7L30 34.394l-3.55-1.242L24 36l-2.448-2.85L18 34.394l-.7-3.692-3.693-.7 1.242-3.547L12 24l2.85-2.454L13.606 18l3.692-.7.7-3.693 3.55 1.24L23.998 12l2.453 2.848 3.55-1.24.7 3.692 3.696.7-1.242 3.546L36 24l-2.848 2.453zm-5.334-6.095l-5.09 5.09-2.546-2.545-1.697 1.697 2.545 2.545 1.697 1.697 6.788-6.787-1.697-1.697z"></path></symbol><symbol id="48x48_chevron_left" height="48" viewBox="0 0 48 48" width="48"><path d="M29.414 5.992c.566 0 1.137.192 1.614.588 1.115.925 1.296 2.613.404 3.77L20.902 24l10.53 13.65c.892 1.156.71 2.844-.404 3.77-1.116.924-2.743.737-3.635-.42L15.57 25.675a2.76 2.76 0 0 1 0-3.35L27.394 6.998a2.548 2.548 0 0 1 2.02-1.008z"></path></symbol><symbol id="48x48_chevron_right" height="48" viewBox="0 0 48 48" width="48"><path d="M18.586 42.008a2.518 2.518 0 0 1-1.614-.588c-1.115-.925-1.296-2.613-.404-3.77L27.098 24l-10.53-13.65c-.892-1.156-.71-2.844.404-3.77 1.116-.924 2.743-.737 3.635.42L32.43 22.325a2.76 2.76 0 0 1 0 3.35L20.606 41.002a2.548 2.548 0 0 1-2.02 1.008z"></path></symbol><symbol id="48x48_food" height="48" viewBox="0 0 48 48" width="48"><path d="M34.76 43h-.007a3.24 3.24 0 0 1-3.206-3.712l1.925-10.275-3.972-2.548c0-8.972 1.262-14.02 4.74-20.417.988-1.82 3.76-1.12 3.76.954V39.76A3.24 3.24 0 0 1 34.76 43zM18.498 26.184l1.245 13.326a3.252 3.252 0 1 1-6.486 0l1.245-13.326A6.5 6.5 0 0 1 10 20V7.5a1.5 1.5 0 0 1 3 0V17a1 1 0 0 0 2 0V7.5a1.5 1.5 0 0 1 3 0V17a1 1 0 0 0 2 0V7.5a1.5 1.5 0 0 1 3 0V20a6.5 6.5 0 0 1-4.502 6.184z"></path></symbol><symbol id="48x48_menu" height="48" viewBox="0 0 48 48" width="48"><path d="M7 5v38h34V5H7zm19 28H15v-3h11v3zm0-8H15v-3h11v3zm0-8H15v-3h11v3zm7 16h-3v-3h3v3zm0-8h-3v-3h3v3zm0-8h-3v-3h3v3z"></path></symbol><symbol id="48x48_nightlife" height="48" viewBox="0 0 48 48" width="48"><path d="M40.626 8.78c.732-.59.318-1.78-.62-1.78H7.994c-.938 0-1.352 1.19-.62 1.78l14.87 16.405.537 11.342-7.222 2.554c-.99.43-.687 1.92.39 1.92h16.105c1.078 0 1.382-1.49.39-1.92L25.22 36.53l.536-11.342L40.626 8.78zM27.966 10c1.644 0 2.976 1.343 2.976 3s-1.332 3-2.975 3c-1.644 0-2.975-1.343-2.975-3s1.33-3 2.975-3z"></path></symbol><symbol id="48x48_scan_menu" height="32" viewBox="0 0 40 32" width="40"><path d="M27 32V15h13v17H27zm8-13h-5v1h5v-1zm0 4h-5v1h5v-1zm0 4h-5v1h5v-1zm2-8h-1v1h1v-1zm0 4h-1v1h1v-1zm0 4h-1v1h1v-1zm-11 1H5a5 5 0 0 1-5-5V9a5 5 0 0 1 5-5h3.1A5 5 0 0 1 13 0h7a5 5 0 0 1 4.9 4H28a5 5 0 0 1 5 5v5h-7v14zM16.5 8a8 8 0 1 0 0 16 8 8 0 0 0 0-16zm0 12.5a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"></path></symbol><symbol id="48x48_shopping" height="48" viewBox="0 0 48 48" width="48"><path d="M36 37V27l2.823-11.848a1 1 0 0 0-.99-1.152H30v-3a6 6 0 0 0-12 0v3h-7.835a1 1 0 0 0-.988 1.152L12 27v10l-2.276 2.553A1 1 0 0 0 10.618 41h26.764a1 1 0 0 0 .894-1.447L36 37zM21 11c0-1.654 1.346-3 3-3s3 1.346 3 3v3h-6v-3z"></path></symbol><symbol id="48x48_tools" height="48" viewBox="0 0 48 48" width="48"><path d="M40.737 16.48a7.45 7.45 0 0 1-1.962 3.447 7.568 7.568 0 0 1-5.366 2.222c-.657 0-1.304-.118-1.94-.287L13.475 39.86a3.794 3.794 0 1 1-5.365-5.366L26.107 16.5c-.168-.637-.284-1.285-.284-1.94a7.57 7.57 0 0 1 2.223-5.365 7.455 7.455 0 0 1 3.448-1.962 7.694 7.694 0 0 1 3.858.024l-4.62 4.62 1.34 4.025 4.026 1.342 4.622-4.622a7.705 7.705 0 0 1 .023 3.857zm-28.12 18.873a1.896 1.896 0 1 0-2.682 2.683 1.896 1.896 0 1 0 2.682-2.683zm1.883-18.67v-.286h-2.898L7.435 9.975l2.54-2.397 6.422 4.024v2.683l4.63 4.22-2.344 2.61-4.183-4.433zm18.83 19.33l1.343-1.34-6.707-6.708 2.683-2.682 8.675 8.68a3.794 3.794 0 0 1-5.365 5.365l-8.68-8.68 1.343-1.34 6.707 6.706z"></path></symbol><symbol id="56x56_compass" height="56" viewBox="0 0 56 56" width="56"><path d="M28 53C14.215 53 3 41.785 3 28S14.215 3 28 3s25 11.215 25 25-11.215 25-25 25zm0-47C15.87 6 6 15.87 6 28s9.87 22 22 22 22-9.87 22-22S40.13 6 28 6zm-4.534 30.84l-8.838 4.595 4.596-8.84 4.596-8.838 17.677-9.192-9.192 17.678-8.84 4.596zm5.37-12.31l2.696 2.697 2.92-5.618-5.616 2.92z"></path></symbol><symbol id="56x56_video_play" height="56" viewBox="0 0 56 56" width="56"><path d="M28 50C15.85 50 6 40.15 6 28S15.85 6 28 6s22 9.85 22 22-9.85 22-22 22zm0-41C17.507 9 9 17.507 9 28s8.507 19 19 19 19-8.507 19-19S38.493 9 28 9zm-6 8l17 10.945L22 39V17z"></path></symbol><symbol id="60x60_beauty" height="60" viewBox="0 0 60 60" width="60"><path d="M14.7 29.147c0-.972.273-1.94.864-2.778.727-1.11 1.908-1.85 3.274-2.12 1.318-.27 2.683 0 3.864.7a5.084 5.084 0 0 1 2.182 3.17 4.95 4.95 0 0 1-.725 3.745c-1.6 2.293-4.83 2.955-7.19 1.413-1.46-.97-2.27-2.557-2.27-4.14zm8.683 14.14c0-1.1.32-2.202.996-3.172 1.82-2.647 5.5-3.347 8.23-1.586 2.73 1.76 3.5 5.33 1.68 7.97-.868 1.273-2.23 2.16-3.78 2.47a6.1 6.1 0 0 1-4.456-.84c-1.363-.887-2.274-2.16-2.545-3.7a4.642 4.642 0 0 1-.137-1.15zM42.066 19.32L28.428 33.73l-.773.036c1.093-1.67 1.502-3.61 1.32-5.544l13.09-8.902zM3.788 31.26l3.093 2.506c.05-.037 2.19-2.418 4.23-2.022.59 1.898 1.82 3.657 3.64 4.803 1.91 1.235 4.13 1.674 6.278 1.41-1.5 2.158-2 4.714-1.5 7.273.544 2.552 2.043 4.712 4.27 6.167 2.227 1.406 4.91 1.935 7.505 1.406a9.747 9.747 0 0 0 6.365-4.14c3.042-4.447 1.815-10.485-2.773-13.44a15.53 15.53 0 0 0-1.64-.794L56.06 8.03c.468-.546-.195-1.32-.803-.94l-27.64 17.25a9.423 9.423 0 0 0-2.68-2.647c-4.23-2.73-9.957-1.586-12.775 2.51a8.754 8.754 0 0 0-1.365 3.527c-3.05-.042-5.775 2.03-7.005 3.53z"></path></symbol><symbol id="60x60_food" height="60" viewBox="0 0 60 60" width="60"><path d="M41.76 55h-.007a3.24 3.24 0 0 1-3.206-3.712L40.73 34.64 36 31.494c0-10.385 2.723-19.82 5.173-25.307.88-1.972 3.827-1.34 3.827.82V51.76A3.24 3.24 0 0 1 41.76 55zM24.273 30.78l1.47 20.73a3.252 3.252 0 1 1-6.486 0l1.47-20.725C17.36 29.96 15 26.763 15 23.215V6.5a1.5 1.5 0 0 1 3 0v14a1.5 1.5 0 0 0 3 0v-14a1.5 1.5 0 0 1 3 0v14a1.5 1.5 0 0 0 3 0v-14a1.5 1.5 0 0 1 3 0v17c0 3.53-2.442 6.482-5.727 7.28z"></path></symbol><symbol id="60x60_nightlife" height="60" viewBox="0 0 60 60" width="60"><path d="M51.2 10.723C51.85 10.1 51.41 9 50.507 9H9.492c-.9 0-1.343 1.1-.69 1.723l19.293 18.455.394 17.326-7.646 2.547c-1.076.36-.818 1.95.316 1.95h17.677c1.134 0 1.392-1.59.316-1.95l-7.643-2.544.395-17.326L51.2 10.722zM35 14a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"></path></symbol><symbol id="60x60_review_circle_container" height="60" viewBox="0 0 60 60" width="60"><path d="M30 60C13.432 60 0 46.568 0 30 0 13.432 13.432 0 30 0c16.568 0 30 13.432 30 30 0 16.568-13.432 30-30 30zm0-58C14.56 2 2 14.56 2 30s12.56 28 28 28 28-12.56 28-28S45.44 2 30 2zm10.11 41H19.89A2.888 2.888 0 0 1 17 40.11v-19.5A3.61 3.61 0 0 1 20.61 17h18.78A3.61 3.61 0 0 1 43 20.61v19.5A2.888 2.888 0 0 1 40.11 43zm-7.437-16.164l-2.74-6.225-2.607 6.227-5.993.875 4.334 4.242-1.023 5.992 5.288-3.483 5.474 3.36-1.073-5.868 4.334-4.24-5.994-.876z"></path></symbol><symbol id="60x60_shopping" height="60" viewBox="0 0 60 60" width="60"><path d="M45.625 17H37v-4.5c0-3.86-3.14-7-7-7s-7 3.14-7 7V17h-8.625a2 2 0 0 0-1.98 2.272L16 44.5l-2.124 3.452c-.82 1.332.14 3.048 1.703 3.048h28.84c1.564 0 2.523-1.716 1.703-3.048L44 44.5l3.606-25.228A2 2 0 0 0 45.626 17zM26 12.5c0-2.206 1.794-4 4-4s4 1.794 4 4V17h-8v-4.5z"></path></symbol><symbol id="60x60_tools" height="60" viewBox="0 0 60 60" width="60"><path d="M49.726 21.176a8.763 8.763 0 0 1-2.312 4.057 8.913 8.913 0 0 1-6.32 2.616c-.77 0-1.533-.138-2.284-.336l-21.196 21.18a4.47 4.47 0 0 1-6.32 0 4.464 4.464 0 0 1 0-6.316L32.49 21.2c-.198-.75-.334-1.512-.334-2.282 0-2.286.872-4.572 2.617-6.315a8.776 8.776 0 0 1 4.06-2.31 9.083 9.083 0 0 1 4.545.028l-5.444 5.44 1.58 4.738 4.74 1.58 5.444-5.44a9.068 9.068 0 0 1 .028 4.54zM16.603 43.39a2.233 2.233 0 1 0 0 3.158 2.233 2.233 0 0 0 0-3.158zm2.217-21.976v-.335h-3.414l-4.908-7.56 2.992-2.82 7.565 4.734v3.158l5.454 4.967-2.763 3.072-4.928-5.22zm22.182 22.754l1.58-1.58-7.9-7.893 3.16-3.157 10.223 10.215a4.46 4.46 0 0 1 0 6.315 4.47 4.47 0 0 1-6.32 0L31.52 37.853l1.582-1.58 7.9 7.895z"></path></symbol><symbol id="78x78_video_play" height="78" viewBox="0 0 78 78" width="78"><path d="M39 73C20.222 73 5 57.778 5 39S20.222 5 39 5s34 15.222 34 34-15.222 34-34 34zm0-61.867c-15.366 0-27.867 12.5-27.867 27.867 0 15.366 12.5 27.867 27.867 27.867 15.366 0 27.867-12.5 27.867-27.867 0-15.366-12.5-27.867-27.867-27.867zm-8.782 44.74a.79.79 0 0 1-1.218-.66V22.787a.79.79 0 0 1 1.218-.66l25.42 16.214a.78.78 0 0 1 0 1.32l-25.42 16.215z"></path></symbol><symbol id="96x96_video_play" height="96" viewBox="0 0 96 96" width="96"><path d="M48 90C24.804 90 6 71.196 6 48S24.804 6 48 6s42 18.804 42 42-18.804 42-42 42zm0-76c-18.748 0-34 15.252-34 34 0 18.748 15.252 34 34 34 18.748 0 34-15.252 34-34 0-18.748-15.252-34-34-34zM36.54 69.84a1 1 0 0 1-1.54-.842V27.662a1 1 0 0 1 1.54-.842l32.152 20.67a1 1 0 0 1 0 1.68l-32.15 20.67z"></path></symbol></svg>

        <script>(function (d, w) {
    var supportsSVG = (
        !!d.createElementNS &&
        !!d.createElementNS(
            'http://www.w3.org/2000/svg',
            'svg'
        ).createSVGRect
    );
    var cdnPath = 'https://s3-media1.fl.yelpcdn.com/assets/srv0/svg_icons/449292e8270f/assets/svg_sprite.js';
    var head = d.getElementsByTagName('head')[0];
    function fallback() {
        var link = d.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://s3-media1.fl.yelpcdn.com/assets/srv0/svg_icons/0171802640e8/assets/sprite.css';
        head.appendChild(link);
    }
    if (!supportsSVG) {
        fallback();
        return;
    }
    if (!w.yelp) {
        w.yelp = {};
    }
    w.yelp.__injectSvgSpritesheet = function (svg) {
        document.body.insertAdjacentHTML('afterbegin', svg);
        delete window.yelp.__injectSvgSpritesheet;
    }
    function onError() {
        d.documentElement.className = [
            d.documentElement.className,
            'icon-svg-unavailable'
        ].join(' ');
        fallback();
        return true;
    }
    var script = d.createElement('script');
    script.async = true;
    script.onerror = onError;
    script.src = cdnPath + '?callback=window.yelp.__injectSvgSpritesheet';
    head.appendChild(script);
}(document, window));</script>
<noscript>
    &lt;link rel="stylesheet" href="https://s3-media1.fl.yelpcdn.com/assets/srv0/svg_icons/0171802640e8/assets/sprite.css"&gt;
</noscript>


            <div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div><iframe name="fb_xdm_frame_https" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_https" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" src="./Best Fried chicken in Atlanta, GA - Yelp_files/0sTQzbapM8j.html" style="border: none;"></iframe></div></div><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div></div></div></div>

        <div id="wrap" class="lang-en" data-component-bound="true">
                <div class="page-header">


                        

                    



                                
                            <ul class="offscreen">
                <li>
                    <a href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1#header_find_form" rel="nofollow">
                        Skip to Search Form
                    </a><div style="display: none;"><a href="https://www.yelp.com/qqqqbrx.html" id="yqxtayqwcaqsbfwdxeeayq" rel="file">btzdxyqwzuvryrq</a></div>
                </li>
                <li>
                    <a href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1#header-nav" rel="nofollow">
                        Skip to Navigation
                    </a>
                </li>
                <li>
                    <a href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1#page-content" rel="nofollow">
                        Skip to Page Content
                    </a>
                </li>
        </ul>






        <div class="main-header main-content-wrap js-main-header webview-hidden">
            <div class="main-header_wrapper">
                <div class="content-container">

                    <div class="arrange arrange--18 arrange--middle main-header_arrange">

                            <div class="arrange_unit main-header--full_arrange_unit">
                                
    <div class="main-header_logo js-analytics-click" id="logo" data-analytics-label="logo">
        <a href="https://www.yelp.com/">Yelp</a>
    </div>

                            </div>



                        <div class="arrange_unit arrange_unit--fill align-middle main-header--full_arrange_unit main-header_search-container">
                    <div class="main-header_search responsive-hidden-medium-only">
                <form method="get" action="https://www.yelp.com/search" id="header_find_form" class="main-search yform u-space-b0" role="search" data-component-bound="true">
        <div class="arrange arrange--stack">
            <div class="arrange_unit arrange_unit--fill">
                <div class="arrange arrange--equal arrange--stack">
                    <div class="arrange_unit main-search_search-field-arrange">
                            <div class="main-search_suggestions-field search-field-container find-decorator">
        <label class="main-search_pseudo-input main-search_pseudo-input--find pseudo-input">
            <span class="pseudo-input_text">Find</span>
            <span class="pseudo-input_field-holder" data-component-bound="true" style="position: relative; display: block;">
                <input disabled="" autocomplete="off" spellcheck="false" tabindex="-1" style="position: absolute; color: rgb(200, 200, 200); -webkit-text-fill-color: rgb(200, 200, 200); width: 100%; box-sizing: border-box; top: 0px; right: 0px; bottom: 0px; left: 0px; display: inline-block; font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; font-style: normal; line-height: 20px; font-weight: 400; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0); font-kerning: auto; vertical-align: baseline; padding: 0px; border-width: 0px;"><input maxlength="64" id="find_desc" autocomplete="off" value="fried chicken" placeholder="pizza, food delivery, cheap eats" class="main-search_field pseudo-input_field" aria-autocomplete="list" tabindex="1" data-component-bound="true" style="display: inline-block; background: transparent; position: relative; width: 100%; box-sizing: border-box;"><input type="hidden" maxlength="64" data-component-bound="true" name="find_desc" value="fried chicken">
            </span>
        </label>
        <div class="main-search_suggestions suggestions-list-container search-suggestions-list-container hidden" data-component-bound="true">
            <ul class="suggestions-list" role="listbox" aria-label="Search results"></ul>
        </div>
    </div>

                    </div>
                    <div class="arrange_unit main-search_near-field-arrange  main-search_search-field-arrange arrange_unit--stack-12">
                            <div class="main-search_suggestions-field search-field-container near-decorator">
        <label class="main-search_pseudo-input main-search_pseudo-input--near pseudo-input">
            <span class="pseudo-input_text">Near</span>
            <span class="main-search_field-holder pseudo-input_field-holder">
                <input maxlength="80" id="dropperText_Mast" autocomplete="off" value="Atlanta, GA" placeholder="address, neighborhood, city, state or zip" data-query="Atlanta, GA" class="main-search_field pseudo-input_field" aria-autocomplete="list" tabindex="2" data-component-bound="true"><input type="hidden" maxlength="80" data-component-bound="true" name="find_loc" value="Atlanta, GA">
                <input type="hidden" name="ns" value="1">
            </span>
        </label>
        <div class="main-search_suggestions suggestions-list-container location-suggestions-list-container hidden" data-component-bound="true">
            <ul class="suggestions-list" role="listbox" aria-label="Search results"></ul>
        </div>
    </div>

                    </div>
                </div>
            </div>
            <div class="arrange_unit main-search_actions arrange_unit--stack-12">
                <div class="arrange arrange--wrap arrange--6">
                    <div class="arrange_unit hidden-non-responsive-inline-block responsive-visible-small-inline-block main-search_action">

    <a class="ybtn ybtn--primary main-header_button js-search-close main-search_close">
                            Cancel
    </a>
                    </div>
                    <div class="arrange_unit main-search_action arrange_unit--stack-12">

    <button class="ybtn ybtn--primary main-search_submit main-header_button" id="header-search-submit" tabindex="3" title="Search" type="submit" value="submit">
                            <span class="main-search_action-icon-wrap js-search-icon-wrap">
                                <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-search icon--size-24 icon--inverse icon--fallback-inverted">
    <svg class="icon_svg">
        <use xlink:href="#24x24_search"></use>
    </svg>
</span>
                                <span class="u-offscreen">Search</span>
                            </span>
                                <div class="circle-spinner js-circle-spinner hidden">
        <div class="circle-spinner_segment container1">
            <div class="circle1"></div>
            <div class="circle2"></div>
            <div class="circle3"></div>
            <div class="circle4"></div>
        </div>
        <div class="circle-spinner_segment container2">
            <div class="circle1"></div>
            <div class="circle2"></div>
            <div class="circle3"></div>
            <div class="circle4"></div>
        </div>
        <div class="circle-spinner_segment container3">
            <div class="circle1"></div>
            <div class="circle2"></div>
            <div class="circle3"></div>
            <div class="circle4"></div>
        </div>
    </div>

    </button>
                    </div>
                </div>
            </div>
        </div>
    </form>

        </div>

                        </div>



                            <div class="arrange_unit main-header--full_arrange_unit">
                                <div class="arrange arrange--6">
                                    <div class="arrange_unit u-nowrap">
                                        <div class="main-header_account webview-hidden">
                                                        <ul class="header-nav">
            <li class="header-nav_item responsive-hidden-small js-analytics-click" data-analytics-label="signup">

    <a class="ybtn ybtn--primary main-header_button header-nav_button--sign-up js-sign-up-button" href="https://www.yelp.com/signup" id="header-sign-up">
                    Sign Up
    </a>
            </li>
        <li class="header-nav_item">
                    <a class="header-nav_link header-nav_link--log-in js-log-in-button" href="https://www.yelp.com/login?return_url=%2Fsearch%3Ffind_desc%3Dfried%2Bchicken%26find_loc%3DAtlanta%252C%2BGA%26ns%3D1">
            Log In
        </a>

        </li>
    </ul>
        
    <div id="topbar-account-item" class="user-account clearfix drop-menu-origin hidden-non-responsive-block responsive-visible-small-block" data-component-bound="true">

    <a class="ybtn ybtn--primary drop-menu-link user-account_button" href="javascript:;" id="topbar-account-link" data-component-bound="true">
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--inverse icon--fallback-inverted u-triangle-direction-down user-account_button-arrow responsive-visible-large-inline-block">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
            <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-hamburger icon--size-24 icon--inverse icon--fallback-inverted drop-menu-link_open">
    <svg class="icon_svg">
        <use xlink:href="#24x24_hamburger"></use>
    </svg>
</span>
            <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-close icon--size-24 icon--inverse icon--fallback-inverted drop-menu-link_close">
    <svg class="icon_svg">
        <use xlink:href="#24x24_close"></use>
    </svg>
</span>
    </a>
        <div id="topbar-account-wrap" class="drop-menu drop-menu-has-arrow" data-component-bound="true">
            <div class="drop-menu-arrow responsive-hidden-small"></div>

                <div class="arrange arrange--6 arrange--equal drop-menu_auth-buttons">
                    <div class="arrange_unit">

    <a class="ybtn ybtn-full" href="https://www.yelp.com/login?return_url=%2Fsearch%3Ffind_desc%3Dfried%2Bchicken%26find_loc%3DAtlanta%252C%2BGA%26ns%3D1">
                            Login
    </a>
                    </div>
                    <div class="arrange_unit">

    <a class="ybtn ybtn--primary ybtn-full" href="https://www.yelp.com/signup">
                            Sign Up
    </a>
                    </div>
                </div>

                <ul class="drop-menu-group--nav drop-menu-group">
                            <li class="drop-down-menu-link">
        <a class="js-analytics-click arrange arrange--middle arrange--6" href="https://www.yelp.com/user_details" data-analytics-label="">
            <strong class="arrange_unit">
                    <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-profile icon--size-24 u-space-r1">
    <svg class="icon_svg">
        <use xlink:href="#24x24_profile"></use>
    </svg>
</span>About Me
            </strong>
            <span class="arrange_unit arrange_unit--fill u-text-right">
                <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-chevron-right icon--size-24 hidden-non-responsive-inline-block responsive-visible-medium-inline-block">
    <svg class="icon_svg">
        <use xlink:href="#24x24_chevron_right"></use>
    </svg>
</span>
            </span>
        </a>
    </li>

                            
                            
                            <li class="drop-down-menu-link hidden-non-responsive-block responsive-visible-medium-block">
        <a class="js-analytics-click arrange arrange--middle arrange--6" href="https://www.yelp.com/talk" data-analytics-label="">
            <strong class="arrange_unit">
                    <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-talk icon--size-24 u-space-r1">
    <svg class="icon_svg">
        <use xlink:href="#24x24_talk"></use>
    </svg>
</span>Talk
            </strong>
            <span class="arrange_unit arrange_unit--fill u-text-right">
                <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-chevron-right icon--size-24 hidden-non-responsive-inline-block responsive-visible-medium-inline-block">
    <svg class="icon_svg">
        <use xlink:href="#24x24_chevron_right"></use>
    </svg>
</span>
            </span>
        </a>
    </li>

                </ul>

        </div>
    </div>



                                        </div>
                                    </div>
                                </div>
                            </div>

                    </div>

                </div>
            </div>
        </div>


            <div class="js-curloc-error-modal curloc-error-modal hidden">
    <div class="modal_head">
            <h2>Oops, we can't find your location</h2>
    </div>
    <div class="modal_body">
        <div class="curloc-permission-denied hidden">
            <p>
                First, try refreshing the page and clicking Current Location again. Make sure you click <b>Allow</b> or <b>Grant Permissions</b> if your browser asks for your location. If your browser doesn't ask you, try these steps:
            </p>
            <div class="chrome hidden">
                <ol class="modal_section u-bg-color">
                    <li>At the top of your Chrome window, near the web address, click <b>the green lock labeled Secure</b>.</li>
                    <li>In the window that pops up, make sure <b>Location</b> is set to <b>Ask</b> or <b>Allow</b>.</li>
                    <li>You're good to go! Reload this Yelp page and try your search again.</li>
                </ol>
                <p>
                    If you're still having trouble, check out <a href="https://support.google.com/chrome/answer/142065?co=GENIE.Platform%3DDesktop&amp;hl=en&amp;oco=0" target="_blank">Google's support page</a>.
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="opera hidden">
                <ol class="modal_section u-bg-color">
                    <li>At the top of your Opera window, near the web address, you should see a <b>gray location pin</b>. Click it.</li>
                    <li>In the window that pops up, click <b>Clear This Setting</b></li>
                    <li>You're good to go! Reload this Yelp page and try your search again.</li>
                </ol>
                <p>
                    If you're still having trouble, check out <a target="_blank">Opera's support page</a>.
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="safari hidden">
                <ol class="modal_section u-bg-color">
                    <li>Click <b>Safari</b> in the Menu Bar at the top of the screen, then <b>Preferences</b>.</li>
                    <li>Click the <b>Privacy</b> tab.</li>
                    <li>Under <b>Website use of location services</b>, click <b>Prompt for each website once each day</b> or <b>Prompt for each website one time only</b>.</li>
                    <li>MacOS may now prompt you to enable Location Services. If it does, follow its instructions to enable Location Services for Safari.</li>
                    <li>Close the Privacy menu and refresh the page. Try using Current Location search again. If it works, great! If not, read on for more instructions.</li>
                    <li>Back in the <b>Privacy</b> dialog, Click <b>Manage Website Data...</b> and type <b>yelp.com</b> into the search bar.</li>
                    <li>Click the <b>yelp.com</b> entry and click Remove.</li>
                    <li>You're good to go! Close the Settings tab, reload this Yelp page, and try your search again.</li>
                </ol>
                <p>
                    If you're still having trouble, check out <a href="https://support.apple.com/en-us/HT204690" target="_blank">Safari's support page</a>.
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="firefox hidden">
                <ol class="modal_section u-bg-color">
                    <li>At the top of your Firefox window, to the left of the web address, you should see a <b>green lock</b>. Click it.</li>
                    <li>In the window that pops up, you should see <b>Blocked</b> or <b>Blocked Temporarily</b> next to <b>Access Your Location</b>. Click the <b>x</b> next to this line.</li>
                    <li>You're good to go! Refresh this Yelp page and try your search again.</li>
                </ol>
                <p>
                    If you're still having trouble, check out <a href="https://www.mozilla.org/en-US/firefox/geolocation/" target="_blank">Firefox's support page</a>.
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="ie hidden">
                <ol class="modal_section u-bg-color">
                    <li>Click the <b>gear</b> in the upper-right hand corner of the window, then <b>Internet options</b>.</li>
                    <li>Click the <b>Privacy</b> tab in the new window that just appeared.</li>
                    <li>Uncheck the box labeled <b>Never allow websites to request your physical location</b> if it's already checked.</li>
                    <li>Click the button labeled <b>Clear Sites</b>.</li>
                    <li>You're good to go! Click <b>OK</b>, then refresh this Yelp page and try your search again.</li>
                </ol>
                <p>
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="edge hidden">
                <ol class="modal_section u-bg-color">
                    <li>At the top-right hand corner of the window, click the <b>button with three dots on it</b>, then <b>Settings</b>.</li>
                    <li>Click <b>Choose what to clear</b> underneath <b>Clear browsing data</b>.</li>
                    <li>Click <b>Show more</b>, then make sure only the box labeled <b>Location permissions</b> is checked.</li>
                    <li>Click <b>Clear</b>.</li>
                    <li>You're good to go! Refresh this Yelp page and try your search again.</li>
                </ol>
                <p>
                    You can also search near a city, place, or address instead.
                </p>
            </div>
            <div class="default hidden">
                <p>
                    Oops! We don't recognize the web browser you're currently using. Try checking the browser's help menu, or searching the Web for instructions to turn on HTML5 Geolocation for your browser.
                    You can also search near a city, place, or address instead.
                </p>
            </div>
        </div>
        <div class="curloc-unavailable hidden">
            Something broke and we're not sure what. Try again later, or search near a city, place, or address instead.
        </div>
        <div class="curloc-timeout hidden">
            We couldn't find you quickly enough! Try again later, or search near a city, place, or address instead.
        </div>
        <div class="curloc-inaccurate hidden">
            We couldn't find an accurate position. If you're using a laptop or tablet, try moving it somewhere else and give it another go. Or, search near a city, place, or address instead.
        </div>
    </div>
</div>

    <div class="main-header_nav-wrapper js-header-nav main-content-wrap responsive-hidden-medium">
        <div class="content-container">
            <div class="main-header_nav u-nowrap">
                <div class="arrange">
                    <div class="arrange_unit arrange_unit--fill">
            <div id="header-nav">

                    <ul class="header-nav">
            <li class="header-nav_item js-analytics-click" data-analytics-label="restaurants">
                


    <div class="header-nav_link_container">
        <a class="header-nav_link" href="https://www.yelp.com/search?cflt=restaurants">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-food icon--size-18 icon--white icon--fallback-inverted u-space-r-half">
    <svg class="icon_svg">
        <use xlink:href="#18x18_food"></use>
    </svg>
</span>

            Restaurants

        </a>
    </div>

            </li>
            <li class="header-nav_item js-analytics-click" data-analytics-label="nightlife">
                


    <div class="header-nav_link_container">
        <a class="header-nav_link" href="https://www.yelp.com/search?cflt=nightlife">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-nightlife icon--size-18 icon--white icon--fallback-inverted u-space-r-half">
    <svg class="icon_svg">
        <use xlink:href="#18x18_nightlife"></use>
    </svg>
</span>

            Nightlife

        </a>
    </div>

            </li>
            <li class="header-nav_item js-analytics-click" data-analytics-label="home services">
                


    <div class="header-nav_link_container has-dropdown dropdown--arrow dropdown--fade" data-component-bound="true">
        <a class="header-nav_link js-dropdown-toggle dropdown_toggle" href="https://www.yelp.com/search?cflt=homeservices">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-tools icon--size-18 icon--white icon--fallback-inverted u-space-r-half">
    <svg class="icon_svg">
        <use xlink:href="#18x18_tools"></use>
    </svg>
</span>

            Home Services

                <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down dropdown_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
        </a>
                <div class="dropdown_menu-container js-dropdown_menu-container">
        <div class="dropdown_menu js-dropdown-menu">
            <div class="dropdown_menu-inner">
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item js-analytics-click" data-analytics-label="air conditioning &amp; heating" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=hvac" role="menuitem">
        <span class="dropdown_label">
                Air Conditioning &amp; Heating
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="contractors" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=contractors" role="menuitem">
        <span class="dropdown_label">
                Contractors
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="electricians" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=electricians" role="menuitem">
        <span class="dropdown_label">
                Electricians
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="home cleaners" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=homecleaning" role="menuitem">
        <span class="dropdown_label">
                Home Cleaners
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="landscapers" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=landscaping" role="menuitem">
        <span class="dropdown_label">
                Landscapers
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="locksmiths" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=locksmiths" role="menuitem">
        <span class="dropdown_label">
                Locksmiths
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="movers" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=movers" role="menuitem">
        <span class="dropdown_label">
                Movers
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="painters" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=painters" role="menuitem">
        <span class="dropdown_label">
                Painters
        </span>
    </a>

                            </li>
                            <li class="dropdown_item js-analytics-click" data-analytics-label="plumbers" role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?cflt=plumbing" role="menuitem">
        <span class="dropdown_label">
                Plumbers
        </span>
    </a>

                            </li>
                    </ul>
            </div>
        </div>
    </div>

    </div>

            </li>
    </ul>


                    <ul class="header-nav">
            <li id="write-review" class="header-nav_item js-analytics-click" data-analytics-label="write-review">
                    


    <div class="header-nav_link_container">
        <a class="header-nav_link" href="https://www.yelp.com/writeareview">

            Write a Review

        </a>
    </div>

            </li>
            <li id="events" class="header-nav_item js-analytics-click" data-analytics-label="events">
                    


    <div class="header-nav_link_container">
        <a class="header-nav_link" href="https://www.yelp.com/events">

            Events

        </a>
    </div>

            </li>
            <li id="talk" class="header-nav_item js-analytics-click" data-analytics-label="talk">
                    


    <div class="header-nav_link_container">
        <a class="header-nav_link" href="https://www.yelp.com/talk">

            Talk

        </a>
    </div>

            </li>
    </ul>

            </div>
                    </div>
                        <div class="arrange_unit js-analytics-click" id="header-log-in" data-analytics-label="login">
                                    <a class="header-nav_link header-nav_link--log-in js-log-in-button" href="https://www.yelp.com/login?return_url=%2Fsearch%3Ffind_desc%3Dfried%2Bchicken%26find_loc%3DAtlanta%252C%2BGA%26ns%3D1">
            Log In
        </a>

                        </div>
                </div>
            </div>
        </div>
    </div>



                        

                        

                        

                        <script>
            (function() {
                var main = null;

                var main=(function(){function a(b){window.yDFP.ABP={};window.yDFP.ABP.getPixelSource=function(c){return b+"?ch="+c+"&rn="+Math.random()*11};window.yDFP.ABP.detect=function(l){var g=false;var f=2;var i=false;var h=false;function k(n,m){if(f===0||m>400){n(f===0&&g)}else{setTimeout(function(){k(n,m*2)},m*2)}}function j(){if(f!==0){return}g=!i&&h}var e=function(){f-=1;j()};var d=new Image();d.onload=e;d.onerror=function(){i=true;e()};d.src=window.yDFP.ABP.getPixelSource(1);var c=new Image();c.onload=e;
c.onerror=function(){h=true;e()};c.src=window.yDFP.ABP.getPixelSource(2);k(l,100)};window.yDFP.ABP.abpInstalledChannel="1382551876";window.yDFP.ABP.abpNotInstalledChannel="2859285073"}window.yDFP=window.yDFP||{};window.yDFP.initABPDetection=a;return window.yDFP.initABPDetection})();

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main("/px.gif");
            })();
    </script>

                        <div id="print-masthead">
        <img src="./Best Fried chicken in Atlanta, GA - Yelp_files/header_print.gif" class="print-bkg-img" alt="Yelp">
    </div>


                </div>



            <span id="page-content" class="offscreen">&nbsp;</span>

                <div class="main-content-wrap main-content-wrap--full">
    <div class="top-shelf top-shelf-grey">
        <div class="content-container">
            
    <div id="alert-container">

    </div>


    <div class="clearfix layout-block layout-full search-page-top">
    <div class="column column-alpha ">
                    <div class="search-header clearfix" data-component-bound="true">
            <div class="search-header-title-container">
                <h1>
                Best fried chicken <span class="query-location">in Atlanta, GA</span>
        </h1>

                <span class="pagination-results-window">
            Showing 1-10 of 1607
        </span>

        
    </div>

        
    <script type="application/ld+json">            {"@context": "http://schema.org", "itemListElement": [{"position": 1, "@type": "ListItem", "item": {"url": "/search?find_loc=Atlanta%2C+GA", "name": "Atlanta"}}], "@type": "BreadcrumbList"}
</script>

        
    
    
    

    </div>

    <div class="filter-panel">
                            <div class="filter-bar suggested-filters" data-component-bound="true">
            <ul class="suggested-filters_filter-list">



                <li class="suggested-filters_filter js-platform-in-panel-filter platform-in-panel-filter">
                </li>

                    <li class="suggested-filters_filter">    <ul class="suggested-filters_price-filters">
            <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.1">

        <span class="filter-label show-tooltip">
            $
                <span class="tooltip-wrapper">
                    <span class="tooltip">Inexpensive</span>
                </span>
        </span>
    </label>
</li>
            <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.2">

        <span class="filter-label show-tooltip">
            $$
                <span class="tooltip-wrapper">
                    <span class="tooltip">Moderate</span>
                </span>
        </span>
    </label>
</li>
            <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.3">

        <span class="filter-label show-tooltip">
            $$$
                <span class="tooltip-wrapper">
                    <span class="tooltip">Pricey</span>
                </span>
        </span>
    </label>
</li>
            <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.4">

        <span class="filter-label show-tooltip">
            $$$$
                <span class="tooltip-wrapper">
                    <span class="tooltip">Ultra High-End</span>
                </span>
        </span>
    </label>
</li>
    </ul>
</li>

                    <li class="suggested-filters_filter">            <label class="feature open-now radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="open_now">


        <span class="filter-label show-tooltip">
            <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-clock icon--size-18 icon--neutral-gray">
    <svg class="icon_svg">
        <use xlink:href="#18x18_clock"></use>
    </svg>
</span>

            Open Now     <span class="current-time"></span>


                <span class="tooltip-wrapper">
                    <span class="tooltip">Find businesses that are open now</span>
                </span>
        </span>
    </label>

</li>
                    <li class="suggested-filters_filter">                
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformDelivery">


        <span class="filter-label show-tooltip">
                <span aria-hidden="true" style="fill: #ca6d00; width: 18px; height: 18px;" class="icon icon--18-order icon--size-18">
    <svg class="icon_svg">
        <use xlink:href="#18x18_order"></use>
    </svg>
</span>

            Order Delivery

                <span class="tooltip-wrapper">
                    <span class="tooltip">Find businesses that deliver to you</span>
                </span>
        </span>
    </label>


</li>
                    <li class="suggested-filters_filter">                
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformPickup">


        <span class="filter-label show-tooltip">
                <span aria-hidden="true" style="fill: #ca6d00; width: 18px; height: 18px;" class="icon icon--18-shopping icon--size-18">
    <svg class="icon_svg">
        <use xlink:href="#18x18_shopping"></use>
    </svg>
</span>

            Order Takeout

                <span class="tooltip-wrapper">
                    <span class="tooltip">Find businesses where you can order pickup</span>
                </span>
        </span>
    </label>


</li>
                    <li class="suggested-filters_filter">        
    

    <div class="coachmark-tooltip js-OnlineReservations-search-coachmark coachmark-tooltip--bottom" data-component-bound="true">
        <div class="js-coachmark-tooltip coachmark-tooltip-content" style="opacity: 1; display: none; margin-top: 0px; top: 40px; left: -6.5px;">
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-close icon--size-14 icon--inverse icon--fallback-inverted coachmark-close js-coachmark-close">
    <svg class="icon_svg">
        <use xlink:href="#14x14_close"></use>
    </svg>
</span>
            <small>Toggle this filter to view restaurants that take online reservations through Yelp</small>
        </div>
        <div class="js-coachmark-target">
            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OnlineReservations">


        <a class="filter-label anchor-link show-tooltip" href="https://www.yelp.com/search?attrs=OnlineReservations&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-reservation icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_reservation"></use>
    </svg>
</span>

            Make a Reservation

                <span class="tooltip-wrapper">
                    <span class="tooltip">Find and book a table</span>
                </span>
        </a>
    </label>

        </div>
    </div>

</li>

                <li class="suggested-filters_filter">    <label class="radio-check">
        <span class="filter-label filters-toggle js-all-filters-toggle show-tooltip">
            <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-filter icon--size-18 icon--currentColor">
    <svg class="icon_svg">
        <use xlink:href="#18x18_filter"></use>
    </svg>
</span> All Filters
            <span class="tooltip-wrapper">
                <span class="tooltip" data-collapsed-text="Show more filters" data-expanded-text="Show fewer filters">Show more filters</span>
            </span>
        </span>
    </label>
</li>
            </ul>
    </div>


                        <div class="filter-bar query-refinement_filters inactive-left-arrow inactive-right-arrow u-hidden" data-supports-auto-enable="True" data-component-bound="true">
        <div class="container">
            <div class="refinement-arrow-left">
                <span aria-hidden="true" style="width: 48px; height: 48px;" class="icon icon--48-chevron-left icon--size-48 refinement-arrow-left-inner">
    <svg class="icon_svg">
        <use xlink:href="#48x48_chevron_left"></use>
    </svg>
</span>
            </div>
            <div class="refinements-container">
                <div class="scroll-container">
                    
                </div>
            </div>
            <div class="refinement-arrow-right">
                <span aria-hidden="true" style="width: 48px; height: 48px;" class="icon icon--48-chevron-right icon--size-48 refinement-arrow-right-inner">
    <svg class="icon_svg">
        <use xlink:href="#48x48_chevron_right"></use>
    </svg>
</span>
            </div>
        </div>
    </div>

                    
    <div class="filter-panel_filters is-collapsed" data-component-bound="true">
            <div class="container">
                <div class="filter-set sort-filters">
            <h4>Sort By</h4>
            <ul class="radio-list radio-list-links main">
                    <li>    <label>
        <input checked="checked" class="radio" name="sort" type="radio" value="best_match">
        <span class="radio-link">Best Match</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="sort" type="radio" value="rating">
        <span class="radio-link">Highest Rated</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="sort" type="radio" value="review_count">
        <span class="radio-link">Most Reviewed</span>
    </label>
</li>
            </ul>
        </div>

                <div class="filter-set place-filters">
            <h4 class="place-filter-title">Neighborhoods</h4>
                <ul class="main">
            <li>    <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Buckhead">
        <span>Buckhead</span>
    </label>
</li>
            <li>    <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Midtown">
        <span>Midtown</span>
    </label>
</li>
            <li>    <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Downtown">
        <span>Downtown</span>
    </label>
</li>
            <li>    <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Old_Fourth_Ward">
        <span>Old Fourth Ward</span>
    </label>
</li>
    </ul>


                <a class="more-link" href="javascript:;">More Neighborhoods</a>

                <ul class="more place-more">
                

    <div class="js-toggle-list-item toggle-list-item toggle-list-item--active">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Atlanta</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Ansley_Park">
        <span>Ansley Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Atlantic_Station">
        <span>Atlantic Station</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Brookhaven">
        <span>Brookhaven</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Buckhead">
        <span>Buckhead</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Cabbagetown">
        <span>Cabbagetown</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Candler_Park">
        <span>Candler Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Castleberry_Hill">
        <span>Castleberry Hill</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Centennial_Place">
        <span>Centennial Place</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Decatur">
        <span>Decatur</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Downtown">
        <span>Downtown</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Druid_Hills">
        <span>Druid Hills</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::East_Atlanta_Village">
        <span>East Atlanta Village</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::East_Lake">
        <span>East Lake</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Edgewood">
        <span>Edgewood</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Emory_Village">
        <span>Emory Village</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Georgia_Tech">
        <span>Georgia Tech</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Grant_Park">
        <span>Grant Park</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Inman_Park">
        <span>Inman Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Kirkwood">
        <span>Kirkwood</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Lake_Claire">
        <span>Lake Claire</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Lindbergh">
        <span>Lindbergh</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Little_Five_Points">
        <span>Little Five Points</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Midtown">
        <span>Midtown</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Morningside_/_Lenox_Park">
        <span>Morningside / Lenox Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Old_Fourth_Ward">
        <span>Old Fourth Ward</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Ormewood_Park">
        <span>Ormewood Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Poncey-Highland">
        <span>Poncey-Highland</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Reynoldstown">
        <span>Reynoldstown</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Vinings">
        <span>Vinings</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Virginia_Highland">
        <span>Virginia Highland</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::West_End">
        <span>West End</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::West_Paces_Ferry_/_Northside">
        <span>West Paces Ferry / Northside</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::Westside_/_Home_Park">
        <span>Westside / Home Park</span>
    </label>

                        </li>
                </ul>
        </div>
        </div>
    </div>

                

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Cities</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Acworth::">
        <span>Acworth</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Alpharetta::">
        <span>Alpharetta</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Atlanta::">
        <span>Atlanta</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Austell::">
        <span>Austell</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Buford::">
        <span>Buford</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Chamblee::">
        <span>Chamblee</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Clarkston::">
        <span>Clarkston</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:College_Park::">
        <span>College Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Conyers::">
        <span>Conyers</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Covington::">
        <span>Covington</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Cumming::">
        <span>Cumming</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Dallas::">
        <span>Dallas</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Doraville::">
        <span>Doraville</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Douglasville::">
        <span>Douglasville</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Duluth::">
        <span>Duluth</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Dunwoody::">
        <span>Dunwoody</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:East_Point::">
        <span>East Point</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Ellenwood::">
        <span>Ellenwood</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Fairburn::">
        <span>Fairburn</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Forest_Park::">
        <span>Forest Park</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Hapeville::">
        <span>Hapeville</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Hiram::">
        <span>Hiram</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Johns_Creek::">
        <span>Johns Creek</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Jonesboro::">
        <span>Jonesboro</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Kennesaw::">
        <span>Kennesaw</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Lawrenceville::">
        <span>Lawrenceville</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Lilburn::">
        <span>Lilburn</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Lithia_Springs::">
        <span>Lithia Springs</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Lithonia::">
        <span>Lithonia</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Mableton::">
        <span>Mableton</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Marietta::">
        <span>Marietta</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Milton::">
        <span>Milton</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Morrow::">
        <span>Morrow</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Norcross::">
        <span>Norcross</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Palmetto::">
        <span>Palmetto</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Peachtree_Corners::">
        <span>Peachtree Corners</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Powder_Springs::">
        <span>Powder Springs</span>
    </label>

                        </li>
                </ul>
                <ul class="column">
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Riverdale::">
        <span>Riverdale</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Roswell::">
        <span>Roswell</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Sandy_Springs::">
        <span>Sandy Springs</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Smyrna::">
        <span>Smyrna</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Snellville::">
        <span>Snellville</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Stockbridge::">
        <span>Stockbridge</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Stone_Mountain::">
        <span>Stone Mountain</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Suwanee::">
        <span>Suwanee</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Tucker::">
        <span>Tucker</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Tyrone::">
        <span>Tyrone</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Union_City::">
        <span>Union City</span>
    </label>

                        </li>
                        <li>
                                <label class="place radio-check">
        <input name="place" type="checkbox" value="GA:Woodstock::">
        <span>Woodstock</span>
    </label>

                        </li>
                </ul>
        </div>
        </div>
    </div>

    </ul>

        </div>

                <div class="filter-set distance-filters">
            <h4>Distance</h4>
            <ul class="radio-list radio-list-links main">
                    <li>    <label>
        <input class="radio" name="l" type="radio" value="g:-84.4759368896,33.7277661673,-84.2713165283,33.8989168844">
        <span class="radio-link">Bird's-eye View</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="l" type="radio" value="g:-84.4247817993,33.7703005481,-84.3224716187,33.8558762051">
        <span class="radio-link">Driving (5 mi.)</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="l" type="radio" value="g:-84.3992042542,33.7918451488,-84.3480491638,33.8346329076">
        <span class="radio-link">Biking (2 mi.)</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="l" type="radio" value="g:-84.3864154816,33.8025440948,-84.3608379364,33.8239379744">
        <span class="radio-link">Walking (1 mi.)</span>
    </label>
</li>
                    <li>    <label>
        <input class="radio" name="l" type="radio" value="g:-84.3768239021,33.810531769,-84.3704295158,33.8158802412">
        <span class="radio-link">Within 4 blocks</span>
    </label>
</li>
            </ul>
        </div>

                <div class="filter-set price-filters" data-supports-auto-enable="True" data-component-bound="true">
            <h4>Price</h4>
            <ul class="main">
                    <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.1">

        <span class="filter-label">
            $
        </span>
    </label>
</li>
                    <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.2">

        <span class="filter-label">
            $$
        </span>
    </label>
</li>
                    <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.3">

        <span class="filter-label">
            $$$
        </span>
    </label>
</li>
                    <li>
    <label class="radio-check">
        <input name="price" type="checkbox" value="RestaurantsPriceRange2.4">

        <span class="filter-label">
            $$$$
        </span>
    </label>
</li>
            </ul>
        </div>

                <div class="filter-set feature-filters" data-supports-auto-enable="True" data-component-bound="true">
            <h4 class="feature-filter-title">Features</h4>
                <ul class="main">
            <li>                
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformDelivery">


        <span class="filter-label">
                <span aria-hidden="true" style="fill: #ca6d00; width: 14px; height: 14px;" class="icon icon--14-order icon--size-14">
    <svg class="icon_svg">
        <use xlink:href="#14x14_order"></use>
    </svg>
</span>

            Order Delivery

        </span>
    </label>


</li>
            <li>                
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformPickup">


        <span class="filter-label">
                <span aria-hidden="true" style="fill: #ca6d00; width: 14px; height: 14px;" class="icon icon--14-order icon--size-14">
    <svg class="icon_svg">
        <use xlink:href="#14x14_order"></use>
    </svg>
</span>

            Order Takeout

        </span>
    </label>


</li>
            <li>                
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OnlineReservations">


        <a class="filter-label anchor-link" href="https://www.yelp.com/search?attrs=OnlineReservations&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1">
                <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-reservation icon--size-14 icon--neutral-gray">
    <svg class="icon_svg">
        <use xlink:href="#14x14_reservation"></use>
    </svg>
</span>

            Make a Reservation

        </a>
    </label>


</li>
            <li>            <label class="feature open-now radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="open_now">


        <span class="filter-label">
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-clock icon--size-14 icon--success">
    <svg class="icon_svg">
        <use xlink:href="#14x14_clock"></use>
    </svg>
</span>

            Open Now     <span class="current-time">6:32 PM</span>


        </span>
    </label>

</li>
    </ul>

                <a class="more-link" href="javascript:;">More Features</a>

                <ul class="more feature-more">
            

    <div class="js-toggle-list-item toggle-list-item toggle-list-item--active">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">General Features</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformDelivery">


        <span class="filter-label">
                <span aria-hidden="true" style="fill: #ca6d00; width: 14px; height: 14px;" class="icon icon--14-order icon--size-14">
    <svg class="icon_svg">
        <use xlink:href="#14x14_order"></use>
    </svg>
</span>

            Order Delivery

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PlatformPickup">


        <span class="filter-label">
                <span aria-hidden="true" style="fill: #ca6d00; width: 14px; height: 14px;" class="icon icon--14-order icon--size-14">
    <svg class="icon_svg">
        <use xlink:href="#14x14_order"></use>
    </svg>
</span>

            Order Takeout

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OnlineReservations">


        <a class="filter-label anchor-link" href="https://www.yelp.com/search?attrs=OnlineReservations&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;ns=1">
                <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-reservation icon--size-14 icon--neutral-gray">
    <svg class="icon_svg">
        <use xlink:href="#14x14_reservation"></use>
    </svg>
</span>

            Make a Reservation

        </a>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OffersRewards">


        <span class="filter-label">

            Cash Back

        </span>
    </label>



                        </li>
                        <li>
                                        <span class="feature open-at radio-check">
        <label>
                <input autocomplete="off" name="feature" type="checkbox" value="open_time">

            Open At:
        </label><br>
            <input type="time" class="open-at html5-input type-time" id="open_at_current_time">
        <select name="day">
                <option value="0">
                    Mon
                </option>
                <option selected="selected" value="1">
                    Tue
                </option>
                <option value="2">
                    Wed
                </option>
                <option value="3">
                    Thu
                </option>
                <option value="4">
                    Fri
                </option>
                <option value="5">
                    Sat
                </option>
                <option value="6">
                    Sun
                </option>
        </select>
    </span>


                        </li>
                        <li>
                                        <label class="feature open-now radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="open_now">


        <span class="filter-label">
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-clock icon--size-14 icon--success">
    <svg class="icon_svg">
        <use xlink:href="#14x14_clock"></use>
    </svg>
</span>

            Open Now     <span class="current-time">6:32 PM</span>


        </span>
    </label>


                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="RestaurantsReservations">


        <span class="filter-label">

            Takes Reservations

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessAcceptsCreditCards">


        <span class="filter-label">

            Accepts Credit Cards

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="RestaurantsDelivery">


        <span class="filter-label">

            Delivery

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OutdoorSeating">


        <span class="filter-label">

            Outdoor Seating

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForKids">


        <span class="filter-label">

            Good for Kids

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="RestaurantsGoodForGroups">


        <span class="filter-label">

            Good for Groups

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="RestaurantsTableService">


        <span class="filter-label">

            Waiter Service

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="RestaurantsTakeOut">


        <span class="filter-label">

            Take-out

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="WheelchairAccessible">


        <span class="filter-label">

            Wheelchair Accessible

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="HasTV">


        <span class="filter-label">

            Has TV

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="DogsAllowed">


        <span class="filter-label">

            Dogs Allowed

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="LikedByTwenties">


        <span class="filter-label">

            Liked by 20-somethings

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="LikedByThirties">


        <span class="filter-label">

            Liked by 30-somethings

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="LikedByForties">


        <span class="filter-label">

            Liked by 40-somethings

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="NewBusiness">


        <span class="filter-label">

            Hot and New

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="OffersMilitaryDiscount">


        <span class="filter-label">

            Offers Military Discount

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="PokestopNearby">


        <span class="filter-label">

            PokéStop Nearby

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GenderNeutralRestrooms">


        <span class="filter-label">

            Gender Neutral Restrooms

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Alcohol</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Alcohol.full_bar">


        <span class="filter-label">

            Full Bar

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Alcohol.beer_and_wine">


        <span class="filter-label">

            Beer &amp; Wine Only

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="HappyHour">


        <span class="filter-label">

            Happy Hour

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Meals Served</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.breakfast">


        <span class="filter-label">

            Breakfast

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.brunch">


        <span class="filter-label">

            Brunch

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.lunch">


        <span class="filter-label">

            Lunch

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.dinner">


        <span class="filter-label">

            Dinner

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.dessert">


        <span class="filter-label">

            Dessert

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="GoodForMeal.latenight">


        <span class="filter-label">

            Late Night

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Music</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Music.dj">


        <span class="filter-label">

            DJ

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Music.jukebox">


        <span class="filter-label">

            Juke Box

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Music.karaoke">


        <span class="filter-label">

            Karaoke

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Music.live">


        <span class="filter-label">

            Live

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Parking</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessParking.street">


        <span class="filter-label">

            Street

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessParking.garage">


        <span class="filter-label">

            Garage

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessParking.valet">


        <span class="filter-label">

            Valet

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessParking.lot">


        <span class="filter-label">

            Private Lot

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="BusinessParking.validated">


        <span class="filter-label">

            Validated

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Wi-Fi</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="WiFi.free">


        <span class="filter-label">

            Free

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="WiFi.paid">


        <span class="filter-label">

            Paid

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

            

    <div class="js-toggle-list-item toggle-list-item">
        <h4 class="arrange arrange--middle toggle-list-link js-toggle-list-trigger u-space-b1">
            <span class="arrange_unit u-cursor-pointer">
                <span class="toggle-link-arrow-wrap u-inline-block">
                    <span class="toggle-link-arrow" role="presentation"></span>
                </span>
            </span>
            <span class="arrange_unit arrange_unit--fill">
                <span class="u-pseudo-link u-decoration-none">Smoking</span>
            </span>
        </h4>
        <div class="js-toggle-list-content toggle-list-content">
        <div class="filter-group">
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Smoking.no">


        <span class="filter-label">

            No

        </span>
    </label>



                        </li>
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Smoking.outdoor">


        <span class="filter-label">

            Outdoor Area / Patio Only

        </span>
    </label>



                        </li>
                </ul>
                <ul class="column">
                        <li>
                                            
    <label class="feature radio-check">
            <input autocomplete="off" name="feature" type="checkbox" value="Smoking.yes">


        <span class="filter-label">

            Yes

        </span>
    </label>



                        </li>
                </ul>
        </div>
        </div>
    </div>

    </ul>

        </div>

        
        <div class="filter-set category-filters">
            <h4>Category</h4>
                <ul class="main">
            <li>
                    <label class="category radio-check">
        <input name="category" type="checkbox" value="restaurants">
        <span>Restaurants</span>
    </label>

            </li>
            <li>
                    <label class="category radio-check">
        <input name="category" type="checkbox" value="chinese">
        <span>Chinese</span>
    </label>

            </li>
            <li>
                    <label class="category radio-check">
        <input name="category" type="checkbox" value="bars">
        <span>Bars</span>
    </label>

            </li>
            <li>
                    <label class="category radio-check">
        <input name="category" type="checkbox" value="tradamerican">
        <span>American (Traditional)</span>
    </label>

            </li>
    </ul>


                <a class="more-link" href="javascript:;">More Categories</a>

                <div class="more category-more filter-group arrange arrange--30 arrange--equal">
            <ul class="arrange_unit">
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="restaurants">
        <span>Restaurants</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="chinese">
        <span>Chinese</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="nightlife">
        <span>Nightlife</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="bars">
        <span>Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="tradamerican">
        <span>American (Traditional)</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="newamerican">
        <span>American (New)</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="southern">
        <span>Southern</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="chicken_wings">
        <span>Chicken Wings</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="food">
        <span>Food</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="breakfast_brunch">
        <span>Breakfast &amp; Brunch</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="seafood">
        <span>Seafood</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="hotdogs">
        <span>Fast Food</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="burgers">
        <span>Burgers</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="mexican">
        <span>Mexican</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="sandwiches">
        <span>Sandwiches</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="sushi">
        <span>Sushi Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="sportsbars">
        <span>Sports Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="thai">
        <span>Thai</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="salad">
        <span>Salad</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="soulfood">
        <span>Soul Food</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="japanese">
        <span>Japanese</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="asianfusion">
        <span>Asian Fusion</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="pizza">
        <span>Pizza</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="bbq">
        <span>Barbeque</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="buffets">
        <span>Buffets</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="korean">
        <span>Korean</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="italian">
        <span>Italian</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="desserts">
        <span>Desserts</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="pubs">
        <span>Pubs</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="tex-mex">
        <span>Tex-Mex</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="cafes">
        <span>Cafes</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="diners">
        <span>Diners</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="gastropubs">
        <span>Gastropubs</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="eventservices">
        <span>Event Planning &amp; Services</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="cocktailbars">
        <span>Cocktail Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="steak">
        <span>Steakhouses</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="indpak">
        <span>Indian</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="grocery">
        <span>Grocery</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="coffee">
        <span>Coffee &amp; Tea</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="soup">
        <span>Soup</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="caribbean">
        <span>Caribbean</span>
    </label>

                    </li>
            </ul>
            <ul class="arrange_unit">
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="cajun">
        <span>Cajun/Creole</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="catering">
        <span>Caterers</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="latin">
        <span>Latin American</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="bakeries">
        <span>Bakeries</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="comfortfood">
        <span>Comfort Food</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="arts">
        <span>Arts &amp; Entertainment</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="vegetarian">
        <span>Vegetarian</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="shopping">
        <span>Shopping</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="vietnamese">
        <span>Vietnamese</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="gluten_free">
        <span>Gluten-Free</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="noodles">
        <span>Noodles</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="chickenshop">
        <span>Chicken Shop</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="greek">
        <span>Greek</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="lounges">
        <span>Lounges</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="mediterranean">
        <span>Mediterranean</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="musicvenues">
        <span>Music Venues</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="ramen">
        <span>Ramen</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="venues">
        <span>Venues &amp; Event Spaces</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="gourmet">
        <span>Specialty Food</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="szechuan">
        <span>Szechuan</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="wine_bars">
        <span>Wine Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="bubbletea">
        <span>Bubble Tea</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="divebars">
        <span>Dive Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="halal">
        <span>Halal</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="icecream">
        <span>Ice Cream &amp; Frozen Yogurt</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="tapas">
        <span>Tapas Bars</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="beerbar">
        <span>Beer Bar</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="breweries">
        <span>Breweries</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="malaysian">
        <span>Malaysian</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="tapasmallplates">
        <span>Tapas/Small Plates</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="beer_and_wine">
        <span>Beer, Wine &amp; Spirits</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="cheesesteaks">
        <span>Cheesesteaks</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="delis">
        <span>Delis</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="drugstores">
        <span>Drugstores</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="foodtrucks">
        <span>Food Trucks</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="irish">
        <span>Irish</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="irish_pubs">
        <span>Irish Pub</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="pakistani">
        <span>Pakistani</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="cuban">
        <span>Cuban</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="mideastern">
        <span>Middle Eastern</span>
    </label>

                    </li>
                    <li>
                            <label class="category radio-check">
        <input name="category" type="checkbox" value="taiwanese">
        <span>Taiwanese</span>
    </label>

                    </li>
            </ul>
    </div>

        </div>

    </div>

    </div>

        <div class="filter-panel_overlay" role="presentation"></div>
    </div>
    </div>
    </div>
        </div>
    </div>

                    <div id="super-container" class="content-container">


    <div class="container">

    <div class="clearfix layout-block layout-full search-exception" data-component-bound="true" style="position: relative;">
    <div class="column column-alpha ">
                <div class="content">
                </div>
    </div>
    <div class="throbber-overlay" style="display: none;"><div class="throbber-container"></div></div></div>

                <div class="clearfix layout-block layout-a scroll-map-container search-results-block">
    <div class="column column-alpha ">
                <div class="results-wrapper indexed-biz-archive" data-component-bound="true" style="position: relative; min-height: 362px;">
            
    <div class="platform-search js-platform-search js-platform-delivery-search no-js-hidden island hidden" data-address-async-url="/transaction_platform/get_recent_addresses" data-is-auto-complete-enabled="False" data-single-address-async-url="/transaction_platform/get_address" data-touch-address-async-url="/transaction_platform/touch_address_identity" data-component-bound="true" style="display: none;">



    <form action="https://www.yelp.com/transaction_platform/disambiguate_address" class="yform yform--continuous arrange arrange--baseline arrange--6 platform-search-form" id="platform-form" method="POST">
        <input type="hidden" name="csrftok" class="csrftok" value="4e17b2f9e859433c8c932c71a4f19013d12a35912cdad0b4ca58996d77013352">
            <div class="vertical-search-text-section arrange_unit nowrap">
                <label>
                    <input class="search-checkbox js-platform-search-checkbox" name="platform-filter" type="checkbox" value="platform-filter">

                    <span class="title-text title-text--no-st-picker js-title-text-order-delivery">
                        <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-order icon--size-24">
    <svg class="icon_svg">
        <use xlink:href="#24x24_order"></use>
    </svg>
</span>
                        Order Delivery
                    </span>
                </label>
            </div>

            <input type="hidden" class="service-type-picker" value="delivery_default" data-service-type="delivery_default">

            <div class="vertical-search-address-section arrange_unit arrange_unit--fill">
                <div class="delivery-address-suggestions-wrap arrange arrange--baseline" data-component-bound="true">
                    <div class="arrange_unit arrange_unit--fill js-delivery-address">
                        <input class="address-picker js-delivery-address-field inline-block" type="text" placeholder="1 Yelp St., San Francisco, CA 94105" maxlength="300" data-address-identity-id="" data-component-bound="true" autocomplete="off">
                    </div>
                    <div class="arrange_unit search-button-wrap">
                        <button type="submit" value="submit" class="ybtn ybtn--primary ybtn--small platform-search-button" style="display: inline-block;"><span><span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-search-small icon--size-18 icon--inverse icon--fallback-inverted">
    <svg class="icon_svg">
        <use xlink:href="#18x18_search_small"></use>
    </svg>
</span></span></button>
                    </div>
                    <div class="delivery-address-suggestions suggestions-list-container auto-complete" data-component-bound="true" style="top: 11px; left: -1px; width: 102px; display: none;"><ul class="suggestions-list"></ul></div>
                </div>
                <p class="text-error js-address-error-message">Enter your address to find businesses that deliver to you.</p>
            </div>
    </form>
    </div>

                <div class="hidden platform-vsearch-popup" data-popup-title="Order Pickup or Delivery">



    <form action="https://www.yelp.com/transaction_platform/disambiguate_address" class="yform" method="POST">
        <input type="hidden" name="csrftok" class="csrftok" value="4e17b2f9e859433c8c932c71a4f19013d12a35912cdad0b4ca58996d77013352">
            <fieldset>
                <label>
                    <input type="radio" name="order_type" value="pickup">
                    <span>Pickup</span>
                </label>
                <label>
                    <input type="radio" name="order_type" value="delivery" checked="">
                    <span>Enter your delivery address</span>
                </label>
            </fieldset>
            <div class="js-delivery-options">
                <div class="yform-inline">
                    <div class="yform-input-field-wrap">
                        <input class="js-platform-popup-address-picker" maxlength="300" placeholder="1 Yelp St., San Francisco, CA 94105" type="text">
                    </div>
                    <button type="submit" value="submit" class="ybtn ybtn--primary ybtn--small js-platform-popup-search-button"><span><span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-search-small icon--size-18 icon--inverse icon--fallback-inverted">
    <svg class="icon_svg">
        <use xlink:href="#18x18_search_small"></use>
    </svg>
</span></span></button>
                </div>
                <div class="disambiguation-links hidden">
                    <h3>Did you mean:</h3>
                    <ul></ul>
                </div>
                <p class="text-error js-address-error-message hidden"></p>
            </div>
            <div class="js-pickup-options hidden">
                <button type="submit" value="submit" class="ybtn ybtn--primary ybtn--small"><span>Find Restaurants</span></button>
            </div>
    </form>
    </div>



            <div class="reservations yform js-reservations no-js-hidden island reservation--inline hidden" data-initial-visibility="hidden" data-component-bound="true" style="display: none;">
        <div class="vertical-search-text-section">
            <label class="reservation-filter-label" for="reservation-filter">
                <input class="search-checkbox" id="reservation-filter" name="reservation-filter" type="checkbox" value="reservation-filter">

                <span class="title-text">
                    <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-reservation icon--size-24 icon--black u-space-r-half">
    <svg class="icon_svg">
        <use xlink:href="#24x24_reservation"></use>
    </svg>
</span>Make a Reservation
                </span>
            </label>
        </div>

    <ul class="inline-layout reservation-fields clearfix">
        <input type="hidden" name="flow_type" value="vertical_search">

            <li class="date-picker js-date-picker" data-date-pattern="EEE, MMM d" data-default-date="2017-09-12" data-component-bound="true">


    <div class="yselect">
            <span class="reservation-search-input-icon">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-reservation icon--size-18 icon--neutral_gray">
    <svg class="icon_svg">
        <use xlink:href="#18x18_reservation"></use>
    </svg>
</span>
            </span>
            <input class="date-input js-date-input reservation-input" name="reservation_datetime_date" type="text" value="Tue, Sep 12" readonly="">
        <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down yselect_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
    </div>
        <div class="reservation-popup-date-picker js-reservation-popup-date-picker hidden" style="display: none;">
            <div class="drop-menu-arrow"></div>
        <div class="goog-date-picker" tabindex="0" style="left: auto;"><table cellspacing="0" cellpadding="0"><thead><tr class="goog-date-picker-head"><td colspan="1"><button class="goog-date-picker-btn goog-date-picker-previousMonth">«</button></td><td colspan="5" class="goog-date-picker-monthyear">September 2017</td><td><button class="goog-date-picker-btn goog-date-picker-nextMonth">»</button></td></tr></thead><tbody role="grid" tabindex="0" aria-activedescendant=":g"><tr><th></th><th class="goog-date-picker-wday" role="columnheader">S</th><th class="goog-date-picker-wday" role="columnheader">M</th><th class="goog-date-picker-wday" role="columnheader">T</th><th class="goog-date-picker-wday" role="columnheader">W</th><th class="goog-date-picker-wday" role="columnheader">T</th><th class="goog-date-picker-wday" role="columnheader">F</th><th class="goog-date-picker-wday" role="columnheader">S</th></tr><tr><th class="" role="rowheader"></th><td id=":0" role="gridcell" class="goog-date-picker-date"></td><td id=":1" role="gridcell" class="goog-date-picker-date"></td><td id=":2" role="gridcell" class="goog-date-picker-date"></td><td id=":3" role="gridcell" class="goog-date-picker-date"></td><td id=":4" role="gridcell" class="goog-date-picker-date"></td><td id=":5" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">1</td><td id=":6" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-start goog-date-picker-disabled">2</td></tr><tr><th class="" role="rowheader"></th><td id=":7" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-end goog-date-picker-disabled">3</td><td id=":8" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">4</td><td id=":9" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">5</td><td id=":a" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">6</td><td id=":b" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">7</td><td id=":c" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">8</td><td id=":d" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-start goog-date-picker-disabled">9</td></tr><tr><th class="" role="rowheader"></th><td id=":e" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-end goog-date-picker-disabled">10</td><td id=":f" role="gridcell" class="goog-date-picker-date goog-date-picker-disabled">11</td><td id=":g" role="gridcell" class="goog-date-picker-date goog-date-picker-today goog-date-picker-selected">12</td><td id=":h" role="gridcell" class="goog-date-picker-date">13</td><td id=":i" role="gridcell" class="goog-date-picker-date">14</td><td id=":j" role="gridcell" class="goog-date-picker-date">15</td><td id=":k" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-start">16</td></tr><tr><th class="" role="rowheader"></th><td id=":l" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-end">17</td><td id=":m" role="gridcell" class="goog-date-picker-date">18</td><td id=":n" role="gridcell" class="goog-date-picker-date">19</td><td id=":o" role="gridcell" class="goog-date-picker-date">20</td><td id=":p" role="gridcell" class="goog-date-picker-date">21</td><td id=":q" role="gridcell" class="goog-date-picker-date">22</td><td id=":r" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-start">23</td></tr><tr class="goog-date-picker-last-week-of-month"><th class="" role="rowheader"></th><td id=":s" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-end">24</td><td id=":t" role="gridcell" class="goog-date-picker-date">25</td><td id=":u" role="gridcell" class="goog-date-picker-date">26</td><td id=":v" role="gridcell" class="goog-date-picker-date">27</td><td id=":w" role="gridcell" class="goog-date-picker-date">28</td><td id=":x" role="gridcell" class="goog-date-picker-date">29</td><td id=":y" role="gridcell" class="goog-date-picker-date goog-date-picker-wkend-start">30</td></tr><tr style="display: none;"><th class="" role="rowheader"></th><td id=":z" role="gridcell" class="goog-date-picker-date"></td><td id=":10" role="gridcell" class="goog-date-picker-date"></td><td id=":11" role="gridcell" class="goog-date-picker-date"></td><td id=":12" role="gridcell" class="goog-date-picker-date"></td><td id=":13" role="gridcell" class="goog-date-picker-date"></td><td id=":14" role="gridcell" class="goog-date-picker-date"></td><td id=":15" role="gridcell" class="goog-date-picker-date"></td></tr></tbody><tfoot><tr class="goog-date-picker-foot"><td colspan="3" class="goog-date-picker-today-cont"><button class="goog-date-picker-btn goog-date-picker-today-btn">Today</button></td><td colspan="3"></td><td colspan="2" class="goog-date-picker-none-cont"><button class="goog-date-picker-btn goog-date-picker-none-btn" style="display: none;">None</button></td></tr></tfoot></table></div></div>
    </li>

            <li class="time-picker">


    <div class="yselect">
            <span class="reservation-search-input-icon">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-clock icon--size-18 icon--neutral_gray">
    <svg class="icon_svg">
        <use xlink:href="#18x18_clock"></use>
    </svg>
</span>
            </span>
            <select name="reservation_datetime_time" class="reservation-time-select js-time-input reservation-input" data-component-bound="true">
                    <option class="js-time-option" value="0000">
                        12:00 am
                    </option>
                    <option class="js-time-option" value="0030">
                        12:30 am
                    </option>
                    <option class="js-time-option" value="0100">
                        1:00 am
                    </option>
                    <option class="js-time-option" value="0130">
                        1:30 am
                    </option>
                    <option class="js-time-option" value="0200">
                        2:00 am
                    </option>
                    <option class="js-time-option" value="0230">
                        2:30 am
                    </option>
                    <option class="js-time-option" value="0300">
                        3:00 am
                    </option>
                    <option class="js-time-option" value="0330">
                        3:30 am
                    </option>
                    <option class="js-time-option" value="0400">
                        4:00 am
                    </option>
                    <option class="js-time-option" value="0430">
                        4:30 am
                    </option>
                    <option class="js-time-option" value="0500">
                        5:00 am
                    </option>
                    <option class="js-time-option" value="0530">
                        5:30 am
                    </option>
                    <option class="js-time-option" value="0600">
                        6:00 am
                    </option>
                    <option class="js-time-option" value="0630">
                        6:30 am
                    </option>
                    <option class="js-time-option" value="0700">
                        7:00 am
                    </option>
                    <option class="js-time-option" value="0730">
                        7:30 am
                    </option>
                    <option class="js-time-option" value="0800">
                        8:00 am
                    </option>
                    <option class="js-time-option" value="0830">
                        8:30 am
                    </option>
                    <option class="js-time-option" value="0900">
                        9:00 am
                    </option>
                    <option class="js-time-option" value="0930">
                        9:30 am
                    </option>
                    <option class="js-time-option" value="1000">
                        10:00 am
                    </option>
                    <option class="js-time-option" value="1030">
                        10:30 am
                    </option>
                    <option class="js-time-option" value="1100">
                        11:00 am
                    </option>
                    <option class="js-time-option" value="1130">
                        11:30 am
                    </option>
                    <option class="js-time-option" value="1200">
                        12:00 pm
                    </option>
                    <option class="js-time-option" value="1230">
                        12:30 pm
                    </option>
                    <option class="js-time-option" value="1300">
                        1:00 pm
                    </option>
                    <option class="js-time-option" value="1330">
                        1:30 pm
                    </option>
                    <option class="js-time-option" value="1400">
                        2:00 pm
                    </option>
                    <option class="js-time-option" value="1430">
                        2:30 pm
                    </option>
                    <option class="js-time-option" value="1500">
                        3:00 pm
                    </option>
                    <option class="js-time-option" value="1530">
                        3:30 pm
                    </option>
                    <option class="js-time-option" value="1600">
                        4:00 pm
                    </option>
                    <option class="js-time-option" value="1630">
                        4:30 pm
                    </option>
                    <option class="js-time-option" value="1700">
                        5:00 pm
                    </option>
                    <option class="js-time-option" value="1730">
                        5:30 pm
                    </option>
                    <option class="js-time-option" value="1800">
                        6:00 pm
                    </option>
                    <option class="js-time-option" value="1830">
                        6:30 pm
                    </option>
                    <option class="js-time-option" selected="selected" value="1900">
                        7:00 pm
                    </option>
                    <option class="js-time-option" value="1930">
                        7:30 pm
                    </option>
                    <option class="js-time-option" value="2000">
                        8:00 pm
                    </option>
                    <option class="js-time-option" value="2030">
                        8:30 pm
                    </option>
                    <option class="js-time-option" value="2100">
                        9:00 pm
                    </option>
                    <option class="js-time-option" value="2130">
                        9:30 pm
                    </option>
                    <option class="js-time-option" value="2200">
                        10:00 pm
                    </option>
                    <option class="js-time-option" value="2230">
                        10:30 pm
                    </option>
                    <option class="js-time-option" value="2300">
                        11:00 pm
                    </option>
                    <option class="js-time-option" value="2330">
                        11:30 pm
                    </option>
            </select>
        <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down yselect_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
    </div>
    </li>

            <li class="people-picker">


    <div class="yselect">
            <span class="reservation-search-input-icon">
                <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-friends icon--size-18 icon--neutral_gray">
    <svg class="icon_svg">
        <use xlink:href="#18x18_friends"></use>
    </svg>
</span>
            </span>
            <select class="reservation-party-size-select js-people-input reservation-input" data-component-bound="true">
                    <option value="1">
                        1 person
                    </option>
                    <option selected="selected" value="2">
                        2 people
                    </option>
                    <option value="3">
                        3 people
                    </option>
                    <option value="4">
                        4 people
                    </option>
                    <option value="5">
                        5 people
                    </option>
                    <option value="6">
                        6 people
                    </option>
                    <option value="7">
                        7 people
                    </option>
                    <option value="8">
                        8 people
                    </option>
                    <option value="9">
                        9 people
                    </option>
                    <option value="10">
                        10 people
                    </option>
            </select>
        <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down yselect_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
    </div>
    </li>


    </ul>
    </div>

        <div class="search-results-content">
                    


    <ul class="ylist ylist-bordered search-results">
        
        
    </ul>

        <ul class="ylist ylist-bordered search-results">
                <li class="js-yloca js-yloca-search yloca-search-result" data-ad-placement="above_search" data-ad-slot="0" data-unique-request-id="f2da9c903fcf056d" data-component-bound="true">
                        <div class="search-result" data-key="ad_business:below_organic:4LqNKlYo8AtKb2_H9ZsL6g" data-component-bound="true">
        <div class="biz-listing-large">
            <div class="main-attributes">
                <div class="media-block media-block--12">
                    <div class="media-avatar">
                                        <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w&amp;campaign_id=TEbM0Hh_xf9wDMZ1CNmBhg&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2&amp;request_id=f2da9c903fcf056d&amp;signature=207d46adad148d9a421bdc96af996ce0050306f8a5c2d7a55a97fd0e770e9471&amp;slot=0" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="CalaBar &amp; Grill" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s.jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/gbgoS-y-OkIy0AWTkvgTVQ/258s.jpg 2.87x" width="90">

        </a>

    </div>




                    </div>
                    <div class="media-story">
                            <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        <h3 class="search-result-title">
                                <span class="yloca-tip" data-hovercard-id="1">
        Ad
    </span>

                                                <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w&amp;campaign_id=TEbM0Hh_xf9wDMZ1CNmBhg&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2&amp;request_id=f2da9c903fcf056d&amp;signature=207d46adad148d9a421bdc96af996ce0050306f8a5c2d7a55a97fd0e770e9471&amp;slot=0" data-hovercard-id="72nxppLYwE8_S9-igGAF0g"><span>CalaBar &amp; Grill</span></a>



                        </h3>
                            <span class="js-track-imp u-absolute js-pixel-logged"></span>

                                    <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            80 reviews
    </span>

        </div>


                                <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=newamerican&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">American (New)</a>,
                    <a href="https://www.yelp.com/search?cflt=cocktailbars&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Cocktail Bars</a>
    </span>


    </div>


                            <ul class="search-result_tags">
    </ul>

                    </div>
                </div>
            </div>
            <div class="secondary-attributes">
                    <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        
                <address>
        4144 Redan Rd<br>Stone Mountain, GA 30083
    </address>


                
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 299-2240
    </span>

            </div>
        </div>

            
        <div class="search-result-ctas u-space-t1">
                    <div class="search-avatar-offset js-ad-platform">
        <div class="island island--slim search-result-cta">
            <div class="arrange arrange--middle arrange--6">
                <div class="arrange_unit">
            <span aria-hidden="true" style="fill: #ca6d00; width: 18px; height: 18px;" class="icon icon--18-order icon--size-18">
    <svg class="icon_svg">
        <use xlink:href="#18x18_order"></use>
    </svg>
</span>
    </div>
    <div class="arrange_unit--fill arrange_unit cta-text">
        <span class="">
            This restaurant accepts pickup orders
        </span>
    </div>


        <div class="arrange_unit nowrap">
            <a href="https://www.yelp.com/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w&amp;click_origin=search_results_platform&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2%23popup%3Aplatform&amp;request_id=f2da9c903fcf056d&amp;signature=d0b621d14d8cf5a8beb417d054dd8ac70202abf134b74278cac36e10682f9701&amp;slot=0" class="ybtn ybtn--small low-intent-search-action-button">Start Order</a>
        </div>
            </div>
        </div>
        <div class="search-result-cta-error-row">
            <div class="platform-vsearch-error-message text-error">
            </div>
        </div>
    </div>

        </div>


                <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="cvcS807r9HHu3KzqPmCxCw">
                <a href="https://www.yelp.com/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w&amp;campaign_id=TEbM0Hh_xf9wDMZ1CNmBhg&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2%3Fhrid%3DVuYbkrQbAYaD1WPgvErYxw&amp;request_id=f2da9c903fcf056d&amp;signature=3b8b8cde9d6b675ee3dc80159358aea06d0e502d0f09a08c5ac2e8514b0872b2&amp;slot=0">
                <img alt="Kai E." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s.jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/jCZ4jmxgCAf-L1ovHhZ05w/60s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/photo/jCZ4jmxgCAf-L1ovHhZ05w/90s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/jCZ4jmxgCAf-L1ovHhZ05w/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        My friend and I came to CalaBar &amp; Grill on a Friday night for girls night. When we walked in there was a man sitting at a table next to the entrance who informed us that there is a…
                        <a href="https://www.yelp.com/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w&amp;campaign_id=TEbM0Hh_xf9wDMZ1CNmBhg&amp;click_origin=read_more&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2%3Fhrid%3DVuYbkrQbAYaD1WPgvErYxw&amp;request_id=f2da9c903fcf056d&amp;signature=3b8b8cde9d6b675ee3dc80159358aea06d0e502d0f09a08c5ac2e8514b0872b2&amp;slot=0" class="nowrap">read more</a>
                </p>
            </div>
        </div>

    </div>

                </li>
                <li class="js-yloca js-yloca-search yloca-search-result" data-ad-placement="above_search" data-ad-slot="1" data-unique-request-id="f2da9c903fcf056d" data-component-bound="true">
                        <div class="search-result" data-key="ad_business:below_organic:C3xZRDXwOpe0HzfdT8UUgA">
        <div class="biz-listing-large">
            <div class="main-attributes">
                <div class="media-block media-block--12">
                    <div class="media-avatar">
                                        <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA&amp;campaign_id=b2KhI8mQPlH-bFU3_SRcbw&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain&amp;request_id=f2da9c903fcf056d&amp;signature=36a764c42b28c4ca09690a027bd82fba8e40994f007825ccd6309251c247fcea&amp;slot=1" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Red Chili Cafe" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(1).jpg" srcset="https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/180s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/ms.jpg 1.11x,https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/120s.jpg 1.33x,https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/168s.jpg 1.87x,https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/ls.jpg 2.78x,https://s3-media3.fl.yelpcdn.com/bphoto/GkfzwUsfLnc-OtS9cVinEA/258s.jpg 2.87x" width="90">

        </a>

    </div>




                    </div>
                    <div class="media-story">
                            <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        <h3 class="search-result-title">
                                <span class="yloca-tip" data-hovercard-id="1">
        Ad
    </span>

                                                <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA&amp;campaign_id=b2KhI8mQPlH-bFU3_SRcbw&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain&amp;request_id=f2da9c903fcf056d&amp;signature=36a764c42b28c4ca09690a027bd82fba8e40994f007825ccd6309251c247fcea&amp;slot=1" data-hovercard-id="bzigtW0Rw4eP2Y0X6kBsUw"><span>Red Chili Cafe</span></a>



                        </h3>
                            <span class="js-track-imp u-absolute js-pixel-logged"></span>

                                    <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            49 reviews
    </span>

        </div>


                                <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=tradamerican&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">American (Traditional)</a>,
                    <a href="https://www.yelp.com/search?cflt=chicken_wings&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Chicken Wings</a>,
                    <a href="https://www.yelp.com/search?cflt=burgers&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Burgers</a>
    </span>


    </div>


                            <ul class="search-result_tags">
    </ul>

                    </div>
                </div>
            </div>
            <div class="secondary-attributes">
                    <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        
                <address>
        5653 Memorial Dr<br>Stone Mountain, GA 30083
    </address>


                
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (470) 239-5798
    </span>

            </div>
        </div>

            
        <div class="search-result-ctas u-space-t1">
                    <div class="search-avatar-offset js-ad-platform">
        <div class="island island--slim search-result-cta">
            <div class="arrange arrange--middle arrange--6">
                <div class="arrange_unit">
            <span aria-hidden="true" style="fill: #ca6d00; width: 18px; height: 18px;" class="icon icon--18-order icon--size-18">
    <svg class="icon_svg">
        <use xlink:href="#18x18_order"></use>
    </svg>
</span>
    </div>
    <div class="arrange_unit--fill arrange_unit cta-text">
        <span class="">
            This restaurant accepts pickup orders
        </span>
    </div>


        <div class="arrange_unit nowrap">
            <a href="https://www.yelp.com/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA&amp;click_origin=search_results_platform&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain%23popup%3Aplatform&amp;request_id=f2da9c903fcf056d&amp;signature=53d77391db25b382cdac31f1fd2b27b15bbfae4a207e8b6eb270e4df34c5e409&amp;slot=1" class="ybtn ybtn--small low-intent-search-action-button">Start Order</a>
        </div>
            </div>
        </div>
        <div class="search-result-cta-error-row">
            <div class="platform-vsearch-error-message text-error">
            </div>
        </div>
    </div>

        </div>


                <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="L_i-qsQsatsdpICA9bMH5g">
                <a href="https://www.yelp.com/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA&amp;campaign_id=b2KhI8mQPlH-bFU3_SRcbw&amp;click_origin=search_results&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain%3Fhrid%3DXC-MBZHUyOBlSYERw7oilw&amp;request_id=f2da9c903fcf056d&amp;signature=d8b7818877a13475043284f3e868ca052aefe27825ca87927f6267ad0587f2dc&amp;slot=1">
                <img alt="Glenda J." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(1).jpg" srcset="https://s3-media1.fl.yelpcdn.com/photo/c1TKclbke7H8zGVstCU-CA/60s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/photo/c1TKclbke7H8zGVstCU-CA/90s.jpg 3.00x,https://s3-media1.fl.yelpcdn.com/photo/c1TKclbke7H8zGVstCU-CA/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        After visiting this restaurant yesterday I felt I had to comment. I was totally surprised when I walked in. The places was very warm and cozy very different from other restaurants in…
                        <a href="https://www.yelp.com/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA&amp;campaign_id=b2KhI8mQPlH-bFU3_SRcbw&amp;click_origin=read_more&amp;placement=above_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain%3Fhrid%3DXC-MBZHUyOBlSYERw7oilw&amp;request_id=f2da9c903fcf056d&amp;signature=d8b7818877a13475043284f3e868ca052aefe27825ca87927f6267ad0587f2dc&amp;slot=1" class="nowrap">read more</a>
                </p>
            </div>
        </div>

    </div>

                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="ApwmEiStq9aP9-Tf2xfVtA" data-key="1" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/guss-world-famous-fried-chicken-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Gus&#39;s World Famous Fried Chicken" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(2).jpg" srcset="https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/180s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/ms.jpg 1.11x,https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/120s.jpg 1.33x,https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/168s.jpg 1.87x,https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/ls.jpg 2.78x,https://s3-media2.fl.yelpcdn.com/bphoto/fl3r9ErnihdLhbEw_JtR-A/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">1.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/guss-world-famous-fried-chicken-atlanta?osq=fried+chicken" data-hovercard-id="TdP-YvQ6PkjA7ozmInUKng"><span>Gus’s World Famous Fried Chicken</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            549 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=chickenshop&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Chicken Shop</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Downtown        </span>

                <address>
        231 West Peachtree Street Northeast A-05<br>Atlanta, GA 30303
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 996-2837
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="F-NQTFP2mLY1ufF1Ng_V-A">
                <a href="https://www.yelp.com/user_details?userid=o_OH_qB5CzAk-CckHNPBVQ">
                <img alt="V D." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/user_30_square.png" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        Ok. Heavy with salt, msg. A bit spicy, didn't expect that for the <span class="highlighted">fried</span> <span class="highlighted">chicken</span> and catfish. Chicken came well done, over fried and dry. Fried green tomatoes great. Fried okra…
                        <a href="https://www.yelp.com/biz/guss-world-famous-fried-chicken-atlanta?hrid=ogBGL0SXc7299Nrysp_-TQ&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="eG-UO83g_5zDk70FIJbm2w" data-key="2" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="South City Kitchen - Midtown" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(3).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">2.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" data-hovercard-id="tvYceAR7TJ7zS6N6kF5y8g"><span>South City Kitchen - Midtown</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4-half rating-large" title="4.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            1777 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=breakfast_brunch&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Breakfast &amp; Brunch</a>,
                    <a href="https://www.yelp.com/search?cflt=gluten_free&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Gluten-Free</a>
    </span>


    </div>


                        <ul class="search-result_tags">
            <li class="tag-18x18_menu-black">
                <small>
                    <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-menu icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_menu"></use>
    </svg>
</span>

                    On the menu: Springer Mountain Farms <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>
                </small>
                
            </li>
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Midtown        </span>

                <address>
        1144 Crescent Ave NE<br>Atlanta, GA 30309
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 873-7358
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="fWYrjHAe26TmZTQWmPvNYA">
                <a href="https://www.yelp.com/user_details?userid=wgJdgkumJlb_zvtRGzlGdA">
                <img alt="Tori P." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(2).jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/nXlkVQ9apfvnGR2svFb7Jg/60s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/photo/nXlkVQ9apfvnGR2svFb7Jg/90s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/nXlkVQ9apfvnGR2svFb7Jg/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        I treated myself to a nice dinner for 1 while visiting for the summer and I absolutely loved the <span class="highlighted">fried</span> <span class="highlighted">chicken</span> and my glass of rosé.
                        <a href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?hrid=7CxSHyAMV-oFYhqR0DSwDQ&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="z9oCxeqOKp2QMfM24m7bUw" data-key="3" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/mary-macs-tea-room-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Mary Mac&#39;s Tea Room" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(4).jpg" srcset="https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/180s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/ms.jpg 1.11x,https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/120s.jpg 1.33x,https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/168s.jpg 1.87x,https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/ls.jpg 2.78x,https://s3-media2.fl.yelpcdn.com/bphoto/TwtkoIDRygOj1mxpPibQow/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">3.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/mary-macs-tea-room-atlanta?osq=fried+chicken" data-hovercard-id="J1q9KDyfksvcce8qiv3wXA"><span>Mary Mac’s Tea Room</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            2241 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=venues&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Venues &amp; Event Spaces</a>,
                    <a href="https://www.yelp.com/search?cflt=comfortfood&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Comfort Food</a>
    </span>


    </div>


                        <ul class="search-result_tags">
            <li class="tag-18x18_menu-black">
                <small>
                    <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-menu icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_menu"></use>
    </svg>
</span>

                    On the menu: <span class="highlighted">Chicken</span> <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>
                </small>
                
            </li>
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Midtown, Old Fourth Ward        </span>

                <address>
        224 Ponce De Leon Ave<br>Atlanta, GA 30308
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 876-1800
    </span>

        </div>
    </div>

    
    
        <div class="search-result-ctas u-space-t1">
                    <div class="search-avatar-offset js-mtb">
        <div class="island island--slim search-result-cta">
            <div class="arrange arrange--middle arrange--6">
                <div class="arrange_unit">
            <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-fast-responder icon--size-18 icon--success">
    <svg class="icon_svg">
        <use xlink:href="#18x18_fast_responder"></use>
    </svg>
</span>
    </div>
    <div class="arrange_unit--fill arrange_unit cta-text">
        <span class="mtb-response-time-fast-responder">
            Responds in about <strong>1 hour</strong>
        </span>
    </div>


            

    <div class="arrange_unit nowrap js-tag-action" data-business-id="z9oCxeqOKp2QMfM24m7bUw" data-multibiz-large-modal="data-multibiz-large-modal" data-popup-title="" data-search-action-uri="/message_the_business/z9oCxeqOKp2QMfM24m7bUw/popup_form">
                <a href="https://www.yelp.com/message_the_business/z9oCxeqOKp2QMfM24m7bUw/popup_form" class="ybtn ybtn--small low-intent-search-action-button">Request a Quote</a>

    </div>

            </div>
        </div>
        <div class="search-result-cta-error-row">
            <div class="platform-vsearch-error-message text-error">
            </div>
        </div>
    </div>

        </div>

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="vBJVHWh9WCSXPTa7LD_lyA">
                <a href="https://www.yelp.com/user_details?userid=03I5PkJiXk2V0I3moiCVXA">
                <img alt="Monique V." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(3).jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/60s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/90s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        plate was absolutely delicious. My best friend ordered the chicken <span class="highlighted">fried</span> <span class="highlighted">chicken</span> with white gravy, macaroni and cheese, and stuffing. He passed out the second he got in the car on…
                        <a href="https://www.yelp.com/biz/mary-macs-tea-room-atlanta?hrid=5kdG0K0sd9HviUiQJpw7Dw&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="AvXqLbcGCxdIEF_qZTY0Kw" data-key="4" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/busy-bee-cafe-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Busy Bee Cafe" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(5).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/WHQS-YNUTb3wgz7YOSvACg/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">4.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/busy-bee-cafe-atlanta?osq=fried+chicken" data-hovercard-id="1gGFI10oK8oGAKx-nJwODQ"><span>Busy Bee Cafe</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            481 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=soulfood&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Soul Food</a>
    </span>


    </div>


                        <ul class="search-result_tags">
            <li class="tag-18x18_menu-black">
                <small>
                    <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-menu icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_menu"></use>
    </svg>
</span>

                    On the menu: <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>
                </small>
                
            </li>
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                    
                <address>
        810 Martin Luther King Jr Dr<br>Atlanta, GA 30314
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 525-9212
    </span>

        </div>
    </div>

    
    
        <div class="search-result-ctas u-space-t1">
                    <div class="search-avatar-offset js-search-join-cash-back">
        <div class="island island--slim search-result-cta">
            <div class="arrange arrange--middle arrange--6">
                <div class="arrange_unit">
            <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-cash-back icon--size-18 icon--success">
    <svg class="icon_svg">
        <use xlink:href="#18x18_cash_back"></use>
    </svg>
</span>
    </div>
    <div class="arrange_unit--fill arrange_unit cta-text">
        <span class="cash-back-cta-text">
            Get 7% Cash Back when you dine here
        </span>
    </div>


                <div class="arrange_unit nowrap js-tag-action" data-business-id="AvXqLbcGCxdIEF_qZTY0Kw" data-popup-title="" data-search-action-uri="/rewards/signup?biz_id=AvXqLbcGCxdIEF_qZTY0Kw">
        <a href="https://www.yelp.com/rewards/signup?biz_id=AvXqLbcGCxdIEF_qZTY0Kw" class="ybtn ybtn--small">Get Cash Back</a>
    </div>

            </div>
        </div>
        <div class="search-result-cta-error-row">
            <div class="platform-vsearch-error-message text-error">
            </div>
        </div>
    </div>

        </div>

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="jU_QlPBJ7SBwY-WN1sQS1w">
                <a href="https://www.yelp.com/user_details?userid=XLXAUM7ZzgW_VHDZc3bS3A">
                <img alt="Joe G." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(4).jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/9IF9v_0xqn6Fd8k9DSY-uA/60s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/photo/9IF9v_0xqn6Fd8k9DSY-uA/90s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/9IF9v_0xqn6Fd8k9DSY-uA/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        I tried the Atlanta staple BUSY BEE during their lunch hours. Busy bee known for their pressure cooked &amp; <span class="highlighted">fried</span> <span class="highlighted">chicken</span> for decades. Let me tell y'all.... POPEYES &amp; BUSY BEE serve the…
                        <a href="https://www.yelp.com/biz/busy-bee-cafe-atlanta?hrid=ySd1JJSVl1QDBnxWRx5fxg&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="5RGQiJcprXTmoA1rxSPVhw" data-key="5" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/richards-southern-fried-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Richards&#39; Southern Fried" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(6).jpg" srcset="https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/180s.jpg 2.00x,https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/ms.jpg 1.11x,https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/120s.jpg 1.33x,https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/168s.jpg 1.87x,https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/ls.jpg 2.78x,https://s3-media4.fl.yelpcdn.com/bphoto/2Ol7CF1mPiLaZfm-sGN9Hg/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">5.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/richards-southern-fried-atlanta?osq=fried+chicken" data-hovercard-id="jQmiUQVRqEaPmrSE6sZ0ww"><span>Richards’ Southern Fried</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            108 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=chicken_wings&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Chicken Wings</a>,
                    <a href="https://www.yelp.com/search?cflt=sandwiches&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Sandwiches</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Inman Park        </span>

                <address>
        99 Krog St NE<br>Atlanta, GA 30307
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (678) 732-9594
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="5WKeOcukh0yc8vbUgaHAaw">
                <a href="https://www.yelp.com/user_details?userid=jheopFKRPEDAR_ur5HGTug">
                <img alt="Kurtis K." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/user_30_square.png" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        The batter and spice of the <span class="highlighted">fried</span> <span class="highlighted">chicken</span> was a bit too oily and salty for my taste. The collard green pho wasn't too bad. The only thing is, there's no noodles in the pho. Pho…
                        <a href="https://www.yelp.com/biz/richards-southern-fried-atlanta?hrid=viCPygD2fwaOke0YirYtng&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="CsWRSsr2PsJ1WvHl0DFufA" data-key="6">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/greens-and-gravy-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Greens &amp; Gravy" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(7).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/Dijq-7DbtygO6ANMESQX9w/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">6.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/greens-and-gravy-atlanta?osq=fried+chicken" data-hovercard-id="ZpdS484nehrxJrerN2JDmQ"><span>Greens &amp; Gravy</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-3-half rating-large" title="3.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="3.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            93 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=soulfood&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Soul Food</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                    
                <address>
        1540 Ralph David Abernathy Blvd<br>Atlanta, GA 30310
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 565-2074
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="IDqab4-VJr3PpIW40zPc3Q">
                <a href="https://www.yelp.com/user_details?userid=Z5RzOoh247q6D7BseqYnWg">
                <img alt="Tammy J." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/user_30_square.png" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        pasta, the lemon pepper fried ribs, the lemon pepper honey <span class="highlighted">fried</span> <span class="highlighted">chicken</span>, the jerk prawns with sweet potato grits, the blackened shrimp deviled eggs, the salmon and the catfish and…
                        <a href="https://www.yelp.com/biz/greens-and-gravy-atlanta?hrid=Wf43xl3ZfyZP2l92hE-tFQ&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="-MV3DQZv9igVp11LERiPZQ" data-key="7">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/colonnade-restaurant-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Colonnade Restaurant" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(8).jpg" srcset="https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/180s.jpg 2.00x,https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/ms.jpg 1.11x,https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/120s.jpg 1.33x,https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/168s.jpg 1.87x,https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/ls.jpg 2.78x,https://s3-media4.fl.yelpcdn.com/bphoto/833dRnJU5M59U0y4J0dLQQ/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">7.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/colonnade-restaurant-atlanta?osq=fried+chicken" data-hovercard-id="oEs3s_rnobbLzWr57HlRPw"><span>Colonnade Restaurant</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            350 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=tradamerican&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">American (Traditional)</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Morningside / Lenox Park        </span>

                <address>
        1879 Cheshire Bridge Rd NE<br>Atlanta, GA 30324
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 874-5642
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="rkWxaznRHGzZv6YAzjfrFQ">
                <a href="https://www.yelp.com/user_details?userid=gtq1Gk7ooO0zxe3tB-3xGQ">
                <img alt="Peter S." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/user_30_square.png" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        We ate here for dinner tonight. Service was very attentive from the host to the waiter and to cashing out. My wife had the <span class="highlighted">fried</span> <span class="highlighted">chicken</span> which she shared with my 6 year old. The…
                        <a href="https://www.yelp.com/biz/colonnade-restaurant-atlanta?hrid=z9Y3egNnKMji2ZkFIIvzWQ&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="gMSCtM6SCUF-bp3Ypw8Jxg" data-key="8" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/south-city-kitchen-buckhead-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="South City Kitchen Buckhead" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(9).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/38QwMSBUL2FOEPG22eD_jA/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">8.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/south-city-kitchen-buckhead-atlanta?osq=fried+chicken" data-hovercard-id="pGwgPtANWAUmeQUwCxNEEg"><span>South City Kitchen Buckhead</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4-half rating-large" title="4.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            248 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=breakfast_brunch&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Breakfast &amp; Brunch</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Buckhead        </span>

                <address>
        3350 Peachtree Rd NE<br>Atlanta, GA 30326
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 815-6677
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="tb1mMTE0yOaMULv60IeKqQ">
                <a href="https://www.yelp.com/user_details?userid=_owCDBDyi17OOgSlaer_3g">
                <img alt="T. M." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(5).jpg" srcset="https://s3-media2.fl.yelpcdn.com/photo/HzzTo0QumRG1e-Gz15df5w/60s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/photo/HzzTo0QumRG1e-Gz15df5w/90s.jpg 3.00x,https://s3-media2.fl.yelpcdn.com/photo/HzzTo0QumRG1e-Gz15df5w/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        South City Kitchen is a breath of fresh air for upscale soul food. The <span class="highlighted">fried</span> <span class="highlighted">chicken</span>, collards, and red potatoes were simply amazing. We also had the scallop appetizer and brined…
                        <a href="https://www.yelp.com/biz/south-city-kitchen-buckhead-atlanta?hrid=8zwNAbKP7VH770z4UQ8Y1A&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="U-i6cq-yFRVJC4pIKSLX9Q" data-key="9" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/poor-calvins-atlanta-15?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Poor Calvin&#39;s" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(10).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/m9MKohMTWTtparXjeRit9A/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">9.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/poor-calvins-atlanta-15?osq=fried+chicken" data-hovercard-id="oAlbeMIqtt84f0IA2wIWNw"><span>Poor Calvin’s</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4-half rating-large" title="4.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            1558 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=asianfusion&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Asian Fusion</a>,
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=comfortfood&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Comfort Food</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Downtown        </span>

                <address>
        510 Piedmont Ave NE<br>Atlanta, GA 30308
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 254-4051
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="vBJVHWh9WCSXPTa7LD_lyA">
                <a href="https://www.yelp.com/user_details?userid=03I5PkJiXk2V0I3moiCVXA">
                <img alt="Monique V." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(3).jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/60s.jpg 2.00x,https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/90s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/N9NmIaNo6M9lVIZ5nokVBQ/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        something lite, but when I saw what all was on the menu that thought went out the window quick. I ended up getting the <span class="highlighted">fried</span> <span class="highlighted">chicken</span> with lobster macaroni and cheese and it came with…
                        <a href="https://www.yelp.com/biz/poor-calvins-atlanta-15?hrid=DM0oitT7xhYvM5IW5WtvYA&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="C0Jiti0T_VcXgNDKv0dCng" data-key="10">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/rocks-chicken-and-fries-atlanta?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Rock&#39;s Chicken &amp; Fries" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(11).jpg" srcset="https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/180s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/ms.jpg 1.11x,https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/120s.jpg 1.33x,https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/168s.jpg 1.87x,https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/ls.jpg 2.78x,https://s3-media2.fl.yelpcdn.com/bphoto/SUTUfC0wsfwA6VEgvV_Rww/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">10.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/rocks-chicken-and-fries-atlanta?osq=fried+chicken" data-hovercard-id="0ozMRzZBnIQHISOcWH3OmQ"><span>Rock’s Chicken &amp; Fries</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4 rating-large" title="4.0 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.0 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            67 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=tradamerican&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">American (Traditional)</a>,
                    <a href="https://www.yelp.com/search?cflt=icecream&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Ice Cream &amp; Frozen Yogurt</a>,
                    <a href="https://www.yelp.com/search?cflt=chickenshop&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Chicken Shop</a>
    </span>


    </div>


                        <ul class="search-result_tags">
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Buckhead        </span>

                <address>
        3500 Peachtree Rd<br>Atlanta, GA 30326
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 665-0176
    </span>

        </div>
    </div>

    
    

    

            <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="URiAfl4ykaZ3cPigbwGFPQ">
                <a href="https://www.yelp.com/user_details?userid=nwRKlJyFC8BkWwwrBG4gzA">
                <img alt="Sabri3l A." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(6).jpg" srcset="https://s3-media1.fl.yelpcdn.com/photo/qvvZr0VZ8Gj9t8TaWfW8ow/60s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/photo/qvvZr0VZ8Gj9t8TaWfW8ow/90s.jpg 3.00x,https://s3-media1.fl.yelpcdn.com/photo/qvvZr0VZ8Gj9t8TaWfW8ow/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        Came to the food court for lunch and had tried a sample of <span class="highlighted">fried</span> <span class="highlighted">chicken</span> from this place while trying to decide what to eat . As soon as i took a bite , that was it , all i wanted…
                        <a href="https://www.yelp.com/biz/rocks-chicken-and-fries-atlanta?hrid=2_zjzWofjCkKIAowtm1Iyw&amp;osq=fried+chicken" class="nowrap">read more</a>
                </p>
            </div>
        </div>



        
    </div>


                </li>
                <li class="js-yloca js-yloca-search yloca-search-result" data-ad-placement="below_search" data-ad-slot="0" data-unique-request-id="f2da9c903fcf056d" data-component-bound="true">
                        <div class="search-result" data-key="ad_business:below_organic:S8qrgwB7lktcArGx-BGoXg">
        <div class="biz-listing-large">
            <div class="main-attributes">
                <div class="media-block media-block--12">
                    <div class="media-avatar">
                                        <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/adredir?ad_business_id=uvh9z5jj8MC0um48vMJDYw&amp;campaign_id=ukL-WBzrgsy8jS0ga8j4Zw&amp;click_origin=search_results&amp;placement=below_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcopelands-atlanta-4&amp;request_id=f2da9c903fcf056d&amp;signature=3fe0c13d50b4dca83f14c00b62f83ec299ad9cb8cf72eb1e5e8003387538d8b5&amp;slot=0" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="Copeland&#39;s" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(12).jpg" srcset="https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/180s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/ms.jpg 1.11x,https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/120s.jpg 1.33x,https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/168s.jpg 1.87x,https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/ls.jpg 2.78x,https://s3-media2.fl.yelpcdn.com/bphoto/MJrEwAYX0N7uDKJrwmsorA/258s.jpg 2.87x" width="90">

        </a>

    </div>




                    </div>
                    <div class="media-story">
                            <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        <h3 class="search-result-title">
                                <span class="yloca-tip" data-hovercard-id="1">
        Ad
    </span>

                                                <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/adredir?ad_business_id=uvh9z5jj8MC0um48vMJDYw&amp;campaign_id=ukL-WBzrgsy8jS0ga8j4Zw&amp;click_origin=search_results&amp;placement=below_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcopelands-atlanta-4&amp;request_id=f2da9c903fcf056d&amp;signature=3fe0c13d50b4dca83f14c00b62f83ec299ad9cb8cf72eb1e5e8003387538d8b5&amp;slot=0" data-hovercard-id="gefrSH6YOpsEQIbfIwVYmA"><span>Copeland’s</span></a>



                        </h3>
                            <span class="js-track-imp u-absolute js-pixel-logged"></span>

                                    <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-3-half rating-large" title="3.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="3.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            288 reviews
    </span>

        </div>


                                <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=cajun&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Cajun/Creole</a>
    </span>


    </div>


                            <ul class="search-result_tags">
    </ul>

                    </div>
                </div>
            </div>
            <div class="secondary-attributes">
                    <span aria-hidden="true" data-hovercard-id="1" style="width: 18px; height: 18px;" class="icon icon--18-info icon--size-18 icon--currentColor yloca-info">
    <svg class="icon_svg">
        <use xlink:href="#18x18_info"></use>
    </svg>
</span>

                        
                <address>
        3101 Cobb Pkwy<br>Atlanta, GA 30339
    </address>


                
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (770) 612-3311
    </span>

            </div>
        </div>


                <div class="snippet-block media-block">
                <div class="media-avatar">
                        <div class="photo-box pb-30s" data-hovercard-id="cEgmZ3ZEoBGWUgYTD4HBqQ">
                <a href="https://www.yelp.com/adredir?ad_business_id=uvh9z5jj8MC0um48vMJDYw&amp;campaign_id=ukL-WBzrgsy8jS0ga8j4Zw&amp;click_origin=search_results&amp;placement=below_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcopelands-atlanta-4%3Fhrid%3Deb7GVuev1fVxrgxHxKUtgQ&amp;request_id=f2da9c903fcf056d&amp;signature=a2dd39124352c91eb9d4d8ef3b457d11cdf9d6f9bfc3cfe608c615c2c2a209f0&amp;slot=0">
                <img alt="Mary M." class="photo-box-img" height="30" src="./Best Fried chicken in Atlanta, GA - Yelp_files/30s(7).jpg" srcset="https://s3-media2.fl.yelpcdn.com/photo/StdXCfcNu2nYLV2Z0flW4Q/60s.jpg 2.00x,https://s3-media2.fl.yelpcdn.com/photo/StdXCfcNu2nYLV2Z0flW4Q/90s.jpg 3.00x,https://s3-media2.fl.yelpcdn.com/photo/StdXCfcNu2nYLV2Z0flW4Q/ss.jpg 1.33x" width="30">

        </a>

    </div>

                </div>
            <div class="media-story">
                <p class="snippet">
                        This review is only based on their brunch. I've been here twice for brunch on Sunday. First, they have $3 mimosas. Okay.. now, on Sunday the wait is EXTENSIVE as ever. The first time…
                        <a href="https://www.yelp.com/adredir?ad_business_id=uvh9z5jj8MC0um48vMJDYw&amp;campaign_id=ukL-WBzrgsy8jS0ga8j4Zw&amp;click_origin=read_more&amp;placement=below_search&amp;redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcopelands-atlanta-4%3Fhrid%3Deb7GVuev1fVxrgxHxKUtgQ&amp;request_id=f2da9c903fcf056d&amp;signature=a2dd39124352c91eb9d4d8ef3b457d11cdf9d6f9bfc3cfe608c615c2c2a209f0&amp;slot=0" class="nowrap">read more</a>
                </p>
            </div>
        </div>

    </div>

                </li>
    </ul>



            <img class="offscreen" src="./Best Fried chicken in Atlanta, GA - Yelp_files/px.gif">
    <img class="offscreen" src="./Best Fried chicken in Atlanta, GA - Yelp_files/px(1).gif">


        <div class="search-pagination">
            
        <div class="pagination-block">
            <div class="arrange arrange--stack arrange--baseline arrange--6">
                    <div class="page-of-pages arrange_unit arrange_unit--fill">
        Page 1 of 100
    </div>

                        <div class="pagination-links arrange_unit">
        <div class="arrange arrange--baseline">

                    <div class="arrange_unit page-option current">
                        <span class="pagination-links_anchor">1</span>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=10">
                            2
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=20">
                            3
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=30">
                            4
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=40">
                            5
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=50">
                            6
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=60">
                            7
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=70">
                            8
                        </a>
                    </div>
                    <div class="arrange_unit page-option">
                        <a class="available-number pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=80">
                            9
                        </a>
                    </div>

                <div class="arrange_unit">
                    <a class="u-decoration-none next pagination-links_anchor" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;start=10">
                        <span class="pagination-label responsive-hidden-small pagination-links_anchor">Next</span>
                        <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-chevron-right icon--size-24 icon--currentColor">
    <svg class="icon_svg">
        <use xlink:href="#24x24_chevron_right"></use>
    </svg>
</span>
                    </a>
                </div>
        </div>
    </div>

            </div>
        </div>

        </div>
        
                <div class="related-search-links u-space-t2">
            <h3>Related Searches in Atlanta</h3>
            <ul class="arrange arrange--12 arrange--wrap arrange--2-units">
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=chicken+tenders&amp;find_loc=Atlanta%2C+GA">Chicken tenders</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=churches+fried+chicken&amp;find_loc=Atlanta%2C+GA">Churches fried chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=country+fried+chicken&amp;find_loc=Atlanta%2C+GA">Country fried chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=fried+chicken+and+donuts&amp;find_loc=Atlanta%2C+GA">Fried chicken and donuts</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=fried+chicken+livers&amp;find_loc=Atlanta%2C+GA">Fried chicken livers</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=fried+chicken+wings&amp;find_loc=Atlanta%2C+GA">Fried chicken wings</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=harolds+fried+chicken&amp;find_loc=Atlanta%2C+GA">Harolds fried chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=nashville+hot+chicken&amp;find_loc=Atlanta%2C+GA">Nashville hot chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=popeye+fried+chicken&amp;find_loc=Atlanta%2C+GA">Popeye fried chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=roscoe+chicken+and+waffle&amp;find_loc=Atlanta%2C+GA">Roscoe chicken and waffle</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=southern+cooking&amp;find_loc=Atlanta%2C+GA">Southern cooking</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=southern+fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern fried chicken</a></li>
                    <li class="arrange_unit"><a href="https://www.yelp.com/search?find_desc=spicy+fried+chicken&amp;find_loc=Atlanta%2C+GA">Spicy fried chicken</a></li>
            </ul>
        </div>

        

        </div>
    <div class="throbber-overlay" style="display: none;"><div class="throbber-container"></div></div></div>

    </div>

    <div class="column column-beta ">
            <div class="map-wrapper" style="position: relative; zoom: 1; z-index: auto;">
                <div class="search-map transform-style-support" data-component-bound="true">
                        <div class="map-header clearfix">
        <a href="javascript:;" class="mo-map-trigger">
            <span aria-hidden="true" style="width: 24px; height: 24px;" class="icon icon--24-chevron-left icon--size-24 mo-map-icon">
    <svg class="icon_svg">
        <use xlink:href="#24x24_chevron_left"></use>
    </svg>
</span><span class="js-mo-map-label">Mo' Map</span>
        </a>

        <div class="cube-wrapper">
            <div class="cube show-face1">
                <div class="face face1">
                    <label>
                        <input class="js-redo-search-checkbox" type="checkbox">
                        Redo search when map moved
                    </label>
                </div>
                <div class="face face2">
                    <a class="ybtn ybtn--primary ybtn--small redo-search">Redo Search in Map</a>
                </div>
            </div>
        </div>
    </div>

                    <div id="map-container" class="yelp-map-container" data-component-bound="true">
                        <div class="engine-container" style="background-color: rgb(229, 227, 223); position: relative; overflow: hidden;" data-component-bound="true"><div style="height: 100%; width: 100%; position: absolute; top: 0px; left: 0px; background-color: rgb(229, 227, 223);"><div class="gm-style" style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px;"><div tabindex="0" style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; cursor: url(&quot;https://maps.gstatic.com/mapfiles/openhand_8_8.cur&quot;) 8 8, default;"><div style="z-index: 1; position: absolute; top: 0px; left: 0px; width: 100%; transform-origin: 0px 0px 0px; transform: matrix(1, 0, 0, 1, 0, 0);"><div style="position: absolute; left: 0px; top: 0px; z-index: 100; width: 100%;"><div style="position: absolute; left: 0px; top: 0px; z-index: 0;"><div aria-hidden="true" style="position: absolute; left: 0px; top: 0px; z-index: 1; visibility: inherit;"><div style="width: 256px; height: 256px; position: absolute; left: -107px; top: -28px;"></div><div style="width: 256px; height: 256px; position: absolute; left: -107px; top: 228px;"></div><div style="width: 256px; height: 256px; position: absolute; left: 149px; top: -28px;"></div><div style="width: 256px; height: 256px; position: absolute; left: 149px; top: 228px;"></div></div></div></div><div style="position: absolute; left: 0px; top: 0px; z-index: 101; width: 100%;"></div><div style="position: absolute; left: 0px; top: 0px; z-index: 102; width: 100%;"></div><div style="position: absolute; left: 0px; top: 0px; z-index: 103; width: 100%;"><div style="position: absolute; left: 0px; top: 0px; z-index: -1;"><div aria-hidden="true" style="position: absolute; left: 0px; top: 0px; z-index: 1; visibility: inherit;"><div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -107px; top: -28px;"></div><div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -107px; top: 228px;"></div><div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 149px; top: -28px;"></div><div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 149px; top: 228px;"></div></div></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 129px; top: 165px; z-index: 1000007;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E1%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 130px; top: 142px; z-index: 1000006;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 133px; top: 154px; z-index: 1000005;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 109px; top: 170px; z-index: 1000004;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E4%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 145px; top: 168px; z-index: 1000003;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E5%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 91px; top: 179px; z-index: 999994;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E6%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 147px; top: 122px; z-index: 999993;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E7%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 142px; top: 88px; z-index: 1000002;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E8%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 132px; top: 157px; z-index: 1000001;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E9%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 146px; top: 83px; z-index: 999990;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E10%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 78px; top: 60px; z-index: 1;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 249px; top: 161px; z-index: 2000000;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div style="width: 26px; height: 36px; overflow: hidden; position: absolute; left: 260px; top: 129px; z-index: 1;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div></div><div style="position: absolute; z-index: 0; left: 0px; top: 0px;"><div style="overflow: hidden;"></div></div><div style="position: absolute; left: 0px; top: 0px; z-index: 0;"><div aria-hidden="true" style="position: absolute; left: 0px; top: 0px; z-index: 1; visibility: inherit;"><div style="position: absolute; left: -107px; top: -28px; transition: opacity 200ms ease-out;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/vt" draggable="false" alt="" style="width: 256px; height: 256px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="position: absolute; left: -107px; top: 228px; transition: opacity 200ms ease-out;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/vt(1)" draggable="false" alt="" style="width: 256px; height: 256px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="position: absolute; left: 149px; top: 228px; transition: opacity 200ms ease-out;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/vt(2)" draggable="false" alt="" style="width: 256px; height: 256px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div style="position: absolute; left: 149px; top: -28px; transition: opacity 200ms ease-out;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/vt(3)" draggable="false" alt="" style="width: 256px; height: 256px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div></div></div></div><div class="gm-style-pbc" style="z-index: 2; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px; opacity: 0;"><p class="gm-style-pbt"></p></div><div style="z-index: 3; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px;"><div style="z-index: 1; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px;"></div></div><div style="z-index: 4; position: absolute; top: 0px; left: 0px; width: 100%; transform-origin: 0px 0px 0px; transform: matrix(1, 0, 0, 1, 0, 0);"><div style="position: absolute; left: 0px; top: 0px; z-index: 104; width: 100%;"></div><div style="position: absolute; left: 0px; top: 0px; z-index: 105; width: 100%;"></div><div style="position: absolute; left: 0px; top: 0px; z-index: 106; width: 100%;"><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 129px; top: 165px; z-index: 1000007;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E1%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 130px; top: 142px; z-index: 1000006;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 133px; top: 154px; z-index: 1000005;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 109px; top: 170px; z-index: 1000004;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E4%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 145px; top: 168px; z-index: 1000003;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E5%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 91px; top: 179px; z-index: 999994;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E6%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 147px; top: 122px; z-index: 999993;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E7%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 142px; top: 88px; z-index: 1000002;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E8%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 132px; top: 157px; z-index: 1000001;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E9%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 146px; top: 83px; z-index: 999990;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23D32323%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%238D0005%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Ctext%20x%3D%2218%22%20y%3D%2222%22%20font-family%3D%22Helvetica%2CArial%2Csans-serif%22%20font-size%3D%2216%22%20fill%3D%22%23FFF%22%20text-anchor%3D%22middle%22%3E10%3C%2Ftext%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 78px; top: 60px; z-index: 1;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 249px; top: 161px; z-index: 2000000;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none; opacity: 1;"></div><div class="gmnoprint" title="" style="width: 26px; height: 36px; overflow: hidden; position: absolute; opacity: 0.01; cursor: pointer; left: 260px; top: 129px; z-index: 1;"><img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%225%20-2%2027%2036%22%20width%3D%2226%22%20height%3D%2236%22%3E%3Cpath%20fill%3D%22%23EDAD0D%22%20d%3D%22M26%2C7.64A11.25%2C11.25%2C0%2C0%2C0%2C10%2C23.56L18%2C31.5l8.27-8.27A11.24%2C11.24%2C0%2C0%2C0%2C26%2C7.64Z%22%2F%3E%3Cpath%20fill%3D%22%23d29a0e%22%20d%3D%22M18%2C32.21%2C9.69%2C23.91A11.75%2C11.75%2C0%2C1%2C1%2C26.31%2C7.29h0a11.71%2C11.71%2C0%2C0%2C1%2C.31%2C16.28ZM18%2C4.85a10.75%2C10.75%2C0%2C0%2C0-7.6%2C18.36L18%2C30.79l7.92-7.92A10.71%2C10.71%2C0%2C0%2C0%2C25.61%2C8h0A10.68%2C10.68%2C0%2C0%2C0%2C18%2C4.85Z%22%2F%3E%3Cpath%20fill%3D%22%23FFF%22%20d%3D%22M13.6208%2022.404l4.3384-13.376%204.3384%2013.376-11.3696-8.272h14.08%22%2F%3E%3C%2Fsvg%3E" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; width: 26px; height: 36px; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div></div><div style="position: absolute; left: 0px; top: 0px; z-index: 107; width: 100%;"></div></div></div><div style="margin-left: 5px; margin-right: 5px; z-index: 1000000; position: absolute; left: 0px; bottom: 0px;"><a target="_blank" href="https://maps.google.com/maps?ll=33.813213,-84.373627&amp;z=10&amp;t=m&amp;hl=en&amp;gl=US&amp;mapclient=apiv3" title="Click to see this area on Google Maps" style="position: static; overflow: visible; float: none; display: inline;"><div style="width: 66px; height: 26px; cursor: pointer;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/google_white5.png" draggable="false" style="position: absolute; left: 0px; top: 0px; width: 66px; height: 26px; user-select: none; border: 0px; padding: 0px; margin: 0px;"></div></a></div><div style="background-color: white; padding: 15px 21px; border: 1px solid rgb(171, 171, 171); font-family: Roboto, Arial, sans-serif; color: rgb(34, 34, 34); box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 16px; z-index: 10000002; display: none; width: 246px; height: 148px; position: absolute; left: 5px; top: 60px;"><div style="padding: 0px 0px 10px; font-size: 16px;">Map Data</div><div style="font-size: 13px;">Map data ©2017 Google</div><div style="width: 13px; height: 13px; overflow: hidden; position: absolute; opacity: 0.7; right: 12px; top: 12px; z-index: 10000; cursor: pointer;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/mapcnt6.png" draggable="false" style="position: absolute; left: -2px; top: -336px; width: 59px; height: 492px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div></div><div class="gmnoprint" style="z-index: 1000001; position: absolute; right: 166px; bottom: 0px; width: 121px;"><div draggable="false" class="gm-style-cc" style="user-select: none; height: 14px; line-height: 14px;"><div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;"><div style="width: 1px;"></div><div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div></div><div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a style="color: rgb(68, 68, 68); text-decoration: none; cursor: pointer; display: none;">Map Data</a><span>Map data ©2017 Google</span></div></div></div><div class="gmnoscreen" style="position: absolute; right: 0px; bottom: 0px;"><div style="font-family: Roboto, Arial, sans-serif; font-size: 11px; color: rgb(68, 68, 68); direction: ltr; text-align: right; background-color: rgb(245, 245, 245);">Map data ©2017 Google</div></div><div class="gmnoprint gm-style-cc" draggable="false" style="z-index: 1000001; user-select: none; height: 14px; line-height: 14px; position: absolute; right: 95px; bottom: 0px;"><div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;"><div style="width: 1px;"></div><div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div></div><div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a href="https://www.google.com/intl/en_US/help/terms_maps.html" target="_blank" style="text-decoration: none; cursor: pointer; color: rgb(68, 68, 68);">Terms of Use</a></div></div><div style="cursor: pointer; width: 25px; height: 25px; overflow: hidden; display: none; margin: 10px 14px; position: absolute; top: 0px; right: 0px;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/sv9.png" draggable="false" class="gm-fullscreen-control" style="position: absolute; left: -52px; top: -86px; width: 164px; height: 175px; user-select: none; border: 0px; padding: 0px; margin: 0px;"></div><div draggable="false" class="gm-style-cc" style="user-select: none; height: 14px; line-height: 14px; position: absolute; right: 0px; bottom: 0px;"><div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;"><div style="width: 1px;"></div><div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div></div><div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a target="_new" title="Report errors in the road map or imagery to Google" href="https://www.google.com/maps/@33.8132131,-84.3736267,10z/data=!10m1!1e1!12b1?source=apiv3&amp;rapsrc=apiv3" style="font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); text-decoration: none; position: relative;">Report a map error</a></div></div><div class="gmnoprint gm-bundled-control" draggable="false" controlwidth="28" controlheight="55" style="margin: 10px; user-select: none; position: absolute; left: 0px; top: 0px;"><div class="gmnoprint" controlwidth="28" controlheight="55" style="position: absolute; left: 0px; top: 0px;"><div draggable="false" style="user-select: none; box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 4px -1px; border-radius: 2px; cursor: pointer; background-color: rgb(255, 255, 255); width: 28px; height: 55px;"><div title="Zoom in" aria-label="Zoom in" tabindex="0" style="position: relative; width: 28px; height: 27px; left: 0px; top: 0px;"><div style="overflow: hidden; position: absolute; width: 15px; height: 15px; left: 7px; top: 6px;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/tmapctrl.png" draggable="false" style="position: absolute; left: 0px; top: 0px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 120px; height: 54px;"></div></div><div style="position: relative; overflow: hidden; width: 67%; height: 1px; left: 16%; background-color: rgb(230, 230, 230); top: 0px;"></div><div title="Zoom out" aria-label="Zoom out" tabindex="0" style="position: relative; width: 28px; height: 27px; left: 0px; top: 0px;"><div style="overflow: hidden; position: absolute; width: 15px; height: 15px; left: 7px; top: 6px;"><img src="./Best Fried chicken in Atlanta, GA - Yelp_files/tmapctrl.png" draggable="false" style="position: absolute; left: 0px; top: -15px; user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 120px; height: 54px;"></div></div></div></div></div></div></div></div>
                    </div>
                </div>
                <div class="right-rail-yla-wrapper" data-component-bound="true">
                </div>
                <div class="adsense-wrapper" data-component-bound="true">
                    <div class="adsense adsense-enabled" id="search-adsense" style="width: 100%; font-weight: normal; text-align: center; height: 194px;"><iframe frameborder="0" marginwidth="0" marginheight="0" allowtransparency="true" scrolling="no" width="100%" name="{&quot;name&quot;:&quot;master-1&quot;,&quot;master-1&quot;:{&quot;container&quot;:&quot;search-adsense&quot;,&quot;linkTarget&quot;:&quot;_top&quot;,&quot;lines&quot;:3,&quot;colorText&quot;:&quot;#555555&quot;,&quot;colorTitleLink&quot;:&quot;#3b65a7&quot;,&quot;colorDomainLink&quot;:&quot;#999999&quot;,&quot;noTitleUnderline&quot;:true,&quot;adIconLocation&quot;:&quot;ad-left&quot;,&quot;width&quot;:&quot;auto&quot;,&quot;detailedAttribution&quot;:true,&quot;type&quot;:&quot;ads&quot;,&quot;hl&quot;:&quot;en&quot;,&quot;columns&quot;:1,&quot;horizontalAlignment&quot;:&quot;left&quot;,&quot;resultsPageQueryParam&quot;:&quot;query&quot;}}" id="master-1" src="./Best Fried chicken in Atlanta, GA - Yelp_files/ads.html" style="visibility: visible; height: 194px;"></iframe></div>
                </div>
            </div>
    </div>
    </div>

    <div class="clearfix layout-block layout-a search-footer-block">
    <div class="column column-alpha ">
            <div class="talk-list-container" data-component-bound="true">
                        <div class="column-borders">
        <div class="column">
            
        <div class="ysection clearfix related-talk">
            <h3>Related Talk Topics</h3>
            <ul class="ylist">
                    <li>
                            <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/topic/smyrna-fried-chicken-hot-fried-chicken-chicken-shacks">
                <img alt="Subash Chandra B." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s.jpg" srcset="https://s3-media2.fl.yelpcdn.com/photo/foYXWLcHIYqJn6EhIpcn_A/90s.jpg 1.50x,https://s3-media2.fl.yelpcdn.com/photo/foYXWLcHIYqJn6EhIpcn_A/168s.jpg 2.80x,https://s3-media2.fl.yelpcdn.com/photo/foYXWLcHIYqJn6EhIpcn_A/ms.jpg 1.67x,https://s3-media2.fl.yelpcdn.com/photo/foYXWLcHIYqJn6EhIpcn_A/180s.jpg 3.00x,https://s3-media2.fl.yelpcdn.com/photo/foYXWLcHIYqJn6EhIpcn_A/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title clearfix">
                    <a href="https://www.yelp.com/topic/smyrna-fried-chicken-hot-fried-chicken-chicken-shacks">
        Fried chicken/hot fried chicken/chicken shacks
    </a>

            </div>
            I know this thread has been done talking about best fried chicken but I'm looking for good buttermilk, crispy, fried chicken. &nbsp;I already eat Popeyes…
        </div>
    </div>

                    </li>
                    <li>
                            <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/topic/atlanta-fried-chicken">
                <img alt="Kozmo C." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s(1).jpg" srcset="https://s3-media4.fl.yelpcdn.com/photo/MgbmW9Yc5vgwmDvPOhHPew/90s.jpg 1.50x,https://s3-media4.fl.yelpcdn.com/photo/MgbmW9Yc5vgwmDvPOhHPew/168s.jpg 2.80x,https://s3-media4.fl.yelpcdn.com/photo/MgbmW9Yc5vgwmDvPOhHPew/ms.jpg 1.67x,https://s3-media4.fl.yelpcdn.com/photo/MgbmW9Yc5vgwmDvPOhHPew/180s.jpg 3.00x,https://s3-media4.fl.yelpcdn.com/photo/MgbmW9Yc5vgwmDvPOhHPew/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title clearfix">
                    <a href="https://www.yelp.com/topic/atlanta-fried-chicken">
        Fried Chicken
    </a>

            </div>
            I need to know about more good fried chicken places that are of the "shack" sort. &nbsp; &nbsp;It seems like almost all the renowned fried chicken places are…
        </div>
    </div>

                    </li>
                    <li>
                            <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/topic/duluth-fried-chicken-dinner">
                <img alt="Jan K." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s(2).jpg" srcset="https://s3-media3.fl.yelpcdn.com/photo/1TZllZqXH5KgVGb0VwP1xw/90s.jpg 1.50x,https://s3-media3.fl.yelpcdn.com/photo/1TZllZqXH5KgVGb0VwP1xw/168s.jpg 2.80x,https://s3-media3.fl.yelpcdn.com/photo/1TZllZqXH5KgVGb0VwP1xw/ms.jpg 1.67x,https://s3-media3.fl.yelpcdn.com/photo/1TZllZqXH5KgVGb0VwP1xw/180s.jpg 3.00x,https://s3-media3.fl.yelpcdn.com/photo/1TZllZqXH5KgVGb0VwP1xw/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title clearfix">
                    <a href="https://www.yelp.com/topic/duluth-fried-chicken-dinner">
        fried Chicken Dinner
    </a>

            </div>
            Just picked up a fried chicken dinner at Publix at Tree Summit in duluth. Their chicken is delicious as is all publix fried chicken. Also got a fruit…
        </div>
    </div>

                    </li>
            </ul>
            <a class="link-more" href="https://www.yelp.com/message_board_search">More Topics</a>
        </div>

        </div>
        <div class="column">
                    <h3>Related Lists</h3>
            <ul class="ylist favorites-list">
            <li>
                    <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/list/c9jQ3qwb717OjT9yUNx0Mg">
                <img alt="Debby L." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s(3).jpg" srcset="https://s3-media2.fl.yelpcdn.com/photo/syeJH5b4K8OB1Re02eGyBA/90s.jpg 1.50x,https://s3-media2.fl.yelpcdn.com/photo/syeJH5b4K8OB1Re02eGyBA/168s.jpg 2.80x,https://s3-media2.fl.yelpcdn.com/photo/syeJH5b4K8OB1Re02eGyBA/ms.jpg 1.67x,https://s3-media2.fl.yelpcdn.com/photo/syeJH5b4K8OB1Re02eGyBA/180s.jpg 3.00x,https://s3-media2.fl.yelpcdn.com/photo/syeJH5b4K8OB1Re02eGyBA/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title">
                    <a href="https://www.yelp.com/list/c9jQ3qwb717OjT9yUNx0Mg">
        ATL - FRIED CHICKEN
    </a>

            </div>
        </div>
    </div>

            </li>
            <li>
                    <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/list/r0XAXANX6k23pFTLAHvAQQ">
                <img alt="Sara M." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s(4).jpg" srcset="https://s3-media1.fl.yelpcdn.com/photo/sU5dp95aiT3qO0yaTZzpzw/90s.jpg 1.50x,https://s3-media1.fl.yelpcdn.com/photo/sU5dp95aiT3qO0yaTZzpzw/168s.jpg 2.80x,https://s3-media1.fl.yelpcdn.com/photo/sU5dp95aiT3qO0yaTZzpzw/ms.jpg 1.67x,https://s3-media1.fl.yelpcdn.com/photo/sU5dp95aiT3qO0yaTZzpzw/180s.jpg 3.00x,https://s3-media1.fl.yelpcdn.com/photo/sU5dp95aiT3qO0yaTZzpzw/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title">
                    <a href="https://www.yelp.com/list/r0XAXANX6k23pFTLAHvAQQ">
        Chicken of the Fried Variety
    </a>

            </div>
                <span class="list-description">
                    My arteries are crying for mercy but how can I resist that crispy, suc…
                </span>
        </div>
    </div>

            </li>
            <li>
                    <div class="media-block media-block--12">
        <div class="media-avatar">
                    <div class="photo-box pb-60s">
                <a href="https://www.yelp.com/list/trUNJV_D97Xzk3gWuHGWyw">
                <img alt="Miriam W." class="photo-box-img" height="60" src="./Best Fried chicken in Atlanta, GA - Yelp_files/60s(5).jpg" srcset="https://s3-media2.fl.yelpcdn.com/photo/_YxmKOqCuvB2eHyUMMJWcA/90s.jpg 1.50x,https://s3-media2.fl.yelpcdn.com/photo/_YxmKOqCuvB2eHyUMMJWcA/168s.jpg 2.80x,https://s3-media2.fl.yelpcdn.com/photo/_YxmKOqCuvB2eHyUMMJWcA/ms.jpg 1.67x,https://s3-media2.fl.yelpcdn.com/photo/_YxmKOqCuvB2eHyUMMJWcA/180s.jpg 3.00x,https://s3-media2.fl.yelpcdn.com/photo/_YxmKOqCuvB2eHyUMMJWcA/120s.jpg 2.00x" width="60">

        </a>

    </div>


        </div>
        <div class="media-story">
            <div class="media-title">
                    <a href="https://www.yelp.com/list/trUNJV_D97Xzk3gWuHGWyw">
        The Best Fried Chicken in Atlanta
    </a>

            </div>
                <span class="list-description">
                    And my continuing quest to find it!
                </span>
        </div>
    </div>

            </li>
    </ul>
    <a class="link-more link-more-favorites" href="https://www.yelp.com/list_search?location=Atlanta%2C+GA&amp;q=fried+chicken&amp;sort=relevance">More Lists</a>


        </div>
        </div>

            </div>
    </div>
    <div class="column column-beta js-search-feedback-container" data-component-bound="true">
            



    <div class="search-feedback-box island">
        <div class="feedback-biz-suggest">
            <div class="text-container">
                <h3>Not here? Tell us what we're missing.</h3>
                <p>If the business you're looking for isn't here, add it!</p>
            </div>
            <a href="https://www.yelp.com/search/add_business/search_button_www?search_loc=Atlanta%2C+GA" class="ybtn ybtn--primary ybtn--small js-show-add-biz-modal">Add A Business</a>
        </div>
        <div class="feedback-contact">
            Got search feedback? <a href="https://www.yelp.com/contact?topic=feedback" class="search-feedback" data-component-bound="true">Help us improve.</a>
        </div>

                <div class="js-add-biz-modal-content u-hidden">
    <div class="modal_head">
            <h2>Add a Business</h2>
    </div>
    <div class="modal_body">
            <p>Are you a customer or the owner/manager of the business you’d like to add?</p>
            <a href="https://www.yelp.com/search/add_business/modal_button_www?search_loc=Atlanta%2C+GA" class="ybtn ybtn-full js-add-biz-as-customer">I am a customer</a>
            <a href="https://www.yelp.com/search/add_business/modal_button_biz" class="ybtn ybtn-full u-space-l0 u-space-t2 js-add-biz-as-owner">This is my business</a>
    </div>
    </div>

    </div>

    </div>
    </div>

        <script>
            (function() {
                var main = null;

                var main=function(){(function(b,h,f,c,a,d){b[c]=b[c]||function(){(b[c]["q"]=b[c]["q"]||[]).push(arguments)},b[c]["t"]=1*new Date();a=h.createElement(f),d=h.getElementsByTagName(f)[0];a.async=1;a.src="//www.google.com/adsense/search/async-ads.js";d.parentNode.insertBefore(a,d)})(window,document,"script","_googCsa")};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script>

    

    

        <script>
            (function() {
                var main = null;

                var main=function(a){adroll_adv_id="BHPKS4B4ONEJJMGH4QCJZR";adroll_pix_id="QB5JPFIKRZDSBOZSULG4YB";adroll_user_identifier=a.yuv;adroll_email=a.hashed_email;(function(){var b=function(){if(document.readyState&&!/loaded|complete/.test(document.readyState)){setTimeout(b,10);return}if(!window.__adroll_loaded){__adroll_loaded=true;setTimeout(b,50);return}var d=document.createElement("script");var c="https://s.adroll.com";d.setAttribute("async","true");d.type="text/javascript";d.src=c+"/j/roundtrip.js";
((document.getElementsByTagName("head")||[null])[0]||document.getElementsByTagName("script")[0].parentNode).appendChild(d)};if(window.addEventListener){window.addEventListener("load",b,false)}else{window.attachEvent("onload",b)}}());adroll_custom_data=a.custom_data};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main({"custom_data": {"city": "Atlanta", "state": "GA", "category_aliases": "chickenshop,soulfood", "chain": null, "latitude": 33.813029, "city_state": "Atlanta, GA", "longitude": -84.3730549, "geoquad": null}, "hashed_email": null, "yuv": "9BF44709B38A0F50"});
            })();
    </script>

    <script>
            (function() {
                var main = null;

                var main=function(){!function(h,a,i,c,j,d,g){if(h.fbq){return}j=h.fbq=function(){j.callMethod?j.callMethod.apply(j,arguments):j.queue.push(arguments)};if(!h._fbq){h._fbq=j}j.push=j;j.loaded=!0;j.version="2.0";j.queue=[];d=a.createElement(i);d.async=!0;d.src=c;g=a.getElementsByTagName(i)[0];g.parentNode.insertBefore(d,g)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","102029836881428");fbq("track","PageView")};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script>



    </div>


    
                    </div>
                </div>



                    <!-- google_ad_section_start(weight=ignore) -->
<!-- <a href="/biz/outlook-autumn-market-fundamental-catwalk-flimsy-roost-legibility-individualism-grocer-predestination-8">yelp</a> -->
    <div class="main-content-wrap main-content-wrap--separated">
        <div class="content-container">
            <div class="main-footer webview-hidden">
    <div class="main-footer_section main-footer_menu arrange arrange--equal arrange--30 arrange--stack-small u-sm-space-b0">
                    <div class="main-footer_item responsive-hidden-small">
            <div class="footer-menu responsive-hidden-small">
        <h3 class="footer-menu_header">About</h3>
        <ul class="footer-menu_list">
                <li class="footer-menu_item">
                    <a href="https://yelp.com/about">About Yelp</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://eat24hours.com/">Order Food on Eat24</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/careers/home">Careers</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/press">Press</a>
                </li>
                <li class="footer-menu_item">
                    <a href="http://yelp-ir.com/">Investor Relations</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/guidelines">Content Guidelines</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/static?p=tos">Terms of Service</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/tos/privacy_policy">Privacy Policy</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/static?locale=en_US&amp;p=privacy#third-parties">Ad Choices</a>
                </li>
        </ul>
    </div>

    </div>

                    <div class="main-footer_item responsive-hidden-small">
            <div class="footer-menu responsive-hidden-small">
        <h3 class="footer-menu_header">Discover</h3>
        <ul class="footer-menu_list">
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/local_yelp">The Local Yelp</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://officialblog.yelp.com/">Yelp Blog</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp-support.com/?l=en_US">Support</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/yelpmobile?source=footer">Yelp Mobile</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/developers?country=US">Developers</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/rss">RSS</a>
                </li>
        </ul>
    </div>

    </div>

                    <div class="main-footer_item responsive-hidden-small">
            <div class="footer-menu responsive-hidden-small">
        <h3 class="footer-menu_header">Yelp for Business Owners</h3>
        <ul class="footer-menu_list">
                <li class="footer-menu_item">
                    <a href="https://biz.yelp.com/?utm_campaign=claim_business&amp;utm_content=claim_footer_link&amp;utm_medium=www&amp;utm_source=footer">Claim your Business Page</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp.com/advertise">Advertise on Yelp</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://eat24hours.com/join">Online Ordering from Eat24</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelpreservations.com/">Yelp Reservations</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://biz.yelp.com/support/case_studies">Business Success Stories</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelp-support.com/Yelp_for_Business_Owners?l=en_US">Business Support</a>
                </li>
                <li class="footer-menu_item">
                    <a href="https://www.yelpblog.com/section/business">Yelp Blog for Business Owners</a>
                </li>
        </ul>
    </div>

    </div>

                    <div class="main-footer_item">
        <div class="footer-menu languages-menu">
            <div class="footer-menu_section footer-language">
                <h3 class="footer-menu_header responsive-hidden-small">Languages</h3>
                

    <div class="dropdown js-dropdown dropdown--hover dropdown--boxed-on-mobile dropdown--separate-groups dropdown--restricted">
        

    <div class="dropdown_toggle js-dropdown-toggle" aria-haspopup="true" role="button" tabindex="-1">
        <a class="dropdown_toggle-action" href="javascript:;" data-dropdown-prefix="English">
            <span class="dropdown_toggle-text js-dropdown-toggle-text" data-dropdown-initial-text=""></span>
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down dropdown_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
        </a>
    </div>

            <div class="dropdown_menu-container js-dropdown_menu-container">
        <div class="dropdown_menu js-dropdown-menu">
            <div class="dropdown_menu-inner">
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=ms_MY&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Bahasa Malaysia (Malaysia)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=cs_CZ&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Čeština (Česká republika)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=da_DK&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Dansk (Danmark)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=de_DE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Deutsch (Deutschland)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=de_CH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Deutsch (Schweiz)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=de_AT&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Deutsch (Österreich)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_AU&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Australia)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_BE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Belgium)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_CA&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Canada)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_HK&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Hong Kong)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_MY&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Malaysia)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_NZ&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (New Zealand)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_PH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Philippines)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_IE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Republic of Ireland)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_SG&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Singapore)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_CH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (Switzerland)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_GB&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (United Kingdom)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=en_US&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                English (United States)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=es_AR&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Español (Argentina)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=es_CL&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Español (Chile)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=es_ES&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Español (España)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=es_MX&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Español (México)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fil_PH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Filipino (Pilipinas)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fr_BE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Français (Belgique)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fr_CA&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Français (Canada)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fr_FR&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Français (France)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fr_CH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Français (Suisse)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=it_IT&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Italiano (Italia)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=it_CH&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Italiano (Svizzera)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=nl_BE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Nederlands (België)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=nl_NL&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Nederlands (Nederland)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=nb_NO&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Norsk (Norge)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=pl_PL&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Polski (Polska)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=pt_BR&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Português (Brasil)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=pt_PT&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Português (Portugal)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=fi_FI&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Suomi (Suomi)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=sv_FI&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Svenska (Finland)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=sv_SE&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Svenska (Sverige)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=tr_TR&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                Türkçe (Türkiye)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=ja_JP&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                日本語 (日本)
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=zh_TW&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                繁體中文 (台灣)
        </span>
    </a>

                            </li>
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/search?find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA&amp;hl=zh_HK&amp;ns=1" rel="nofollow" role="menuitem">
        <span class="dropdown_label">
                繁體中文 (香港)
        </span>
    </a>

                            </li>
                    </ul>
            </div>
        </div>
    </div>

    </div>

            </div>
            <div class="footer-menu_section footer-country">
                <h3 class="footer-menu_header responsive-hidden-small">Countries</h3>
                

    <div class="dropdown js-dropdown dropdown--hover dropdown--boxed-on-mobile dropdown--restricted">
        

    <div class="dropdown_toggle js-dropdown-toggle" aria-haspopup="true" role="button" tabindex="-1">
        <a class="dropdown_toggle-action" href="javascript:;" data-dropdown-prefix="United States">
            <span class="dropdown_toggle-text js-dropdown-toggle-text" data-dropdown-initial-text=""></span>
            <span aria-hidden="true" style="width: 14px; height: 14px;" class="icon icon--14-triangle-down icon--size-14 icon--currentColor u-triangle-direction-down dropdown_arrow">
    <svg class="icon_svg">
        <use xlink:href="#14x14_triangle_down"></use>
    </svg>
</span>
        </a>
    </div>

            <div class="dropdown_menu-container js-dropdown_menu-container">
        <div class="dropdown_menu js-dropdown-menu">
            <div class="dropdown_menu-inner">
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/buenos-aires" role="menuitem">
        <span class="dropdown_label">
                Argentina
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/sydney" role="menuitem">
        <span class="dropdown_label">
                Australia
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/wien" role="menuitem">
        <span class="dropdown_label">
                Austria
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/bruxelles" role="menuitem">
        <span class="dropdown_label">
                Belgium
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/s%C3%A3o-paulo" role="menuitem">
        <span class="dropdown_label">
                Brazil
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/toronto" role="menuitem">
        <span class="dropdown_label">
                Canada
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/santiago" role="menuitem">
        <span class="dropdown_label">
                Chile
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/praha" role="menuitem">
        <span class="dropdown_label">
                Czech Republic
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/k%C3%B8benhavn" role="menuitem">
        <span class="dropdown_label">
                Denmark
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/helsinki" role="menuitem">
        <span class="dropdown_label">
                Finland
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/paris" role="menuitem">
        <span class="dropdown_label">
                France
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/berlin" role="menuitem">
        <span class="dropdown_label">
                Germany
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/hk" role="menuitem">
        <span class="dropdown_label">
                Hong Kong
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/roma" role="menuitem">
        <span class="dropdown_label">
                Italy
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/%E6%9D%B1%E4%BA%AC" role="menuitem">
        <span class="dropdown_label">
                Japan
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/kl" role="menuitem">
        <span class="dropdown_label">
                Malaysia
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/m%C3%A9xico-df" role="menuitem">
        <span class="dropdown_label">
                Mexico
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/auckland" role="menuitem">
        <span class="dropdown_label">
                New Zealand
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/oslo" role="menuitem">
        <span class="dropdown_label">
                Norway
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/manila" role="menuitem">
        <span class="dropdown_label">
                Philippines
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/warszawa" role="menuitem">
        <span class="dropdown_label">
                Poland
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/lisboa" role="menuitem">
        <span class="dropdown_label">
                Portugal
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/dublin" role="menuitem">
        <span class="dropdown_label">
                Republic of Ireland
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/singapore" role="menuitem">
        <span class="dropdown_label">
                Singapore
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/madrid" role="menuitem">
        <span class="dropdown_label">
                Spain
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/stockholm" role="menuitem">
        <span class="dropdown_label">
                Sweden
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/z%C3%BCrich" role="menuitem">
        <span class="dropdown_label">
                Switzerland
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/%E5%8F%B0%E5%8C%97%E5%B8%82" role="menuitem">
        <span class="dropdown_label">
                Taiwan
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/amsterdam" role="menuitem">
        <span class="dropdown_label">
                The Netherlands
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/istanbul" role="menuitem">
        <span class="dropdown_label">
                Turkey
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/london" role="menuitem">
        <span class="dropdown_label">
                United Kingdom
        </span>
    </a>

                            </li>
                    </ul>
                    <ul class="dropdown_menu-group" role="menu" aria-hidden="false">
                            <li class="dropdown_item " role="presentation">
                                        <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/sf" role="menuitem">
        <span class="dropdown_label">
                United States
        </span>
    </a>

                            </li>
                    </ul>
            </div>
        </div>
    </div>

    </div>

            </div>
        </div>
    </div>

                
    </div>

                                    <div class="main-footer_section lesser-text responsive-hidden-small">
            <div class="footer-menu footer-menu--inline footer-menu--bordered footer-menu--separated footer-menu--directory">
                <span class="footer-menu_header">Site Map</span>
                <ul class="footer-menu_list">
                        <li class="footer-menu_item"><a href="https://www.yelp.com/atlanta">Atlanta</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/austin">Austin</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/boston">Boston</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/chicago">Chicago</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/dallas">Dallas</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/denver">Denver</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/detroit">Detroit</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/honolulu">Honolulu</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/houston">Houston</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/la">Los Angeles</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/miami">Miami</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/minneapolis">Minneapolis</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/nyc">New York</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/philadelphia">Philadelphia</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/portland">Portland</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/sacramento">Sacramento</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/san-diego">San Diego</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/sf">San Francisco</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/san-jose">San Jose</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/seattle">Seattle</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/dc">Washington, DC</a></li>
                        <li class="footer-menu_item"><a href="https://www.yelp.com/locations">More Cities</a></li>
                </ul>
            </div>
        </div>

            
                <div class="main-footer_mobile-links responsive-visible-small-block hidden-non-responsive-block">
            <ul class="footer-menu--inline u-text-centered">
            <li class="footer-menu_item">
                <a href="https://yelp.com/about">About</a>
            </li>
            <li class="footer-menu_item">
                <a href="https://officialblog.yelp.com/">Blog</a>
            </li>
            <li class="footer-menu_item">
                <a href="https://www.yelp-support.com/?l=en_US">Support</a>
            </li>
            <li class="footer-menu_item">
                <a href="https://www.yelp.com/static?p=tos">Terms</a>
            </li>
    </ul>

    </div>

            
    <div class="main-footer_city-landscape-img" role="presentation"></div>

                <small class="main-footer_copyright">
            Copyright © 2004–2017 Yelp Inc. Yelp, <img src="./Best Fried chicken in Atlanta, GA - Yelp_files/logo_desktop_xsmall_outline.png" alt="Yelp logo" class="main-footer_logo-copyright" srcset="https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_styleguide/0aade8725c91/assets/img/logos/logo_desktop_xsmall_outline@2x.png 2x">, <img src="./Best Fried chicken in Atlanta, GA - Yelp_files/burst_desktop_xsmall_outline.png" alt="Yelp burst" class="main-footer_logo-burst" srcset="https://s3-media1.fl.yelpcdn.com/assets/srv0/yelp_styleguide/dcb526e86d86/assets/img/logos/burst_desktop_xsmall_outline@2x.png 2x"> and related marks are registered trademarks of Yelp.
    </small>

                <!--Source: Freebase (https://www.freebase.com/), licensed under CC-BY (https://creativecommons.org/licenses/by/2.5/)-->

        <p class="data-provider-attribution">
            <small><a rel="nofollow" href="http://www.databyacxiom.com/" target="_blank">Some Data By Acxiom</a></small>
        </p>

            </div>
        </div>
    </div>
<!-- google_ad_section_end -->

            <div style="display: none;" id="page-popups">
            </div>

                    
        
        

        </div> 

        

    <script>            yConfig = {"bingMapsUrl": "https://www.bing.com/api/maps/mapcontrol?v=8.0\u0026mkt=en-US\u0026s=1\u0026callback=", "cookies": {"ADMIN_SEARCH_USERDATA_RADIUS": "udr", "RECENT_LOCATIONS": "recentlocations", "SEARCH_PREFS": "searchPrefs", "JS_TRACK": "js_track", "YUV": "yuv", "DEBUG": "debug", "SELECTED_ACTIVITY_FEED": "fd", "CCJ": "ccj", "SIGNUP_TRACK": "strack", "EXPR_OVERRIDE": "expr", "SCJ": "scj", "COOKIE_INFO": "cim", "ADMIN_BUSINESS_ATTRIBUTE_CHANGESET_UTILS_PREFS": "bap", "APP_PITCH_CLOSED": "ap", "ADMIN_CM_SCOREBOARD_SETTINGS": "acms", "SEARCH_SUGGEST_INFO": "search_suggest", "LOCATION": "location", "ADMIN_SEARCH_USERDATA_LOCATION": "udl", "DISMISSIBLE_MESSAGE_COOKIE": "dm", "UPGRADES_IN_ARREARS": "uia", "USED_LOCALE_SELECTOR": "used_locale_selector", "PRIVACY_POLICY_NOTICE": "ppn", "HIDE_BROWSER_BAR": "hidebrowserbar", "SUGGEST_COOKIE": "ssi", "RESERVATION_SEARCH_PARAMS": "rsp", "XCJ": "xcj", "HOMEPAGE_SERVICE_ACTIVITY_FEED": "hsfd", "ADMIN_SEARCH_USERDATA": "ud", "MESSAGE_SENDER_PASSED_CAPTCHA": "mspc", "QUANTCAST": "qntcst", "AD_CLICKS": "adc"}, "webviewFlow": null, "enabledSitRepChannels": {"search_suggest_events": true, "vertical_search_platform": true, "ytp_session_events": true, "search_ux": true, "message_the_business": true, "vertical_search_reservation": true}, "isWebviewRequest": false, "uniqueRequestId": "f2da9c903fcf056d", "googleMapsUrl": "//maps.googleapis.com/maps/api/js?client=gme-yelp\u0026language=en\u0026sensor=false", "cdn": {"hostnamePattern": {"s3": "s3-media%s.fl.yelpcdn.com", "yelp": "media%s.fl.yelpcdn.com"}, "shardCount": 4}, "yelpcodeTemplateVersion": "ea5dbad6eb", "isLoggedIn": false, "imageUrls": {"mapMarkers": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/61a4c5ed6fcc/map/map_markers_sprite.png", "stars": "https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_design_web/9b34e39ccbeb/assets/img/stars/stars.png"}, "mapMarkerSerial": "20160801", "uaInfo": {"device": {"family": "Other"}, "os": {"major": "10", "patch_minor": null, "minor": "12", "family": "Mac OS X", "patch": "6"}, "string": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", "user_agent": {"major": "60", "minor": "0", "family": "Chrome", "patch": "3112"}, "attributes": {}}, "isSitRepEnabled": true, "comscore": {"c15": "", "c3": "", "c2": 7130511, "c1": 2, "c6": "", "c5": "", "c4": ""}, "webviewInfo": {}, "vendorExternalURLs": {}, "cookieDomain": ".www.yelp.com", "recaptchaPublicKey": "6Le5OSYTAAAAADy8seTrWT0eqpS795iV32Gm9Ag1", "isLive": true, "bingMapsKey": "AjhDhG82AEA_I4CdC-0o2DTDxg1Ojh0AZdcp_o-IbNuJGlb5fMMrig728eetoW8S", "isClientErrorsEnabled": false, "googlePlacesUrl": "//maps.googleapis.com/maps/api/js?key=AIzaSyByT6TXVL4jSf0MrzRwg0eG66A8-P4r0ps\u0026language=en\u0026libraries=places"};
</script>
        
        
        
        

            <noscript>&lt;img src="https://sb.scorecardresearch.com/p?cj=1&amp;amp;c15=&amp;amp;c3=&amp;amp;c2=7130511&amp;amp;c1=2&amp;amp;c6=&amp;amp;c5=&amp;amp;c4="&gt;</noscript>
            

                <script>
            (function() {
                var main = null;

                var main=(function(){function a(c,b){window._qevents=window._qevents||[];window._qevents.push({qacct:b});window.yDFP.quantcast={};window.yDFP.quantcast.cookieName=c;window.yDFP.quantcast.adTagName="qncst_segs";window.yDFP.quantcast.getTargetingData=function(){var g=new RegExp(window.yDFP.quantcast.cookieName+"=([^;]*)");var f=document.cookie.match(g);if(f){var e=decodeURIComponent(f[1]);var d=e.split(",");return{key:window.yDFP.quantcast.adTagName,value:d}}else{return null}};if(Boolean(window.googletag)&&Boolean(window.googletag.cmd)){window.googletag.cmd.push(function(){var d=window.yDFP.quantcast.getTargetingData();
if(d){window.googletag.pubads().setTargeting(d.key,d.value)}})}}window.yDFP=window.yDFP||{};window.yDFP.initQuantcast=a;return a})();

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main("qntcst","p-M4yfUTCPeS3vn");
            })();
    </script>
                    <noscript>
        &lt;img
            style="display: none;"
            src="https://pixel.quantserve.com/pixel/p-M4yfUTCPeS3vn.gif"
            alt="Quantcast"
            border="0"
            height="1"
            width="1"
        /&gt;
    </noscript>

                

            

        <script src="./Best Fried chicken in Atlanta, GA - Yelp_files/closure_localizations_en_US.min.js" type="text/javascript"></script>
        <script src="./Best Fried chicken in Atlanta, GA - Yelp_files/polyfill.min.js" integrity="sha384-FbHUaR69a828hqWjPw4PFllFj1bvveKOTWORGkyosCw720HXy/56+2hSuQDaogMb"></script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/jquery.min.js"></script><script>if(document.readyState === 'interactive') jQuery.ready();
        yConfig = window.yConfig || {};
        yConfig.vendorExternalURLs = yConfig.vendorExternalURLs || {};
        </script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/module_tmp_third_party.min.js"></script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/yelp-js-packages.min.js"></script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/module_core.min.js"></script><script>
                yConfig.vendorExternalURLs["plugin-detect"]=['https://s3-media4.fl.yelpcdn.com/assets/2/www/js/bfd62b330c7a/assets/vendor_external/plugin-detect-0.6.3.min.js']
                
                yConfig.vendorExternalURLs["fast-click"]=['https://s3-media1.fl.yelpcdn.com/assets/2/www/js/960df06ce458/assets/vendor_external/fastclick.min.js']
                yelp.www.util.analytics.initJSCustomDimensions();
yelp.www.init.initSearchSuggest("#find_desc", ".find-decorator", "#dropperText_Mast", true, true);
yelp.www.init.initAccountMenu("#topbar-account-item");
yelp.www.init.initHeaderNavTracking();
yelp.common.init.adVisibilityTracker({"servletURI": "/ad_visibility", "loggingCSRF": "70fb1166b82d58a3917229160c48fc2e66c7ae7b5eb132451e49abb02b16b614"});
yelp.www.init.initTimeOnPageAnalyticsBeforeUnload();
yelp.init.initDelegatedDropdowns();
yelp.init.attachGhostHovercard("qype", "    \u003cdiv id=\"qype-ghost-user-hovercard\"\u003e\n        \u003cdiv class=\"whatsthis-hovercard\"\u003e\n            \u003ch3\u003eWhat's This?\u003c/h3\u003e\n            \u003cp\u003eThis user has arrived from Qype, a company acquired by Yelp in 2012. We have integrated the two sites to bring you one great local experience.\u003c/p\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n");
yelp.init.attachGhostHovercard("rk", "    \u003cdiv id=\"rk-ghost-user-hovercard\"\u003e\n        \u003cdiv class=\"whatsthis-hovercard\"\u003e\n            \u003ch3\u003eWhat's This?\u003c/h3\u003e\n            \u003cp\u003eThis user has arrived from Restaurant-Kritik.de, a company acquired by Yelp in 2014. We have integrated the two sites to bring you one great local experience.\u003c/p\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n");
yelp.init.attachGhostHovercard("cityvox", "    \u003cdiv id=\"cityvox-ghost-user-hovercard\"\u003e\n        \u003cdiv class=\"whatsthis-hovercard\"\u003e\n            \u003ch3\u003eWhat's This?\u003c/h3\u003e\n            \u003cp\u003eThis user has arrived from Cityvox, a company acquired by Yelp in 2014. We have integrated the two sites to bring you one great local experience.\u003c/p\u003e\n        \u003c/div\u003e\n    \u003c/div\u003e\n");
yelp.www.init.initAsyncImageLoader();
yelp.pages.init();
yelp.www.init.facebook("97534753161", "//connect.facebook.net/en_US/sdk.js", "v2.7", "v2", ["email", "user_birthday"], ["publish_actions"], ["publish_actions", "user_friends"]);
yelp.init.quantcast();
yelp.init.initCCJCookieSetup(".yelp.com", 30);
</script><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/module_search.min.js"></script><script>yelp.www.init.search.Controller({"adVisibilityURI": "/ad_visibility", "isReservationSearchEnabled": true, "adAckURI": "/ad_acknowledgment", "feedbackPopupOptions": {"businessRedirectUri": "/biz_attribute", "businessSearchUri": "/contact/business_search_html"}, "searchMapMinZoom": 8, "adAckCSRF": "edaafd7204b3051191730570be1a10a859b4d432e8db7da06691ea825fb056b5", "isPlatformSearchEnabled": true, "adVisibilityCSRF": "70fb1166b82d58a3917229160c48fc2e66c7ae7b5eb132451e49abb02b16b614", "showCurlocMarker": true, "searchAdSense": {"canShowAdsense": true, "num_ads": 2, "query": "fried chicken", "loc": "Atlanta, GA", "isAdsenseEnabledForCountry": true, "detailed_attribution": true, "googleMapsEnterpriseKey": "ABQIAAAA-4PdDZI3yUT7Q6QmlfyYQBR-H9_hULZDKDkXlc3vkn3yqIJUbRQJYjw-XzY7Nb8a-Xj4njoI-o-BLg", "pubId": "pub-1554273207255362", "tracking_adsense_channel": "8818642271", "show_site_links": true, "baseLang": "en", "channel": "7129511946"}, "parentRequestId": "f2da9c903fcf056d", "locInputSelector": "#dropperText_Mast", "inputSelector": "#find_desc", "showCurlocSuggestion": true, "ajaxSearchURI": "/search/snippet", "snippetSerial": "20130418", "seoUrlParams": null, "currentSearchUrl": "/search?find_desc=fried+chicken\u0026find_loc=Atlanta%2C+GA", "searchMap": {"overlay_width": null, "fit_to_geobox": false, "should_draw_checkbox": false, "max_zoomlevel": 8, "service_areas": [], "library": "google", "zoom_control_position": "top_left", "market": null, "mo_map_possible": true, "center": {"latitude": 33.81321311652279, "longitude": -84.37362670898438}, "min_zoomlevel": 18, "zoom": 10, "markers": {"1": {"url": "/biz/guss-world-famous-fried-chicken-atlanta", "location": {"latitude": 33.760069, "longitude": -84.386257}, "key": 1, "hovercard_id": "TdP-YvQ6PkjA7ozmInUKng", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 0], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 0], "size": [24, 32]}}, "2": {"url": "/biz/south-city-kitchen-midtown-atlanta-2", "location": {"latitude": 33.7860123, "longitude": -84.3844605}, "key": 2, "hovercard_id": "tvYceAR7TJ7zS6N6kF5y8g", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 32], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 32], "size": [24, 32]}}, "3": {"url": "/biz/mary-macs-tea-room-atlanta", "location": {"latitude": 33.772851, "longitude": -84.379883}, "key": 3, "hovercard_id": "J1q9KDyfksvcce8qiv3wXA", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 64], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 64], "size": [24, 32]}}, "4": {"url": "/biz/busy-bee-cafe-atlanta", "location": {"latitude": 33.7544007, "longitude": -84.4140497}, "key": 4, "hovercard_id": "1gGFI10oK8oGAKx-nJwODQ", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 96], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 96], "size": [24, 32]}}, "5": {"url": "/biz/richards-southern-fried-atlanta", "location": {"latitude": 33.7564682423503, "longitude": -84.3641726392868}, "key": 5, "hovercard_id": "jQmiUQVRqEaPmrSE6sZ0ww", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 128], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 128], "size": [24, 32]}}, "6": {"url": "/biz/greens-and-gravy-atlanta", "location": {"latitude": 33.7432838173717, "longitude": -84.4378814504538}, "key": 6, "hovercard_id": "ZpdS484nehrxJrerN2JDmQ", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 160], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 160], "size": [24, 32]}}, "7": {"url": "/biz/colonnade-restaurant-atlanta", "location": {"latitude": 33.8092592, "longitude": -84.3609894}, "key": 7, "hovercard_id": "oEs3s_rnobbLzWr57HlRPw", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 192], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 192], "size": [24, 32]}}, "8": {"url": "/biz/south-city-kitchen-buckhead-atlanta", "location": {"latitude": 33.8476821, "longitude": -84.3681861}, "key": 8, "hovercard_id": "pGwgPtANWAUmeQUwCxNEEg", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 224], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 224], "size": [24, 32]}}, "9": {"url": "/biz/poor-calvins-atlanta-15", "location": {"latitude": 33.768452, "longitude": -84.3822579}, "key": 9, "hovercard_id": "oAlbeMIqtt84f0IA2wIWNw", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 256], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 256], "size": [24, 32]}}, "10": {"url": "/biz/rocks-chicken-and-fries-atlanta", "location": {"latitude": 33.8534607, "longitude": -84.363039}, "key": 10, "hovercard_id": "0ozMRzZBnIQHISOcWH3OmQ", "resource_type": "business", "icon": {"regular_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "scaled_size": [48, 320], "anchor_offset": [12, 32], "name": "business", "active_origin": [24, 288], "active_uri": "https://media2.fl.yelpcdn.com/mapmarkers/yelp_map_range/20160801/1/10.png", "regular_origin": [0, 288], "size": [24, 32]}}, "ad_business:below_organic:S8qrgwB7lktcArGx-BGoXg": {"slot": 0, "placement": "below_search", "url": "/adredir?ad_business_id=uvh9z5jj8MC0um48vMJDYw\u0026campaign_id=ukL-WBzrgsy8jS0ga8j4Zw\u0026click_origin=search_results\u0026placement=below_search\u0026redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcopelands-atlanta-4\u0026request_id=f2da9c903fcf056d\u0026signature=3fe0c13d50b4dca83f14c00b62f83ec299ad9cb8cf72eb1e5e8003387538d8b5\u0026slot=0\u0026click_origin=map_pin", "campaign_id": "ukL-WBzrgsy8jS0ga8j4Zw", "location": {"latitude": 33.8790269, "longitude": -84.4564502}, "key": "ad_business:below_organic:S8qrgwB7lktcArGx-BGoXg", "hovercard_id": "d7k6eJjfd0OGl4GfgwETAg", "resource_type": "ad_business", "icon": {"regular_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/50e4cce4ec9e/ico/yelp_map/ad_marker@2x.png", "scaled_size": [24, 32], "anchor_offset": [12, 32], "name": "ad_business", "active_origin": [0, 0], "active_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/c474cddf6199/ico/yelp_map/ad_marker_highlighted@2x.png", "regular_origin": [0, 0], "size": [24, 32]}}, "ad_business:below_organic:4LqNKlYo8AtKb2_H9ZsL6g": {"slot": 0, "placement": "above_search", "url": "/adredir?ad_business_id=PX_xyQcEj1bnaec2oMwH2w\u0026campaign_id=TEbM0Hh_xf9wDMZ1CNmBhg\u0026click_origin=search_results\u0026placement=above_search\u0026redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fcalabar-and-grill-stone-mountain-2\u0026request_id=f2da9c903fcf056d\u0026signature=207d46adad148d9a421bdc96af996ce0050306f8a5c2d7a55a97fd0e770e9471\u0026slot=0\u0026click_origin=map_pin", "campaign_id": "TEbM0Hh_xf9wDMZ1CNmBhg", "location": {"latitude": 33.7640893, "longitude": -84.2213327}, "key": "ad_business:below_organic:4LqNKlYo8AtKb2_H9ZsL6g", "hovercard_id": "v1pwv0WToysNn8AHjyiIFw", "resource_type": "ad_business", "icon": {"regular_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/50e4cce4ec9e/ico/yelp_map/ad_marker@2x.png", "scaled_size": [24, 32], "anchor_offset": [12, 32], "name": "ad_business", "active_origin": [0, 0], "active_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/c474cddf6199/ico/yelp_map/ad_marker_highlighted@2x.png", "regular_origin": [0, 0], "size": [24, 32]}}, "current_location": {"location": null, "key": "current_location", "icon": {"regular_uri": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/56b9eee3f027/ico/yelp_map/current_location_dot@2x.png", "scaled_size": [46, 46], "anchor_offset": [23, 23], "name": "current_location", "active_origin": [0, 0], "active_uri": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/56b9eee3f027/ico/yelp_map/current_location_dot@2x.png", "regular_origin": [0, 0], "size": [46, 46]}}, "ad_business:below_organic:C3xZRDXwOpe0HzfdT8UUgA": {"slot": 1, "placement": "above_search", "url": "/adredir?ad_business_id=LrkXX1pBqanN7StrzS-FiA\u0026campaign_id=b2KhI8mQPlH-bFU3_SRcbw\u0026click_origin=search_results\u0026placement=above_search\u0026redirect_url=https%3A%2F%2Fwww.yelp.com%2Fbiz%2Fred-chili-cafe-stone-mountain\u0026request_id=f2da9c903fcf056d\u0026signature=36a764c42b28c4ca09690a027bd82fba8e40994f007825ccd6309251c247fcea\u0026slot=1\u0026click_origin=map_pin", "campaign_id": "b2KhI8mQPlH-bFU3_SRcbw", "location": {"latitude": 33.8003559300065, "longitude": -84.2064668306884}, "key": "ad_business:below_organic:C3xZRDXwOpe0HzfdT8UUgA", "hovercard_id": "GkCmgO2j2s21SieUngRAkw", "resource_type": "ad_business", "icon": {"regular_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/50e4cce4ec9e/ico/yelp_map/ad_marker@2x.png", "scaled_size": [24, 32], "anchor_offset": [12, 32], "name": "ad_business", "active_origin": [0, 0], "active_uri": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/c474cddf6199/ico/yelp_map/ad_marker_highlighted@2x.png", "regular_origin": [0, 0], "size": [24, 32]}}}, "top_biz_bounds": null, "hoods": [], "scrollwheel_zoom": false}});
</script><div class="body-overlay" data-component-bound="true"></div><div class="hovercard yloca-hovercard"><div class="hovercard-inner clearfix"><div data-component-bound="true" class="loading-msg" style="display: block;"><span class="throbber"></span>Loading...</div></div><span class="arrow-icon"></span></div><script src="./Best Fried chicken in Atlanta, GA - Yelp_files/beacon.js"></script><script>
                if (window.COMSCORE && window.COMSCORE['beacon']) {
                    window.COMSCORE['beacon']({'c15': '', 'c3': '', 'c2': 7130511, 'c1': 2, 'c6': '', 'c5': '', 'c4': ''});
                }
                </script>

                <script>
            (function() {
                var main = null;

                var main=function(){if(["iPhone","iPod","iPad"].indexOf(navigator.platform)===-1||!window.requestAnimationFrame){return}window.bannerDetectionInitialScroll=window.bannerDetectionInitialScroll||window.scrollY||-100;requestAnimationFrame(function(){window.scrollTo(0,-100);requestAnimationFrame(function(){window.scrollBy(0,1);requestAnimationFrame(function(){window.userHasYelpApp=!window.scrollY;window.scrollTo(0,window.bannerDetectionInitialScroll)})})})};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script>
            <script>
            (function() {
                var main = null;

                var main=function loadSpice(g){var j=0;var k=1;var h=2;var e="0";var i="1";var l=function(){if(document.querySelector){return document.querySelector(".delay-spice")}var m=document.getElementsByTagName("div");var p=m.length;var o=new RegExp("(^|\\s)delay-spice(\\s|$)");for(var n=0;n<p;++n){if(o.test(m[n].className)){return m[n]}}return null};function d(){return(window._gaUserPrefs&&window._gaUserPrefs["ioo"]&&typeof(window._gaUserPrefs["ioo"])==="function"&&window._gaUserPrefs["ioo"]()===true||false)?"1":"0"
}function f(o,n){var p;if(n===j){p=["/ad_sp","ice?","r=",g]}else{p=["/sp","ice?","r=",g];if(n===h){p.push("&log_ad_spice=1")}}p.push("&pagevis="+o);p.push("&gablock="+d());var m=new Image();m.src=p.join("")}function b(m){if(l()){f(m,k);c(m)}else{f(m,h)}}function c(m){if(l()){window.setTimeout(function(){c(m)},500)}else{f(m,j)}}if(!document.webkitHidden){b(e)}else{var a=false;document.addEventListener("webkitvisibilitychange",function(){if(document.webkitHidden||a){return}a=true;b(i)})}};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main("f2da9c903fcf056d");
            })();
    </script>

                    <script>
            (function() {
                var main = null;

                var main=function(){var a=new Image(1,1);a.onerror=a.onload=function(){a.onerror=a.onload=null};a.src=["//secure-us.imrworldwide.com/cgi-bin/m?ci=us-804377h&cg=0&cc=1&si=",escape(window.location.href),"&rp=",escape(document.referrer),"&ts=compact&rnd=",(new Date()).getTime()].join("")};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script>
        <noscript>
            &lt;img src="//secure-us.imrworldwide.com/cgi-bin/m?ci=us-804377h&amp;amp;cg=0&amp;amp;cc=1&amp;amp;ts=noscript" width="1" height="1" alt=""&gt;
        </noscript>


    <script>            yConfig.csrf = {"SitRep": "ce17454967483e7a21af7917656623af00aa6adbbf5bb35e3d9620f2adf24d87", "FacebookTokenRefresh": "a57049573c26b20476bea125fda5d04bb97e653aa8b0a7ec078e8a6be7337bff"};
</script>


            <link rel="stylesheet" type="text/css" media="all" href="./Best Fried chicken in Atlanta, GA - Yelp_files/www-pkg.css"><link onload="document.getElementById(&#39;middleware_injected&#39;).disabled=true;" rel="stylesheet" type="text/css" media="all" href="./Best Fried chicken in Atlanta, GA - Yelp_files/search.css">

            <div id="ttdUniversalPixelTag290e816a69e9439f960a9588bc2ffb54" style="display:none">
                <script src="https://js.adsrvr.org/up_loader.1.1.0.js" type="text/javascript"></script>
                <script>
            (function() {
                var main = null;

                var main=function(){(function(b){if(typeof TTDUniversalPixelApi==="function"){var a=new TTDUniversalPixelApi();a.init("igcouad",["mvh4ai1"],"https://insight.adsrvr.org/track/up","ttdUniversalPixelTag290e816a69e9439f960a9588bc2ffb54")}})(this)};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script>
            </div>

            <noscript>
                &lt;img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=102029836881428&amp;ev=PageView&amp;noscript=1"/&gt;
            </noscript>

                <script>
            (function() {
                var main = null;

                var main=function(){var c=Math.random()+"";var b=c*10000000000000;document.write('<iframe src="https://6372968.fls.doubleclick.net/activityi;src=6372968;type=invmedia;cat=qr3hlsqk;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord='+b+'?" width="1" height="1" frameborder="0" style="display:none"></iframe>')};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
    </script><iframe src="./Best Fried chicken in Atlanta, GA - Yelp_files/activityi.html" width="1" height="1" frameborder="0" style="display:none"></iframe>
    <noscript>
        &lt;iframe src="https://6372968.fls.doubleclick.net/activityi;src=6372968;type=invmedia;cat=qr3hlsqk;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=1?" width="1" height="1" frameborder="0" style="display:none"&gt;&lt;/iframe&gt;
    </noscript>

    
<div id="d__fFH" style="position: absolute; top: -5000px; left: -5000px;"><object id="d_dlg" classid="clsid:3050f819-98b5-11cf-bb82-00aa00bdce0b" width="0px" height="0px"></object><span id="d__fF" style="font-family: Courier, serif; font-size: 72px; visibility: hidden;">The quick brown fox jumps over the lazy dog.</span></div><div class="modal modal--large" data-component-bound="true" style="display: none;"><div class="modal_inner"><div class="modal_close js-modal-close">×</div><div class="modal_dialog" role="dialog"><div data-component-bound="true"></div></div></div></div></body></html>

'''

print yelp_html




