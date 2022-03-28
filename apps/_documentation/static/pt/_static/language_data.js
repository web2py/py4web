/*
 * language_data.js
 * ~~~~~~~~~~~~~~~~
 *
 * This script contains the language-specific data used by searchtools.js,
 * namely the list of stopwords, stemmer, scorer and splitter.
 *
 * :copyright: Copyright 2007-2022 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 */

var stopwords = ["a","ao","aos","aquela","aquelas","aquele","aqueles","aquilo","as","at\u00e9","com","como","da","das","de","dela","delas","dele","deles","depois","do","dos","e","ela","elas","ele","eles","em","entre","era","eram","essa","essas","esse","esses","esta","estamos","estas","estava","estavam","este","esteja","estejam","estejamos","estes","esteve","estive","estivemos","estiver","estivera","estiveram","estiverem","estivermos","estivesse","estivessem","estiv\u00e9ramos","estiv\u00e9ssemos","estou","est\u00e1","est\u00e1vamos","est\u00e3o","eu","foi","fomos","for","fora","foram","forem","formos","fosse","fossem","fui","f\u00f4ramos","f\u00f4ssemos","haja","hajam","hajamos","havemos","hei","houve","houvemos","houver","houvera","houveram","houverei","houverem","houveremos","houveria","houveriam","houvermos","houver\u00e1","houver\u00e3o","houver\u00edamos","houvesse","houvessem","houv\u00e9ramos","houv\u00e9ssemos","h\u00e1","h\u00e3o","isso","isto","j\u00e1","lhe","lhes","mais","mas","me","mesmo","meu","meus","minha","minhas","muito","na","nas","nem","no","nos","nossa","nossas","nosso","nossos","num","numa","n\u00e3o","n\u00f3s","o","os","ou","para","pela","pelas","pelo","pelos","por","qual","quando","que","quem","se","seja","sejam","sejamos","sem","serei","seremos","seria","seriam","ser\u00e1","ser\u00e3o","ser\u00edamos","seu","seus","somos","sou","sua","suas","s\u00e3o","s\u00f3","tamb\u00e9m","te","tem","temos","tenha","tenham","tenhamos","tenho","terei","teremos","teria","teriam","ter\u00e1","ter\u00e3o","ter\u00edamos","teu","teus","teve","tinha","tinham","tive","tivemos","tiver","tivera","tiveram","tiverem","tivermos","tivesse","tivessem","tiv\u00e9ramos","tiv\u00e9ssemos","tu","tua","tuas","t\u00e9m","t\u00ednhamos","um","uma","voc\u00ea","voc\u00eas","vos","\u00e0","\u00e0s","\u00e9ramos"];


/* Non-minified version is copied as a separate JS file, is available */
BaseStemmer=function(){this.setCurrent=function(r){this.current=r;this.cursor=0;this.limit=this.current.length;this.limit_backward=0;this.bra=this.cursor;this.ket=this.limit};this.getCurrent=function(){return this.current};this.copy_from=function(r){this.current=r.current;this.cursor=r.cursor;this.limit=r.limit;this.limit_backward=r.limit_backward;this.bra=r.bra;this.ket=r.ket};this.in_grouping=function(r,t,i){if(this.cursor>=this.limit)return false;var s=this.current.charCodeAt(this.cursor);if(s>i||s<t)return false;s-=t;if((r[s>>>3]&1<<(s&7))==0)return false;this.cursor++;return true};this.in_grouping_b=function(r,t,i){if(this.cursor<=this.limit_backward)return false;var s=this.current.charCodeAt(this.cursor-1);if(s>i||s<t)return false;s-=t;if((r[s>>>3]&1<<(s&7))==0)return false;this.cursor--;return true};this.out_grouping=function(r,t,i){if(this.cursor>=this.limit)return false;var s=this.current.charCodeAt(this.cursor);if(s>i||s<t){this.cursor++;return true}s-=t;if((r[s>>>3]&1<<(s&7))==0){this.cursor++;return true}return false};this.out_grouping_b=function(r,t,i){if(this.cursor<=this.limit_backward)return false;var s=this.current.charCodeAt(this.cursor-1);if(s>i||s<t){this.cursor--;return true}s-=t;if((r[s>>>3]&1<<(s&7))==0){this.cursor--;return true}return false};this.eq_s=function(r){if(this.limit-this.cursor<r.length)return false;if(this.current.slice(this.cursor,this.cursor+r.length)!=r){return false}this.cursor+=r.length;return true};this.eq_s_b=function(r){if(this.cursor-this.limit_backward<r.length)return false;if(this.current.slice(this.cursor-r.length,this.cursor)!=r){return false}this.cursor-=r.length;return true};this.find_among=function(r){var t=0;var i=r.length;var s=this.cursor;var e=this.limit;var h=0;var u=0;var n=false;while(true){var c=t+(i-t>>>1);var a=0;var f=h<u?h:u;var l=r[c];var o;for(o=f;o<l[0].length;o++){if(s+f==e){a=-1;break}a=this.current.charCodeAt(s+f)-l[0].charCodeAt(o);if(a!=0)break;f++}if(a<0){i=c;u=f}else{t=c;h=f}if(i-t<=1){if(t>0)break;if(i==t)break;if(n)break;n=true}}do{var l=r[t];if(h>=l[0].length){this.cursor=s+l[0].length;if(l.length<4)return l[2];var v=l[3](this);this.cursor=s+l[0].length;if(v)return l[2]}t=l[1]}while(t>=0);return 0};this.find_among_b=function(r){var t=0;var i=r.length;var s=this.cursor;var e=this.limit_backward;var h=0;var u=0;var n=false;while(true){var c=t+(i-t>>1);var a=0;var f=h<u?h:u;var l=r[c];var o;for(o=l[0].length-1-f;o>=0;o--){if(s-f==e){a=-1;break}a=this.current.charCodeAt(s-1-f)-l[0].charCodeAt(o);if(a!=0)break;f++}if(a<0){i=c;u=f}else{t=c;h=f}if(i-t<=1){if(t>0)break;if(i==t)break;if(n)break;n=true}}do{var l=r[t];if(h>=l[0].length){this.cursor=s-l[0].length;if(l.length<4)return l[2];var v=l[3](this);this.cursor=s-l[0].length;if(v)return l[2]}t=l[1]}while(t>=0);return 0};this.replace_s=function(r,t,i){var s=i.length-(t-r);this.current=this.current.slice(0,r)+i+this.current.slice(t);this.limit+=s;if(this.cursor>=t)this.cursor+=s;else if(this.cursor>r)this.cursor=r;return s};this.slice_check=function(){if(this.bra<0||this.bra>this.ket||this.ket>this.limit||this.limit>this.current.length){return false}return true};this.slice_from=function(r){var t=false;if(this.slice_check()){this.replace_s(this.bra,this.ket,r);t=true}return t};this.slice_del=function(){return this.slice_from("")};this.insert=function(r,t,i){var s=this.replace_s(r,t,i);if(r<=this.bra)this.bra+=s;if(r<=this.ket)this.ket+=s};this.slice_to=function(){var r="";if(this.slice_check()){r=this.current.slice(this.bra,this.ket)}return r};this.assign_to=function(){return this.current.slice(0,this.limit)}};
PortugueseStemmer=function(){var r=new BaseStemmer;var e=[["",-1,3],["ã",0,1],["õ",0,2]];var i=[["",-1,3],["a~",0,1],["o~",0,2]];var s=[["ic",-1,-1],["ad",-1,-1],["os",-1,-1],["iv",-1,1]];var a=[["ante",-1,1],["avel",-1,1],["ível",-1,1]];var u=[["ic",-1,1],["abil",-1,1],["iv",-1,1]];var o=[["ica",-1,1],["ância",-1,1],["ência",-1,4],["logia",-1,2],["ira",-1,9],["adora",-1,1],["osa",-1,1],["ista",-1,1],["iva",-1,8],["eza",-1,1],["idade",-1,7],["ante",-1,1],["mente",-1,6],["amente",12,5],["ável",-1,1],["ível",-1,1],["ico",-1,1],["ismo",-1,1],["oso",-1,1],["amento",-1,1],["imento",-1,1],["ivo",-1,8],["aça~o",-1,1],["uça~o",-1,3],["ador",-1,1],["icas",-1,1],["ências",-1,4],["logias",-1,2],["iras",-1,9],["adoras",-1,1],["osas",-1,1],["istas",-1,1],["ivas",-1,8],["ezas",-1,1],["idades",-1,7],["adores",-1,1],["antes",-1,1],["aço~es",-1,1],["uço~es",-1,3],["icos",-1,1],["ismos",-1,1],["osos",-1,1],["amentos",-1,1],["imentos",-1,1],["ivos",-1,8]];var t=[["ada",-1,1],["ida",-1,1],["ia",-1,1],["aria",2,1],["eria",2,1],["iria",2,1],["ara",-1,1],["era",-1,1],["ira",-1,1],["ava",-1,1],["asse",-1,1],["esse",-1,1],["isse",-1,1],["aste",-1,1],["este",-1,1],["iste",-1,1],["ei",-1,1],["arei",16,1],["erei",16,1],["irei",16,1],["am",-1,1],["iam",20,1],["ariam",21,1],["eriam",21,1],["iriam",21,1],["aram",20,1],["eram",20,1],["iram",20,1],["avam",20,1],["em",-1,1],["arem",29,1],["erem",29,1],["irem",29,1],["assem",29,1],["essem",29,1],["issem",29,1],["ado",-1,1],["ido",-1,1],["ando",-1,1],["endo",-1,1],["indo",-1,1],["ara~o",-1,1],["era~o",-1,1],["ira~o",-1,1],["ar",-1,1],["er",-1,1],["ir",-1,1],["as",-1,1],["adas",47,1],["idas",47,1],["ias",47,1],["arias",50,1],["erias",50,1],["irias",50,1],["aras",47,1],["eras",47,1],["iras",47,1],["avas",47,1],["es",-1,1],["ardes",58,1],["erdes",58,1],["irdes",58,1],["ares",58,1],["eres",58,1],["ires",58,1],["asses",58,1],["esses",58,1],["isses",58,1],["astes",58,1],["estes",58,1],["istes",58,1],["is",-1,1],["ais",71,1],["eis",71,1],["areis",73,1],["ereis",73,1],["ireis",73,1],["áreis",73,1],["éreis",73,1],["íreis",73,1],["ásseis",73,1],["ésseis",73,1],["ísseis",73,1],["áveis",73,1],["íeis",73,1],["aríeis",84,1],["eríeis",84,1],["iríeis",84,1],["ados",-1,1],["idos",-1,1],["amos",-1,1],["áramos",90,1],["éramos",90,1],["íramos",90,1],["ávamos",90,1],["íamos",90,1],["aríamos",95,1],["eríamos",95,1],["iríamos",95,1],["emos",-1,1],["aremos",99,1],["eremos",99,1],["iremos",99,1],["ássemos",99,1],["êssemos",99,1],["íssemos",99,1],["imos",-1,1],["armos",-1,1],["ermos",-1,1],["irmos",-1,1],["ámos",-1,1],["arás",-1,1],["erás",-1,1],["irás",-1,1],["eu",-1,1],["iu",-1,1],["ou",-1,1],["ará",-1,1],["erá",-1,1],["irá",-1,1]];var c=[["a",-1,1],["i",-1,1],["o",-1,1],["os",-1,1],["á",-1,1],["í",-1,1],["ó",-1,1]];var f=[["e",-1,1],["ç",-1,2],["é",-1,1],["ê",-1,1]];var l=[17,65,16,0,0,0,0,0,0,0,0,0,0,0,0,0,3,19,12,2];var n=0;var m=0;var b=0;function k(){var i;while(true){var s=r.cursor;r:{r.bra=r.cursor;i=r.find_among(e);if(i==0){break r}r.ket=r.cursor;switch(i){case 1:if(!r.slice_from("a~")){return false}break;case 2:if(!r.slice_from("o~")){return false}break;case 3:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=s;break}return true}function _(){b=r.limit;m=r.limit;n=r.limit;var e=r.cursor;r:{e:{var i=r.cursor;i:{if(!r.in_grouping(l,97,250)){break i}s:{var s=r.cursor;a:{if(!r.out_grouping(l,97,250)){break a}u:while(true){o:{if(!r.in_grouping(l,97,250)){break o}break u}if(r.cursor>=r.limit){break a}r.cursor++}break s}r.cursor=s;if(!r.in_grouping(l,97,250)){break i}a:while(true){u:{if(!r.out_grouping(l,97,250)){break u}break a}if(r.cursor>=r.limit){break i}r.cursor++}}break e}r.cursor=i;if(!r.out_grouping(l,97,250)){break r}i:{var a=r.cursor;s:{if(!r.out_grouping(l,97,250)){break s}a:while(true){u:{if(!r.in_grouping(l,97,250)){break u}break a}if(r.cursor>=r.limit){break s}r.cursor++}break i}r.cursor=a;if(!r.in_grouping(l,97,250)){break r}if(r.cursor>=r.limit){break r}r.cursor++}}b=r.cursor}r.cursor=e;var u=r.cursor;r:{e:while(true){i:{if(!r.in_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}m=r.cursor;e:while(true){i:{if(!r.in_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,250)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}n=r.cursor}r.cursor=u;return true}function v(){var e;while(true){var s=r.cursor;r:{r.bra=r.cursor;e=r.find_among(i);if(e==0){break r}r.ket=r.cursor;switch(e){case 1:if(!r.slice_from("ã")){return false}break;case 2:if(!r.slice_from("õ")){return false}break;case 3:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=s;break}return true}function d(){if(!(b<=r.cursor)){return false}return true}function g(){if(!(m<=r.cursor)){return false}return true}function w(){if(!(n<=r.cursor)){return false}return true}function h(){var e;r.ket=r.cursor;e=r.find_among_b(o);if(e==0){return false}r.bra=r.cursor;switch(e){case 1:if(!w()){return false}if(!r.slice_del()){return false}break;case 2:if(!w()){return false}if(!r.slice_from("log")){return false}break;case 3:if(!w()){return false}if(!r.slice_from("u")){return false}break;case 4:if(!w()){return false}if(!r.slice_from("ente")){return false}break;case 5:if(!g()){return false}if(!r.slice_del()){return false}var i=r.limit-r.cursor;r:{r.ket=r.cursor;e=r.find_among_b(s);if(e==0){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}switch(e){case 1:r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}break}}break;case 6:if(!w()){return false}if(!r.slice_del()){return false}var t=r.limit-r.cursor;r:{r.ket=r.cursor;if(r.find_among_b(a)==0){r.cursor=r.limit-t;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-t;break r}if(!r.slice_del()){return false}}break;case 7:if(!w()){return false}if(!r.slice_del()){return false}var c=r.limit-r.cursor;r:{r.ket=r.cursor;if(r.find_among_b(u)==0){r.cursor=r.limit-c;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-c;break r}if(!r.slice_del()){return false}}break;case 8:if(!w()){return false}if(!r.slice_del()){return false}var f=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-f;break r}r.bra=r.cursor;if(!w()){r.cursor=r.limit-f;break r}if(!r.slice_del()){return false}}break;case 9:if(!d()){return false}if(!r.eq_s_b("e")){return false}if(!r.slice_from("ir")){return false}break}return true}function p(){if(r.cursor<b){return false}var e=r.limit_backward;r.limit_backward=b;r.ket=r.cursor;if(r.find_among_b(t)==0){r.limit_backward=e;return false}r.bra=r.cursor;if(!r.slice_del()){return false}r.limit_backward=e;return true}function q(){r.ket=r.cursor;if(r.find_among_b(c)==0){return false}r.bra=r.cursor;if(!d()){return false}if(!r.slice_del()){return false}return true}function z(){var e;r.ket=r.cursor;e=r.find_among_b(f);if(e==0){return false}r.bra=r.cursor;switch(e){case 1:if(!d()){return false}if(!r.slice_del()){return false}r.ket=r.cursor;r:{var i=r.limit-r.cursor;e:{if(!r.eq_s_b("u")){break e}r.bra=r.cursor;var s=r.limit-r.cursor;if(!r.eq_s_b("g")){break e}r.cursor=r.limit-s;break r}r.cursor=r.limit-i;if(!r.eq_s_b("i")){return false}r.bra=r.cursor;var a=r.limit-r.cursor;if(!r.eq_s_b("c")){return false}r.cursor=r.limit-a}if(!d()){return false}if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("c")){return false}break}return true}this.stem=function(){var e=r.cursor;k();r.cursor=e;_();r.limit_backward=r.cursor;r.cursor=r.limit;var i=r.limit-r.cursor;r:{e:{var s=r.limit-r.cursor;i:{var a=r.limit-r.cursor;s:{var u=r.limit-r.cursor;a:{if(!h()){break a}break s}r.cursor=r.limit-u;if(!p()){break i}}r.cursor=r.limit-a;var o=r.limit-r.cursor;s:{r.ket=r.cursor;if(!r.eq_s_b("i")){break s}r.bra=r.cursor;var t=r.limit-r.cursor;if(!r.eq_s_b("c")){break s}r.cursor=r.limit-t;if(!d()){break s}if(!r.slice_del()){return false}}r.cursor=r.limit-o;break e}r.cursor=r.limit-s;if(!q()){break r}}}r.cursor=r.limit-i;var c=r.limit-r.cursor;z();r.cursor=r.limit-c;r.cursor=r.limit_backward;var f=r.cursor;v();r.cursor=f;return true};this["stemWord"]=function(e){r.setCurrent(e);this.stem();return r.getCurrent()}};
Stemmer = PortugueseStemmer;



var splitChars = (function() {
    var result = {};
    var singles = [96, 180, 187, 191, 215, 247, 749, 885, 903, 907, 909, 930, 1014, 1648,
         1748, 1809, 2416, 2473, 2481, 2526, 2601, 2609, 2612, 2615, 2653, 2702,
         2706, 2729, 2737, 2740, 2857, 2865, 2868, 2910, 2928, 2948, 2961, 2971,
         2973, 3085, 3089, 3113, 3124, 3213, 3217, 3241, 3252, 3295, 3341, 3345,
         3369, 3506, 3516, 3633, 3715, 3721, 3736, 3744, 3748, 3750, 3756, 3761,
         3781, 3912, 4239, 4347, 4681, 4695, 4697, 4745, 4785, 4799, 4801, 4823,
         4881, 5760, 5901, 5997, 6313, 7405, 8024, 8026, 8028, 8030, 8117, 8125,
         8133, 8181, 8468, 8485, 8487, 8489, 8494, 8527, 11311, 11359, 11687, 11695,
         11703, 11711, 11719, 11727, 11735, 12448, 12539, 43010, 43014, 43019, 43587,
         43696, 43713, 64286, 64297, 64311, 64317, 64319, 64322, 64325, 65141];
    var i, j, start, end;
    for (i = 0; i < singles.length; i++) {
        result[singles[i]] = true;
    }
    var ranges = [[0, 47], [58, 64], [91, 94], [123, 169], [171, 177], [182, 184], [706, 709],
         [722, 735], [741, 747], [751, 879], [888, 889], [894, 901], [1154, 1161],
         [1318, 1328], [1367, 1368], [1370, 1376], [1416, 1487], [1515, 1519], [1523, 1568],
         [1611, 1631], [1642, 1645], [1750, 1764], [1767, 1773], [1789, 1790], [1792, 1807],
         [1840, 1868], [1958, 1968], [1970, 1983], [2027, 2035], [2038, 2041], [2043, 2047],
         [2070, 2073], [2075, 2083], [2085, 2087], [2089, 2307], [2362, 2364], [2366, 2383],
         [2385, 2391], [2402, 2405], [2419, 2424], [2432, 2436], [2445, 2446], [2449, 2450],
         [2483, 2485], [2490, 2492], [2494, 2509], [2511, 2523], [2530, 2533], [2546, 2547],
         [2554, 2564], [2571, 2574], [2577, 2578], [2618, 2648], [2655, 2661], [2672, 2673],
         [2677, 2692], [2746, 2748], [2750, 2767], [2769, 2783], [2786, 2789], [2800, 2820],
         [2829, 2830], [2833, 2834], [2874, 2876], [2878, 2907], [2914, 2917], [2930, 2946],
         [2955, 2957], [2966, 2968], [2976, 2978], [2981, 2983], [2987, 2989], [3002, 3023],
         [3025, 3045], [3059, 3076], [3130, 3132], [3134, 3159], [3162, 3167], [3170, 3173],
         [3184, 3191], [3199, 3204], [3258, 3260], [3262, 3293], [3298, 3301], [3312, 3332],
         [3386, 3388], [3390, 3423], [3426, 3429], [3446, 3449], [3456, 3460], [3479, 3481],
         [3518, 3519], [3527, 3584], [3636, 3647], [3655, 3663], [3674, 3712], [3717, 3718],
         [3723, 3724], [3726, 3731], [3752, 3753], [3764, 3772], [3774, 3775], [3783, 3791],
         [3802, 3803], [3806, 3839], [3841, 3871], [3892, 3903], [3949, 3975], [3980, 4095],
         [4139, 4158], [4170, 4175], [4182, 4185], [4190, 4192], [4194, 4196], [4199, 4205],
         [4209, 4212], [4226, 4237], [4250, 4255], [4294, 4303], [4349, 4351], [4686, 4687],
         [4702, 4703], [4750, 4751], [4790, 4791], [4806, 4807], [4886, 4887], [4955, 4968],
         [4989, 4991], [5008, 5023], [5109, 5120], [5741, 5742], [5787, 5791], [5867, 5869],
         [5873, 5887], [5906, 5919], [5938, 5951], [5970, 5983], [6001, 6015], [6068, 6102],
         [6104, 6107], [6109, 6111], [6122, 6127], [6138, 6159], [6170, 6175], [6264, 6271],
         [6315, 6319], [6390, 6399], [6429, 6469], [6510, 6511], [6517, 6527], [6572, 6592],
         [6600, 6607], [6619, 6655], [6679, 6687], [6741, 6783], [6794, 6799], [6810, 6822],
         [6824, 6916], [6964, 6980], [6988, 6991], [7002, 7042], [7073, 7085], [7098, 7167],
         [7204, 7231], [7242, 7244], [7294, 7400], [7410, 7423], [7616, 7679], [7958, 7959],
         [7966, 7967], [8006, 8007], [8014, 8015], [8062, 8063], [8127, 8129], [8141, 8143],
         [8148, 8149], [8156, 8159], [8173, 8177], [8189, 8303], [8306, 8307], [8314, 8318],
         [8330, 8335], [8341, 8449], [8451, 8454], [8456, 8457], [8470, 8472], [8478, 8483],
         [8506, 8507], [8512, 8516], [8522, 8525], [8586, 9311], [9372, 9449], [9472, 10101],
         [10132, 11263], [11493, 11498], [11503, 11516], [11518, 11519], [11558, 11567],
         [11622, 11630], [11632, 11647], [11671, 11679], [11743, 11822], [11824, 12292],
         [12296, 12320], [12330, 12336], [12342, 12343], [12349, 12352], [12439, 12444],
         [12544, 12548], [12590, 12592], [12687, 12689], [12694, 12703], [12728, 12783],
         [12800, 12831], [12842, 12880], [12896, 12927], [12938, 12976], [12992, 13311],
         [19894, 19967], [40908, 40959], [42125, 42191], [42238, 42239], [42509, 42511],
         [42540, 42559], [42592, 42593], [42607, 42622], [42648, 42655], [42736, 42774],
         [42784, 42785], [42889, 42890], [42893, 43002], [43043, 43055], [43062, 43071],
         [43124, 43137], [43188, 43215], [43226, 43249], [43256, 43258], [43260, 43263],
         [43302, 43311], [43335, 43359], [43389, 43395], [43443, 43470], [43482, 43519],
         [43561, 43583], [43596, 43599], [43610, 43615], [43639, 43641], [43643, 43647],
         [43698, 43700], [43703, 43704], [43710, 43711], [43715, 43738], [43742, 43967],
         [44003, 44015], [44026, 44031], [55204, 55215], [55239, 55242], [55292, 55295],
         [57344, 63743], [64046, 64047], [64110, 64111], [64218, 64255], [64263, 64274],
         [64280, 64284], [64434, 64466], [64830, 64847], [64912, 64913], [64968, 65007],
         [65020, 65135], [65277, 65295], [65306, 65312], [65339, 65344], [65371, 65381],
         [65471, 65473], [65480, 65481], [65488, 65489], [65496, 65497]];
    for (i = 0; i < ranges.length; i++) {
        start = ranges[i][0];
        end = ranges[i][1];
        for (j = start; j <= end; j++) {
            result[j] = true;
        }
    }
    return result;
})();

function splitQuery(query) {
    var result = [];
    var start = -1;
    for (var i = 0; i < query.length; i++) {
        if (splitChars[query.charCodeAt(i)]) {
            if (start !== -1) {
                result.push(query.slice(start, i));
                start = -1;
            }
        } else if (start === -1) {
            start = i;
        }
    }
    if (start !== -1) {
        result.push(query.slice(start));
    }
    return result;
}


