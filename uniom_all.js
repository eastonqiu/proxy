/*==============================================================================*/
/* Casper generated Sat Sep 19 2015 17:03:12 GMT+0800 (CST) */
/*==============================================================================*/
var fs = require("fs"),
    captchaFile = "captcha.png",
    parsedFile = "captcha.txt",
    captcha = null;
	loginPage = "https://login.woego.cn/woego/login/pageInit";

casper.waitForCaptcha = function(captchaFile, parsedFile){
    casper.then(function(){
        this.captureSelector(captchaFile, "#check_img");
    });
    casper.waitFor(function check(){
        return fs.exists(parsedFile);
    }, function then(){
        // do something on time
        captcha = fs.read(parsedFile); 
        this.echo("+++++captcha:"+captcha);
        fs.remove(captchaFile);
        fs.remove(parsedFile);
		this.echo("+++++finish remove");
    }, function onTimeout(){
        this.echo("you did not enter the captcha....");
      // do something when failed
    }, 120000); // 1min should suffice as a timeout
   return this;
};

var x = require('casper').selectXPath;
casper.options.viewportSize = {width: 1301, height: 657};
casper.on('page.error', function(msg, trace) {
    this.echo('Error: ' + msg, 'ERROR');
    for(var i=0; i<trace.length; i++) {
        var step = trace[i];
        this.echo('   ' + step.file + ' (line ' + step.line + ')', 'ERROR');
    }
});
casper.test.begin('Resurrectio test', function(test) {
    casper.start(loginPage);
    //yanzhengma
    casper.waitForCaptcha(captchaFile, parsedFile);
    casper.waitForSelector("input[name='STAFF_ID']",
        function success() {
            this.sendKeys("input[name='STAFF_ID']", "51b1x7t");
        },
        function fail() {
            test.assertExists("input[name='STAFF_ID']");
    });
    casper.waitForSelector("form#form_id input[name='LOGIN_PASSWORD']",
        function success() {
            test.assertExists("form#form_id input[name='LOGIN_PASSWORD']");
            this.click("form#form_id input[name='LOGIN_PASSWORD']");
        },
        function fail() {
            test.assertExists("form#form_id input[name='LOGIN_PASSWORD']");
    });
    casper.waitForSelector("input[name='LOGIN_PASSWORD']",
        function success() {
            this.sendKeys("input[name='LOGIN_PASSWORD']", "111111");
        },
        function fail() {
            test.assertExists("input[name='LOGIN_PASSWORD']");
    });
    casper.waitForSelector("form#form_id input[name='VERIFY_CODE']",
        function success() {
            test.assertExists("form#form_id input[name='VERIFY_CODE']");
            this.click("form#form_id input[name='VERIFY_CODE']");
        },
        function fail() {
            test.assertExists("form#form_id input[name='VERIFY_CODE']");
    });
    casper.waitForSelector("input[name='VERIFY_CODE1']",
        function success() {
            this.sendKeys("input[name='VERIFY_CODE1']", captcha);
        },
        function fail() {
            test.assertExists("input[name='VERIFY_CODE1']");
    });

    casper.waitForSelector("form#form_id input[type=submit][value='登录']",
        function success() {
            test.assertExists("form#form_id input[type=submit][value='登录']");
            this.click("form#form_id input[type=submit][value='登录']");
        },
        function fail() {
            test.assertExists("form#form_id input[type=submit][value='登录']");
    });

    casper.then(function() {
	    // fail
        if(this.getTitle() == loginPage) {
			this.echo("============== error: login error, retry");		
	        this.waitForCaptcha(captchaFile, parsedFile);
        } else {
			this.echo("++++++++ login success");			
		}
    });

	casper.wait(1000);
/*
    casper.waitForSelector(".close span:nth-child(1)",
        function success() {
            test.assertExists(".close span:nth-child(1)");
            this.click(".close span:nth-child(1)");
        },
        function fail() {
            test.assertExists(".close span:nth-child(1)");
    });
*/
	casper.thenOpen('http://www.woego.cn/woego/goods/pageInit?gdsId=109696&skuId=156516&shopLocaleCode=51', function() {
    	this.echo("url popup loaded : " + this.getCurrentUrl(),"INFO");
	});
/*
	casper.waitForSelector(x("//*[@id='hot_words']/a[6]"),
       function success() {
           test.assertExists(x("//*[@id='hot_words']/a[6]"));
this.captureSelector("t.jpg", x("//*[@id='hot_words']/a[6]"));
           this.click(x("//*[@id='hot_words']/a[6]"));
       },
       function fail() {
           test.assertExists(x("//*[@id='hot_words']/a[6]"));
   });

	// this will wait for the popup to be opened and loaded
	casper.waitForPopup(/shopLocaleCode/, function() {
	    this.test.assertEquals(this.popups.length, 1);
	});
*/
// this will set the popup DOM as the main active one only for time the
// step closure being executed
	casper.then(function() {
		this.captureSelector("login_success.png", "html");
	});

	/*casper.waitForSelector("#checkvalue_1_1",
	   function success() {
	       this.click("#checkvalue_1_1");
	   },
	   function fail() {
	       test.assertExists("#checkvalue_1_1");
   });*/


	casper.waitForSelector("input#BUY_NUM",
	   function success() {
	       this.sendKeys("input#BUY_NUM", "1");
	   },
	   function fail() {
	       test.assertExists("input#BUY_NUM");
   });

   casper.waitForSelector("a[class='btn_Purchase']",
	   function success() {
	       test.assertExists("a[class='btn_Purchase']");
	       this.click("a[class='btn_Purchase']");
	   },
	   function fail() {
	       test.assertExists("a[class='btn_Purchase']");
   });

	casper.waitForSelector("input[name='orderAmount']",
	   function success() {
	       test.assertExists("input[name='orderAmount']");
	       this.sendKeys("input[name='orderAmount']", "1");
	   },
	   function fail() {
	       test.assertExists("input[name='orderAmount']");
   });

	casper.waitForSelector(x("//a[@id='toSettlement']"),
	   function success() {
	       test.assertExists(x("//a[@id='toSettlement']"));
	       this.click(x("//a[@id='toSettlement']"));
	   },
	   function fail() {
	       test.assertExists(x("//a[@id='toSettlement']"));
   });

	casper.waitForSelector("button#submitOrder",
	   function success() {
	       test.assertExists("button#submitOrder");
	       this.click("button#submitOrder");
	   },
	   function fail() {
	       test.assertExists("button#submitOrder");
   });

	var orderParam = null;

	casper.waitForSelector("div[class='payPd']", 
		function success() {
			var url = this.getCurrentUrl();
	this.echo("++++++++++ url:" + url + "," + url.indexOf("OrderId") + ", " + url.indexOf("&Key"));
			orderParam = url.substr(url.indexOf("?")+2); //rderId=5115091908424832&Key=WOEGO01
			orderParam = 'o' + orderParam; 
			this.echo("++++++++++ orderParam:" + orderParam);

			casper.thenOpen('http://www.woego.cn/woego/orderPayment/pageInit?' + orderParam, function() {
    			this.echo("url popup loaded : " + this.getCurrentUrl(),"INFO");
			});
		}
		,
	   function fail() {
	       test.assertExists("div[class='payPd']");
   		}
	);
/*
   casper.waitForSelector(x("//*[@id='uclist']/ul/li[1]/a"),
	   function success() {
	       test.assertExists(x("//*[@id='uclist']/ul/li[1]/a"));
	       this.click(x("//*[@id='uclist']/ul/li[1]/a"));
	   },
	   function fail() {
	       test.assertExists(x("//*[@id='uclist']/ul/li[1]/a"));
   });
   casper.waitForSelector("a[class='buttonWo-pj small-long-btn']"),
	   function success() {
	       test.assertExists("a[class='buttonWo-pj small-long-btn']");
	       this.click("a[class='buttonWo-pj small-long-btn']");
	   },
	   function fail() {
	       test.assertExists("a[class='buttonWo-pj small-long-btn']");
   });*/

   casper.waitForSelector("#underline_pay",
	   function success() {
	       test.assertExists("#underline_pay");
	       this.click("#underline_pay");
	   },
	   function fail() {
	       test.assertExists("#underline_pay");
   });

   casper.waitForSelector("input[name='imageFile_1']",
	   function success() {
	       test.assertExists("input[name='imageFile_1']");
	       //this.click("input[name='imageFile_1']");
		   var ret = this.evaluate(function(file){
			    return __utils__.sendAJAX("http://www.woego.cn/woego/orderPayment/uploadImage", "POST", {file: file}, false);
		   }, "/home/hy/Pictures/CapthcaImage.jpg");
			this.echo("+++++ upload ret:" + ret, "INFO");
		},
		function fail() {
			test.assertExists("input[name='imageFile_1']");
   });
   casper.waitForSelector("input[name='imageFile_2']",
	   function success() {
	       test.assertExists("input[name='imageFile_2']");
	       //this.click("input[name='imageFile_2']");
	   },
	   function fail() {
	       test.assertExists("input[name='imageFile_2']");
   });


	
    casper.run(function() {test.done();});
});







