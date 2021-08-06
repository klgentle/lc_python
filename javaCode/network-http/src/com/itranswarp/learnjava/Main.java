package com.itranswarp.learnjava;

import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.io.InputStream;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpClient.Version;
import java.net.http.HttpRequest;
import java.net.http.HttpRequest.BodyPublishers;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	static HttpClient httpClient = HttpClient.newBuilder().build();

	public static void main(String[] args) throws Exception {
		httpGet("https://www.sina.com.cn/");
		httpPost("https://accounts.douban.com/j/mobile/login/basic",
				"name=bob%40example.com&password=12345678&remember=false&ck=&ticket=");
		httpGetImage("https://img.t.sinajs.cn/t6/style/images/global_nav/WB_logo.png");
	}

	static void httpGet(String url) throws Exception {
		HttpRequest request = HttpRequest.newBuilder(new URI(url))
				// 设置Header:
				.header("User-Agent", "Java HttpClient").header("Accept", "*/*")
				// 设置超时:
				.timeout(Duration.ofSeconds(5))
				// 设置版本:
				.version(Version.HTTP_2).build();
		HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
		System.out.println(response.body().substring(0, 1024) + "...");
	}

	static void httpGetImage(String url) throws Exception {
		HttpRequest request = HttpRequest.newBuilder(new URI(url))
				// 设置Header:
				.header("User-Agent", "Java HttpClient").header("Accept", "*/*")
				// 设置超时:
				.timeout(Duration.ofSeconds(5))
				// 设置版本:
				.version(Version.HTTP_2).build();
		HttpResponse<InputStream> response = httpClient.send(request, HttpResponse.BodyHandlers.ofInputStream());
		// 显示Http返回的图片:
		BufferedImage img = ImageIO.read(response.body());
		ImageIcon icon = new ImageIcon(img);
		JFrame frame = new JFrame();
		frame.setLayout(new FlowLayout());
		frame.setSize(400, 200);
		JLabel lbl = new JLabel();
		lbl.setIcon(icon);
		frame.add(lbl);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	static void httpPost(String url, String body) throws Exception {
		HttpRequest request = HttpRequest.newBuilder(new URI(url))
				// 设置Header:
				.header("User-Agent", "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0) like Gecko")
				.header("Accept", "*/*").header("Content-Type", "application/x-www-form-urlencoded")
				// 设置超时:
				.timeout(Duration.ofSeconds(5))
				// 设置版本:
				.version(Version.HTTP_2)
				// 使用POST并设置Body:
				.POST(BodyPublishers.ofString(body, StandardCharsets.UTF_8)).build();
		HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
		System.out.println(response.body());
	}
}
