package use_properties;

import java.io.*;
import java.util.Properties;

public class Properties1 {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		Properties props = new Properties();
		props.load(new java.io.FileInputStream("src/setting.properties"));  // FileNotFoundException

		String filepath = props.getProperty("last_open_file");
		String interval = props.getProperty("auto_save_interval", "120");
        System.out.println(filepath);
        System.out.println(interval);
        
        Properties props2 = new Properties();
        props2.setProperty("url", "http://www.liaoxuefeng.com");
        props2.setProperty("language", "Java");
        props2.store(new FileOutputStream("C:\\Users\\pactera\\Downloads\\Documents\\setting.properties"), "这是写入的properties注释");
	}

}
