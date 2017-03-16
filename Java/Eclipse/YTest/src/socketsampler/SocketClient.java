package socketsampler;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class SocketClient {
	
	
	public static void main(String[] args) {
	        
	        boolean X = false;
	        System.out.println("X:"+X);
	        boolean testSocket = new SocketClient().sendMessage("localhost", 12345, "test11");
	        
	    }
	
    
    public boolean sendMessage(String ipAddress,int port,String data){
    	try {
            // 1�������ͻ���Socket��ָ����������ַ�Ͷ˿�
            // Socket socket=new Socket("127.0.0.1",5200);
            Socket socket = new Socket(ipAddress, port);
            System.out.println("�ͻ��������ɹ�");
            // 2����ȡ���������������˷�����Ϣ
            // �򱾻���52000�˿ڷ����ͻ�����
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            // ��ϵͳ��׼�����豸����BufferedReader����
            PrintWriter write = new PrintWriter(socket.getOutputStream());
            // ��Socket����õ��������������PrintWriter����
            //3����ȡ������������ȡ�������˵���Ӧ��Ϣ 
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            // ��Socket����õ�����������������Ӧ��BufferedReader����
            String readline;
            readline = br.readLine(); // ��ϵͳ��׼�������һ�ַ���
            
            while (!readline.equals("end")) {
                // ���ӱ�׼���������ַ���Ϊ "end"��ֹͣѭ��
                write.println(readline);
                // ����ϵͳ��׼���������ַ��������Server
                write.flush();
                // ˢ���������ʹServer�����յ����ַ���
                System.out.println("Client:" + readline);
                // ��ϵͳ��׼����ϴ�ӡ������ַ���
                System.out.println("Server:" + in.readLine());
                // ��Server����һ�ַ���������ӡ����׼�����
                readline = br.readLine(); // ��ϵͳ��׼�������һ�ַ���
            } // ����ѭ��
            //4���ر���Դ 
            write.close(); // �ر�Socket�����
            in.close(); // �ر�Socket������
            socket.close(); // �ر�Socket
            return true;
        } catch (Exception e) {
            System.out.println("can not listen to:" + e);// ������ӡ������Ϣ
            return false;
        }
    }
}
