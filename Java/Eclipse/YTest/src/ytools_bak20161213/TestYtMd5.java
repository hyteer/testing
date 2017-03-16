package ytools_bak20161213;
import java.security.MessageDigest;
import java.util.Properties;

import ytools.YtMD5;

public class TestYtMd5 {

	/**
     * @param args the command line arguments
     */
	public static final String MD5="MD5";
    public static final String UTF8="UTF-8";
	
	public static void main(String[] args) {
		Properties props = System.getProperties();
		System.out.println(props.get("file.encoding"));
		
		String test4="body=YT测试&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46";
		String test1="body=test1&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46";
        //byte[] utf8Bytes = test1.getBytes(UTF8);
        //String s1 = "hello涓浗浜�?"; 
        String test2="body=YT测试&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46";
        String test3="body=test1&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn¬ify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46";
        String [] test={test1,test2,test3};
        for (String s : test) {
            String str=ytools.YtMD5.EncryptionStr32(s, MD5, "UTF-8");
            System.out.println("数据�?" + s+"\n 加密之后的结果为�?"+str+" 字符串长度为�?"+str.length());
            str = ytools.YtMD5.EncryptionStr16(s, MD5, UTF8);
            System.out.println("数据�?" + s+"\n 加密之后的结果为�?"+str+" 字符串长度为�?"+str.length());
        }
    }
	
}
