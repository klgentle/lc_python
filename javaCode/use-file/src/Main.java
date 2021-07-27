import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 写入文本并指定编码:
		try {
			Files.writeString(Paths.get("C:\\Users\\pactera\\Downloads\\Documents\\file.txt"), "文本内容test...",
					StandardCharsets.UTF_8);
			// 默认使用UTF-8编码读取:
			String content1 = Files.readString(Paths.get("C:\\Users\\pactera\\Downloads\\Documents\\file.txt"));
			System.out.println(content1);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
