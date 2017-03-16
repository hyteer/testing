package socketdemo;

import java.io.BufferedInputStream;  
import java.io.BufferedWriter;  
import java.io.IOException;  
import java.io.OutputStreamWriter;  
import java.net.ServerSocket;  
import java.net.Socket;  
  
public class EchoServer {  
  
    //����˵�Ĭ�϶˿�  
    private static int defaultPort = 12345;   
    //���ڽ�����վ�Ŀͻ���  
    private Socket client;  
    //���ڴ��������Ҽ���ָ���˿�  
    private ServerSocket server;  
    public static final String END_FLAG = "over";  
      
    public static void main(String[] args) {  
        try {  
            EchoServer echoServer = new EchoServer();  
            /** 
             *  ResponseThread������Ӧ��վ�Ŀͻ���������߳� 
             *  һ������վ���󣬽���ȡ��ͻ��˵�Socket��Ϊÿһ����վ�����������µ��̵߳������� 
             * */  
            ResponseThread responseThread = echoServer.new ResponseThread();  
            //����������վ������߳�  
            responseThread.start();  
            //�ȴ��߳�  
            responseThread.join();  
        } catch (InterruptedException e) {  
            // TODO Auto-generated catch block  
            e.printStackTrace();  
        } catch (IOException e) {  
            // TODO Auto-generated catch block  
            e.printStackTrace();  
        }  
          
    }  
  
    public EchoServer() throws IOException {  
        //�½�����˵�Socket  
        server = new ServerSocket(defaultPort);  
    }  
      
    private class ResponseThread extends Thread {  
          
        @Override  
        public void run() {  
              
            while (true) {  
                try {  
                    //��ͣ�ļ�����վ���󣬻�����  
                    client = server.accept();  
                    //һ����ȡ����վ�Ŀͻ����������½�HandlerThread�߳�����������ÿһ������  
                    System.out.println("accpet from client : " + client.getInetAddress() + " , port : " + client.getPort());  
                    Thread readThread = new HandlerThread(client);  
                    //���������߳�  
                    readThread.start();  
                } catch (IOException e) {  
                    // TODO Auto-generated catch block  
                    e.printStackTrace();  
                }  
            }  
              
        }  
    }  
          
    //���ڴ���������߳�  
    private class HandlerThread extends Thread {  
        //��ȡ�ͻ��˵�Socket  
        private Socket client;  
          
        public HandlerThread(Socket client) {  
            this.client = client;  
        }  
          
        @Override  
        public void run() {  
            BufferedInputStream bis = null;  
            BufferedWriter bw = null;  
            try {  
                //��ȡ��д�����ĳ�ʼ��  
                bis = new BufferedInputStream(client.getInputStream());  
                bw = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()));  
                String readString = null;  
                String writeString = null;  
                byte[] buf = new byte[1024];  
                int len = -1;  
                while (true) {  
                    //�����л�ȡ�ͻ���д�����Ϣ���������ȴ�  
                    len = bis.read(buf);              
                    readString = new String(buf, 0, len);  
                    String myString = "[Response from Server]: \nstatus:success \nJust a test. \r\n";
                    writeString = myString.toUpperCase();
                    //writeString = readString.toUpperCase();  
                    //�ж��Ƿ������ǰ����  
                    if (readString.equalsIgnoreCase(END_FLAG)) {  
                        break;  
                    }  
                    bw.write(writeString);  
                    bw.flush();  
                }  
                //����Echo��Ϣ�ķ��ͣ����ر�д�������ͻ��˵Ķ�ȡ�����׳��쳣����  
                System.out.println("client end client : "  + client.getInetAddress() + " , port : " + client.getPort());  
            } catch (IOException e) {  
                // TODO Auto-generated catch block  
                e.printStackTrace();  
            } finally {  
                if (bis != null) {  
                    try {  
                        bis.close();  
                    } catch (IOException e) {  
                        // TODO Auto-generated catch block  
                        e.printStackTrace();  
                    }  
                }  
                if (bw != null) {  
                    try {  
                        bw.close();  
                    } catch (IOException e) {  
                        // TODO Auto-generated catch block  
                        e.printStackTrace();  
                    }  
                }  
            }  
              
        }  
          
    }  
      
}  


