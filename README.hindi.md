![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/github-contributions) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/github-contributions)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/github-contributions)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/github-contributions) 
![GitHub](https://img.shields.io/github/license/BEPb/github-contributions) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/github-contributions)
![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)
<p align="left">
<img src="https://visitor-badge.laobi.icu/badge?page_id=BEPb.github-contributions" alt="visitors"/>
</p>

अन्य भाषाओं में पढ़ें: [English](README.md), [Russian](README.ru.md), [中國人](README.chinese.md)


# गिटहब योगदान
यदि आप अपने गिटहब गतिविधि इतिहास को सुशोभित करना चाहते हैं, तो पायथन लिपि की क्षमताएं ``github_paint.py``
निर्दिष्ट अवधि के लिए योगदान को बदलने में आपकी सहायता करेगा।

## GitHub पर गतिविधि को फिर से करना, प्रोफ़ाइल में आरेखण करना
एक स्रोत के रूप में, आपको पहले से 52 गुणा 7 पिक्सेल की एक छवि तैयार करनी होगी: यह
स्वचालित रूप से आपकी ओर से आपके अलग भंडार में कमिट में परिवर्तित हो जाता है।


यह प्रोग्राम स्वयं README.md फ़ाइल के साथ एक खाली रिपॉजिटरी को इनिशियलाइज़ करता है और इसके साथ फ़ाइल अपडेट जनरेट करना शुरू करता है
योगदान जोड़ना: YYYY-MM-DD HH:MM आपकी प्रत्येक प्रतिबद्धता के लिए।

बनाने के लिए --date स्विच का उपयोग करता है
अतीत में करता है।

### कैसे इस्तेमाल करे
1. एक नया खाली GitHub रिपॉजिटरी बनाएं। README.md फ़ाइल शामिल न करें और रिपॉजिटरी को इनिशियलाइज़ न करें।
2. इस रिपॉजिटरी को क्लोन करें या github_paint.py फ़ाइल और अपनी कमिट ड्रॉइंग को कॉपी करें।
3. रिपॉजिटरी में, html पेज Git.html खोलें और अपनी ड्राइंग बनाएं
4. अपना चित्र सहेजें
5. इसे 52x7 . में बदलें
6. github_paint.py की पंक्तियों को अपने आरेखण के फ़ाइल नाम और वर्ष के अंतिम दिन के साथ बदलें जिसमें आप
   अपना चित्र पोस्ट करें
7. github_paint.py प्रोग्राम को कुंजी (आपके भंडार का पता) के साथ चलाएं जैसा कि नीचे दिए गए उदाहरण में दिखाया गया है: 

```commandline
python github_paint.py --repository = https: //github.com/user/repo.git
```
(HTTPS विधि: खाता प्रमाणीकरण)
प्रक्रिया में इतना समय (3-5 मिनट) नहीं लगता है।
7. परिणाम का आनंद लें

> नोट:
यदि आपने एक बार इस स्क्रिप्ट का उपयोग रिपॉजिटरी में किया है, तो आप इसे उसी रिपॉजिटरी के साथ दोहरा नहीं पाएंगे।
आपको एक और भंडार बनाना होगा अन्यथा आपको स्क्रिप्ट लॉग में त्रुटियां मिलेंगी।
एक ऐसे भंडार का उपयोग करने पर जोर दें जिसे प्रारंभ नहीं किया गया है।



### कार्य उदाहरण:
1. प्रारंभिक ड्राइंग `जीनोम`:

![](./example/genom.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/genom_mini.png)

परिणाम:
![](./example/genom_res.png)

2. प्रारंभिक ड्राइंग `Я люблю Python`:

![](./example/i_l_p.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/i_l_p_mini.png)

परिणाम:
![](./example/i_l_p_res.png)

2. प्रारंभिक ड्राइंग `Я люблю Python`:

![](./example/heart.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/heart_mini.png)

परिणाम:
![](./example/heart_res.png)

3. प्रारंभिक ड्राइंग `I love you`:

![](./example/I_love_you.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/I_love_you_mini.png)

परिणाम:

![](./example/I_love_you_res.png)

4. प्रारंभिक ड्राइंग `bugs, hex, sux`:

![](./example/bugs_hex_sux.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/bugs_hex_sux_mini.png)

परिणाम:

![](./example/bugs_hex_sux_res.png)


5. प्रारंभिक ड्राइंग `do it`:

![](./example/do_it.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/do_it_mini.png)

परिणाम:
![](./example/do_it_res.png)

6. प्रारंभिक ड्राइंग `pacman`:

![](./example/pacman.png)

वही ड्राइंग लेकिन 52x7 रिज़ॉल्यूशन में:
![](./example/pacman_mini.png)

परिणाम:
![](./example/pacman_res.png)

7. प्रारंभिक ड्राइंग `send nudes`:

![](./example/send_nudes.png)

8. प्रारंभिक ड्राइंग `sex_drugs_alco`:

![](./example/sex_drugs_alco.png)


काम के सभी उदाहरण फ़ोल्डर में रखे गए हैं `example`
पी.एस. GUI एप्लिकेशन या html पेज बनाने की दीर्घकालिक योजनाएँ जहाँ से आप सभी ऑपरेशन कर सकते हैं
रिपॉजिटरी में अपलोड करने से पहले ड्राइंग, लेकिन इसके लिए अभी तक समय नहीं है ..... इसलिए सभी उत्साही इस परियोजना को विकसित करते हैं
मैं आपको भाग लेने, अपनी शाखा बनाने के लिए आमंत्रित करता हूं।

पी.एस.एस. यदि आपको प्रोजेक्ट पसंद आया है, तो स्टार लगाना न भूलें, और यदि आप रुचि रखते हैं, तो एक अनुयायी के रूप में साइन अप करें।

