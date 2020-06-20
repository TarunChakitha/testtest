package com.mindtree.helloworldapplication.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {
	
	@RequestMapping("/")
	public String printHello() {
		return "Hello World..!! I'm JAR Application";
	}

}
