Action()
{
	//for (num=0; num<1; num++) {
	lr_think_time(3);

	// 取到服务器的返回信息
	web_reg_save_param("ResponseBody", "LB=", "RB=", "Search=Body", LAST);

    // 设置检查内容
    web_reg_find("SaveCount=String_Count",
				 "Text=\"code\":0",
				 LAST);
	
	lr_start_transaction("getArch");


	// 发送请求
	web_custom_request("get_arch", 
		"URL=http://192.168.1.102:1082/api/Archives/GetArchTypes",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);

	lr_end_transaction("getArch", LR_AUTO);

	//lr_think_time(1);

	// 转换为UTF-8编码
	// 注意这里将服务器返回的编码格式保存为本地格式
	lr_convert_string_encoding(lr_eval_string("{ResponseBody}"), LR_ENC_UTF8, LR_ENC_SYSTEM_LOCALE, "resp");
	//lr_output_message(lr_eval_string("{resp}"));

    if (atoi(lr_eval_string("{String_Count}")) > 0) {
		lr_output_message("\n==========\n获取案卷成功：%s\n==========\n\n", lr_eval_string("{String_Count}"));
	}
	else {
		lr_error_message("获取案卷失败！");
		lr_abort();
	}

    //strcpy(buf, lr_eval_string("{resp}"));
	//lr_output_message(buf);
	//ptr = (char *)strstr(buf, "code");

	ptr = (char *)strstr(lr_eval_string("{resp}"), "code\":0");
	if (!ptr) {
		lr_error_message("数据获取失败！");
		lr_abort();
	}

	//}

	return 0;
}