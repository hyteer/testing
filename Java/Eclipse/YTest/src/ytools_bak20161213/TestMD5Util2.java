package ytools_bak20161213;
import ytools.MD5Util2;

public class TestMD5Util2 {
	
	public static void main(String[] args) {
        // TODO code application logic here
		String txt = "body=YT≤‚ ‘&cashierid=1&mch_id=1000000037&nonce_str=xbfg5ewrl44yp46x9dsw6dxzk4ycfhqn&notify_url=http://pay.speedpos.snsshop.net/notify/1000100001/1000100001201611021915213701&openid=oRs4YwmoyqGiWYqZn5FG0QCxlu9Q&out_trade_no=10002000711177073802461836cb&return_url=http://pay.speedpos.snsshop.net/success/1000100001/1000100001201611021915213701&spbill_create_ip=127.0.0.1&total_fee=1&trade_type=WXPAY.JSAPI&key=lg81oqo89knyugdifr850molrioeqw46";
    	String res = new ytools.MD5Util2().md5(txt);
		System.out.println(res);
    	
    	
    }
}
