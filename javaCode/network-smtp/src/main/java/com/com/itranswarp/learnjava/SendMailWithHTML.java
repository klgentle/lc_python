package com.itranswarp.learnjava;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SendMailWithHTML {

	public static void main(String[] args) throws Exception {
		final String smtp = "smtp.sina.com";
		final String username = "klgentle@sina.com";
		final String password = "need to modify"; // need to modify
		final String from = username;
		final String to = "1063237864@qq.com";
		SendMail sender = new SendMail(smtp, username, password);
		Session session = sender.createTLSSession();
		Message message = createHtmlMessage(session, from, to, "Java HTML邮件",
				"<h1>Hello</h1><p>这是一封<u>javamail</u>HTML邮件！</p>");
		Transport.send(message);
	}

	static Message createHtmlMessage(Session session, String from, String to, String subject, String body)
			throws MessagingException {
		MimeMessage message = new MimeMessage(session);
		message.setFrom(new InternetAddress(from));
		message.setRecipient(Message.RecipientType.TO, new InternetAddress(to));
		message.setSubject(subject, "UTF-8");
		message.setText(body, "UTF-8", "html");
		return message;
	}

}
