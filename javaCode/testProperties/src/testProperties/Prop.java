package testProperties;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Prop {

	public static void main(String[] args) throws IOException {
		Properties props = new Properties();
		// TODO 调用 
//		props.load(inputStreamFromClassPath("/default.properties"));
//		properties.load(inputStreamFromFile("./conf.properties"));
	}
	
	public void inputStreamFromClassPath (String conf) throws IOException {
//		String conf = "/default.properties";
		try (InputStream input = getClass().getResourceAsStream(conf)) {
		    if (input != null) {
		        // TODO:
		    }
		}		
	}	
	
	public void inputStreamFromFile(String conf) throws FileNotFoundException, IOException {
//		String conf = "C:\\conf\\default.properties";
		try (InputStream input = new FileInputStream(conf)) {
		    // TODO:
		}
	}

}
