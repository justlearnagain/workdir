Action()
{
	//for (num=0; num<1; num++) {
	lr_think_time(3);

	sprintf(post_data,"\
{\r\n\
\"PageIndex\":\"1\",\r\n\
\"PageSize\":\"20\",\r\n\
\"ARCHIVESID\":\"13060\"\r\n\
}");

	lr_convert_string_encoding(post_data, LR_ENC_SYSTEM_LOCALE, LR_ENC_UTF8, "req");
	strcpy(utf8_data, lr_eval_string("{req}"));
	lr_save_string(utf8_data, "utf8_req_body");

    web_save_header(REQUEST, "RequestHeader");   // REQUEST为内置变量，保存请求的头信息，需在发送URL请求前注册使用
	web_save_header(RESPONSE, "ResponseHeader"); // RESPONSE保存响应的头信息
	
	// 取到服务器的返回信息
	web_reg_save_param("ResponseBody", "LB=", "RB=", "Search=Body", LAST);

    // 设置检查内容
    web_reg_find("SaveCount=String_Count",
				 "Text=\"code\":0",
				 LAST);

	// 发送请求
	web_custom_request("serach_file", 
		"URL=http://192.168.1.102:1082/api/Archives/GetARCHIVESFILELIST",
		"Method=POST",
        "EncType=application/json",   
        "RecContentType=application/json",  
		"Body={utf8_req_body}",
		LAST);

	//lr_think_time(1);

    //lr_output_message("\n==========\nRequestHeader:\n%s", lr_eval_string("{RequestHeader}"));
	//lr_output_message("\n==========\nRequestBody:\n%s", utf8_data);
	//lr_output_message("\n==========\nResponseHeader:\n%s", lr_eval_string("{ResponseHeader}"));
	//lr_output_message("\n==========\nResponseBody:\n%s", lr_eval_string("{ResponseBody}"));


	// 转换为UTF-8编码
	// 注意这里将服务器返回的编码格式保存为本地格式
	lr_convert_string_encoding(lr_eval_string("{ResponseBody}"), LR_ENC_UTF8, LR_ENC_SYSTEM_LOCALE, "resp");
	//lr_output_message(lr_eval_string("{resp}"));

    if (atoi(lr_eval_string("{String_Count}")) > 0) {
		lr_output_message("\n==========\n文件查询成功：%s\n==========\n\n", lr_eval_string("{String_Count}"));
	}
	else {
		lr_error_message("文件查询卷失败！");
		lr_abort();
	}

    //strcpy(buf, lr_eval_string("{resp}"));
	//lr_output_message(buf);
	//ptr = (char *)strstr(buf, "code");

	ptr = (char *)strstr(lr_eval_string("{resp}"), "code");
	if (!ptr) {
		lr_error_message("文件查询失败！");
		lr_abort();
	}

	//}

	return 0;
}
