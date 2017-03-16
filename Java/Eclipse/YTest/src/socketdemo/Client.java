package socketdemo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;
 
public class Client {
   public static void main(String[] args) {
      try {
         Socket s = new Socket("localhost",12345);
         
         //����IO
         InputStream is = s.getInputStream();
         OutputStream os = s.getOutputStream();
         
         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(os));
         //��������˷���һ����Ϣ
         bw.write("test11");
         bw.flush();
         
         //��ȡ���������ص���Ϣ
         BufferedReader br = new BufferedReader(new InputStreamReader(is));
         String mess = br.readLine();
         System.out.println("��������"+mess);
      } catch (UnknownHostException e) {
         e.printStackTrace();
      } catch (IOException e) {
         e.printStackTrace();
      }
   }
}

