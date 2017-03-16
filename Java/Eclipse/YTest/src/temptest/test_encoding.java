package temptest;
import java.nio.charset.Charset;
import java.util.Properties;

public class test_encoding {
	
	public static void main(String[] args) {
		
		Properties props = System.getProperties();
		System.out.println(props.get("file.encoding"));
		props.put("file.encoding","utf-8");
		System.out.println(props.get("file.encoding"));
	
	}
}
